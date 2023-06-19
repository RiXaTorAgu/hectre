from sqlalchemy import Column, Date, ForeignKey, Integer, String, Time
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):

    __tablename__ = 'employee'

    id_employee = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name_1 = Column(String)
    last_name_2 = Column(String)
    midweek_start_time = Column(Time)
    midweek_end_time = Column(Time)
    weekend_start_time = Column(Time)
    weekend_end_time = Column(Time)

    def __init__(self, id_employee, first_name, last_name_1, last_name_2, midweek_start_time, midweek_end_time, weekend_start_time, weekend_end_time):

        self.id_employee = id_employee
        self.first_name = first_name
        self.last_name_1 = last_name_1
        self.last_name_2 = last_name_2
        self.midweek_start_time = midweek_start_time
        self.midweek_end_time = midweek_end_time
        self.weekend_start_time = weekend_start_time
        self.weekend_end_time = weekend_end_time

    def __repr__(self):

        return f'Employee({self.id_employee}, {self.first_name}, {self.last_name_1}, {self.last_name_2})'
    
class Attendance(Base):

    __tablename__ = 'attendance'

    date = Column(Date, primary_key=True)
    id_employee = Column(Integer, ForeignKey('employee.id_employee'), primary_key=True)
    start_time = Column(Time)
    end_time = Column(Time)

    def __init__(self, date, id_employee, start_time, end_time):

        self.date = date
        self.id_employee = id_employee
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):

        return f'Attendance({self.date}, {self.id_employee}, {self.start_time}, {self.end_time})'
    
    