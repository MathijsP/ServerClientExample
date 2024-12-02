from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)


def test_do_work():
    with open("./test_data/simple.json") as f:
        input_data = json.load(f)

    print(input_data)
    response = client.post("/work", json=input_data)
    assert response.status_code == 200, response.text
