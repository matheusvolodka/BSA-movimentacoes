import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('credentials.env')

########################################################################
class Extraction:
    def __init__(self):
        self.uri = 'https://api.football-data.org/v4/competitions/'
        self.endpoint = 'BSA/teams'
        self.api_key = os.getenv("API_KEY")
        self.headers = {'X-Auth-Token': f'{self.api_key}'}
        self.raw_data = None
        self.path = None
        self.dir_name = None
        self.date = datetime.today().strftime('%Y-%m-%d')

    def extract(self):
        response = requests.get(f'{self.uri}{self.endpoint}', headers=self.headers)
        if response.status_code == 200:
            self.raw_data = response.json()
        else:
            print(f"Erro de requisição{response.status_code}")
            self.raw_data = None
    
    def create_dir(self):
        self.dir_name = f'{self.endpoint}-{self.date}'
        os.makedirs(f'../{self.dir_name}', exist_ok=True)

    def save(self, data):
        if data:
            self.path = f'../{self.dir_name}/teams-{self.date}.json'
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f'Dados salvos em: {self.path}')
        else:
            print("Nenhum dado para salvar.")
    
    def run(self):
        self.extract()
        self.create_dir()
        self.save(self.raw_data)
        return self.path
########################################################################

if __name__=='__main__':
    extractor = Extraction()
    extractor.run()