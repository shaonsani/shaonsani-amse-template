# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes weather data from two german cities (Jena and Aachen). 
Both cities weather datasets contain important meteorological data like temperature, humidity, and PM2.5, PM10, Co2. 


## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis helps to make correlation between temperature vs other parameters. In addition, it helps to find a pattern if there is any environmental relationship between temperature and other parameters exist or not.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Luftqualitätsdaten August 2021
* Metadata URL: https://mobilithek.info/offers/-6211083015561254713
* Data URL: https://www.mcloud.de/downloads/mcloud/27899FD1-EBC5-428D-9214-996752F42EBB/AirQuality_Datensatz_August2021_Aachen.csv
* Data Type: CSV

This dataset contains Aachen weather data with parameters of MinValue, MaxValue, AvgValue, DataType(Temperature, Pm2.5, Humidity) and Timesteps.

### Datasource2: Jena Weather Dataset
* Metadata URL: https://www.kaggle.com/datasets/harishedison/jena-weather-dataset?resource=download
* Data URL: https://www.kaggle.com/datasets/harishedison/jena-weather-dataset?resource=download
* Data Type: CSV

This dataset contains Jena weather data with parameters of Datetime, pressure, Temperature, Rain, Co2.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Preprocess Luftqualitätsdaten August 2021 dataset [#1][i1]
2. Preprocess Luftqualitätsdaten August 2021 dataset [#2][i2]
3. Load data into database [#3][i3]
4. Data analysis and make correlation [#4][i4]
5. Visualization [#5][i5]

[i1]: https://github.com/shaonsani/shaonsani-amse-template/issues/1
[i2]: https://github.com/shaonsani/shaonsani-amse-template/issues/2
[i3]: https://github.com/shaonsani/shaonsani-amse-template/issues/3
[i4]: https://github.com/shaonsani/shaonsani-amse-template/issues/4
[i5]: https://github.com/shaonsani/shaonsani-amse-template/issues/5
