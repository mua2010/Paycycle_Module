

from datetime import (
    datetime,
    timedelta,
    date as date_class
)

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




















# def getValidBusinessDate(dt):
#     # For weekday(), Monday is 0 and Sunday is 6.
#     breakpoint()
#     days_to_substract = dt.weekday() - 4
#     if days_to_substract > 0:
#         d = dt - datetime.timedelta(days=days_to_substract)
#         return d
#     else:
#         return dt

# d = datetime.datetime(2020, 1, 8)
# print( getValidBusinessDate(d) )

# from datetime import (
#     datetime,
#     timedelta,
#     date as date_class
# )

# freq = timedelta(weeks=2)
# start = date_class(2018, 1, 12)
# end = date_class(2018, 12, 31)

# paydays = [start]
# curr_d = start
# while curr_d < end:
#     curr_d += freq
#     paydays.append(curr_d)

# print(paydays)

# breakpoint()