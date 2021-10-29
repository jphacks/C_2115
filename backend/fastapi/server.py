from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, File, UploadFile
import cv2



app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/api/objectdetection")
async def object_detection_file(file: UploadFile = File(...)):
    return {"filename": len(file)}

@app.post("/api/searchlabel")
async def serach_file_labels(file: UploadFile = File(...)):
    return {"api": len(file)}


#データを画像に変換する
def read_image(bin_data, size=(256,256)):
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, size)
    return img    


