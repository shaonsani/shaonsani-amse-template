import pandas as pd
import numpy as np
import sqlite3 as sqlite
import time


class DataPipeline:
    def __init__(self):
        self.data_source_1_url = "https://www.mcloud.de/downloads/mcloud/27899FD1-EBC5-428D-9214-996752F42EBB/AirQuality_Datensatz_August2021_Aachen.csv"
        self.data_source_2_url = "https://meteostat.net/en/station/10501?t=2021-08-01/2021-08-31"
        self.weather_aachen_1 = None
        self.weather_aachen_2 = None
        self.conn = None
        self.load_data()
        self.save_to_db()
        
    def prepare_database(self):
        self.conn = sqlite.connect("saki.sqlite")
        
        
    def load_data(self):
        self.aachen_mobilithek = pd.read_csv(self.data_source_1_url)
        self.aachen_mobilithek = self.transform_new_aachen_dataset()
        self.aachen_meteostat = pd.read_csv("static_dataset/aachen_august_dataset.csv")
        self.aachen_meteostat.drop(["snow", "tsun", "coco"], inplace=True, axis=1)
        
    def transform_new_aachen_dataset(self):
        modified_dataset = pd.DataFrame({
            "parameter": self.aachen_mobilithek["DataType"],
            "value": self.aachen_mobilithek["AverageValue"],
            "NumberOfVehicles": self.aachen_mobilithek["NumberOfVehicles"],
            "Geohash7": self.aachen_mobilithek["Geohash7"],
            "Period": self.aachen_mobilithek["Period"]
        })
        return modified_dataset
    
    def save_to_db(self):
        self.prepare_database()
        self.aachen_mobilithek.to_sql(name="aachen_mobilithek", con=self.conn, if_exists="replace", index=False)
        self.aachen_meteostat.to_sql(name="aachen_meteostat", con=self.conn, if_exists="replace", index=False)
        self.conn.close()
        

object = DataPipeline()
        
        
        