import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from assistant.assistant_controller import  controller as AssistantAudioController
from project_config import setup_app_config


# initialise all the variable
setup_app_config()
app = FastAPI()


@app.get("/healthcheck")
async def health_check():
    return {"message": "The health check is successful"}

origins =[
    "http://localhost",
    "http://localhost:5173",
    "*"
]


app.include_router(AssistantAudioController,tags=['assistant'])
app.add_middleware(

    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)