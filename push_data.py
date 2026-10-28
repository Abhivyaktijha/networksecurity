import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(f"Connecting to: {MONGO_DB_URL}")

ca = certifi.where()

class NetworkDataExtract:
    
    def __init__(self):
        pass
        
    def csv_to_json_converter(self, filepath: str) -> list:
        try: 
            data = pd.read_csv(filepath)
            data.reset_index(drop=True, inplace=True)
            # JSON conversion line perfectly optimized
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            # FIXED: Commas ko hataya taaki yeh strict strings rahein
            self.database_name = database
            self.collection_name = collection
            self.records = records
            
            # FIXED: SSL Certificate validation (ca) pass kiya Cloud connection ke liye
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)  
            
            self.db = self.mongo_client[self.database_name]
            self.coll = self.db[self.collection_name]
            
            # Records push logic execution
            self.coll.insert_many(self.records)
            return len(self.records)   
        except Exception as e:
             raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    Filepath = "D:\\Projects2026\\networkSecurity\\Network_Data\\phisingData.csv"
    DATABASE = "ABHIVYAKTIJHA2206_DB" 
    Collection = "Network_Data"  
    
    networkobject = NetworkDataExtract()
    records = networkobject.csv_to_json_converter(Filepath)
    
    no_of_records = networkobject.insert_data_mongodb(records=records, database=DATABASE, collection=Collection)
    print(f"Successfully inserted {no_of_records} records into MongoDB!")