from pymongo import MongoClient

mongodb_uri = "mongodb+srv://okpomfonstephanie:missokpomfon@firstcluster.bsbwkyb.mongodb.net/?retryWrites=true&w=majority&appName=FirstCluster"
port = 8000
client = MongoClient(mongodb_uri, port)

# Configuring the name of our database

db = client["HobPanioNApp"]
print("Connected to database successfully")

# Below here we can now have multiple collections as such

users_collection = db["Users"]