from enum import Enum


class DayTypeEnum(str, Enum):
    WEEKDAY = "weekday"
    WEEKEND = "weekend"

    def __str__(self) -> str:
        return str(self.value)
