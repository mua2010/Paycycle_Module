from datetime import (
    datetime,
    timedelta,
    date as date_class
)
from enum import Enum

from utils import get_valid_date_object


# TODO: ADD DOC STRINGS for all methods 


class PayCycle(object):

    def __init__(self, pay_cycle_type: str):
        """Constructor for PayCycle class.

        Args:
            pay_cycle_type (str): The type of paycylce. Possible values: 'bi-weekly', 'semi-monthly', 'monthly', or 'weekly'. 
        """
        if pay_cycle_type == 'bi-weekly':
            self.frequency = timedelta(weeks=2)
        

    def is_payday(self, date: str = None) -> bool:
        if not date:
            date_object = date_class.today()
        else:
            try:
                date_object = get_valid_date_object(date)
            except ValueError:
                raise

    def next_payday(self, date: str) -> date_class:
        try:
            date_object = get_valid_date_object(date)
        except ValueError:
            raise

        return date_object + self.frequency

    def next_x_paydays(self, x_number_of_paydays: int, date: str = None) -> list:
        if not date:
            date_object = date_class.today()
        else:
            try:
                date_object = get_valid_date_object(date)
            except ValueError:
                raise

        next_x_paydays_array = []
        for _ in range(x_number_of_paydays):
            next_paydate_object = date_object + self.frequency
            date_object = next_paydate_object
            next_x_paydays_array.append(next_paydate_object)

        return next_x_paydays_array