from datetime import timedelta
from enum import Enum

class PayCycleType(Enum):
    BI_WEEKLY = timedelta(weeks=2)

class WeekPlaceholder(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6