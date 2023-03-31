import requests
import os
import json
from urllib.parse import urljoin
import graphene


class Pipefy:
    def __init__(self,):
        self.base_url = 'https://api.pipefy.com/graphql'
        self.api_key = os.getenv('PIPEFY_API_KEY')
        self.id_email = os.getenv('PIPEFY_ID_EMAIL')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json'}

    