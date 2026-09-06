from enum import Enum


class PaidViaEnum(str, Enum):
    BLIK = "blik"

    def __str__(self) -> str:
        return str(self.value)
