# this was done on google colab
!sudo apt-get install python3-dev default-libmysqlclient-dev
!pip install pymysql sqlalchemy

from sqlalchemy import create_engine

import pandas as pd

MYSQL_HOSTNAME = '35.239.123.178'
MYSQL_USER = 'reshad'
MYSQL_PASSWORD = 'reshad11'
MYSQL_DATABASE = 'db1'
# had trouble setting up the .env file for this

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string

db = create_engine(connection_string)

db

query = 'select * from db1.table1;'
query

df = pd.read_sql(query, con=db)

real_df = pd.read_csv('https://healthdata.gov/resource/aitj-yx37.csv')
real_df

real_df.to_sql('table2', con=db, if_exists='replace')



sql_query = """ select * from db1.table2 where state = 'AL' """;

results_47 = pd.read_sql(sql_query, con=db)

results_47