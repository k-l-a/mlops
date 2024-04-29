import requests
import json

# Define the API endpoint
url = "http://127.0.0.1:8000/predict/"

# Sample data with 30 dummy feature values
data = {
    "features": [
        1.799e+01, 1.038e+01, 1.228e+02, 1.001e+03, 1.184e-01, 2.776e-01, 3.001e-01, 
        1.471e-01, 2.419e-01, 7.871e-02, 1.095e+00, 9.053e-01, 8.589e+00, 1.534e+02, 
        6.399e-03, 4.904e-02, 5.373e-02, 1.587e-02, 3.003e-02, 6.193e-03, 2.538e+01, 
        1.733e+01, 1.846e+02, 2.019e+03, 1.622e-01, 6.656e-01, 7.119e-01, 2.654e-01, 
        4.601e-01, 1.189e-01
    ]
}

# Send a POST request
response = requests.post(url, json=data)

# Print the response
print("Status Code:", response.status_code)
print("Response Body:", response.json())
