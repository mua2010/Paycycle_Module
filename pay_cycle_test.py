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

class TestPayCycle(unittest.TestCase):

    def setUp(self):
        pay_cycle_type = 'BI_WEEKLY'
        self.first_payday = date_class(2018,1,12)
        last_payday = date_class(2020,8,21)
        default_payday = 'FRIDAY'
        self.pay_cycle = PayCycle(
            pay_cycle_type=pay_cycle_type,
            first_payday=self.first_payday, last_payday=last_payday,
            default_payday=default_payday,
            holidays=US_HOLIDAYS
        )

    def tearDown(self):
        pass

    # TESTS is_payday

    def test_is_payday_positive0(self):
        """Positive Test case to check valid payday.
        """
        # 2 weeks after first_payday
        date_to_check = date_class(2019,1,25)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2019,12,27)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2020,1,10)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2020,11,27)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2020,12,24)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

    def test_is_payday_positive1(self):
        """Positive Test case to check a valid payday when a payday
           becomes Thursday because Friday was a holiday.
        """
        date_to_check = date_class(2021,1,8)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

        date_to_check = date_class(2022,11,25)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == True

    def test_is_payday_negative0(self):
        """Negative Test case to check if a date before first_day is rejected.
        """
        date_to_check = date_class(2019,1,10)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

    def test_is_payday_negative1(self):
        """Negative Test case to check if holiday is not a payday.
        """
        date_to_check = date_class(2020,12,25)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

    def test_is_payday_negative2(self):
        """Negative Test case to check wrong paydays.
        """
        date_to_check = date_class(2019,11,22)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

        date_to_check = date_class(2020,12,18)
        is_payday = self.pay_cycle.is_payday(date_to_check)
        assert is_payday == False

    # TESTS get_next_payday

    def test_get_next_payday_positive0(self):
        """Positive Test case to check if a date class object is returned.
        """
        date = date_class(2020,1,1)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert isinstance(next_payday, date_class), \
            f'Got {type(next_payday)}, expected Date Class Object'

    def test_next_payday_positive1(self):
        """Positive Test case to check if a correct payday is returned
           when given date is <= first_pay of the user.
        """
        date = date_class(2018,1,11)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == self.first_payday, \
            f'Got {next_payday}, expected {self.first_payday}'

    def test_next_payday_positive2(self):
        """Positive Test case to check if the next payday is the very next day
           after the date.
        """
        date = date_class(2019,7,11)
        expected_next_payday = date_class(2019,7,12)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'

        date = date_class(2022,11,24)
        expected_next_payday = date_class(2022,11,25)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'
    
    def test_next_payday_positive3(self):
        """Positive Test case to check if the next payday is on a thursday because
           the default payday (i.e Friday) is a holiday.
        """
        date = date_class(2020,12,12)
        expected_next_payday = date_class(2020,12,24)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'
        assert WeekPlaceholder(next_payday.weekday()) == WeekPlaceholder.THURSDAY
    
    def test_next_payday_positive4(self):
        """Positive Test case to check if a correct payday from the next year
           is returned when the given date is last day of previous year.
        """
        date = date_class(2020,12,31)
        expected_next_payday = date_class(2021,1,8)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'

    def test_next_payday_positive5(self):
        """Positive Test case to check if a correct next bi-weekly payday is returned
           when the date passed in is a payday.
        """
        date = date_class(2021,11,12)
        expected_next_payday = date_class(2021,11,26)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'

        date = date_class(2022,11,10)
        expected_next_payday = date_class(2022,11,25)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'
        
        date = date_class(2022,11,25)
        expected_next_payday = date_class(2022,12,9)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'


    def test_next_payday_positive6(self):
        """Positive Test case to check if a correct next bi-weekly payday is returned
           when a non payday date is passed in.
        """
        date = date_class(2019,1,12)
        expected_next_payday = date_class(2019,1,25)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'

        date = date_class(2022,11,26)
        expected_next_payday = date_class(2022,12,9)
        next_payday = self.pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'

    def test_next_payday_positive7(self):
        """Positive Test case to check if a correct next bi-weekly payday is returned
           when the date passed in is the first payday.
        """
        expected_next_payday = date_class(2018,1,26)
        next_payday = self.pay_cycle.get_next_payday(self.first_payday)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'

    def test_next_payday_negative0(self):
        """Negative Test case to check if Exception is raised if 
           invalid date class object is passed in.
        """
        expected_exception = RuntimeError
        date = [date_class(2020, 12, 25)]
        try:
            next_payday = self.pay_cycle.get_next_payday(date)
        except Exception as exc:
            exception = exc.__class__
        assert exception == expected_exception

    # TESTS get_next_x_paydays

    def test_get_next_x_paydays_positive0(self):
        """Positive Test case to check if correct next x number 
           of bi-weekly paydate objects are returned if the
           given date is a payday.
        """
        start_date = date_class(2019,11,15)
        x_number_of_paydays = 5
        expected_next_x_paydays = [
            date_class(2019, 11, 29),
            date_class(2019, 12, 13),
            date_class(2019, 12, 27),
            date_class(2020, 1, 10),
            date_class(2020, 1, 24)
        ]

        next_x_paydays_list = self.pay_cycle.get_next_x_paydays(x_number_of_paydays, start_date)

        assert len(next_x_paydays_list) == x_number_of_paydays, \
            f'Got {len(next_x_paydays_list)}, expected {x_number_of_paydays}'
        assert next_x_paydays_list == expected_next_x_paydays, \
            f'Got {next_x_paydays_list}, expected {expected_next_x_paydays}'

    def test_get_next_x_paydays_positive1(self):
        """Positive Test case to check if correct next x number 
           of bi-weekly paydate objects are returned if the
           given date is not a payday.
        """
        start_date = date_class(2018,11,1)
        x_number_of_paydays = 4
        expected_next_x_paydays = [
            date_class(2018,11,2),
            date_class(2018,11,16),
            date_class(2018,11,30),
            date_class(2018,12,14),
        ]

        next_x_paydays_list = self.pay_cycle.get_next_x_paydays(x_number_of_paydays, start_date)

        assert len(next_x_paydays_list) == x_number_of_paydays, \
            f'Got {len(next_x_paydays_list)}, expected {x_number_of_paydays}'
        assert next_x_paydays_list == expected_next_x_paydays, \
            f'Got {next_x_paydays_list}, expected {expected_next_x_paydays}'


# REMOVE THIS
if __name__ == '__main__':
    unittest.main(verbosity=2)