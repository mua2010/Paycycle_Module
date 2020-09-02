'''
ASSUMING THE FOLLOWING DATA WILL BE PROVIDED

pay_cycle_date = '{
    ‘pay_cycle_type’: 'BI_WEEKLY',
    ‘first_payday': ‘2019-01-11’,
    'last_payday': '2020-12-24',
    ‘Holidays’: [
        list of holidays applicable to the user
    ],
    'default_payday': 'FRIDAY'
}’

TODO:
originally I  had a  very simple soultion - doing module 14 
but I incorptrted holidays
its this 3 lines of code

WRITE ALL THE ASSUMPTION
normally, if I module by 14 i end up  a 0, it is a payday.
but there is holidays
1. I decided to store last payday 

2. write down every single edge case - make a list
    can I priortize the list

for the sake of simiplicity i ginore holidays,
but we could incoroprate them by edge case

effort vs impact
confidence
Brian Wong
8:32 PM
write down every single real world consideration
Brian Wong
8:34 PM
for the sake of simplicity
but we could incorporate them by ....
Brian Wong
8:38 PM
tradeoffs and benefits of different ideas

'''


# Standard Library Imports
from datetime import (
    date as date_class,
    timedelta
)

# Local Imports
from helpers import (
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
                 first_payday: date_class,
                 default_payday: str,
                 holidays: list):
        """Constructor for PayCycle Class.

        Note: This assumes that along with pay cycle type, users will accurately report 
        their first payday. TODO: DO THEY WANT TO REPORT HOLIDAYS or we default use something?

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

        payday = get_nearest_payday(
            date=date,
            frequency=self.frequency,
            holidays=self.holidays,
            nearest_given_payday=self.first_payday,
            default_payday=self.default_payday
        )

        if date == payday:
            return True
        else:
            return False

            
        # It's possible that date is not the default payday
        # for the user because it was was holiday on the default payday
        # In this case, check if the default payday in that week was
        # a holiday.
        if date.weekday() != self.default_payday.value:
            # if yes, reset the date to follow its original pay cycle
            offset = self.default_payday.value - date.weekday()
            date_after_offset = date + timedelta(days=offset)
            if date_after_offset in self.holidays:
                return True 

        payday = self.first_payday

        # It's possible that payday changes because it was a holiday on the day
        # when the user gets paid normally i.e default payday
        # if the payday is not the default payday
        if payday.weekday() != self.default_payday.value:
            # then, reset the payday to follow its original pay cycle
            offset = self.default_payday.value - payday.weekday()
            payday += timedelta(days=offset)    

        # Calculating the number of weeks between payday and 'date'
        difference_in_weeks = ((date - payday).days) / 7
        
        # If difference_in_weeks is a whole number and even, then date is a pay date.
        if difference_in_weeks % 2 == 0:
            return True
        return False

    def get_next_payday(self, date: date_class=date_class.today()) -> date_class:
        """Given a date, find the next payday for the user.
        """

        #TODO: IF I can get ispayday working, then next payday will be calling is payday until next 14days

        if not isinstance(date, date_class):
            raise RuntimeError('A date class object is required to find the next payday.')
        if date < self.first_payday:
            return self.first_payday

        # Pick the given payday that is nearest to 'date'
        nearest_given_payday = pick_nearest_date(date, self.first_payday, self.last_payday)

        # skip to the payday nearest to the 'date'
        payday = get_nearest_payday(
            date=date,
            frequency=self.frequency,
            holidays=self.holidays,
            nearest_given_payday=nearest_given_payday,
            default_payday=self.default_payday
        )

        # Edge Case: After skipping, If we land on the given 'date' or before 
        #            then we need to add the frequency to get the next payday.
        if date >= payday:
            if (holiday := (payday + self.frequency)) in self.holidays:
                payday = get_valid_date(holiday)
            else:
                payday += self.frequency

        return payday 

    def get_next_x_paydays(self, x_number_of_paydays: int, date: date_class=date_class.today()) -> list:
        if x_number_of_paydays <= 0:
            raise RuntimeError('The number of paydays to request needs to be a positive number.')
        
        next_x_paydays_list = []
        if date < self.first_payday:
            date = self.first_payday
            next_x_paydays_list.append(date)
        
        # OPTIMIZE by caching the paydays in a self. variable
        for _ in range(x_number_of_paydays):
            date = self.get_next_payday(date)
            next_x_paydays_list.append(date)

        return next_x_paydays_list

