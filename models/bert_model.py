import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import tensorflow_text as text


class BertModel(tf.keras.Model):
    def __init__(self, model_dir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_dir = model_dir
        self.load_options = tf.saved_model.LoadOptions(experimental_io_device="/job:localhost")
        self.loaded_model = tf.keras.models.load_model(self.model_dir, compile=False, options=self.load_options)

    def predict_sentiment(self, text, return_sentiment=True):
        # Set the device used during inference
        inputs = text
        prediction = self.loaded_model.predict(inputs)
        # Set the threshold and return the sentiment
        threshold = 0.5
        sentiment = prediction
        if return_sentiment:
            sentiment = [
                {"sentiment": "positive", "score": float(pred)} if pred >= threshold
                else {"sentiment": "negative", "score": float(pred)}
                for pred in prediction]

        return sentiment


