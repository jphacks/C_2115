from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, File, UploadFile

from io import BytesIO
import io
import json
import base64
#from model import yolov5 as model
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sample API"}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

"""
@app.post("/api/objectdetection")
async def object_detection_file(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = Image.open(io.BytesIO(file_bytes))
    name = f"/data/{str(uuid.uuid4())}.png"
    # image.save(name)
    image.filename = name
    label = model(image)
    
    return 
"""
#@app.post("/api/searchlabel")
#async def serach_file_labels(file: UploadFile = File(...)):
#    return {"api": len(file)}


#データを画像に変換する
def read_image(bin_data, size=(256,256)):
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, size)
    return img    

def base64_encode_img(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    img_byte = buffered.getvalue()
    encoded_img = "data:image/png;base64," + base64.b64encode(img_byte).decode()
    return encoded_img

