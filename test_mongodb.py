from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://abhivyaktijha2206_db_user:Mongodbatlas123@cluster0.hgzpjni.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
