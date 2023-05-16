# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes weather data from two data sources for Aachen. 
Both weather datasets contain important meteorological data like temperature, humidity, and PM2.5, PM10, Wind Speed. 


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

### Datasource2: Aachen weather data.
* Metadata URL: https://meteostat.net/en/station/10501?t=2023-04-19/2023-04-26
* Data URL: https://meteostat.net/en/station/10501?t=2023-04-19/2023-04-26
* Data Type: CSV

This dataset contains Aachen weather data with parameters of Datetime, Air Pressure, Temperature, Wind Speed.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Preprocess Luftqualitätsdaten August 2021 dataset [#1][i1]
2. Create datapipeline [#2][i6]
3. Remove unwanted columns from Aachen Weather Dataset  [#3][i2]
4. Load data into database [#4][i3]
5. Write automated test case [#5][i7]
6. Data analysis and make correlation [#6][i4]
7. Visualization [#7][i5]

[i1]: https://github.com/shaonsani/shaonsani-amse-template/issues/1
[i2]: https://github.com/shaonsani/shaonsani-amse-template/issues/2
[i3]: https://github.com/shaonsani/shaonsani-amse-template/issues/3
[i4]: https://github.com/shaonsani/shaonsani-amse-template/issues/4
[i5]: https://github.com/shaonsani/shaonsani-amse-template/issues/5
[i6]: https://github.com/shaonsani/shaonsani-amse-template/issues/6
[i7]: https://github.com/shaonsani/shaonsani-amse-template/issues/7
