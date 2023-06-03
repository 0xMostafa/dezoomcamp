#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
from sqlalchemy import create_engine

def download_trip_data():
    os.system('wget -N https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz')
    os.system('gzip -d green_tripdata_2019-01.csv.gz')

def download_zones_data():
    os.system('wget -N https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv')

def db_conn(params):
    user = params.get('user')
    pw = params.get('password')
    host = params.get('host')
    port = params.get('port')
    db = params.get('db')

    # Setup Database Engine
    db_engine = create_engine(f'postgresql://{user}:{pw}@{host}:{port}/{db}')
    return db_engine

def zones_pipeline(params):
    print('starting zones pipeline execution...')
    file_name = 'taxi+_zone_lookup.csv'
    db = db_conn(params)
    table = 'zones'
    df_iter = pd.read_csv(file_name, iterator=True, chunksize=10000)
    # Ingest data in chunks
    for chunk in df_iter:
        # logging
        print('====================================')
        print('inserting chunk..........')
        # insert into postgresql
        chunk.to_sql(name=table, con=db, if_exists='append')

        # logging
        print('inserted chunk')
    print('✅✅✅✅ finished zones pipeline execution')

def trip_pipeline(params):
    print('starting trip pipeline execution...')
    file_name = 'green_tripdata_2019-01.csv'
    db = db_conn(params)
    table = 'trips'
    df_iter = pd.read_csv(file_name, iterator=True, chunksize=10000)
    # Ingest data in chunks
    for chunk in df_iter:
        # logging
        print('====================================')
        print('inserting chunk..........')

        # clean chunk data:
        # - convert timestamps to datetime type
        chunk.lpep_pickup_datetime = pd.to_datetime(chunk.lpep_pickup_datetime)
        chunk.lpep_dropoff_datetime = pd.to_datetime(chunk.lpep_dropoff_datetime)

        # insert into postgresql
        chunk.to_sql(name=table, con=db, if_exists='append')

        # logging
        print('inserted chunk')
    print('✅✅✅✅ finished trip pipeline execution')

if __name__ == '__main__':
    # download the data
    download_trip_data()
    download_zones_data()

    # run pipelines
    zones_pipeline(os.environ)
    trip_pipeline(os.environ)
