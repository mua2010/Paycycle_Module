# Standard Library Imports
from unittest import (
    TestCase as UnitTestCase, 
    mock
)

from datetime import (
    date as date_class,
    timedelta
)

# Local Imports
from pay_cycle import PayCycle
from enums import WeekPlaceholder

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
            date_to_check = date_class(2018,1,12)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2018,2,23)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2018,11,16)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2018,12,28)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

        @classmethod
        def __data_set_is_payday_positive_04(cls):
            """Positive Test case with date 2 weeks after first payday."""
            date_to_check = date_class(2019,2,8)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

        @classmethod
        def __data_set_is_payday_positive_05_06_07(cls):
            """Positive Test case with dates in the same year as first payday."""
            date_to_check = date_class(2019,11,1)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2019,11,29)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2019,12,13)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))
        
        @classmethod
        def __data_set_is_payday_positive_08_09_10(cls):
            """Positive Test case with dates greater than first payday's year."""
            date_to_check = date_class(2020,1,10)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2020,1,24)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2022,10,14)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))
        
        @classmethod
        def __data_set_is_payday_positive_11_12_13(cls):
            """Positive Test case with dates on Thursday as paydays 
               because Friday was a holiday.
            """
            date_to_check = date_class(2020,12,24)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2021,12,23)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

            date_to_check = date_class(2022,11,10)
            cls.TEST_DATA_SET.append((pay_cycle_object(), date_to_check, True))

        @classmethod
        def test_setup(cls):
            """Positive test case with start date well before end date
            """
            cls.__data_set_is_payday_positive_00_01_02_03()
            cls.__data_set_is_payday_positive_04()
            cls.__data_set_is_payday_positive_05_06_07()
            cls.__data_set_is_payday_positive_08_09_10()
            cls.__data_set_is_payday_positive_11_12_13()
            # cls.__data_set_is_payday_positive_5_6_7()

    __TestData.test_setup()

    @parameterized.expand(__TestData.TEST_DATA_SET)
    def test_is_payday(self, pay_cycle: PayCycle, date_to_check: date_class, result: bool):
        is_payday = pay_cycle.is_payday(date_to_check)
        assert is_payday == result

    def test_is_payday_positive0(self):
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
    

    # # TESTS is_payday

    # def test_is_payday_positive0(self):
    #     """Positive Test case to check for paydays in the year
    #        before first payday year.
    #     """
    #     date_to_check = date_class(2018,1,12)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2018,2,23)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2018,11,16)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2018,12,28)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    # def test_is_payday_positive1(self):
    #     """Positive Test case to check if 2 weeks after first payday
    #        was a payday.
    #     """
    #     date_to_check = date_class(2019,2,8)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    # def test_is_payday_positive2(self):
    #     """Positive Test case to check for paydays in the same year
    #        as first payday.
    #     """
    #     date_to_check = date_class(2019,11,1)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2019,11,29)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2019,12,13)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    # def test_is_payday_positive3(self):
    #     """Positive Test case to check for paydays in years
    #        greater than the first payday year.
    #     """
    #     date_to_check = date_class(2020,1,10)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2020,1,24)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2022,10,14)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    # def test_is_payday_positive4(self):
    #     """Positive Test case to check if there were 3 paydays in
    #        the month of October, 2020. (2nd, 16th, 30th)
    #     """
    #     date_to_check = date_class(2020,10,2)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2020,10,16)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2020,10,30)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True


    # def test_is_payday_positive5(self):
    #     """Positive Test case when a payday becomes Thursday 
    #        because Friday was a holiday.
    #     """
    #     date_to_check = date_class(2020,12,24)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2021,12,23)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2022,11,10)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True
    
    # def test_is_payday_positive6(self):
    #     """Positive Test case to check for valid paydays when the first payday
    #        was on a thursday because Friday was a holiday.
    #     """
    #     # Overriding first_payday
    #     self.pay_cycle.first_payday = date_class(2020,12,24)
    #     date_to_check = date_class(2021,1,8)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    #     date_to_check = date_class(2022,8,5)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == True

    # def test_is_payday_negative0(self):
    #     """Negative Test case to check a date less than first payday.
    #     """
    #     date_to_check = date_class(2019,1,24) # The day before first payday
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    #     date_to_check = date_class(2018,12,27)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    #     date_to_check = date_class(2018,2,28)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    # def test_is_payday_negative1(self):
    #     """Negative Test case to check if there is a holiday on 
    #        the default payday then that day is not a payday.
    #     """
    #     date_to_check = date_class(2020,12,25) # Christmas
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    #     date_to_check = date_class(2021,12,24)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    #     date_to_check = date_class(2022,11,11)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    # def test_is_payday_negative2(self):
    #     """Negative Test case to check default paydays in between
    #        biweekly paydays.
    #     """
    #     date_to_check = date_class(2018,11,23)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    #     date_to_check = date_class(2019,1,18)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    #     date_to_check = date_class(2021,12,17)
    #     is_payday = self.pay_cycle.is_payday(date_to_check)
    #     assert is_payday == False

    # # TESTS get_next_payday

    # def test_get_next_payday_positive0(self):
    #     """Positive Test case to check if a date class object is returned.
    #     """
    #     date = date_class(2020,1,1)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert isinstance(next_payday, date_class), \
    #         f'Got {type(next_payday)}, expected Date Class Object'

    # def test_next_payday_positive1(self):
    #     """Positive Test case to check if a correct payday is returned
    #        when given date is <= first_pay of the user.
    #     """
    #     date = date_class(2018,1,14)
    #     expected_next_payday = date_class(2018,1,26)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'
        
    #     date = date_class(2018,11,29)
    #     expected_next_payday = date_class(2018,11,30)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'

    # def test_next_payday_positive2(self):
    #     """Positive Test case to check if the next payday is the very next day
    #        after the date.
    #     """
    #     date = date_class(2019,7,11)
    #     expected_next_payday = date_class(2019,7,12)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'

    #     date = date_class(2022,11,24)
    #     expected_next_payday = date_class(2022,11,25)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'
    
    # def test_next_payday_positive3(self):
    #     """Positive Test case to check if the next payday is on a thursday because
    #        the default payday (i.e Friday) is a holiday.
    #     """
    #     date = date_class(2020,12,12)
    #     expected_next_payday = date_class(2020,12,24)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'
    #     assert WeekPlaceholder(next_payday.weekday()) == WeekPlaceholder.THURSDAY
    
    # def test_next_payday_positive4(self):
    #     """Positive Test case to check if a correct payday from the next year
    #        is returned when the given date is last day of previous year.
    #     """
    #     date = date_class(2020,12,31)
    #     expected_next_payday = date_class(2021,1,8)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'

    # def test_next_payday_positive5(self):
    #     """Positive Test case to check if a correct next bi-weekly payday is returned
    #        when the date passed in is a payday.
    #     """
    #     date = date_class(2021,11,12)
    #     expected_next_payday = date_class(2021,11,26)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'

    #     date = date_class(2022,11,10)
    #     expected_next_payday = date_class(2022,11,25)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'
        
    #     date = date_class(2022,11,25)
    #     expected_next_payday = date_class(2022,12,9)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'


    # def test_next_payday_positive6(self):
    #     """Positive Test case to check if a correct next bi-weekly payday is returned
    #        when a non payday date is passed in.
    #     """
    #     date = date_class(2019,1,12)
    #     expected_next_payday = date_class(2019,1,25)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'

    #     date = date_class(2022,11,26)
    #     expected_next_payday = date_class(2022,12,9)
    #     next_payday = self.pay_cycle.get_next_payday(date)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'

    # def test_next_payday_positive7(self):
    #     """Positive Test case to check if a correct next bi-weekly payday is returned
    #        when the date passed in is the first payday.
    #     """
    #     expected_next_payday = date_class(2019,2,8)
    #     next_payday = self.pay_cycle.get_next_payday(self.first_payday)
    #     assert next_payday == expected_next_payday, \
    #         f'Got {next_payday}, expected {expected_next_payday}'

    # # TESTS get_next_x_paydays

    # def test_get_next_x_paydays_positive0(self):
    #     """Positive Test case to check if correct next x number 
    #        of bi-weekly paydate objects are returned if the
    #        given date is less than first payday.
    #     """
    #     start_date = date_class(2018,1,22)
    #     x_number_of_paydays = 3
    #     expected_next_x_paydays = [
    #         date_class(2018,1,26),
    #         date_class(2018,2,9),
    #         date_class(2018,2,23)
    #     ]

    #     next_x_paydays_list = self.pay_cycle.get_next_x_paydays(x_number_of_paydays, start_date)

    #     assert len(next_x_paydays_list) == x_number_of_paydays, \
    #         f'Got {len(next_x_paydays_list)}, expected {x_number_of_paydays}'
    #     assert next_x_paydays_list == expected_next_x_paydays, \
    #         f'Got {next_x_paydays_list}, expected {expected_next_x_paydays}'

    # def test_get_next_x_paydays_positive1(self):
    #     """Positive Test case to check if correct next x number 
    #        of bi-weekly paydate objects are returned if the
    #        given date is a payday.
    #     """
    #     start_date = date_class(2019,11,15)
    #     x_number_of_paydays = 5
    #     expected_next_x_paydays = [
    #         date_class(2019, 11, 29),
    #         date_class(2019, 12, 13),
    #         date_class(2019, 12, 27),
    #         date_class(2020, 1, 10),
    #         date_class(2020, 1, 24)
    #     ]

    #     next_x_paydays_list = self.pay_cycle.get_next_x_paydays(x_number_of_paydays, start_date)

    #     assert len(next_x_paydays_list) == x_number_of_paydays, \
    #         f'Got {len(next_x_paydays_list)}, expected {x_number_of_paydays}'
    #     assert next_x_paydays_list == expected_next_x_paydays, \
    #         f'Got {next_x_paydays_list}, expected {expected_next_x_paydays}'

    # def test_get_next_x_paydays_positive2(self):
    #     """Positive Test case to check if correct next x number 
    #        of bi-weekly paydate objects are returned if the
    #        given date is not a payday.
    #     """
    #     start_date = date_class(2022,11,3)
    #     x_number_of_paydays = 4
    #     expected_next_x_paydays = [
    #         date_class(2022,11,10),
    #         date_class(2022,11,25),
    #         date_class(2022,12,9),
    #         date_class(2022,12,23),
    #     ]

    #     next_x_paydays_list = self.pay_cycle.get_next_x_paydays(x_number_of_paydays, start_date)

    #     assert len(next_x_paydays_list) == x_number_of_paydays, \
    #         f'Got {len(next_x_paydays_list)}, expected {x_number_of_paydays}'
    #     assert next_x_paydays_list == expected_next_x_paydays, \
    #         f'Got {next_x_paydays_list}, expected {expected_next_x_paydays}'
