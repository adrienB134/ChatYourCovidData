from pandasai.responses import ResponseParser
from pandasai import SmartDataframe, SmartDatalake
from pandasai.llm import OpenAI

# from pandasai.callbacks import FileCallback
from pandasai.helpers.openai_info import get_openai_callback
from pandasai.schemas.df_config import Config
from pandasai import clear_cache
from typing import Any, Annotated

import os


def init():
    class ResponseTuned(ResponseParser):
        _context = None

        def __init__(self, context) -> None:
            super().__init__(context)

        def format_plot(self, result: dict) -> Any:
            """
            Does nothing besides overriding the parent method
            Hack to be cleaned up later
            """

    clear_cache()

    API_KEY = os.environ.get("OPENAI_KEY")
    user_defined_path = os.getcwd() + "/static/png"
    llm = OpenAI(api_token=API_KEY)
    config__ = {
        "llm": llm,
        "save_charts": True,
        "open_charts": False,
        "data_viz_library": "plotly",
        "save_charts_path": "./static/png/",
        "response_parser": ResponseTuned,
        "verbose": True,
    }

    df = SmartDataframe("data.csv", config=Config(**config__))
    # dl = SmartDatalake([df], config=Config(**config__))

    return df


def get_answer(df, chat_message):
    with get_openai_callback() as cb:
        df.chat(chat_message)
        response = df.last_result
        try:
            answer_type = response.get("type")
            answer_value = response.get("value")
        except:
            answer_type = "string"
            answer_value = "I'm sorry I couldn't get an answer please rephrase."
    return answer_type, answer_value
