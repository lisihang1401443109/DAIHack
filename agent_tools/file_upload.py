# a file upload endpoint

from fastapi import FastAPI
from fastapi import File, UploadFile

import json
import numpy as np
import os


app = FastAPI()


@app.post("/file_upload")
async def file_upload(file: UploadFile = File(...)):
    # return whether the file is successfully uploaded
    pass 