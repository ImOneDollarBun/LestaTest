from fastapi import APIRouter, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from math import log
from collections import Counter

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/')
async def operate(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")
    words = [word.lower() for word in text.split() if word.isalpha()]
    total_docs = 1

    tf_counter = Counter(words)

    tf_idf_data = []
    for word, count in tf_counter.items():
        tf = count
        idf = log((total_docs + 1) / (1 + 1)) + 1
        tf_idf_data.append((word, tf, round(idf, 4)))

    tf_idf_data.sort(key=lambda x: x[2], reverse=True)
    top_words = tf_idf_data[:50]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "words": top_words
    })