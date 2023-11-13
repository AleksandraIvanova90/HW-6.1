from datetime import datetime

from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    print(get_employees('HR'))
    print(calculate_salary(120000, 15, 9))
    print(datetime.now())


