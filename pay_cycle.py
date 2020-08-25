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
from utils import get_valid_payday

def __get_frequency(pay_cycle_type: str) -> timedelta:
    if pay_cycle_type == 'bi-weekly':
        return timedelta(weeks=2)

def is_payday(pay_cycle_type: str, 
              holidays: list, 
              first_payday: date_class, 
              date: date_class = None) -> bool:
    if not date:
        date = date_class.today()
    if (date < first_payday) or (date in holidays):
        return False
    
    frequency = __get_frequency(pay_cycle_type)
    curr_day = first_payday
    while curr_day <= date:
        if curr_day == date:
            return True
        if (holiday:=(curr_day + frequency)) in holidays:
            curr_day = get_valid_payday(holiday)
        else:
            curr_day += frequency
    return False

# negative test
pay_cycle_type = 'bi-weekly'
first_payday = date_class(2020, 10, 2)
date_to_check = date_class(2020, 12, 25)
holidays = [date_class(2020,10,12), date_class(2020,11,11), date_class(2020,11,26), date_class(2020,12,25)]
print(is_payday(pay_cycle_type, holidays, first_payday, date_to_check)) # false

# positvie test diff in months TODO: check for multiple months
first_payday = date_class(2020, 10, 2)
date_to_check = date_class(2020, 12, 24)
holidays = [date_class(2020,10,12), date_class(2020,11,11), date_class(2020,11,26), date_class(2020,12,25)]
print(is_payday(pay_cycle_type, holidays, first_payday, date_to_check)) # True

# postiive test diff in years TODO: add a negative test case
first_payday = date_class(2019, 12, 13)
date_to_check = date_class(2020, 1, 10)
holidays = [date_class(2019,12,25), date_class(2020,1,1), date_class(2020,1,20)]
print(is_payday(pay_cycle_type, holidays, first_payday, date_to_check)) # True

# TODO: check for a future payday 2021?? or maybe done



def next_payday(self, date: date_class) -> date_class:
    return date + self.frequency
    # TODO: frequency icrment then call get valid payday holiday

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