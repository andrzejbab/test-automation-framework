from enum import Enum


class ParentTrainingPaymentStatusEnum(str, Enum):
    PAID = "paid"
    PAYED_IN_CLUB = "payed_in_club"
    PAY_IN_CLUB = "pay_in_club"
    UNPAID = "unpaid"

    def __str__(self) -> str:
        return str(self.value)
