from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SzkoleniaParentZoneCalendarMonthPayInClubCreateBody")


@_attrs_define
class SzkoleniaParentZoneCalendarMonthPayInClubCreateBody:
    """
    Attributes:
        month (str): Month in YYYY-MM format Example: 2026-07.
    """

    month: str

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "month": month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        szkolenia_parent_zone_calendar_month_pay_in_club_create_body = cls(
            month=month,
        )

        return szkolenia_parent_zone_calendar_month_pay_in_club_create_body
