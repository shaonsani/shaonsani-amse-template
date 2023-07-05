import zipfile
import urllib.request
import pandas as pd
import sqlalchemy

class Exercise5:
    def __init__(self):
        self.data_url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
        self.engine = sqlalchemy.create_engine("sqlite:///gtfs.sqlite")
        self.zip_filename = "GTFS.zip"
        self.data = None

    def load_data(self):
        urllib.request.urlretrieve(self.data_url, self.zip_filename)
        with zipfile.ZipFile(self.zip_filename, 'r') as zip:
            zip.extractall("./exercises/data/")
    
    def validation(self):
        self.data = pd.read_csv("./exercises/data/stops.txt", sep=",")
        self.data = self.data[["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]]
        self.data = self.data[self.data["zone_id"] == 2001]
        self.data = self.data[(self.data["stop_lat"] >= -90) & (self.data["stop_lat"] <= 90)]
        self.data = self.data[(self.data["stop_lon"] >= -90) & (self.data["stop_lon"] <= 90)]
        #self.data = self.data[self.data['stop_name'].str.contains('[^a-zA-Z0-9äöüÄÖÜß]+')]
    
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
        print("Solving Exercise 5.........!")
        print("Loading Data.........!")
        self.load_data()
        print("Validating Data.........!")
        self.validation()
        self.save_to_database()


object = Exercise5()
object.solve()