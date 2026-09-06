from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SportsReservationsPartialUpdateBody")


@_attrs_define
class SportsReservationsPartialUpdateBody:
    """
    Attributes:
        sport_object (int | Unset):  Example: 1.
        start_time (datetime.datetime | Unset):  Example: 2026-07-07T10:00:00Z.
        end_time (datetime.datetime | Unset):  Example: 2026-07-07T11:00:00Z.
        title (str | Unset):  Example: Updated reservation.
        notes (str | Unset):  Example: Updated notes.
        status (str | Unset):  Example: cancelled.
        send_cancellation_email (bool | Unset):  Example: True.
    """

    sport_object: int | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    title: str | Unset = UNSET
    notes: str | Unset = UNSET
    status: str | Unset = UNSET
    send_cancellation_email: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sport_object = self.sport_object

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        title = self.title

        notes = self.notes

        status = self.status

        send_cancellation_email = self.send_cancellation_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sport_object is not UNSET:
            field_dict["sport_object"] = sport_object
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if title is not UNSET:
            field_dict["title"] = title
        if notes is not UNSET:
            field_dict["notes"] = notes
        if status is not UNSET:
            field_dict["status"] = status
        if send_cancellation_email is not UNSET:
            field_dict["send_cancellation_email"] = send_cancellation_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sport_object = d.pop("sport_object", UNSET)

        _start_time = d.pop("start_time", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        _end_time = d.pop("end_time", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = datetime.datetime.fromisoformat(_end_time)

        title = d.pop("title", UNSET)

        notes = d.pop("notes", UNSET)

        status = d.pop("status", UNSET)

        send_cancellation_email = d.pop("send_cancellation_email", UNSET)

        sports_reservations_partial_update_body = cls(
            sport_object=sport_object,
            start_time=start_time,
            end_time=end_time,
            title=title,
            notes=notes,
            status=status,
            send_cancellation_email=send_cancellation_email,
        )

        sports_reservations_partial_update_body.additional_properties = d
        return sports_reservations_partial_update_body

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
