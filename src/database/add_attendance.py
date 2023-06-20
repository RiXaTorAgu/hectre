from datetime import time

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Attendance

if __name__ == '__main__':

    records = pd.read_csv('Registro asistencia.txt', delimiter='\t', usecols=['ID', 'Hora'])
    records = records.rename(columns={'ID': 'ID_EMPLOYEE', 'Hora': 'TIME'})

    records['TIME'] = pd.to_datetime(records['TIME'], format=' %Y-%m-%d     %H:%M:%S')
    records['DATE'] = records['TIME'].dt.date
    records['TIME'] = records['TIME'].dt.time

    records = records.groupby(['ID_EMPLOYEE', 'DATE']).agg({'TIME': ['min', 'max']})
    records.columns = ['START_TIME', 'END_TIME']

    for index, record in records.iterrows():

        start_time = record['START_TIME']
        end_time = record['END_TIME']

        if start_time == end_time and end_time < time(12, 0):

            records.loc[index, 'END_TIME'] = None

        elif start_time == end_time and time(12, 0) < start_time:

            records.loc[index, 'START_TIME'] = None
    
    records = records.reset_index()

    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    for _, record in records.iterrows():

        date = record['DATE']
        id_employee = record['ID_EMPLOYEE']
        start_time = record['START_TIME']
        end_time = record['END_TIME']

        session.merge(Attendance(date, id_employee, start_time, end_time))

    session.commit()
    session.close()