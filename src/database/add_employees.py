import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Employee

if __name__ == '__main__':

    employees = pd.read_csv('employees.csv')
    employees = employees.replace(np.nan, None)

    employees['MIDWEEK_START_TIME'] = pd.to_datetime(employees['MIDWEEK_START_TIME'], format='%H:%M').dt.time
    employees['MIDWEEK_END_TIME'] = pd.to_datetime(employees['MIDWEEK_END_TIME'], format='%H:%M').dt.time
    employees['WEEKEND_START_TIME'] = pd.to_datetime(employees['WEEKEND_START_TIME'], format='%H:%M').dt.time
    employees['WEEKEND_END_TIME'] = pd.to_datetime(employees['WEEKEND_END_TIME'], format='%H:%M').dt.time

    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    for _, employee in employees.iterrows():

        id_employee = employee['ID_EMPLOYEE']
        first_name = employee['FIRST_NAME']
        last_name_1 = employee['LAST_NAME_1']
        last_name_2 = employee['LAST_NAME_2']
        midweek_start_time = employee['MIDWEEK_START_TIME']
        midweek_end_time = employee['MIDWEEK_END_TIME']
        weekend_start_time = employee['WEEKEND_START_TIME']
        weekend_end_time = employee['WEEKEND_END_TIME']

        session.merge(Employee(id_employee, first_name, last_name_1, last_name_2, midweek_start_time, midweek_end_time, weekend_start_time, weekend_end_time))

    session.commit()
    session.close()