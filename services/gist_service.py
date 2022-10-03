# -*- coding: utf-8 -*-
import requests



class GistService:

    def __init__(self):
        self.address = "https://gist.githubusercontent.com/lucasrafaldini/ff873c2b3d4c5f587803a6e4d540b8c9/raw/9a02fd39ab2b50cb1482b6d02291f2bf6b75e049/strains-db.json"

    def get_gist(self):
        response = requests.get(self.address)
        return response.json()
