'''
Assuming the following data will be provided
1. pay_cycle_type
2. first_payday
3. list of holidays
4. default_payday

'''

# Standard Library Imports
from datetime import (
    date as date_class
)

# Local Imports
from helpers import (
    get_nearest_payday,
    get_nearest_business_day,
    update_payday
)
from enums import PayCycleType, WeekPlaceholder


class PayCycle:
    """Pay Cycle Class.
    """

    def __init__(self, 
                 pay_cycle_type: str, 
                 first_payday: date_class,
                 default_payday: str,
                 holidays: list):
        """Constructor for PayCycle Class.

        Note: This assumes that along with the type of pay cycle, users will 
        accurately report their first payday.

        Args:
            pay_cycle_type (str): Type of user's pay cycle. 
                                  ‘BI-WEEKLY, ‘SEMI-MONTHLY’, ‘MONTHLY’, or ‘WEEKLY’.
            first_payday (date_class): First payday after the user started employment. 
            default_payday (str): The day of the week when the user normally
                                  gets paid.
            holidays (list): A list of date class objects representing the holidays
                             applicable to the user.
        """
        self.frequency = PayCycleType[pay_cycle_type].value
        self.first_payday = first_payday
        self.holidays = holidays

        self.default_payday = WeekPlaceholder.__getitem__(default_payday)

    def is_payday(self, date: date_class=date_class.today()) -> bool:
        """Return True if the given date is payday for the user; False otherwise.
        """
        if date == self.first_payday:
            return True
        if date in self.holidays:
            return False
        
        # skip to the payday nearest to the 'date'
        payday = get_nearest_payday(
            date=date,
            frequency=self.frequency,
            holidays=self.holidays,
            given_payday=self.first_payday,
            default_payday=self.default_payday
        )

        if date == payday:
            return True
        else:
            return False

    def get_next_payday(self, date: date_class=date_class.today()) -> date_class:
        """Given a date, find the next payday for the user.
        """
        # skip to the payday nearest to the 'date'
        _payday = get_nearest_payday(
            date=date,
            frequency=self.frequency,
            holidays=self.holidays,
            given_payday=self.first_payday,
            default_payday=self.default_payday
        )

        # Edge Case: After skipping, If we land on the given 'date' or before 
        # then we need to add the frequency to get the next payday.
        if date >= _payday:
            _payday = update_payday(
                payday=_payday,
                frequency=self.frequency,
                holidays=self.holidays,
                default_payday=self.default_payday
            )

        return _payday 

    def get_next_x_paydays(self, x_number_of_paydays: int, date: date_class=date_class.today()) -> list:
        next_x_paydays_list = []
        
        # OPTIMIZE by caching the paydays in a self. variable
        for _ in range(x_number_of_paydays):
            date = self.get_next_payday(date)
            next_x_paydays_list.append(date)

        return next_x_paydays_list

