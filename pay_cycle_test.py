# Standard Library Imports
import unittest
from datetime import (
    date as date_class
)
import logging

# Local Imports
from pay_cycle import PayCycle

# Third-Party Imports
import holidays

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

# UNIT TEST MOCK PATCH
# https://www.youtube.com/watch?v=WFRljVPHrkE
        

US_HOLIDAYS = holidays.UnitedStates()

class TestPayCycle(unittest.TestCase):

    def setUp(self):
        pay_cycle_type = 'BI_WEEKLY'
        # ASSUMING THE PAYDAY IS A FRIDAY
        first_payday = date_class(2019,1,11)
        last_payday = date_class(2020,8,21)
        self.pay_cycle = PayCycle(
            pay_cycle_type=pay_cycle_type,
            first_payday=first_payday, last_payday=last_payday,
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
        """Negative Test case to check if holiday is a payday.
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

    # TESTS next_payday

    # def test_next_payday_positive0(self):
    #     """Positive Test case to check if a correct next bi-weekly paydate object is returned.
    #     """
    #     pay_cycle = PayCycle('BI_WEEKLY')
    #     current_date = "2020-01-01"
    #     expected_next_paydate = date_class(2020, 1, 15)

    #     next_paydate_object = pay_cycle.next_payday(current_date)

    #     assert next_paydate_object == expected_next_paydate

    # def test_next_payday_positive1(self):
    #     """Positive Test case to check if a correct next bi-weekly paydate object is returned 
    #        with a leap year.
    #     """
    #     pay_cycle = PayCycle('bi-weekly')
    #     current_date = "2020-02-25"
    #     expected_next_paydate = date_class(2020, 3, 10)

    #     next_paydate_object = pay_cycle.next_payday(current_date)

    #     assert next_paydate_object == expected_next_paydate

    # # TESTS next_x_paydays
    # # 1. number of paydays = 26
    # def test_next_x_paydays_positive0(self):
    #     """Positive Test case to check if correct next x number of bi-weekly paydate objects are returned.
    #     """
    #     pay_cycle = PayCycle('bi-weekly')

    #     start_date = "2019-11-15" # Nov 15th, 2019
    #     x_number_of_paydays = 5
    #     expected_next_x_paydays = [
    #         date_class(2019, 11, 29),
    #         date_class(2019, 12, 13),
    #         date_class(2019, 12, 27),
    #         date_class(2020, 1, 10),
    #         date_class(2020, 1, 24)
    #     ]

    #     next_x_paydays_list = pay_cycle.next_x_paydays(x_number_of_paydays, start_date)

    #     assert len(next_x_paydays_list) == 5
    #     assert next_x_paydays_list == expected_next_x_paydays


if __name__ == '__main__':
    unittest.main(verbosity=2)