# Standard Library Imports
from unittest import TestCase as UnitTestCase

from datetime import (
    date as date_class,
    timedelta
)

# Local Imports
from pay_cycle import PayCycle

# Third-Party Imports
import holidays
from parameterized import parameterized

        

US_HOLIDAYS = holidays.UnitedStates()

'''
NOTE: To establish test cases, I am using example calendars inside 
      “Example Calendars.pdf”
'''

def pay_cycle_object():
    pay_cycle_type = 'BI_WEEKLY'
    first_payday = date_class(2019,1,25)
    default_payday = 'FRIDAY'
    return PayCycle(
        pay_cycle_type=pay_cycle_type,
        first_payday=first_payday,
        default_payday=default_payday,
        holidays=US_HOLIDAYS
    )

class TestIsPayday(UnitTestCase):
    """Tests Pay Cycle's BI-WEEKLY logic for -is_payday-
    """
    
    class __TestData(object):
        TEST_DATA_SET = []

        @classmethod
        def __data_set_is_payday_positive_00_01_02_03(cls):
            """Positive Test case with dates before first payday."""
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2018,1,12)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2018,2,23)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2018,11,16)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2018,12,28)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

        @classmethod
        def __data_set_is_payday_positive_04(cls):
            """Positive Test case with date 2 weeks after first payday."""
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2019,2,8)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

        @classmethod
        def __data_set_is_payday_positive_05_06_07(cls):
            """Positive Test case with dates in the same year as first payday."""
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2019,11,1)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2019,11,29)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2019,12,13)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))
        
        @classmethod
        def __data_set_is_payday_positive_08_09_10(cls):
            """Positive Test case with dates greater than first payday's year."""
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2020,1,10)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2020,1,24)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2022,10,14)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))
        
        @classmethod
        def __data_set_is_payday_positive_11_12_13(cls):
            """Positive Test case with dates on Thursday as paydays 
               because Friday was a holiday.
            """
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2020,12,24)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2021,12,23)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2022,11,10)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

        @classmethod
        def __data_set_is_payday_positive_14_15(cls):
            """Positive Test case with first payday as Thursday.
            """
            _pay_cycle_object = pay_cycle_object()
            _pay_cycle_object.first_payday = date_class(2020,12,24)

            date_to_check = date_class(2021,1,8)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

            date_to_check = date_class(2022,8,5)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, True))

        @classmethod
        def __data_set_is_payday_negative_16_17_18(cls):
            """Negative Test case with dates less than first payday.
            """
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2019,1,24) # The day before first payday
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))

            date_to_check = date_class(2018,12,27)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))

            date_to_check = date_class(2018,2,28)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))
        
        @classmethod
        def __data_set_is_payday_negative_19_20_21(cls):
            """Negative Test case with dates as holidays.
            """
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2020,12,25) # Christmas
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))

            date_to_check = date_class(2021,12,24)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))

            date_to_check = date_class(2022,11,11)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))
        
        @classmethod
        def __data_set_is_payday_negative_22_23_24(cls):
            """Negative Test case with dates in between bi-weekly paydays.
            """
            _pay_cycle_object = pay_cycle_object()
            date_to_check = date_class(2018,11,23)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))

            date_to_check = date_class(2019,1,18)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))

            date_to_check = date_class(2021,12,17)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date_to_check, False))

        @classmethod
        def test_setup(cls):
            cls.__data_set_is_payday_positive_00_01_02_03()
            cls.__data_set_is_payday_positive_04()
            cls.__data_set_is_payday_positive_05_06_07()
            cls.__data_set_is_payday_positive_08_09_10()
            cls.__data_set_is_payday_positive_11_12_13()
            cls.__data_set_is_payday_positive_14_15()
            cls.__data_set_is_payday_negative_16_17_18()
            cls.__data_set_is_payday_negative_19_20_21()
            cls.__data_set_is_payday_negative_22_23_24()

    __TestData.test_setup()

    @parameterized.expand(__TestData.TEST_DATA_SET)
    def test_is_payday(self, pay_cycle: PayCycle, date_to_check: date_class, result: bool):
        is_payday = pay_cycle.is_payday(date_to_check)
        assert is_payday == result

    def test_is_payday_positive_25(self):
        """Positive Test case to check if there were 3 paydays in
           October, 2020. (2nd, 16th, 30th)
        """
        expected_count = 3
        expected_paydays = [
            date_class(2020,10,2), 
            date_class(2020,10,16), 
            date_class(2020,10,30)
        ]

        curr_date = date_class(2020,10,1)
        end_date = date_class(2020,10,31)
        paydays = []

        while curr_date <= end_date:
            is_payday = pay_cycle_object().is_payday(curr_date)
            if is_payday: 
                paydays.append(curr_date)
            curr_date += timedelta(days=1)

        assert len(paydays) == expected_count, \
            f'Got {len(paydays)}, expected {expected_count}'
        assert paydays == expected_paydays, \
            f'Got {paydays}, expected {expected_paydays}'
