from application.data import numbers_days


def calculate_salary(salary, days_worked, month):
    res = salary / numbers_days[month] * days_worked
    return format(res, ',.2f')