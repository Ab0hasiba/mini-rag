from fastapi import FastAPI, APIRouter
 

ini_router=APIRouter()
@ini_router.get("/")
def welcome():
    return {
        "message":
        "Welcome to the Mini RAG API"
        }

