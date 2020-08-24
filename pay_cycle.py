from datetime import (
    datetime,
    timedelta,
    date as date_class
)

from enum import Enum
from utils import get_valid_date_object


# TODO: ADD DOC STRINGS for all methods 
'''

pay_cycle_date = {
                    ‘pay_cycle_type’: ‘bi-weekly’,
                    'last_payday_in_year': {
                                                2018: '2018-12-28',
                                                2019: '2019-12-20',
                                                2020: '2020-08-21',
                                            }
                  }
------------------------------------
pay_cycle_date = {
                    ‘pay_cycle_type’: ‘bi-weekly’,
                    'last_payday': '2020-08-21'
                  }
'''
'''
IMP: accodring to my current startggy, what if I pass in a date in 2021, what am I checking against?
'''
'''
NOTES:
1. Track Holidays -> 
    https://stackoverflow.com/questions/2394235/detecting-a-us-holiday
    https://pypi.org/project/holidays/

'''


def __get_frequency(pay_cycle_type: str) -> timedelta:
    if pay_cycle_type == 'bi-weekly'
        return timedelta(weeks=2)

def is_payday(pay_cycle_type: str, date: date_class = None) -> bool:
    if not date:
        date = date_class.today()
    if date == self.last_payday:
        return True
    frequency = __get_frequency(pay_cycle_type)
    if (date - self.last_payday) % frequency == 0:
        return True
    return False

def next_payday(self, date: date_class) -> date_class:
    return date + self.frequency

def next_x_paydays(self, x_number_of_paydays: int, date: date_class = None) -> list:
    if not date:
        date = date_class.today()

    next_x_paydays_array = []
    for _ in range(x_number_of_paydays):
        date = self.next_payday(date)
        next_x_paydays_array.append(date)

    return next_x_paydays_array









# class PayCycleType(Enum):
#     BI_WEEKLY = timedelta(weeks=2)


# class PayCycle:

#     def __init__(self, pay_cycle_type: str, last_payday: date_class):
#         # pay_cycle_type = 'BI_WEEKLY'
#         self.frequency = PayCycleType[pay_cycle_type].value
#         # if pay_cycle_type == 'bi-weekly':
#         #     self.frequency = timedelta(weeks=2)
#         self.last_payday = last_payday
        
#     def is_payday(self, date: date_class = None) -> bool:
#         if not date:
#             date = date_class.today()
#         if date == self.last_payday:
#             return True
#         (date - self.last_payday)

#     def next_payday(self, date: date_class) -> date_class:
#         return date + self.frequency

#     def next_x_paydays(self, x_number_of_paydays: int, date: date_class = None) -> list:
#         if not date:
#             date = date_class.today()

#         next_x_paydays_array = []
#         for _ in range(x_number_of_paydays):
#             date = self.next_payday(date)
#             next_x_paydays_array.append(date)

#         return next_x_paydays_array






    # def is_payday(self, date: str = None) -> bool:
    #     if not date:
    #         date_object = date_class.today()
    #     else:
    #         try:
    #             date_object = get_valid_date_object(date)
    #         except ValueError:
    #             raise

    # def next_payday(self, date: str) -> date_class:
    #     try:
    #         date_object = get_valid_date_object(date)
    #     except ValueError:
    #         raise

    #     return date_object + self.frequency

    # def next_x_paydays(self, x_number_of_paydays: int, date: str = None) -> list:
    #     if not date:
    #         date_object = date_class.today()
    #     else:
    #         try:
    #             date_object = get_valid_date_object(date)
    #         except ValueError:
    #             raise

    #     next_x_paydays_array = []
    #     for _ in range(x_number_of_paydays):
    #         date_object = date_object + self.frequency
    #         next_x_paydays_array.append(date_object)

    #     return next_x_paydays_array