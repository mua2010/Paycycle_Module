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
    timedelta,
    date as date_class
)
from enum import Enum

# Local Imports
from helpers import (
    is_payday_helper,
    get_valid_payday,
    pick_nearest_date,
)


# TODO: ADD DOC STRINGS for all methods 

class PayCycleType(Enum):
    BI_WEEKLY = timedelta(weeks=2)

class WeekPlaceholder(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

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
            holidays (list): A list of date class objects representing the holidays
                             applicable to the user.
        """
        self.frequency = PayCycleType[pay_cycle_type].value
        self.first_payday = first_payday
        self.last_payday = last_payday
        self.holidays = holidays

        self.default_payday = WeekPlaceholder.__getitem__(default_payday)

    def is_payday(self, date: date_class=date_class.today()) -> bool:
        """Checks whether the given date is payday for the user.

        Args:
            date (date_class, optional): Any date. Defaults to today's date.

        Returns:
            bool: Return True if the date is a payday for the user. False Otherwise.
        """
        if (date < self.first_payday) or (date in self.holidays):
            return False
        if (date == self.first_payday) or (date == self.last_payday):
            return True
        
        # Pick the payday that is nearest to 'date'
        nearest_payday = pick_nearest_date(date, self.first_payday, self.last_payday)

        # TODO: Can be made faster by checking difference and skipping months/years

        # ======================
        # frequency = self.frequency

        # if date < nearest_payday:
        #     # set config to go backwards
        #     condition = curr_day >= date
        # holiday = None
        # # Go Forward
        # while (curr_day <= date):
        #     if curr_day == date:
        #         return True
        #     if curr_day.weekday() != self.default_payday.value:
        #         # reset the curr_day to follow its original pay cycle
        #         curr_day = holiday

        #     if (holiday := (curr_day + self.frequency)) in self.holidays:
        #         curr_day = get_valid_payday(holiday)
        #     else:
        #         curr_day += self.frequency
        # return False
        # # TODO: ==================== implement the above logic into next_payday

        # return is_payday_helper(
        #         date=date,
        #         frequency=self.frequency,
        #         curr_day=nearest_payday, default_payday=self.default_payday,
        #         holidays=self.holidays
        #     )

        holiday = None
        curr_day = nearest_payday
        if date < curr_day:
            # Go Backward
            while (curr_day >= date):
                if curr_day == date:
                    return True
                if curr_day.weekday() != self.default_payday.value:
                    # reset the curr_day to follow its original pay cycle
                    curr_day = holiday

                if (holiday := (curr_day - self.frequency)) in self.holidays:
                    curr_day = get_valid_payday(holiday)
                else:
                    curr_day -= self.frequency
            return False
        else: 
            # Go Forward
            while (curr_day <= date):
                if curr_day == date:
                    return True
                if curr_day.weekday() != self.default_payday.value:
                    # reset the curr_day to follow its original pay cycle
                    curr_day = holiday

                if (holiday := (curr_day + self.frequency)) in self.holidays:
                    curr_day = get_valid_payday(holiday)
                else:
                    curr_day += self.frequency
            return False

    def next_payday(self, date: date_class=date_class.today()) -> date_class:
        if not isinstance(date, date_class):
            raise RuntimeError('A date class object is required to find the next payday.')
        if date <= self.first_payday:
            return self.first_payday

        # Pick the payday that is nearest to 'date'
        nearest_payday = pick_nearest_date(date, self.first_payday, self.last_payday)



        

    def next_x_paydays(self, x_number_of_paydays: int, date: date_class = None) -> list:
        pass
        # check if x is positive

        # if not date:
        #     date = date_class.today()

        # next_x_paydays_array = []
        # for _ in range(x_number_of_paydays):
        #     date = self.next_payday(date)
        #     next_x_paydays_array.append(date)

        # return next_x_paydays_array

