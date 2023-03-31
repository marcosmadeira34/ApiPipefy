import requests
import os
import json
from urllib.parse import urljoin


import pandas as pd



class Pipefy:
    def __init__(self,):
        self.base_url = 'https://api.pipefy.com/graphql'
        self.token = os.getenv('PIPEFY_TOKEN')
        self.id_email = os.getenv('PIPEFY_ID_EMAIL')
        self.headers = {
            'Authorization': f'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEyNDU0NTAsImVtYWlsIjoiYWRyaWFuYWtvamFAa2FtaWNvLmNvbS5iciIsImFwcGxpY2F0aW9uIjozMDAyMjcxNDJ9fQ.yyzo-qbInk_CYQJuazYJU4HSv68ZKWLdIL5AwZ_Xv9vgrcw6vTs4iJ5Se9LZE5-gDMaPBsO1MJ2zH1TyZLDBEQ',
            'Accept': 'application/json'}

    def get_cards_of_pipes(self):
        url = self.base_url        
        allpipes = pd.read_excel('kamico_project_api/api/integrations/all_pipes.xlsx')
        
        cards_list = []
        for pipe in allpipes['pipes']:                
            try:
                print(f'Pipe {pipe} - OK')
                query = f"""
                query MyQuery {{
                allCards(pipeId: "{pipe}", first: 100) {{
                    edges {{
                    cursor
                    node {{
                        age
                        assignees {{
                        avatarUrl
                        avatar_url
                        confirmationTokenHasExpired
                        confirmed
                        createdAt
                        created_at
                        departmentKey
                        displayName
                        email
                        hasUnreadNotifications
                        id
                        intercomHash
                        intercomId
                        invited
                        locale
                        name
                        phone
                        signupData
                        timeZone
                        time_zone
                        timezone
                        username
                        uuid
                        }}
                        attachments_count
                        checklist_items_checked_count
                        checklist_items_count
                        comments_count
                        createdAt
                        created_at
                        creatorEmail
                        current_phase_age
                        done
                        due_date
                        emailMessagingAddress
                        expired
                        finished_at
                        id
                        inboxEmailsRead
                        late
                        overdue
                        path
                        public_form_submitter_email
                        started_current_phase_at
                        suid
                        subtitles {{
                        array_value
                        date_value
                        datetime_value
                        filled_at
                        float_value
                        indexName
                        name
                        native_value
                        report_value
                        updated_at
                        value
                        }}
                        title
                        updated_at
                        url
                        uuid
                    }}
                    }}
                    pageInfo {{
                    endCursor
                    hasNextPage
                    hasPreviousPage
                    startCursor
                    }}
                }}
                }}
                """   

                payload = {
                    "query": query,
                    "variables": {"pipeId": pipe}
                }
            
                response = requests.post(url, headers=self.headers, json=payload)
                if response.status_code == 200:
                    print(f'Pipe {pipe} - OK')                   
                    
                
                for card in json.loads(response.text)['data']['allCards']['edges']:
                    cardId = card['node']['id']
                    print(f'Card {cardId} - OK')
                    
                    cards_row = [
                            card['node']['id'],
                            card['node']['title'],
                            card['node']['attachments_count'],
                            card['node']['checklist_items_checked_count'],
                            card['node']['checklist_items_count'],
                            card['node']['comments_count'],
                            card['node']['createdAt'],
                            card['node']['creatorEmail'],
                            card['node']['current_phase_age'],
                            card['node']['done'],
                            card['node']['due_date'],
                            card['node']['emailMessagingAddress'],
                            card['node']['expired'],
                            card['node']['finished_at'],
                            card['node']['inboxEmailsRead'],
                            card['node']['late'],
                            card['node']['path'],
                            card['node']['started_current_phase_at'],
                            card['node']['suid'],
                            card['node']['updated_at'],
                            card['node']['url'],
                            card['node']['uuid']
                            
                            ]        
                        
                    
                    cards_list.append(cards_row)

                            
            except TypeError as e:
                print(f'Erro gerado na Pipe: {pipe}. Pipe vazia ou não encontrada.')
                continue    

            colunas = ['id', 'title', 'attachments_count', 'checklist_items_checked_count', 
                        'checklist_items_count', 'comments_count', 'createdAt', 'creatorEmail', 
                        'current_phase_age', 'done', 'due_date', 'emailMessagingAddress', 'expired', 
                        'finished_at', 'inboxEmailsRead', 'late', 'path', 'started_current_phase_at', 
                        'suid', 'updated_at', 'url', 'uuid' ]

           
            df = pd.DataFrame(cards_list, columns=colunas)
            df.to_excel('kamico_project_api/api/integrations/allcards.xlsx', index=False)
            print('Arquivo salvo com sucesso!')
            card_lens = len(cards_list)
            print(f'Quantidade de cards encontrados: {card_lens}')
    
    def get_info_cards(self):
        url = self.base_url
        allcards = pd.read_excel('kamico_project_api/api/integrations/allcards.xlsx')

        info_cards = []
        for card in allcards['id']:
            try:
                print(f'Card {card} - OK')
                card_id = f"""
                    query {{
                    card(id: "{card}") {{
                        attachments {{
                            path
                            url
                        field {{
                            description
                            help
                            id
                            index
                            index_name
                            internal_id
                            label
                            options
                            type
                            uuid
                        }}
                        path
                        phase {{
                            can_receive_card_directly_from_draft
                            color
                            created_at
                            custom_sorting_preferences
                            description
                            done
                            expiredCardsCount
                        }}
                        }}
                        attachments_count
                        checklist_items_checked_count
                        checklist_items_count
                        comments_count
                        createdAt
                        creatorEmail
                        currentLateness {{
                        becameLateAt
                        id
                        shouldBecomeLateAt
                        sla
                        }}
                        current_phase {{
                        can_receive_card_directly_from_draft
                        cards_can_be_moved_to_phases {{
                            can_receive_card_directly_from_draft
                            color
                            created_at
                            custom_sorting_preferences
                            description
                            done
                            expiredCardsCount
                        }}
                        }}
                        current_phase_age
                        done
                        due_date
                        emailMessagingAddress
                        expired
                        finished_at
                        id
                        inboxEmailsRead
                        late
                        overdue
                        path
                        pipe {{
                        anyone_can_create_card
                        cards_count
                        }}
                        title
                        updated_at
                        url
                        uuid
                    }}
                    }}
                    """
                
                payload = {
                        "query": card_id,
                        "variables": {"id": card}
                    }
                

                response = requests.post(url, headers=self.headers, json=payload)
                if response.status_code == 200:
                    result = json.loads(response.text)
                for res in result['data']['card']['attachments']:
                    cards_rows = [
                            res['url']
                        ]
                    
                    info_cards.append(cards_rows)
                
                columns_cards = ['url']
                df = pd.DataFrame(info_cards, columns=columns_cards)
                df.to_excel('kamico_project_api/api/integrations/info_cards.xlsx', index=False)
                print('Anexos salvos com sucesso!')
                card_lens = len(info_cards)
                print(f'Quantidade de links encontrados: {card_lens}') 

            except TypeError as e:
                print(f'Erro gerado no card: {card}. Card vazio ou não encontrado.')
                continue
                                        


if __name__ == '__main__':
    pipefy = Pipefy()
    pipefy.get_cards_of_pipes()
    pipefy.get_info_cards()