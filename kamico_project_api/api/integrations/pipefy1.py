import requests
import os
import json
from urllib.parse import urljoin
import graphene
import dotenv
import pandas as pd


dotenv.load_dotenv()
class Pipefy:
    def __init__(self,):
        self.base_url = 'https://api.pipefy.com/graphql'
        self.token = os.getenv('PIPEFY_TOKEN')
        self.id_email = os.getenv('PIPEFY_ID_EMAIL')
        self.headers = {
            'Authorization': f'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEyNDU0NTAsImVtYWlsIjoiYWRyaWFuYWtvamFAa2FtaWNvLmNvbS5iciIsImFwcGxpY2F0aW9uIjozMDAyMjcxNDJ9fQ.yyzo-qbInk_CYQJuazYJU4HSv68ZKWLdIL5AwZ_Xv9vgrcw6vTs4iJ5Se9LZE5-gDMaPBsO1MJ2zH1TyZLDBEQ',
            'Accept': 'application/json'}

    def get_cards_of_pipes(self,):
        url = self.base_url
        id = 301673526

        
        datacards = {
            "query":
               "{allCards (pipeId: 301673526) {edges {node {id title attachments_count\
                checklist_items_checked_count checklist_items_count comments_count createdAt creatorEmail current_phase_age done due_date emailMessagingAddress expired finished_at inboxEmailsRead late path started_current_phase_at suid updated_at url uuid} }}}"
        }
        
        response = requests.post(url, json=datacards, headers=self.headers)
        if response.status_code == 200:
            print(f'Requisição bem sucedida para o pipeId: {id}')
            print('Planilha pipefy_{}.xlsx criada com sucesso!'.format(id))
        
        pipes_list = []
        # criar um looping e iterar sobre o json para pegar todos os cards
        for i in json.loads(response.text)['data']['allCards']['edges']:
            #print(i['node']['title'])
            pipes_rows = [
                i['node']['id'],
                i['node']['title'],
                i['node']['attachments_count'],
                i['node']['checklist_items_checked_count'],
                i['node']['checklist_items_count'],
                i['node']['comments_count'],
                i['node']['createdAt'],
                i['node']['creatorEmail'],
                i['node']['current_phase_age'],
                i['node']['done'],
                i['node']['due_date'],
                i['node']['emailMessagingAddress'],
                i['node']['expired'],
                i['node']['finished_at'],
                i['node']['inboxEmailsRead'],
                i['node']['late'],
                i['node']['path'],
                i['node']['started_current_phase_at'],
                i['node']['suid'],
                i['node']['updated_at'],
                i['node']['url'],
                i['node']['uuid'],
        ]
            pipes_list.append(pipes_rows)
            
            columns = ['id', 'title', 'attachments_count', 'checklist_items_checked_count', 'checklist_items_count',
                'comments_count', 'createdAt', 'creatorEmail', 'current_phase_age', 'done','due_date',
                'emailMessagingAddress', 'expired', 'finished_at', 'inboxEmailsRead', 'late', 'path',
                'started_current_phase_at', 'suid', 'updated_at', 'url', 'uuid']

            pipes_df = pd.DataFrame(pipes_list, columns=columns)
            pipes_df.to_excel(f'pipefy_{id}.xlsx', index=False)

    
    def create_card(self, pipe_id):
        url = urljoin(self.base_url, 'pipes/{}/cards'.format(pipe_id))
        data = {}
        response = requests.post(url, headers=self.headers, payload = json.dumps(data))
        return response.json()    

    
    def get_card(self, card_id):
        url = urljoin(self.base_url, 'cards/{}'.format(card_id))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments(self, card_id):
        url = urljoin(self.base_url, 'cards/{}/comments'.format(card_id))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_user(self, card_id, user_id):
        url = urljoin(self.base_url, 'cards/{}/comments?user_id={}'.format(card_id, user_id))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_user_and_date(self, card_id, user_id, date):
        url = urljoin(self.base_url, 'cards/{}/comments?user_id={}&date={}'.format(card_id, user_id, date))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_date(self, card_id, date):
        url = urljoin(self.base_url, 'cards/{}/comments?date={}'.format(card_id, date))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_date_and_user(self, card_id, date, user_id):
        url = urljoin(self.base_url, 'cards/{}/comments?date={}&user_id={}'.format(card_id, date, user_id))
        response = requests.post(url, headers=self.headers)
        return response.json()
    
    def get_card_comments_by_date_and_user_and_text(self, card_id, date, user_id, text):
        url = urljoin(self.base_url, 'cards/{}/comments?date={}&user_id={}&text={}'.format(card_id, date, user_id, text))
        response = requests.post(url, headers=self.headers)
        return response.json()
    
    def get_card_comments_by_date_and_text(self, card_id, date, text):
        url = urljoin(self.base_url, 'cards/{}/comments?date={}&text={}'.format(card_id, date, text))
        response = requests.post(url, headers=self.headers)
        return response.json()
    
    def get_card_comments_by_user_and_text(self, card_id, user_id, text):
        url = urljoin(self.base_url, 'cards/{}/comments?user_id={}&text={}'.format(card_id, user_id, text))
        response = requests.post(url, headers=self.headers)
        return response.json()
    
    def get_card_comments_by_text(self, card_id, text):
        url = urljoin(self.base_url, 'cards/{}/comments?text={}'.format(card_id, text))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_user_and_date_and_text(self, card_id, user_id, date, text):
        url = urljoin(self.base_url, 'cards/{}/comments?user_id={}&date={}&text={}'.format(card_id, user_id, date, text))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_date_and_user_and_text(self, card_id, date, user_id, text):
        url = urljoin(self.base_url, 'cards/{}/comments?date={}&user_id={}&text={}'.format(card_id, date, user_id, text))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_date_and_text(self, card_id, date, text):
        url = urljoin(self.base_url, 'cards/{}/comments?date={}&text={}'.format(card_id, date, text))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_user_and_text(self, card_id, user_id, text):
        url = urljoin(self.base_url, 'cards/{}/comments?user_id={}&text={}'.format(card_id, user_id, text))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_card_comments_by_text(self, card_id, text):
        url = urljoin(self.base_url, 'cards/{}/comments?text={}'.format(card_id, text))
        response = requests.post(url, headers=self.headers)
        return response.json()

    def email(self, card_id, email):
        url = urljoin(self.base_url, 'cards/{}/email'.format(card_id))
        response = requests.post(url, headers=self.headers, data={'email': email})
        return response.json()



if __name__ == '__main__':
    client = Pipefy()
    client.get_cards_of_pipes()