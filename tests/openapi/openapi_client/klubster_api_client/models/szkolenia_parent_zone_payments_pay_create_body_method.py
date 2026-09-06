from enum import Enum


class SzkoleniaParentZonePaymentsPayCreateBodyMethod(str, Enum):
    BLIK = "blik"
    CLUB = "club"

    def __str__(self) -> str:
        return str(self.value)
