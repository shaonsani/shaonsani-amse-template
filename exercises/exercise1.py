import pandas as pd
import sqlalchemy

class Exercise:
    def __init__(self):
        self.data_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
        self.data = None
        
    def load_data(self):
        self.data = pd.read_csv(self.data_url, sep=";")
        
    def save_to_db(self):
        engine = sqlalchemy.create_engine("sqlite:///airports.sqlite")
        column_types = {
            'column_1': sqlalchemy.Integer,
            'column_2': sqlalchemy.String(255),
            'column_3': sqlalchemy.String(255),
            'column_4': sqlalchemy.String(255),
            'column_5': sqlalchemy.String(10),
            'column_6': sqlalchemy.String(10),
            'column_7': sqlalchemy.Float,
            'column_8': sqlalchemy.Float,
            'column_9': sqlalchemy.Integer,
            'column_10': sqlalchemy.Float,
            'column_11': sqlalchemy.String(10),
            'column_12': sqlalchemy.String(50),
            'geo_punkt': sqlalchemy.String(50)
        }
        self.data.to_sql(name="airports", con=engine, if_exists="replace", index=False, dtype=column_types)

    def pipeline_process(self):
        self.load_data()
        self.save_to_db()

obj = Exercise().pipeline_process()
