# app/models/model.py
import tensorflow as tf
import numpy as np

MODEL_PATH = "./saved_model/model.h5"

class NeuralNetworkModel:
    def __init__(self):
        # Load the pre-trained model
        self.model = tf.keras.models.load_model(MODEL_PATH)

    def predict(self, input_data):
        """
        Perform inference on input data.

        Args:
            input_data (list or np.array): Input data for the model.

        Returns:
            list: Model predictions.
        """
        input_array = np.array(input_data)
        predictions = self.model.predict(input_array)
        return predictions.tolist()

# Singleton instance of the model
model_instance = NeuralNetworkModel()
