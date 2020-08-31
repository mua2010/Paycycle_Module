'''
======
NOTES:
======
ASSUMING THE FOLLOWING DATA WILL BE PROVIDED
1.  pay_cycle_date = '{
        ‘pay_cycle_type’: 'BI_WEEKLY',
        ‘first_payday': ‘2019-01-11’,
        'last_payday': '2020-12-24',
        ‘Holidays’: [
            ‘New Year's Day’,
            …
            'Christmas Day'
        ],
        'default_payday': 'FRIDAY'
    }’

'''


# Standard Library Imports
from datetime import (
    date as date_class
)

# Local Imports
from helpers import (
    pick_nearest_date,
    get_nearest_payday,
    get_valid_date
)
from enums import PayCycleType, WeekPlaceholder


# TODO: ADD DOC STRINGS for all methods 


class PayCycle:
    """Pay Cycle Class.
    """

    def __init__(self, 
                 pay_cycle_type: str, 
                 first_payday: date_class, last_payday: date_class,
                 default_payday: str,
                 holidays: list):
        """Constructor for PayCycle Class.

        Note: This assumes that along with pay cycle type, users will accurately report 
        their first payday. TODO: DO THEY WANT TO REPORT HOLIDAYS or we default use something?

        Args:
            pay_cycle_type (str): Type of user's pay cycle. 
                                  ‘BI-WEEKLY, ‘SEMI-MONTHLY’, ‘MONTHLY’, or ‘WEEKLY’.
            first_payday (date_class): First payday after the user started employment. 
            last_payday (date_class): The lastest date when the user got paid.
            default_payday (str): The day of the week when the user normally
                                  gets paid.
            holidays (list): A list of date class objects representing the holidays
                             applicable to the user.
        """
        self.frequency = PayCycleType[pay_cycle_type].value
        self.first_payday = first_payday
        self.last_payday = last_payday
        self.holidays = holidays

        self.default_payday = WeekPlaceholder.__getitem__(default_payday)

    def is_payday(self, date: date_class=date_class.today()) -> bool:
        """Return True if the given date is payday for the user; False otherwise.
        """
        if (date < self.first_payday) or (date in self.holidays):
            return False
        if (date == self.first_payday) or (date == self.last_payday):
            return True
        
        # Pick the payday that is nearest to 'date'
        nearest_given_payday = pick_nearest_date(date, self.first_payday, self.last_payday)

        # TODO: Can be made faster by checking difference and skipping months/years

        # skip to the payday nearest to the 'date'
        payday = get_nearest_payday(
            date=date,
            frequency=self.frequency,
            holidays=self.holidays,
            nearest_given_payday=nearest_given_payday,
            default_payday=self.default_payday
        )

        if date == payday:
            return True
        else:
            return False

    def get_next_payday(self, date: date_class=date_class.today()) -> date_class:
        """Given a date, find the next payday for the user.
        """
        if not isinstance(date, date_class):
            raise RuntimeError('A date class object is required to find the next payday.')
        if date < self.first_payday:
            return self.first_payday

        # Pick the payday that is nearest to 'date'
        nearest_given_payday = pick_nearest_date(date, self.first_payday, self.last_payday)

        # skip to the payday nearest to the 'date'
        payday = get_nearest_payday(
            date=date,
            frequency=self.frequency,
            holidays=self.holidays,
            nearest_given_payday=nearest_given_payday,
            default_payday=self.default_payday
        )

        # Edge Case: After skipping, If we land on the given 'date', 
        #            that means the 'date' was a payday so, we need to 
        #            add the frequency to get the next payday.
        if date >= payday:
            if (holiday := (payday + self.frequency)) in self.holidays:
                payday = get_valid_date(holiday)
            else:
                payday += self.frequency

        return payday 

    def get_next_x_paydays(self, x_number_of_paydays: int, date: date_class=date_class.today()) -> list:
        if x_number_of_paydays <= 0:
            raise RuntimeError('The number of paydays to request needs to be a positive number.')
        if date < self.first_payday:
            date = self.first_payday

        next_x_paydays_list = []
        for _ in range(x_number_of_paydays):
            date = self.get_next_payday(date)
            next_x_paydays_list.append(date)

        return next_x_paydays_list

