from fastapi import APIRouter

from models.bert_model import BertModel
from models.utils import get_model_path
from models.text_processor import TextProcessor
from models.typing import ListTextsInput

router = APIRouter()


@router.post("/predict_sentiment/solo")
async def predict_sentiment_endpoint(texts_input: ListTextsInput):
    model_dir = get_model_path()
    model = BertModel(model_dir=model_dir)
    predictions = model.predict_sentiment(
        texts_input.texts,
        # return_sentiment=False
    )
    return predictions[0]


@router.post("/predict_sentiment/multi")
def predict_sentiment(texts_input: ListTextsInput):
    results = []
    model_dir = get_model_path()
    model = BertModel(model_dir=model_dir)
    for text in texts_input.texts:
        predicted_label = model.predict_sentiment(
            [text],
            # return_sentiment=False
        )
        results.append(predicted_label)
    return results


@router.get("/process_text")
async def hello():
    return {"message": "je suis la pour traiter le text"}


@router.get("/process_text/upper")
async def process_text(text: str):
    return {'processed_text': TextProcessor.process_upper(text)}


@router.post('/process_text/upper')
async def process_text(item: dict):
    processed_text = TextProcessor.process_upper(text=item['text'])
    return {'processed_text': processed_text}


@router.get("/")
async def root():
    return {"message": "Welcome to the OCR API! I could predict the sentiment of your tweet"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
