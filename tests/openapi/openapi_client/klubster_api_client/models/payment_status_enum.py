from enum import Enum


class PaymentStatusEnum(str, Enum):
    PAID = "paid"
    PAY_IN_CLUB = "pay_in_club"
    UNPAID = "unpaid"

    def __str__(self) -> str:
        return str(self.value)
