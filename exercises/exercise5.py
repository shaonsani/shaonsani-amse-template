import requests, zipfile, io
import pandas as pd
import sqlalchemy

class Exercise5:
    def __init__(self):
        self.data_url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
        self.engine = sqlalchemy.create_engine("sqlite:///gtfs.sqlite")
        self.data = None

    def load_data(self):
        r = requests.get(self.data_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./exercises/data/")
    
    def steps(self):
        self.data = pd.read_csv("./exercises/data/stops.txt", sep=",")
        self.data = self.data[["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]]
        self.data = self.data[self.data["zone_id"] == 2001]
        self.data = self.data[(self.data["stop_lat"] >= -90) & (self.data["stop_lat"] <= 90)]
        self.data = self.data[(self.data["stop_lon"] >= -90) & (self.data["stop_lon"] <= 90)]
        self.data = self.data[self.data['stop_name'].str.contains('[^a-zA-Z0-9äöüÄÖÜß]+')]
    
    def save_to_database(self):
        column_types = {
                    'stop_id': sqlalchemy.Integer,
                    'stop_name': sqlalchemy.String(255),
                    'stop_lat': sqlalchemy.Float,
                    'stop_lon': sqlalchemy.Float,
                    'zone_id': sqlalchemy.Integer,
                }
        self.data.to_sql(name="stops", con=self.engine, if_exists="replace", index=False, dtype=column_types)

    def solve(self):
        self.load_data()
        self.steps()
        self.save_to_database()


object = Exercise5()
object.solve()