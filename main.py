"""Service entry point"""

from os import getenv

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect

from routes import api_router
load_dotenv()
app = FastAPI()

connect(host=getenv("I_HIRE_MONGO_URL").replace('"', ''))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
async def main():
    """Entry point"""
    return {"message": "Welcome to Kemdi Attire's AI service ⚡️"}


@app.get("/ping")
async def ping():
    """Check service status"""
    return {"status": True}
