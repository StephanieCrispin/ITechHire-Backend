"""Service entry point"""


import asyncio
import aiohttp

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


async def ping_self():
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://itechhire-backend.onrender.com"):
                print("Ping successful")
        await asyncio.sleep(200)  # Sleep for 5 minutes (300 seconds)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(ping_self())


@app.get("/")
async def main():
    """Entry point"""
    return {"message": "Welcome to ITechHire Backend Service ⚡️"}


@app.get("/ping")
async def ping():
    """Check service status"""
    return {"status": True}
