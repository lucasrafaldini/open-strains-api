# -*- coding: utf-8 -*-
# from typing import Union

from fastapi import FastAPI
from services.gist_service import GistService


app = FastAPI()


@app.get("/")
def healthy():
    return {"Health": "Everything is fine ;)"}


@app.get("/strains/")
def get_all_strains():
    service = GistService()
    response = service.get_gist()
    return response
