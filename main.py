# -*- coding: utf-8 -*-
# from typing import Union

from fastapi import FastAPI, Response, status
from difflib import SequenceMatcher
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

@app.get("/strains/search/{strain_name}", status_code=status.HTTP_200_OK)
def get_strain_by_name(strain_name: str, response: Response):
    service = GistService()
    all_strains = service.get_gist()
    result = []
    result.append(strain for strain in all_strains if SequenceMatcher(None, str(strain["name"]).lower(), strain_name.lower()).ratio() > 0.6)
    if result:
       return result
    response.status_code = status.HTTP_404_NOT_FOUND

@app.get("/strains/{strain_name}", status_code=status.HTTP_200_OK)
def get_strain_by_name(strain_name: str, response: Response):
    service = GistService()
    all_strains = service.get_gist()
    result = next((strain for strain in all_strains if str(strain["name"]).lower() == strain_name.lower()), None)
    if result:
       return result
    response.status_code = status.HTTP_404_NOT_FOUND
