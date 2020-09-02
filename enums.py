from datetime import timedelta
from enum import Enum
from dateutil.relativedelta import relativedelta

class PayCycleType(Enum):
    BI_WEEKLY = timedelta(weeks=2)
    WEEKLY = timedelta(weeks=1)

class WeekPlaceholder(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6