# Standard Library Imports
import unittest
from datetime import (
    date as date_class
)
import logging

# Local Imports
from pay_cycle import (
    PayCycle
)
from enums import WeekPlaceholder


# Third-Party Imports
import holidays

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

# UNIT TEST MOCK PATCH
# https://www.youtube.com/watch?v=WFRljVPHrkE
        
# TODO: Add comments with assertions

US_HOLIDAYS = holidays.UnitedStates()

'''
NOTE: I am taking an example calendar for 2018-2022 for testing.
      Please refer to 'Example Calendars for Perpay Assignment.pdf'
'''

class TestPayCycle(unittest.TestCase):

    def setUp(self):
        pay_cycle_type = 'WEEKLY'
        self.first_payday = date_class(2019,1,25)
        default_payday = 'FRIDAY'
        self.pay_cycle = PayCycle(
            pay_cycle_type=pay_cycle_type,
            first_payday=self.first_payday,
            default_payday=default_payday,
            holidays=US_HOLIDAYS
        )

    def tearDown(self):
        pass

    # TESTS is_payday

    def test_is_payday_positive0(self):
        """Positive Test case to check for paydays in the year
           before first payday year.
        """
        date_to_check = date_class(2018,1,12)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2018,2,23)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2018,11,16)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2018,12,28)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

    def test_is_payday_positive1(self):
        """Positive Test case to check if 2 weeks after first payday
           was a payday.
        """
        date_to_check = date_class(2019,2,8)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

    def test_is_payday_positive2(self):
        """Positive Test case to check for paydays in the same year
           as first payday.
        """
        date_to_check = date_class(2019,11,1)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2019,11,29)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2019,12,13)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

    def test_is_payday_positive3(self):
        """Positive Test case to check for paydays in years
           greater than the first payday year.
        """
        date_to_check = date_class(2020,1,10)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2020,1,24)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

    def test_is_payday_positive4(self):
        """Positive Test case to check if there were 3 paydays in
           the month of October, 2020. (2nd, 16th, 30th)
        """
        date_to_check = date_class(2020,10,2)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2020,10,16)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2020,10,30)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True


    def test_is_payday_positive5(self):
        """Positive Test case to check a valid payday when a payday
           becomes Thursday because Friday was a holiday.
        """
        date_to_check = date_class(2020,12,24)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2021,12,23)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2022,11,10)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True
    
    def test_is_payday_positive6(self):
        """Positive Test case to check paydays when the first payday
           was on a thursday because Friday was a holiday.
        """
        # Overriding first_payday
        self.first_payday = date_class(2020,12,24)
        date_to_check = date_class(2021,1,8)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

    def test_is_payday_negative0(self):
        """Negative Test case to check a date before first_day.
        """
        date_to_check = date_class(2019,1,24)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

        date_to_check = date_class(2018,12,27)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

        date_to_check = date_class(2018,2,28)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

    def test_is_payday_negative1(self):
        """Negative Test case to check if holiday on default payday
           is not a payday.
        """
        date_to_check = date_class(2020,12,25)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

        date_to_check = date_class(2021,12,24)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

        date_to_check = date_class(2022,11,11)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

    def test_is_payday_negative2(self):
        """Negative Test case to check default paydays in between
           biweekly paydays.
        """
        date_to_check = date_class(2018,11,23)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

        date_to_check = date_class(2019,1,18)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

        date_to_check = date_class(2021,12,17)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

# REMOVE THIS
if __name__ == '__main__':
    import time
    start = time.time()
    unittest.main(verbosity=2)
    end = time.time()
    print(end - start)