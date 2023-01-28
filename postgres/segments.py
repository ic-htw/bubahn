import pandas as pd
from sqlalchemy import create_engine, text

import const as c

engine = create_engine(
    f'postgresql://{c.pg_userid}:{c.pg_password}@{c.pg_host}/{c.pg_db}', 
    connect_args = {'options': '-c search_path=umobility,public', 'keepalives_idle': 120},
    pool_size=1, 
    max_overflow=0,
    execution_options={ 'isolation_level': 'AUTOCOMMIT' }
)

with engine.connect() as con:
    sql = "select * from segment"
    segment_pdf = pd.read_sql_query(text(sql), con)
    
    
segment_pdf.to_csv("segment.csv", index=False)

engine.dispose()