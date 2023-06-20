from ..database.model import Employee

class Reporte:

    def __init__(self, id_employee, start_date, end_date):
        
        self.id_employee = id_employee
        self.start_date = start_date
        self.end_date = end_date

    def generate_report(self):

        self.nombre = 'Ricardo'