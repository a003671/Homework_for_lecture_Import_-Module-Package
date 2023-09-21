from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_emloyees
from prank.prank import prank_play


def date_now():
    now_date = datetime.now()
    return F'число: {now_date.day}, месяц: {now_date.month}, год: {now_date.year}'



if __name__ == '__main__':
    calculate_salary()
    get_emloyees()
    print(date_now())
    prank_play()