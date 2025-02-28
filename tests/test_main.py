import pytest
from tests.test_utils import JsonUtils  # Assuming the utility class is in the 'utils.py' file
from fastapi.testclient import TestClient
from app.main import app  # Assuming your FastAPI app is in the `main.py` file.
import json
import os

# Create a test client for the FastAPI app
client = TestClient(app)

# Test POST /message/ endpoint
def test_process_message():
    # Define the request payload
    message = {
        "author": "brian",
        "message": "I am available 2 - 3 pm"
    }

    # Send a POST request to /message/
    response = client.post("/send_message", json=message)

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Assert that the response contains the correct message data
    data = response.json()
    
    # Define the relative path to the expected JSON file
    expected_json_file_path = os.path.join(os.path.dirname(__file__), 'expected', 'expected_availability.json')

    # Load expected JSON from file using the utility method
    expected_json = JsonUtils.load_json_from_file(expected_json_file_path)
    
    # Use the utility method to compare actual and expected JSON
    JsonUtils.assert_json_equal(data["response"]["content"], expected_json)
    
    
    print("OpenAI Response:", json.dumps(data, indent=2))
