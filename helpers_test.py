# Standard Library Imports
import unittest
from datetime import (
    date as date_class
)

# Local Imports
from helpers import (
    get_valid_date,
    pick_nearest_date
)

# TODO: Add comments with assertions

class TestHelpers(unittest.TestCase):
    
    # TESTS get_valid_date

    def test_get_valid_date_positive0(self):
        """Positive Test case to check if Dec 24th, 2020 is a valid payday 
           given Dec 25th, 2020 is a holiday.
        """
        holiday = date_class(2020, 12, 25)
        expected_valid_payday = date_class(2020, 12, 24)
        valid_payday = get_valid_date(holiday)
        assert valid_payday == expected_valid_payday

    def test_get_valid_date_positive1(self):
        """Positive Test case to check if Nov 27th, 2020 is a valid payday 
           given Nov 26th, 2020 is a holiday.
        """
        holiday = date_class(2020, 11, 27)
        expected_valid_payday = date_class(2020, 11, 26)
        valid_payday = get_valid_date(holiday)
        assert valid_payday == expected_valid_payday

    def test_get_valid_date_negative0(self):
        """Negative Test case to check if Exception is raised if 
           invalid data is passed to 'get_valid_date'.
        """
        holiday = None
        expected_exception = RuntimeError
        try:
            valid_payday = get_valid_date(holiday)
        except Exception as exc:
            exception = exc.__class__
        assert exception == expected_exception

        holiday = [date_class(2020, 12, 25)]
        try:
            valid_payday = get_valid_date(holiday)
        except Exception as exc:
            exception = exc.__class__
        assert exception == expected_exception

    # TESTS pick_nearest_date

    def test_pick_nearest_date_positive0(self):
        """Positive Test case to check if correct payday is picked
           given a date closer to first payday.
        """
        date = date_class(2020,3,1)
        first_date = date_class(2020,1,1)
        second_date = date_class(2020,12,31)

        nearest_payday = pick_nearest_date(date, first_date, second_date)
        
        assert nearest_payday == first_date

    def test_pick_nearest_date_positive1(self):
        """Positive Test case to check if correct payday is picked
           given a date closer to last payday.
        """
        date = date_class(2020,11,1)
        first_date = date_class(2020,1,1)
        second_date = date_class(2020,12,31)

        nearest_payday = pick_nearest_date(date, first_date, second_date)
        
        assert nearest_payday == second_date


if __name__ == '__main__':
    unittest.main()