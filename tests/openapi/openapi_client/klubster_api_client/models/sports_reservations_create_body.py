from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SportsReservationsCreateBody")


@_attrs_define
class SportsReservationsCreateBody:
    """
    Attributes:
        sport_object (int):  Example: 1.
        start_time (datetime.datetime):  Example: 2026-07-07T10:00:00Z.
        end_time (datetime.datetime):  Example: 2026-07-07T11:00:00Z.
        title (str | Unset):  Example: Morning training reservation.
        notes (str | Unset):  Example: Optional details.
        status (str | Unset):  Example: booked.
        send_confirmation_email (bool | Unset):  Example: True.
    """

    sport_object: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    title: str | Unset = UNSET
    notes: str | Unset = UNSET
    status: str | Unset = UNSET
    send_confirmation_email: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sport_object = self.sport_object

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        title = self.title

        notes = self.notes

        status = self.status

        send_confirmation_email = self.send_confirmation_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sport_object": sport_object,
                "start_time": start_time,
                "end_time": end_time,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if notes is not UNSET:
            field_dict["notes"] = notes
        if status is not UNSET:
            field_dict["status"] = status
        if send_confirmation_email is not UNSET:
            field_dict["send_confirmation_email"] = send_confirmation_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sport_object = d.pop("sport_object")

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        end_time = datetime.datetime.fromisoformat(d.pop("end_time"))

        title = d.pop("title", UNSET)

        notes = d.pop("notes", UNSET)

        status = d.pop("status", UNSET)

        send_confirmation_email = d.pop("send_confirmation_email", UNSET)

        sports_reservations_create_body = cls(
            sport_object=sport_object,
            start_time=start_time,
            end_time=end_time,
            title=title,
            notes=notes,
            status=status,
            send_confirmation_email=send_confirmation_email,
        )

        sports_reservations_create_body.additional_properties = d
        return sports_reservations_create_body

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
