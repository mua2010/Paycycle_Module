# Standard Library Imports
import unittest
from datetime import (
    date as date_class
)

# Local Imports
from utils import get_valid_payday


class TestUtils(unittest.TestCase):
    
    def test_get_valid_payday_positive0(self):
        """Positive Test case to check if Dec 24th, 2020 is a valid payday 
           given Dec 25th, 2020 is a holiday.
        """
        holiday = date_class(2020, 12, 25)
        expected_valid_payday = date_class(2020, 12, 24)
        valid_payday = get_valid_payday(holiday)
        assert valid_payday == expected_valid_payday

    def test_get_valid_payday_positive1(self):
        """Positive Test case to check if Nov 27th, 2020 is a valid payday 
           given Nov 26th, 2020 is a holiday.
        """
        holiday = date_class(2020, 11, 27)
        expected_valid_payday = date_class(2020, 11, 26)
        valid_payday = get_valid_payday(holiday)
        assert valid_payday == expected_valid_payday

    def test_get_valid_payday_negative0(self):
        """Negative Test case to check if Exception is raised if 
           invalid data is passed to 'get_valid_payday' utility.
        """
        holiday = None
        expected_exception = RuntimeError
        try:
            valid_payday = get_valid_payday(holiday)
        except Exception as re:
            exception = re.__class__
        assert exception == expected_exception

        holiday = [date_class(2020, 12, 25)]
        expected_respnse = RuntimeError
        try:
            valid_payday = get_valid_payday(holiday)
        except Exception as re:
            exception = re.__class__
        assert exception == expected_exception


if __name__ == '__main__':
    unittest.main()