#!/usr/bin/env python
# coding: utf-8

import os

def pipeline(params):
    print('starting pipeline execution...')

    user = params.get('user')
    pw = params.get('password')
    host = params.get('host')
    port = params.get('port')
    db = params.get('db')
    table_name = params.get('table')
    url = params.get('url')

    # import dependencies
    import pandas as pd
    from sqlalchemy import create_engine

    # Setup Database Engine
    db_engine = create_engine(f'postgresql://{user}:{pw}@{host}:{port}/{db}')

    # Download CSV
    # csv_name = './yellow_tripdata_2021-01.csv'
    csv_name = 'taxi.csv'
    os.system(f'wget {url} -O {csv_name}')

    # Ingest data
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)


    # Ingest data in chunks
    for chunk in df_iter:
        # logging
        print('====================================')
        print('inserting chunk..........')

        # clean chunk data:
        # - convert timestamps to datetime type
        chunk.tpep_dropoff_datetime = pd.to_datetime(chunk.tpep_dropoff_datetime)
        chunk.tpep_pickup_datetime = pd.to_datetime(chunk.tpep_pickup_datetime)
    
        # insert into postgresql
        chunk.to_sql(name=table_name, con=db_engine, if_exists='append')

        # logging
        print('inserted chunk')

    print('✅✅✅✅ finished  pipeline execution')


if __name__ == '__main__':
    pipeline(os.environ)
