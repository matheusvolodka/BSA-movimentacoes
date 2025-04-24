import json
import pandas as pd
from extraction import Extraction
from datetime import datetime

class Transform:
    def __init__(self, json_path):
        self.json_path = json_path
        self.data = None
        self.df = None
        self.filter_colums = ['area', 'runningCompetitions']
        self.date = datetime.today().strftime('%Y-%m-%d')

    def load_json(self):
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"Arquivo JSON não encontrado: {self.json_path}")
            self.data = None

    def to_dataframe(self):
        if self.data:
            teams = self.data['teams']
            self.df = pd.DataFrame(teams)
            for filtro in self.filter_colums:
                if filtro in self.df.columns:
                    self.df.drop(columns=[filtro], inplace=True)
                else:
                    print("Nenhum dado carregado no DataFrame")

        else:
            print("Nenhum dado carregado para transformar.")

    def save_csv(self):
        if self.df is not None:
            csv_path = self.json_path.replace('.json', '.csv')
            self.df.to_csv(csv_path, index=False)
            print(f"CSV salvo em: {csv_path}")

    def run(self):
        self.load_json()
        self.to_dataframe()
        self.save_csv()


if __name__ =="__main__":
    extractor = Extraction()
    json_path = extractor.run()
    transformer = Transform(json_path)
    transformer.run()
