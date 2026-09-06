from enum import Enum


class SportObjectReservationStatusEnum(str, Enum):
    CANCELLED = "cancelled"
    CONFIRMED = "confirmed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
