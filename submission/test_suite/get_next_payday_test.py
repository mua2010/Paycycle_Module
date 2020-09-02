# Standard Library Imports
from unittest import TestCase as UnitTestCase
from datetime import date as date_class

# Local Imports
from pay_cycle import PayCycle
from enums import WeekNamePlaceholder

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

class TestNextPayday(UnitTestCase):
    """Tests Pay Cycle's BI-WEEKLY logic for -get_next_payday-
    """
    
    class __TestData(object):
        TEST_DATA_SET = []

        @classmethod
        def __data_set_get_next_payday_positive_0_1(cls):
            """Positive Test case with dates before first payday.
            """
            _pay_cycle_object = pay_cycle_object()
            date = date_class(2018,1,14)
            expected_next_payday = date_class(2018,1,26)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date, expected_next_payday))

            date = date_class(2018,11,29)
            expected_next_payday = date_class(2018,11,30)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date, expected_next_payday))

        @classmethod
        def __data_set_get_next_payday_positive_2_3(cls):
            """Positive Test case with date one day after first payday.
            """
            _pay_cycle_object = pay_cycle_object()
            date = date_class(2019,7,11)
            expected_next_payday = date_class(2019,7,12)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date, expected_next_payday))

            date = date_class(2022,11,24)
            expected_next_payday = date_class(2022,11,25)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date, expected_next_payday))

        @classmethod
        def __data_set_get_next_payday_positive_4(cls):
            """Positive Test case with date as last day of the a year.
            """
            _pay_cycle_object = pay_cycle_object()
            date = date_class(2020,12,31)
            expected_next_payday = date_class(2021,1,8)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date, expected_next_payday))

        @classmethod
        def __data_set_get_next_payday_positive_5(cls):
            """Positive Test case with date as first payday.
            """
            _pay_cycle_object = pay_cycle_object()
            date = _pay_cycle_object.first_payday #date_class(2019,1,25)
            expected_next_payday = date_class(2019,2,8)
            cls.TEST_DATA_SET.append((_pay_cycle_object, date, expected_next_payday))

        @classmethod
        def test_setup(cls):
            cls.__data_set_get_next_payday_positive_0_1()
            cls.__data_set_get_next_payday_positive_2_3()
            cls.__data_set_get_next_payday_positive_4()
            cls.__data_set_get_next_payday_positive_5()

    __TestData.test_setup()

    @parameterized.expand(__TestData.TEST_DATA_SET)
    def test_get_next_payday(self, pay_cycle: PayCycle, date: date_class, expected_next_payday: date_class):
        next_payday = pay_cycle.get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'

    def test_get_next_payday_positive_6(self):
        """Positive Test case to check if a date class object is returned.
        """
        date = date_class(2020,1,1)
        next_payday = pay_cycle_object().get_next_payday(date)
        assert isinstance(next_payday, date_class), \
            f'Got {type(next_payday)}, expected Date Class Object'
        
    def test_get_next_payday_positive_7(self):
        """Positive Test case to check if the next payday is on a thursday because
           the default payday (i.e Friday) is a holiday.
        """
        date = date_class(2020,12,12)
        expected_next_payday = date_class(2020,12,24)
        next_payday = pay_cycle_object().get_next_payday(date)
        assert next_payday == expected_next_payday, \
            f'Got {next_payday}, expected {expected_next_payday}'
        assert WeekNamePlaceholder(next_payday.weekday()) == WeekNamePlaceholder.THURSDAY