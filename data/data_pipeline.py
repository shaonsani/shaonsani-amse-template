import pandas as pd
import numpy as np
import sqlite3 as sqlite


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
        self.weather_aachen_1 = pd.read_csv(self.data_source_1_url)
        self.weather_aachen_1 = self.transform_new_aachen_dataset()
        self.weather_aachen_2 = pd.read_csv("Static_dataset/aachen_2.csv")
        self.weather_aachen_2 = self.weather_aachen_2.drop(["snow", "tsun"], axis=1)
        
        
    def transform_new_aachen_dataset(self):
        modified_dataset = pd.DataFrame(columns=["parameter", "value", "NumberOfVehicles", "Geohash7",  "Period"])
        for index, row in self.weather_aachen_1.iterrows():
            modified_row = {
                "parameter": row["DataType"], "value": row["AverageValue"], "NumberOfVehicles": row["NumberOfVehicles"],
                "Geohash7": row["Geohash7"], "Period": row["Period"]
            }
            modified_dataset.loc[index] = modified_row
        return modified_dataset
    
    def save_to_db(self):
        self.prepare_database()
        self.weather_aachen_1.to_sql(name="aachen_1", con=self.conn, if_exists="replace", index=False)
        self.weather_aachen_2.to_sql(name="aachen_2", con=self.conn, if_exists="replace", index=False)
        self.conn.close()
        

object = DataPipeline()
        
        
        