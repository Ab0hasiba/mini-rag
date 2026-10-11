from fastapi import FastAPI, APIRouter
import os

ini_router=APIRouter(
    prefix='/api/version1',
    tags=['api_v1'],
)
@ini_router.get("/")
async def welcome():
    appname=os.getenv('APP_NAME')
    appversion=os.getenv('APP_VERSION')
    return {
        'appname' : appname,
        'appversion' : appversion,
    }


