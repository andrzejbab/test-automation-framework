from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_status_enum import PaymentStatusEnum
from ..models.sport_object_reservation_status_enum import SportObjectReservationStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SportObjectReservation")


@_attrs_define
class SportObjectReservation:
    """
    Attributes:
        id (int):
        sport_object (int):
        reserved_by (int | None):
        reserved_by_name (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status (SportObjectReservationStatusEnum | Unset): * `pending` - Oczekująca
            * `confirmed` - Potwierdzona
            * `cancelled` - Anulowana
        payment_status (PaymentStatusEnum | Unset): * `unpaid` - Nie zapłacono
            * `pay_in_club` - Płatność w klubie
            * `paid` - Zapłacono
        extras (list[int] | Unset):
        recurring_weeks (int | None | Unset):
        recurring_weekdays (Any | Unset):
        notes (str | Unset):
    """

    id: int
    sport_object: int
    reserved_by: int | None
    reserved_by_name: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: SportObjectReservationStatusEnum | Unset = UNSET
    payment_status: PaymentStatusEnum | Unset = UNSET
    extras: list[int] | Unset = UNSET
    recurring_weeks: int | None | Unset = UNSET
    recurring_weekdays: Any | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sport_object = self.sport_object

        reserved_by: int | None
        reserved_by = self.reserved_by

        reserved_by_name = self.reserved_by_name

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_status: str | Unset = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        extras: list[int] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras

        recurring_weeks: int | None | Unset
        if isinstance(self.recurring_weeks, Unset):
            recurring_weeks = UNSET
        else:
            recurring_weeks = self.recurring_weeks

        recurring_weekdays = self.recurring_weekdays

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sport_object": sport_object,
                "reserved_by": reserved_by,
                "reserved_by_name": reserved_by_name,
                "start_time": start_time,
                "end_time": end_time,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
        if extras is not UNSET:
            field_dict["extras"] = extras
        if recurring_weeks is not UNSET:
            field_dict["recurring_weeks"] = recurring_weeks
        if recurring_weekdays is not UNSET:
            field_dict["recurring_weekdays"] = recurring_weekdays
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sport_object = d.pop("sport_object")

        def _parse_reserved_by(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        reserved_by = _parse_reserved_by(d.pop("reserved_by"))

        reserved_by_name = d.pop("reserved_by_name")

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        end_time = datetime.datetime.fromisoformat(d.pop("end_time"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _status = d.pop("status", UNSET)
        status: SportObjectReservationStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SportObjectReservationStatusEnum(_status)

        _payment_status = d.pop("payment_status", UNSET)
        payment_status: PaymentStatusEnum | Unset
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = PaymentStatusEnum(_payment_status)

        extras = cast(list[int], d.pop("extras", UNSET))

        def _parse_recurring_weeks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        recurring_weeks = _parse_recurring_weeks(d.pop("recurring_weeks", UNSET))

        recurring_weekdays = d.pop("recurring_weekdays", UNSET)

        notes = d.pop("notes", UNSET)

        sport_object_reservation = cls(
            id=id,
            sport_object=sport_object,
            reserved_by=reserved_by,
            reserved_by_name=reserved_by_name,
            start_time=start_time,
            end_time=end_time,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            payment_status=payment_status,
            extras=extras,
            recurring_weeks=recurring_weeks,
            recurring_weekdays=recurring_weekdays,
            notes=notes,
        )

        sport_object_reservation.additional_properties = d
        return sport_object_reservation

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
