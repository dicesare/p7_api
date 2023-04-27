from models.text_processor import TextProcessor
from models.bert_model import BertModel
from models.utils import get_model_path


def test_text_processor():
    processor = TextProcessor()
    text = "hello, world!"
    assert processor.process_upper(text) == "HELLO, WORLD!"


def test_load_model():
    model_dir = get_model_path()
    model = BertModel(model_dir=model_dir)
    assert model is not None


def test_solo_predict():
    # Load the latest model from the Sentiment140 directory
    model_dir = get_model_path()
    model = BertModel(model_dir=model_dir)
    test_text = ["I love this movie!"]
    predicted_label = model.predict_sentiment(test_text, return_sentiment=True)[0]
    assert predicted_label['score'] >= 0.5, f"Expected positive sentiment, got {predicted_label['sentiment']}"  # positive sentiment


def test_multi_predict():
    # Load the latest model from the Sentiment140 directory
    model_dir = get_model_path()
    model = BertModel(model_dir=model_dir)
    # Test texts
    positive_texts = [
        "I love this movie!",
        "This is an amazing product.",
        "I had a great time at the party.",
        "The food was delicious.",
        "Their customer service is outstanding.",
    ]

    negative_texts = [
        "I hate this movie!",
        "This is a terrible product.",
        "I had a horrible time at the party.",
        "The food was disgusting.",
        "Their customer service is awful.",
    ]

    # Test positive sentiments
    for text in positive_texts:
        predicted_label = model.predict_sentiment([text], return_sentiment=False)
        print(f"Predicted label: {predicted_label}")
        assert predicted_label >= 0.5, f"Expected positive sentiment, got {predicted_label}"

    # Test negative sentiments
    for text in negative_texts:
        predicted_label = model.predict_sentiment([text], return_sentiment=False)
        print(f"Predicted label: {predicted_label}")
        assert predicted_label < 0.5, f"Expected negative sentiment, got {predicted_label}"
