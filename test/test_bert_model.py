import pytest
from models.bert_model import BertModel
from models.utils import get_model_path


def test_create_bert_model():
    model_dir = get_model_path()
    bert_model = BertModel(model_dir)
    assert bert_model is not None


@pytest.fixture
def bert_model():
    model_dir = get_model_path()
    bert_model = BertModel(model_dir)
    return bert_model


def test_bert_predict_positive(bert_model):
    text = ["This movie is great!"]
    prediction = bert_model.predict_sentiment(text)
    print(prediction)
    assert prediction[0]['sentiment'] == "positive"
    assert prediction[0]['score'] > 0.5


def test_bert_predict_negative(bert_model):
    text = ["This movie is horrible!"]
    prediction = bert_model.predict_sentiment(text)
    print(prediction)
    assert prediction[0]['sentiment'] == "negative"
    assert prediction[0]['score'] < 0.5

