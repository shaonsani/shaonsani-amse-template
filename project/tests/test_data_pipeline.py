import pandas as pd
import pytest
import subprocess
import os, time


@pytest.fixture(scope="module")
def aachen_mcloud_airquality_data_url():
    return "https://www.mcloud.de/downloads/mcloud/27899FD1-EBC5-428D-9214-996752F42EBB/AirQuality_Datensatz_August2021_Aachen.csv"

@pytest.fixture(scope="module")
def aachen_meteostat_airquality_data_path():
    return "./data/static_dataset/aachen_2.csv"

@pytest.fixture(scope="module")
def aachen_mcloud_airquality_data(aachen_mcloud_airquality_data_url):
    # Load the air quality dataset from url
    return pd.read_csv(aachen_mcloud_airquality_data_url)

@pytest.fixture(scope="module")
def aachen_meteostat_airquality_data(aachen_meteostat_airquality_data_path):
    # Load the air quality dataset from path
    return pd.read_csv(aachen_meteostat_airquality_data_path)

def test_aachen_mcloud_airquality_loaded(aachen_mcloud_airquality_data):
    # Check if the air quality dataset is not empty
    assert not aachen_mcloud_airquality_data.empty, 'Air Quality dataset is empty.'

def test_aachen_meteostat_airquality_loaded(aachen_meteostat_airquality_data):
    # Check if the air quality dataset is not empty
    assert not aachen_meteostat_airquality_data.empty, 'Air Quality dataset is empty.'

def test_aachen_mcloud_airquality_dataset_columns_exist(aachen_mcloud_airquality_data):
    # Check if the required columns exist in the dataset
    required_columns = ['DataType', 'TimeStep', 'AverageValue']
    assert all(col in aachen_mcloud_airquality_data.columns for col in required_columns), 'Required columns do not exist in the dataset.'

def test_temperature_range(aachen_meteostat_airquality_data):
    # Check if the temperature values are within a valid range
    min_temp = aachen_meteostat_airquality_data['tmin'].min()
    max_temp = aachen_meteostat_airquality_data['tmax'].max()
    assert min_temp >= -50, 'Invalid temperature range.'
    assert max_temp <= 50, 'Invalid temperature range.'

"""
System-test level
"""

def test_pipeline_execution():
    # Trigger the execution of the data processing pipeline
    try:
        os.chdir('./data')
        subprocess.run(['python', 'data_pipeline.py'])
        time.sleep(30)
        assert os.path.exists("saki.sqlite"), f"sqlite file 'saki.sqlite' not found."
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Pipeline execution failed with error code {e.returncode}.")