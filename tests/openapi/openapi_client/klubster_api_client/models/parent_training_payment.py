from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paid_via_enum import PaidViaEnum
from ..models.parent_training_payment_status_enum import ParentTrainingPaymentStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParentTrainingPayment")


@_attrs_define
class ParentTrainingPayment:
    """
    Attributes:
        id (int):
        amount (str):
        status (ParentTrainingPaymentStatusEnum): * `unpaid` - Nieopłacona
            * `paid` - Opłacona
            * `pay_in_club` - Opłać w klubie
            * `payed_in_club` - Opłacona w klubie
        status_label (str):
        paid_via (PaidViaEnum): * `blik` - BLIK
        paid_via_label (str):
        paid_at (datetime.datetime | None):
        child (int):
        child_name (str):
        group_name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        title (str | Unset):
        currency (str | Unset):
        due_date (datetime.date | None | Unset):
        notes (str | Unset):
        group (int | None | Unset):
    """

    id: int
    amount: str
    status: ParentTrainingPaymentStatusEnum
    status_label: str
    paid_via: PaidViaEnum
    paid_via_label: str
    paid_at: datetime.datetime | None
    child: int
    child_name: str
    group_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    title: str | Unset = UNSET
    currency: str | Unset = UNSET
    due_date: datetime.date | None | Unset = UNSET
    notes: str | Unset = UNSET
    group: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        status = self.status.value

        status_label = self.status_label

        paid_via = self.paid_via.value

        paid_via_label = self.paid_via_label

        paid_at: None | str
        if isinstance(self.paid_at, datetime.datetime):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        child = self.child

        child_name = self.child_name

        group_name = self.group_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        title = self.title

        currency = self.currency

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        notes = self.notes

        group: int | None | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "amount": amount,
                "status": status,
                "status_label": status_label,
                "paid_via": paid_via,
                "paid_via_label": paid_via_label,
                "paid_at": paid_at,
                "child": child,
                "child_name": child_name,
                "group_name": group_name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if currency is not UNSET:
            field_dict["currency"] = currency
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        amount = d.pop("amount")

        status = ParentTrainingPaymentStatusEnum(d.pop("status"))

        status_label = d.pop("status_label")

        paid_via = PaidViaEnum(d.pop("paid_via"))

        paid_via_label = d.pop("paid_via_label")

        def _parse_paid_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = datetime.datetime.fromisoformat(data)

                return paid_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        paid_at = _parse_paid_at(d.pop("paid_at"))

        child = d.pop("child")

        child_name = d.pop("child_name")

        group_name = d.pop("group_name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        title = d.pop("title", UNSET)

        currency = d.pop("currency", UNSET)

        def _parse_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = datetime.date.fromisoformat(data)

                return due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        notes = d.pop("notes", UNSET)

        def _parse_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        parent_training_payment = cls(
            id=id,
            amount=amount,
            status=status,
            status_label=status_label,
            paid_via=paid_via,
            paid_via_label=paid_via_label,
            paid_at=paid_at,
            child=child,
            child_name=child_name,
            group_name=group_name,
            created_at=created_at,
            updated_at=updated_at,
            title=title,
            currency=currency,
            due_date=due_date,
            notes=notes,
            group=group,
        )

        parent_training_payment.additional_properties = d
        return parent_training_payment

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
