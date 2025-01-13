from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

class Database:
    instance = None
    client = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            load_dotenv()

            cls.instance = super().__new__(cls, *args, **kwargs)
            cls.client = cls.create_client()
        return cls.instance
    
    @staticmethod
    def create_client():
        uri = os.getenv("MONGO_URI")

        return AsyncIOMotorClient(uri)
    
    def get_db(self, db_name: str):
        if not self.client:
            raise Exception("Database client is not initialized")
        
        print("Database connection established")
        return self.client[db_name]
    
    def close(self):
        if self.client:
            self.client.close()
            print("Database connection closed")

connection = Database()