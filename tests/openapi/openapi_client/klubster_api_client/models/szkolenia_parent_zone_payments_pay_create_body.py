from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.szkolenia_parent_zone_payments_pay_create_body_method import (
    SzkoleniaParentZonePaymentsPayCreateBodyMethod,
)

T = TypeVar("T", bound="SzkoleniaParentZonePaymentsPayCreateBody")


@_attrs_define
class SzkoleniaParentZonePaymentsPayCreateBody:
    """
    Attributes:
        method (SzkoleniaParentZonePaymentsPayCreateBodyMethod):  Example: blik.
    """

    method: SzkoleniaParentZonePaymentsPayCreateBodyMethod

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = SzkoleniaParentZonePaymentsPayCreateBodyMethod(d.pop("method"))

        szkolenia_parent_zone_payments_pay_create_body = cls(
            method=method,
        )

        return szkolenia_parent_zone_payments_pay_create_body
