import requests

# URL of the FastAPI server
base_url = "http://127.0.0.1:8090"

# Make a GET request to the root endpoint
response = requests.get(f"{base_url}/")
print(response)




#base_url_coord="http://127.0.0.1:8090/inference_coord"

# Make a GET request to the /items/{item_id} endpoint
#item_id = 42
#params = {"q": "some query"}


para={
  "coord_E": 0.01,
  "coord_N": 0.01,
}

response = requests.get(f"{base_url}/inference_coord", params=para)
print(response.json())


# Parameters to be sent in the query string
params = {
    'model': 'mlp'
}

# Headers to be sent with the request
headers = {
    'accept': 'application/json'
}

# Path to the CSV file you want to upload
file_path = "share_zeta/MLP16/example_mlp16.csv"

# Open the CSV file in binary mode and prepare the files dictionary
with open(file_path, 'rb') as f:
    files = {'dataset': (file_path, f, 'text/csv')}
    # Make the POST request
    response = requests.post(f"{base_url}/inference_complete", params=params, headers=headers, files=files)
print(response)


# Check if the request was successful
if response.status_code == 200:
    # Get the filename from the Content-Disposition header
    content_disposition = response.headers.get('Content-Disposition')
    if content_disposition:
        # Extract the filename from the header
        filename = content_disposition.split('filename=')[-1].strip('"')
    else:
        # Default filename if header is not present
        filename = 'downloaded_file.csv'

    # Save the content to a file
    with open(filename, 'wb') as f:
        f.write(response.content)
    
    print(f"File '{filename}' downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")