import os
import numpy as np
import xgboost as xgb
from django.conf import settings


class PredictionModel:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        """Load the saved XGBoost regressor model"""
        model_path = os.path.join(
            settings.BASE_DIR,
            'prediction',
            'ml_model',
            'xgboost_model.json'
        )

        # Ensure the model is loaded as a regressor
        self.model = xgb.XGBRegressor()
        self.model.load_model(model_path)
        print("Model is a regressor")

    def preprocess_features(self, contract_duration, employee_variation_rate, client_age):
        """Preprocess the input features"""
        # Create feature array with the same order as training data
        # Initialize a zero array with the expected number of features
        features = np.zeros((1, 99))

        # Assign the values of your features to the first three positions
        features[0, :3] = [contract_duration, employee_variation_rate, client_age]
        return features

    def predict(self, contract_duration, employee_variation_rate, client_age):
        """Make prediction using the loaded model"""
        try:
            # Preprocess features
            features = self.preprocess_features(
                contract_duration,
                employee_variation_rate,
                client_age
            )

            # Predict using the regressor
            prediction = self.model.predict(features)[0]

            return {
                'success': True,
                'prediction': float(prediction),  # Output the prediction
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


# Create a singleton instance
prediction_model = PredictionModel()
