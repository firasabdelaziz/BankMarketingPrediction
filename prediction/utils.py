import os
import numpy as np
import xgboost as xgb
from django.conf import settings


class PredictionModel:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        """Load the saved XGBoost classifier model"""
        model_path = os.path.join(
            settings.BASE_DIR,
            'prediction',
            'ml_model',
            'xgboost_model.json'
        )

        # Load the model as a classifier
        self.model = xgb.XGBClassifier()
        self.model.load_model(model_path)
        print("Model is a classifier")

    def preprocess_features(self, contact_duration, employee_variation_rate, client_age):
        """Preprocess the input features"""
        # Initialize array with 103 features set to zero
        features = np.zeros((1, 103))
        
        # Set the three known features at their correct positions
        features[0, 0] = contact_duration
        features[0, 1] = employee_variation_rate
        features[0, 2] = client_age
        
        return features

    def predict(self, contact_duration, employee_variation_rate, client_age):
        """Make prediction using the loaded model"""
        try:
            # Preprocess features
            features = self.preprocess_features(
                contact_duration,
                employee_variation_rate,
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
                'error': str(e)
            }


# Create a singleton instance
prediction_model = PredictionModel()