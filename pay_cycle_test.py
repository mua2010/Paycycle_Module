import unittest
from datetime import (
    date as date_class
)

import logging

from utils import get_valid_date_object
from pay_cycle import PayCycle

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

class TestPayCycle(unittest.TestCase):

    # TESTS is_payday

    def test_is_payday_positive0(self):
        """Positive Test case to check if ...
        """
        pay_cycle = PayCycle('BI_WEEKLY')
        date = date_class(2020)
        expected_next_paydate = date_class(2020, 1, 15)

        next_paydate_object = pay_cycle.next_payday(current_date)

        assert next_paydate_object == expected_next_paydate

    # TESTS next_payday

    def test_next_payday_positive0(self):
        """Positive Test case to check if a correct next bi-weekly paydate object is returned.
        """
        pay_cycle = PayCycle('BI_WEEKLY')
        current_date = "2020-01-01"
        expected_next_paydate = date_class(2020, 1, 15)

        next_paydate_object = pay_cycle.next_payday(current_date)

        assert next_paydate_object == expected_next_paydate

    def test_next_payday_positive1(self):
        """Positive Test case to check if a correct next bi-weekly paydate object is returned 
           with a leap year.
        """
        pay_cycle = PayCycle('bi-weekly')
        current_date = "2020-02-25"
        expected_next_paydate = date_class(2020, 3, 10)

        next_paydate_object = pay_cycle.next_payday(current_date)

        assert next_paydate_object == expected_next_paydate

    # TESTS next_x_paydays

    def test_next_x_paydays_positive0(self):
        """Positive Test case to check if correct next x number of bi-weekly paydate objects are returned.
        """
        pay_cycle = PayCycle('bi-weekly')

        start_date = "2019-11-15" # Nov 15th, 2019
        x_number_of_paydays = 5
        expected_next_x_paydays = [
            date_class(2019, 11, 29),
            date_class(2019, 12, 13),
            date_class(2019, 12, 27),
            date_class(2020, 1, 10),
            date_class(2020, 1, 24)
        ]

        next_x_paydays_list = pay_cycle.next_x_paydays(x_number_of_paydays, start_date)

        assert len(next_x_paydays_list) == 5
        assert next_x_paydays_list == expected_next_x_paydays


if __name__ == '__main__':
    unittest.main()