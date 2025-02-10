from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Hardcoded MongoDB URI (replace this with your MongoDB Atlas URI)
mongo_uri = "mongodb+srv://workspace:workspace@flames.cj67n.mongodb.net/?retryWrites=true&w=majority&appName=flames"

# Connect to MongoDB
client = MongoClient(mongo_uri)

# Connect to your database and collection
db = client["flames_game_db"]
collection = db["results"]

# Define Pydantic model for input validation
class FlamesResult(BaseModel):
    name1: str
    name2: str
    result: str

@app.post("/save_flames_result/")
async def save_flames_result(data: FlamesResult):
    # Save result to MongoDB
    result_data = {
        "name1": data.name1,
        "name2": data.name2,
        "result": data.result
    }
    collection.insert_one(result_data)
    return {"status": "Data saved to MongoDB!"}
