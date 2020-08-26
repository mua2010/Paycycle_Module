'''
======
NOTES:
======
1.  pay_cycle_date = '{
        ‘pay_cycle_type’: 'BI_WEEKLY',
        ‘first_payday': ‘2019-01-11’,
        'last_payday': '2020-12-24',
        ‘Holidays’: [
            ‘New Year's Day’,
            …
            'Christmas Day'
        ]
    }’

2.  Tracking Holidays:
        - https://stackoverflow.com/questions/2394235/detecting-a-us-holiday
        - https://pypi.org/project/holidays/

'''


# Standard Library Imports
from datetime import (
    timedelta,
    date as date_class
)
from enum import Enum

# Local Imports
from helpers import get_valid_payday



# TODO: ADD DOC STRINGS for all methods 

class PayCycleType(Enum):
    BI_WEEKLY = timedelta(weeks=2)


class PayCycle:

    def __init__(self, 
                 pay_cycle_type: str, 
                 first_payday: date_class, last_payday: date_class,
                 holidays: list):
        """Constructor for PayCycle Class.

        Args:
            pay_cycle_type (str): Type of user's pay cycle. 
                                  ‘BI-WEEKLY, ‘SEMI-MONTHLY’, ‘MONTHLY’, or ‘WEEKLY’.
            first_payday (date_class): The first pay date when the user started employment.
            last_payday (date_class): The lastest date when the user got paid.
            holidays (list): A list of date class objects representing the holidays.
        """
        self.frequency = PayCycleType[pay_cycle_type].value
        self.first_payday = first_payday
        self.last_payday = last_payday
        self.holidays = holidays

    def is_payday(self, date: date_class = None) -> bool:
        if not date:
            date = date_class.today()
        if (date < self.first_payday) or (date in self.holidays):
            return False
        
        while (curr_day:=self.first_payday) <= date:
            if curr_day == date:
                return True
            if (holiday:=(curr_day + self.frequency)) in self.holidays:
                curr_day = get_valid_payday(holiday)
            else:
                curr_day += self.frequency
        return False

    def next_payday(self, date: date_class) -> date_class:
        pass
        # return date + self.frequency
        # if not date:
            # raise RuntimeError('Empty date passed in. A date is required to find the next_payday.')
        # TODO: frequency icrment then call get valid payday holiday

    def next_x_paydays(self, x_number_of_paydays: int, date: date_class = None) -> list:
        pass
        # if not date:
        #     date = date_class.today()

        # next_x_paydays_array = []
        # for _ in range(x_number_of_paydays):
        #     date = self.next_payday(date)
        #     next_x_paydays_array.append(date)

        # return next_x_paydays_array

