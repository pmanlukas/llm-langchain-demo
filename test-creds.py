import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from google.cloud import aiplatform

# Load environment variables from .env file
load_dotenv()

# Set up your environment variable to point to your service account key file
service_account_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Authenticate and initialize the client
credentials = service_account.Credentials.from_service_account_file(service_account_path)

# Initialize the Vertex AI client
client = aiplatform.gapic.PredictionServiceClient(credentials=credentials)

# Example: List endpoint names
project = 'hooli-420412'
location = 'us-central1'
parent = f"projects/{project}/locations/{location}"

response = client.api_endpoint
print(response)
