# Standard Library Imports
from unittest import TestCase as UnitTestCase
from datetime import date as date_class

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

class TestNextPayday(UnitTestCase):
    """Tests Pay Cycle's BI-WEEKLY logic for -get_next_x_paydays-
    """
    
    class __TestData(object):
        TEST_DATA_SET = []

        @classmethod
        def __data_set_get_next_x_paydays_positive_0(cls):
            """Positive Test case with dates before first payday.
            """
            _pay_cycle_object = pay_cycle_object()
            start_date = date_class(2018,1,22)
            x_number_of_paydays = 3
            expected_next_x_paydays = [
                date_class(2018,1,26),
                date_class(2018,2,9),
                date_class(2018,2,23)
            ]
            cls.TEST_DATA_SET.append((
                _pay_cycle_object,
                start_date,
                x_number_of_paydays,
                expected_next_x_paydays
            ))

        @classmethod
        def __data_set_get_next_x_paydays_positive_1(cls):
            """Positive Test case to check if correct next x number 
               of bi-weekly paydate objects are returned if the
               given date is a payday.
            """
            _pay_cycle_object = pay_cycle_object()
            start_date = date_class(2019,11,15)
            x_number_of_paydays = 5
            expected_next_x_paydays = [
                date_class(2019, 11, 29),
                date_class(2019, 12, 13),
                date_class(2019, 12, 27),
                date_class(2020, 1, 10),
                date_class(2020, 1, 24)
            ]
            cls.TEST_DATA_SET.append((
                _pay_cycle_object,
                start_date,
                x_number_of_paydays,
                expected_next_x_paydays
            ))
        
        @classmethod
        def __data_set_get_next_x_paydays_positive_2(cls):
            """Positive Test case to check if correct next x number 
               of bi-weekly paydate objects are returned if the
               given date is not a payday.
            """
            _pay_cycle_object = pay_cycle_object()
            start_date = date_class(2022,11,3)
            x_number_of_paydays = 4
            expected_next_x_paydays = [
                date_class(2022,11,10),
                date_class(2022,11,25),
                date_class(2022,12,9),
                date_class(2022,12,23),
            ]

            cls.TEST_DATA_SET.append((
                _pay_cycle_object,
                start_date,
                x_number_of_paydays,
                expected_next_x_paydays
            ))

        @classmethod
        def test_setup(cls):
            cls.__data_set_get_next_x_paydays_positive_0()
            cls.__data_set_get_next_x_paydays_positive_1()
            cls.__data_set_get_next_x_paydays_positive_2()

    __TestData.test_setup()

    @parameterized.expand(__TestData.TEST_DATA_SET)
    def test_get_next_x_paydays(
            self, 
            pay_cycle: PayCycle, 
            start_date: date_class, 
            x_number_of_paydays: int,
            expected_next_x_paydays: list):
            
        next_x_paydays_list = pay_cycle.get_next_x_paydays(x_number_of_paydays, start_date)

        assert len(next_x_paydays_list) == x_number_of_paydays, \
            f'Got {len(next_x_paydays_list)}, expected {x_number_of_paydays}'
        assert next_x_paydays_list == expected_next_x_paydays, \
            f'Got {next_x_paydays_list}, expected {expected_next_x_paydays}'
