# fast api endpoint for segmenting_anything

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
import numpy as np  


app = FastAPI()


@app.post("/segment_anything")
async def segment_anything(image: str, clue: str):
    # calls the segment anything api
    pass