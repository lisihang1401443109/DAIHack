# a file upload endpoint

from fastapi import FastAPI
from fastapi import File, UploadFile

import json
import numpy as np
import os
from pathlib import Path

app = FastAPI()
cwd = Path(__file__).parent
file_dir = cwd / 'uploads'



@app.post("/file_upload")
async def file_upload(uuid: str, file: UploadFile = File(...),):
    # return whether the file is successfully uploaded
    content = await file.read()
    
    # store the file in a local directory
    with open(file_dir / uuid / 'user_image.png', "wb") as f:
        f.write(content)
    
    return {"success": True}