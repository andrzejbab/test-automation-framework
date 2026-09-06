from enum import Enum


class KindEnum(str, Enum):
    CLOSED = "closed"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
