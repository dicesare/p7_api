from routes.crud import router
from fastapi.testclient import TestClient
from itertools import chain


client = TestClient(router)


# def flatten(lst):
#     return [item for sublist in lst for item in sublist]


def test_response_server():
    response = client.get("/")
    assert response.status_code == 200


def test_response_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the OCR API! I could predict the sentiment of your tweet"}
    # assert response.json() == {"message": "Test failed to Welcome to the OCR API!"}


def test_response_route_message():
    response = client.get("/hello/World!")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
    # assert response.json() == {"message": "Test failed to Welcome to the OCR API!"}


def test_response_server_process_text():
    response = client.get("/process_text")
    assert response.status_code == 200


def test_post_server_process_text():
    data = {
        'text': 'This is a test text'
    }
    response = client.post("/process_text/upper", json=data)
    assert response.status_code == 200


def test_post_server_process_text_upper():
    data = {
        'text': 'This is a test text'
    }
    expected_output = {
        'processed_text': 'THIS IS A TEST TEXT'
    }
    response = client.post("/process_text/upper", json=data)
    assert response.status_code == 200
    assert response.json() == expected_output


def test_solo_predict_api():
    endpoint = "/predict_sentiment/solo"
    data = {
        "texts": ["I love this movie!"]
    }
    response = client.post(endpoint, json=data)
    predicted_label = response.json()
    print(f"Predicted label: {predicted_label}")
    assert predicted_label['score'] >= 0.5, f"Expected positive sentiment, got {predicted_label['sentiment']}"


def test_multi_predict_api():
    endpoint = "/predict_sentiment/multi"

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
    response = client.post(endpoint, json={"texts": positive_texts})
    predicted_labels = response.json()
    # print(predicted_labels)
    for label in list(chain(predicted_labels))[0]:
        assert label['score'] >= 0.5, f"Expected positive sentiment, got {label['sentiment']}"

    # Test negative sentiments
    response = client.post(endpoint, json={"texts": negative_texts})
    predicted_labels = response.json()
    # print(predicted_labels)
    for label in list(chain(predicted_labels))[0]:
        assert label['score'] < 0.5, f"Expected negative sentiment, got {label['sentiment']}"
