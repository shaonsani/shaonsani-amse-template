import pandas as pd
import pytest


@pytest.fixture(scope="module")
def aachen_mcloud_airquality_data_url():
    return "https://www.mcloud.de/downloads/mcloud/27899FD1-EBC5-428D-9214-996752F42EBB/AirQuality_Datensatz_August2021_Aachen.csv"

@pytest.fixture(scope="module")
def aachen_mcloud_airquality_data(aachen_mcloud_airquality_data_url):
    # Load the air quality dataset from url
    return pd.read_csv(aachen_mcloud_airquality_data_url)

def test_aachen_mcloud_airquality_loaded(aachen_mcloud_airquality_data):
    # Check if the air quality dataset is not empty
    assert not aachen_mcloud_airquality_data.empty, 'Air Quality dataset is empty.'