import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
from sklearn.utils.validation import check_is_fitted
from django.conf import settings
import joblib


class PredictionModel:
    def __init__(self):
        self.model = None
        self.feature_names = [
            'contact_duration', 
            'employment_variation_rate', 
            'client_age'
        ]
        try:
            self.load_model()
        except FileNotFoundError:
            print("No saved model found, creating new model...")
            self.create_model()

    def create_model(self):
        """Create and configure the stacking classifier"""
        print("Initializing new stacking classifier...")
        # Define base estimators
        estimators = [
            ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
            ('gb', GradientBoostingClassifier(n_estimators=100, random_state=42))
        ]

        # Define meta-classifier
        final_estimator = LogisticRegression(random_state=42)

        # Create stacking classifier
        self.model = StackingClassifier(
            estimators=estimators,
            final_estimator=final_estimator,
            cv=5,
            stack_method='predict_proba',
            n_jobs=-1
        )
        print("Model initialized successfully")

    def preprocess_features(self, contact_duration, employment_variation_rate, client_age):
        """Preprocess the input features with only the selected features"""
        # Create a DataFrame with the three specified features
        features_dict = {
            'contact_duration': contact_duration,
            'employment_variation_rate': employment_variation_rate,
            'client_age': client_age
        }

        # Convert to DataFrame with a single row and the selected feature names
        features_df = pd.DataFrame([features_dict], columns=self.feature_names)

        return features_df

    def save_model(self):
        """Save the trained stacking model"""
        if self.model is None:
            raise ValueError("No model to save - please train the model first")

        model_dir = os.path.join(settings.BASE_DIR, 'prediction', 'ml_model')
        os.makedirs(model_dir, exist_ok=True)

        model_path = os.path.join(model_dir, 'best_stacking_model.joblib')
        print(f"Saving model to {model_path}")
        joblib.dump(self.model, model_path)
        print("Model saved successfully")

    def load_model(self):
        """Load the saved stacking model"""
        model_path = os.path.join(
            settings.BASE_DIR,
            'prediction',
            'ml_model',
            'best_stacking_model.joblib'
        )

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"No saved model found at {model_path}")

        print(f"Loading model from {model_path}")
        self.model = joblib.load(model_path)
        print("Model loaded successfully")

    def fit(self, X, y):
        """Train the stacking model"""
        if self.model is None:
            self.create_model()

        # Filter the training data to only include the selected features
        X = X[self.feature_names]

        print("Training model...")
        self.model.fit(X, y)
        print("Model training completed")
        self.save_model()

    def predict(self, contact_duration, employment_variation_rate, client_age):
        """Make prediction using the loaded model"""
        if self.model is None:
            return {
                'success': False,
                'error': 'Model not initialized. Please train the model first.'
            }

        try:
            # Check if the model is fitted
            check_is_fitted(self.model)

            # Preprocess features
            features = self.preprocess_features(
                contact_duration,
                employment_variation_rate,
                client_age
            )

            # Get class probabilities
            probabilities = self.model.predict_proba(features)[0]
            # Get predicted class
            prediction = self.model.predict(features)[0]

            return {
                'success': True,
                'prediction': int(prediction),
                'probabilities': {
                    f'class_{i}': float(prob) for i, prob in enumerate(probabilities)
                }
            }

        except Exception as e:
            return {
                'success': False,
                'error': f'Prediction error: {str(e)}'
            }


# Create a singleton instance
prediction_model = PredictionModel()