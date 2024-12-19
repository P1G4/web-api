import requests

def test_submit_data():
    # URL of the JavaScript server endpoint
    url = "http://localhost:3000/submit_data"

    # Test data to send
    test_payload = [
        {"ldrValue": "on", "doorStatus": "open"},
        {"ldrValue": "off", "doorStatus": "closed"},
        {"ldrValue": "on", "doorStatus": "ajar"},
    ]

    for i, payload in enumerate(test_payload):
        try:
            # Sending POST request
            response = requests.post(url, data=payload)

            # Printing the response from the server
            print(f"Test {i + 1}:")
            print(f"Payload: {payload}")
            print(f"Response status code: {response.status_code}")
            print(f"Response body: {response.text}\n")

            if response.status_code != 200:
                print(f"Error: Test {i + 1} failed with status code {response.status_code}\n")

        except Exception as e:
            print(f"Error during test {i + 1}: {e}\n")

if __name__ == "__main__":
    test_submit_data()
