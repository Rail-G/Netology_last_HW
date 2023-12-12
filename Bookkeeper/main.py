from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import pytz

class BookKeeper:

    def __init__(self, name) -> str:
        self.name = name

    def sala(self) -> int:
        return calculate_salary()

    def employees(self) -> str:
        return get_employees()

    def date(self):
        utc = datetime.datetime.now(pytz.utc)
        utc3 = pytz.timezone('Etc/GMT-3')
        local_time = utc.astimezone(utc3)
        return local_time
    
if __name__ == '__main__':
    peop = BookKeeper('Rashit')
    print(f'{peop.sala()}\n')
    print(f'{peop.date()}\n')
    print(peop.employees())