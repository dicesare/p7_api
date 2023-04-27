from models.bert_model import BertModel


def test_create_bert_model():
    tfhub_handle_preprocess = 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'
    tfhub_handle_encoder = 'https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4'
    model_dir = 'test_model_dir'
    bert_model = BertModel(tfhub_handle_preprocess, tfhub_handle_encoder, model_dir)
    assert bert_model is not None
