# This would be the client that calls to the api.
import json
import requests

if __name__ == "__main__":
    # Make the data object.
    # or load a json file.
    with open("./test_data/simple.json") as f:
        input_data = json.load(f)

    # Send an process a request.
    print("sending: ")
    print(input_data)

    r = requests.post(url="http://0.0.0.0:8000/work", json=input_data)
    print(r)
    print(r.status_code)
    print(r.text)
