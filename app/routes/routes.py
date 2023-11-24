from fastapi import APIRouter, Form, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from .pandasai import init, get_answer

import time


df = init()

router = APIRouter()
templates = Jinja2Templates(directory="./templates")


@router.get("/")
async def index():
    return FileResponse("./templates/index.html")


@router.post("/message")
async def human_message(request: Request, chat_message: str = Form(...)):
    return templates.TemplateResponse(
        "message.html", {"request": request, "txt": chat_message}
    )


@router.post("/answer")
def analytics(request: Request, chat_message: str = Form(...)):
    answer_type, answer_value = get_answer(df, chat_message=chat_message)
    # Pause to avoid message/answer inversion when loading the answer from cache
    time.sleep(0.1)
    print(answer_value)
    return templates.TemplateResponse(
        "chart.html",
        {"request": request, "type": answer_type, "img": answer_value},
    )
