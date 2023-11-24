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
    """
    Index page
    """
    return FileResponse("./templates/index.html")


@router.post("/message")
async def human_message(request: Request, chat_message: str = Form(...)):
    """
    Returns the human message template with the content of the input form.
    It also swaps the input form to clear it.
    """

    time.sleep(0.1)
    # Pause to avoid replacing the input form before /answer has been called
    return templates.TemplateResponse(
        "message.html", {"request": request, "txt": chat_message}
    )


@router.post("/answer")
def ai_message(request: Request, chat_message: str = Form(...)):
    """
    Returns the ai_message template with the answer from pandasAI.
    """
    answer_type, answer_value, _ = get_answer(df, chat_message=chat_message)
    # Pause to avoid message/answer inversion when loading the answer from cache
    time.sleep(0.1)

    return templates.TemplateResponse(
        "ai_message.html",
        {"request": request, "type": answer_type, "value": answer_value},
    )
