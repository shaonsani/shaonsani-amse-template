import pandas as pd
import numpy as np
import sqlite3 as sqlite


class Exercise:
    def __init__(self):
        self.data_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
        self.data = None
        
    def load_data(self):
        self.data = pd.read_csv(self.data_url, sep=";")
        
    def save_to_db(self):
        conn = sqlite.connect("airports.sqlite")
        column_types = {
            'column_1': 'INTEGER',
            'column_2': 'VARCHAR(255)',
            'column_3': 'VARCHAR(255)',
            'column_4': 'VARCHAR(255)',
            'column_5': 'VARCHAR(10)',
            'column_6': 'VARCHAR(10)',
            'coulmn_7': 'DOUBLE',
            'column_8': 'DOUBLE',
            'column_9': 'INTEGER',
            'column_10': 'FLOAT',
            'column_11': 'VARCHAR(10)',
            'column_12': 'VARCHAR(50)',
            'geo_punkt': 'DOUBLE'
        }
        data.to_sql(name="airports", con=conn, if_exists="replace", index=False,  dtype=column_types)
    def pipeline_process(self):
        self.load_data()
        self.save_to_db()

obj = Exercise().pipeline_process()
    

