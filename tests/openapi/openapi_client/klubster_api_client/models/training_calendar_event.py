from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingCalendarEvent")


@_attrs_define
class TrainingCalendarEvent:
    """
    Attributes:
        id (int):
        title (str):
        group (int | None):
        group_name (str):
        sport_object (int | None):
        sport_object_name (str):
        sport_object_location (str):
        trainer_price_per_hour (str):
        object_price_per_hour (str):
        child_price_per_hour (str):
        group_members_count (str):
        reservation (int | None):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        group_id (int | Unset):
        sport_object_id (int | None | Unset):
        reservation_id (int | None | Unset):
        reservation_ids (list[int] | Unset):
        notes (str | Unset):
    """

    id: int
    title: str
    group: int | None
    group_name: str
    sport_object: int | None
    sport_object_name: str
    sport_object_location: str
    trainer_price_per_hour: str
    object_price_per_hour: str
    child_price_per_hour: str
    group_members_count: str
    reservation: int | None
    start_time: datetime.datetime
    end_time: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    group_id: int | Unset = UNSET
    sport_object_id: int | None | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    reservation_ids: list[int] | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        group: int | None
        group = self.group

        group_name = self.group_name

        sport_object: int | None
        sport_object = self.sport_object

        sport_object_name = self.sport_object_name

        sport_object_location = self.sport_object_location

        trainer_price_per_hour = self.trainer_price_per_hour

        object_price_per_hour = self.object_price_per_hour

        child_price_per_hour = self.child_price_per_hour

        group_members_count = self.group_members_count

        reservation: int | None
        reservation = self.reservation

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        group_id = self.group_id

        sport_object_id: int | None | Unset
        if isinstance(self.sport_object_id, Unset):
            sport_object_id = UNSET
        else:
            sport_object_id = self.sport_object_id

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        reservation_ids: list[int] | Unset = UNSET
        if not isinstance(self.reservation_ids, Unset):
            reservation_ids = self.reservation_ids

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "group": group,
                "group_name": group_name,
                "sport_object": sport_object,
                "sport_object_name": sport_object_name,
                "sport_object_location": sport_object_location,
                "trainer_price_per_hour": trainer_price_per_hour,
                "object_price_per_hour": object_price_per_hour,
                "child_price_per_hour": child_price_per_hour,
                "group_members_count": group_members_count,
                "reservation": reservation,
                "start_time": start_time,
                "end_time": end_time,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if sport_object_id is not UNSET:
            field_dict["sport_object_id"] = sport_object_id
        if reservation_id is not UNSET:
            field_dict["reservation_id"] = reservation_id
        if reservation_ids is not UNSET:
            field_dict["reservation_ids"] = reservation_ids
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if isinstance(self.group, int):
            files.append(("group", (None, str(self.group).encode(), "text/plain")))
        else:
            files.append(("group", (None, str(self.group).encode(), "text/plain")))

        files.append(("group_name", (None, str(self.group_name).encode(), "text/plain")))

        if isinstance(self.sport_object, int):
            files.append(("sport_object", (None, str(self.sport_object).encode(), "text/plain")))
        else:
            files.append(("sport_object", (None, str(self.sport_object).encode(), "text/plain")))

        files.append(("sport_object_name", (None, str(self.sport_object_name).encode(), "text/plain")))

        files.append(("sport_object_location", (None, str(self.sport_object_location).encode(), "text/plain")))

        files.append(("trainer_price_per_hour", (None, str(self.trainer_price_per_hour).encode(), "text/plain")))

        files.append(("object_price_per_hour", (None, str(self.object_price_per_hour).encode(), "text/plain")))

        files.append(("child_price_per_hour", (None, str(self.child_price_per_hour).encode(), "text/plain")))

        files.append(("group_members_count", (None, str(self.group_members_count).encode(), "text/plain")))

        if isinstance(self.reservation, int):
            files.append(("reservation", (None, str(self.reservation).encode(), "text/plain")))
        else:
            files.append(("reservation", (None, str(self.reservation).encode(), "text/plain")))

        files.append(("start_time", (None, self.start_time.isoformat().encode(), "text/plain")))

        files.append(("end_time", (None, self.end_time.isoformat().encode(), "text/plain")))

        files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.group_id, Unset):
            files.append(("group_id", (None, str(self.group_id).encode(), "text/plain")))

        if not isinstance(self.sport_object_id, Unset):
            if isinstance(self.sport_object_id, int):
                files.append(("sport_object_id", (None, str(self.sport_object_id).encode(), "text/plain")))
            else:
                files.append(("sport_object_id", (None, str(self.sport_object_id).encode(), "text/plain")))

        if not isinstance(self.reservation_id, Unset):
            if isinstance(self.reservation_id, int):
                files.append(("reservation_id", (None, str(self.reservation_id).encode(), "text/plain")))
            else:
                files.append(("reservation_id", (None, str(self.reservation_id).encode(), "text/plain")))

        if not isinstance(self.reservation_ids, Unset):
            for reservation_ids_item_element in self.reservation_ids:
                files.append(("reservation_ids", (None, str(reservation_ids_item_element).encode(), "text/plain")))

        if not isinstance(self.notes, Unset):
            files.append(("notes", (None, str(self.notes).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_group(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        group = _parse_group(d.pop("group"))

        group_name = d.pop("group_name")

        def _parse_sport_object(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sport_object = _parse_sport_object(d.pop("sport_object"))

        sport_object_name = d.pop("sport_object_name")

        sport_object_location = d.pop("sport_object_location")

        trainer_price_per_hour = d.pop("trainer_price_per_hour")

        object_price_per_hour = d.pop("object_price_per_hour")

        child_price_per_hour = d.pop("child_price_per_hour")

        group_members_count = d.pop("group_members_count")

        def _parse_reservation(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        reservation = _parse_reservation(d.pop("reservation"))

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        end_time = datetime.datetime.fromisoformat(d.pop("end_time"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        group_id = d.pop("group_id", UNSET)

        def _parse_sport_object_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sport_object_id = _parse_sport_object_id(d.pop("sport_object_id", UNSET))

        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservation_id", UNSET))

        reservation_ids = cast(list[int], d.pop("reservation_ids", UNSET))

        notes = d.pop("notes", UNSET)

        training_calendar_event = cls(
            id=id,
            title=title,
            group=group,
            group_name=group_name,
            sport_object=sport_object,
            sport_object_name=sport_object_name,
            sport_object_location=sport_object_location,
            trainer_price_per_hour=trainer_price_per_hour,
            object_price_per_hour=object_price_per_hour,
            child_price_per_hour=child_price_per_hour,
            group_members_count=group_members_count,
            reservation=reservation,
            start_time=start_time,
            end_time=end_time,
            created_at=created_at,
            updated_at=updated_at,
            group_id=group_id,
            sport_object_id=sport_object_id,
            reservation_id=reservation_id,
            reservation_ids=reservation_ids,
            notes=notes,
        )

        training_calendar_event.additional_properties = d
        return training_calendar_event

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
