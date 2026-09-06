from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentsManagementTrainingPaymentsMarkPaidCreateBody")


@_attrs_define
class PaymentsManagementTrainingPaymentsMarkPaidCreateBody:
    """
    Attributes:
        child_id (int):  Example: 10.
        month (str): YYYY-MM Example: 2026-07.
        group_id (int | Unset):  Example: 5.
    """

    child_id: int
    month: str
    group_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        child_id = self.child_id

        month = self.month

        group_id = self.group_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "child_id": child_id,
                "month": month,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        child_id = d.pop("child_id")

        month = d.pop("month")

        group_id = d.pop("group_id", UNSET)

        payments_management_training_payments_mark_paid_create_body = cls(
            child_id=child_id,
            month=month,
            group_id=group_id,
        )

        return payments_management_training_payments_mark_paid_create_body
