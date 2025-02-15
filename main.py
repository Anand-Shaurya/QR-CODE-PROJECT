from fastapi import FastAPI
import qrcode
from io import BytesIO
from PIL import Image
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get('/')
def home_page():
    return {"status":"success"}


@app.get('/qr')
def qr_code_generator(text : str):
    img = qrcode.make(text)
    image_stream = BytesIO()
    img.save(image_stream, format="PNG")
    image_stream.seek(0)
    return StreamingResponse(image_stream, media_type="image/png")

