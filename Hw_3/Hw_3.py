from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://99bruno:Ka203884@lnu.gaczz.mongodb.net/?retryWrites=true&w=majority&appName=LNU"

# Create a new client and connect to the server
try:
    client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)
    # Connect to the database
    db = client['sample_mflix']
    # Connect to the collection
    collection = db['comments']
    # Retrieve and print some documents
    documents = collection.find({
        "name": "%Mer%"
    }).limit(20)  # Adjust the limit as needed
    for doc in documents:
        print(doc)
        print(type(doc))
except Exception as e:
    print("An error occurred:", e)