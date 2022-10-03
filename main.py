# -*- coding: utf-8 -*-
# from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def healthy():
    return {"Health": "Everything is fine ;)"}


# @app.get("/strains/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
