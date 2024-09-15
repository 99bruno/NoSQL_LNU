"""
Description: This script connects to the MongoDB Atlas cluster and retrieves some documents
from the "comments" collection in the "sample_mflix" database.
"""

# Import the required libraries
import os
import dotenv

# Import the required classes from the PyMongo library
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load the environment variables from the .env file
dotenv.load_dotenv()

# Create a new client and connect to the server
try:
    client = MongoClient(os.getenv("URI"), server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)

    # Connect to the database
    db = client['sample_mflix']

    # Connect to the collection
    collection = db['comments']

    # Retrieve and print some documents
    documents = collection.find().limit(20)  # Adjust the limit as needed

    for doc in documents:
        print(doc)
except Exception as e:
    print("An error occurred:", e)