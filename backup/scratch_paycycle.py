
# import calendar
from datetime import (
    datetime,
    timedelta,
    date as date_class
)
from dateutil import relativedelta
from helpers import pick_nearest_date, get_valid_date, get_nearest_payday
from enums import WeekPlaceholder
import holidays as h
holidays = h.UnitedStates()

first_payday = date_class(2019,1,11)
last_payday = date_class(2020,8,21)
date=date_class(2022,9,2)
frequency = timedelta(weeks=2)
default_payday = WeekPlaceholder.__getitem__('FRIDAY')
nearest_given_payday = pick_nearest_date(date, first_payday, last_payday)

holiday = None
nearest_payday = nearest_given_payday
if date < nearest_payday:
    # Go Backward
    while (nearest_payday > date):
        if nearest_payday.weekday() != default_payday.value:
            # reset the nearest_payday to follow its original pay cycle
            nearest_payday = holiday

        if (holiday := (nearest_payday - frequency)) in holidays:
            nearest_payday = get_valid_date(holiday)
        else:
            nearest_payday -= frequency
else: 
    # Go Forward
    while (nearest_payday < date):
        if nearest_payday.weekday() != default_payday.value:
            # reset the nearest_payday to follow its original pay cycle
            nearest_payday = holiday

        if (holiday := (nearest_payday + frequency)) in holidays:
            nearest_payday = get_valid_date(holiday)
        else:
            nearest_payday += frequency

print(nearest_payday)


# print(next_payday(date))
























# def next_payday(date: date_class=date_class.today()) -> date_class:
#         if not isinstance(date, date_class):
#             raise RuntimeError('A date class object is required to find the next payday.')
#         if date <= first_payday:
#             return first_payday

#         # Pick the payday that is nearest to 'date'
#         nearest_payday = pick_nearest_date(date, first_payday, last_payday)

#         import calendar
#         from dateutil.relativedelta import relativedelta
#         # calendar.isleap(year)
#         '''
#         first_payday = date_class(2019,1,11)
#         last_payday = date_class(2020,12,24)
#         default_payday = Friday = 4
#         date=date((2022),1,1)
#         nearest_payday = pick_nearest_date(date, first_payday, last_payday)
#         nearest_payday is lastpayday


#         '''
#         time_difference = relativedelta(date, nearest_payday)
#         difference_in_years = time_difference.years
#         if difference_in_years > 0:
#             # relativedelta takes care of the leap year
#             curr_date = nearest_payday + relativedelta(weeks=52*difference_in_years)
#         time_difference = relativedelta(date, curr_date)
#         difference_in_months = time_difference.months 
#         if difference_in_months > 0:
#             # relativedelta takes care of the leap year
#             curr_date = nearest_payday + relativedelta(weeks=difference_in_months*4)
#         time_difference = relativedelta(date, curr_date)
#         difference_in_weeks = time_difference.weeks 
#         if difference_in_weeks > 0:
#             # relativedelta takes care of the leap year
#             curr_date = nearest_payday + relativedelta(weeks=difference_in_weeks)
#         time_difference = relativedelta(date, curr_date)
#         difference_in_days = time_difference.days 
#         if difference_in_days > 0:
#             # relativedelta takes care of the leap year
#             curr_date = nearest_payday + relativedelta(weeks=difference_in_weeks)




#         start = date_class(2020,12,24) # Thursday
#         default_payday = 4 # Friday
#         if curr_day.weekday() != default_payday:
#             # reset the curr_day to follow its original pay cycle
#             # a function which will goto to the default payday
#             # curr_day = reset/get_to_default_payday()
        


#         time_difference = relativedelta(date, nearest_payday)
#         difference_in_years = time_difference.years
#         if difference_in_years > 0:
#             # relativedelta takes care of the leap year
            
#             curr_date = nearest_payday + relativedelta(weeks=52*difference_in_years)
        

#         if (holiday := (curr_day + relativedelta(weeks=52)) in self.holidays:
#             curr_day = get_valid_payday(holiday)
#         else:
#             curr_day += self.frequency
        

#         # fucntions
#         # 1. move by years
#         # 2. move by months(do 4 weeks)
#         # 3. move by weeks (1 week)
#         # 4. move by days (1 day)
        

# date=date_class(2022,11,23)
# print(next_payday(date))



















"""
#           YYYY-MM-DD
# first_pd = '2019-01-11'
first_pd = date_class(2020, 1, 10)
# date_to_check = '2020-01-10' # it is a paydate
date_to_check = date_class(2020, 1, 24)

frequency = timedelta(weeks=2)

while first_pd <= date_to_check:
    if first_pd == date_to_check:
        print('YAYYY')
    '''
    if date_to_check is holiday
        return false
    
    if first_pd + frequency(+14) == a holiday
        first_pd = get_next_available_date(holiday)
    '''
    if first_pd + frequency == a holiday
        first_pd = get_next_available_date(holiday)

    first_pd = first_pd + frequency

from datetime import date
# Making sure that the next avaialble date is a business day AND nearest
def get_valid_payday(holiday: date):

    # for a weekday, monday is 0 and sunday is 6
    week_day_placeholder = (holiday + timedelta(days=1)).weekday()
    num_of_days_after = 1
    while week_day_placeholder in {5,6}:
        num_of_days_after += 1
        week_day_placeholder = (holiday + timedelta(days=num_of_days_after)).weekday()
        
    week_day_placeholder = (holiday - timedelta(days=1)).weekday()
    num_of_days_before = 1
    while week_day_placeholder in {5,6}:
        num_of_days_before += 1
        week_day_placeholder = (holiday - timedelta(days=num_of_days_before)).weekday()

    # POST PROCESS
    if num_of_days_before < num_of_days_after:
        return holiday - timedelta(days=num_of_days_before)
    else:
        return holiday + timedelta(days=num_of_days_after)
        



holiday = date(2020,10,12)
print(get_next_available_date(holiday))

# def is_payday(date: date_class = None) -> bool:

#     if (date - self.last_payday) % frequency == 0:
#         return True
#     return False
# while first_pd <= date_to_check:

# breakpoint()










"""









