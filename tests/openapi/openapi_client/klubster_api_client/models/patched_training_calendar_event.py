from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTrainingCalendarEvent")


@_attrs_define
class PatchedTrainingCalendarEvent:
    """
    Attributes:
        id (int | Unset):
        title (str | Unset):
        group (int | None | Unset):
        group_id (int | Unset):
        group_name (str | Unset):
        sport_object (int | None | Unset):
        sport_object_id (int | None | Unset):
        sport_object_name (str | Unset):
        sport_object_location (str | Unset):
        trainer_price_per_hour (str | Unset):
        object_price_per_hour (str | Unset):
        child_price_per_hour (str | Unset):
        group_members_count (str | Unset):
        reservation (int | None | Unset):
        reservation_id (int | None | Unset):
        reservation_ids (list[int] | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        notes (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    title: str | Unset = UNSET
    group: int | None | Unset = UNSET
    group_id: int | Unset = UNSET
    group_name: str | Unset = UNSET
    sport_object: int | None | Unset = UNSET
    sport_object_id: int | None | Unset = UNSET
    sport_object_name: str | Unset = UNSET
    sport_object_location: str | Unset = UNSET
    trainer_price_per_hour: str | Unset = UNSET
    object_price_per_hour: str | Unset = UNSET
    child_price_per_hour: str | Unset = UNSET
    group_members_count: str | Unset = UNSET
    reservation: int | None | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    reservation_ids: list[int] | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    notes: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        group: int | None | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        group_id = self.group_id

        group_name = self.group_name

        sport_object: int | None | Unset
        if isinstance(self.sport_object, Unset):
            sport_object = UNSET
        else:
            sport_object = self.sport_object

        sport_object_id: int | None | Unset
        if isinstance(self.sport_object_id, Unset):
            sport_object_id = UNSET
        else:
            sport_object_id = self.sport_object_id

        sport_object_name = self.sport_object_name

        sport_object_location = self.sport_object_location

        trainer_price_per_hour = self.trainer_price_per_hour

        object_price_per_hour = self.object_price_per_hour

        child_price_per_hour = self.child_price_per_hour

        group_members_count = self.group_members_count

        reservation: int | None | Unset
        if isinstance(self.reservation, Unset):
            reservation = UNSET
        else:
            reservation = self.reservation

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        reservation_ids: list[int] | Unset = UNSET
        if not isinstance(self.reservation_ids, Unset):
            reservation_ids = self.reservation_ids

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        notes = self.notes

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if group is not UNSET:
            field_dict["group"] = group
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if sport_object is not UNSET:
            field_dict["sport_object"] = sport_object
        if sport_object_id is not UNSET:
            field_dict["sport_object_id"] = sport_object_id
        if sport_object_name is not UNSET:
            field_dict["sport_object_name"] = sport_object_name
        if sport_object_location is not UNSET:
            field_dict["sport_object_location"] = sport_object_location
        if trainer_price_per_hour is not UNSET:
            field_dict["trainer_price_per_hour"] = trainer_price_per_hour
        if object_price_per_hour is not UNSET:
            field_dict["object_price_per_hour"] = object_price_per_hour
        if child_price_per_hour is not UNSET:
            field_dict["child_price_per_hour"] = child_price_per_hour
        if group_members_count is not UNSET:
            field_dict["group_members_count"] = group_members_count
        if reservation is not UNSET:
            field_dict["reservation"] = reservation
        if reservation_id is not UNSET:
            field_dict["reservation_id"] = reservation_id
        if reservation_ids is not UNSET:
            field_dict["reservation_ids"] = reservation_ids
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if notes is not UNSET:
            field_dict["notes"] = notes
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.group, Unset):
            if isinstance(self.group, int):
                files.append(("group", (None, str(self.group).encode(), "text/plain")))
            else:
                files.append(("group", (None, str(self.group).encode(), "text/plain")))

        if not isinstance(self.group_id, Unset):
            files.append(("group_id", (None, str(self.group_id).encode(), "text/plain")))

        if not isinstance(self.group_name, Unset):
            files.append(("group_name", (None, str(self.group_name).encode(), "text/plain")))

        if not isinstance(self.sport_object, Unset):
            if isinstance(self.sport_object, int):
                files.append(("sport_object", (None, str(self.sport_object).encode(), "text/plain")))
            else:
                files.append(("sport_object", (None, str(self.sport_object).encode(), "text/plain")))

        if not isinstance(self.sport_object_id, Unset):
            if isinstance(self.sport_object_id, int):
                files.append(("sport_object_id", (None, str(self.sport_object_id).encode(), "text/plain")))
            else:
                files.append(("sport_object_id", (None, str(self.sport_object_id).encode(), "text/plain")))

        if not isinstance(self.sport_object_name, Unset):
            files.append(("sport_object_name", (None, str(self.sport_object_name).encode(), "text/plain")))

        if not isinstance(self.sport_object_location, Unset):
            files.append(("sport_object_location", (None, str(self.sport_object_location).encode(), "text/plain")))

        if not isinstance(self.trainer_price_per_hour, Unset):
            files.append(("trainer_price_per_hour", (None, str(self.trainer_price_per_hour).encode(), "text/plain")))

        if not isinstance(self.object_price_per_hour, Unset):
            files.append(("object_price_per_hour", (None, str(self.object_price_per_hour).encode(), "text/plain")))

        if not isinstance(self.child_price_per_hour, Unset):
            files.append(("child_price_per_hour", (None, str(self.child_price_per_hour).encode(), "text/plain")))

        if not isinstance(self.group_members_count, Unset):
            files.append(("group_members_count", (None, str(self.group_members_count).encode(), "text/plain")))

        if not isinstance(self.reservation, Unset):
            if isinstance(self.reservation, int):
                files.append(("reservation", (None, str(self.reservation).encode(), "text/plain")))
            else:
                files.append(("reservation", (None, str(self.reservation).encode(), "text/plain")))

        if not isinstance(self.reservation_id, Unset):
            if isinstance(self.reservation_id, int):
                files.append(("reservation_id", (None, str(self.reservation_id).encode(), "text/plain")))
            else:
                files.append(("reservation_id", (None, str(self.reservation_id).encode(), "text/plain")))

        if not isinstance(self.reservation_ids, Unset):
            for reservation_ids_item_element in self.reservation_ids:
                files.append(("reservation_ids", (None, str(reservation_ids_item_element).encode(), "text/plain")))

        if not isinstance(self.start_time, Unset):
            files.append(("start_time", (None, self.start_time.isoformat().encode(), "text/plain")))

        if not isinstance(self.end_time, Unset):
            files.append(("end_time", (None, self.end_time.isoformat().encode(), "text/plain")))

        if not isinstance(self.notes, Unset):
            files.append(("notes", (None, str(self.notes).encode(), "text/plain")))

        if not isinstance(self.created_at, Unset):
            files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.updated_at, Unset):
            files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        def _parse_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        group_id = d.pop("group_id", UNSET)

        group_name = d.pop("group_name", UNSET)

        def _parse_sport_object(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sport_object = _parse_sport_object(d.pop("sport_object", UNSET))

        def _parse_sport_object_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sport_object_id = _parse_sport_object_id(d.pop("sport_object_id", UNSET))

        sport_object_name = d.pop("sport_object_name", UNSET)

        sport_object_location = d.pop("sport_object_location", UNSET)

        trainer_price_per_hour = d.pop("trainer_price_per_hour", UNSET)

        object_price_per_hour = d.pop("object_price_per_hour", UNSET)

        child_price_per_hour = d.pop("child_price_per_hour", UNSET)

        group_members_count = d.pop("group_members_count", UNSET)

        def _parse_reservation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation = _parse_reservation(d.pop("reservation", UNSET))

        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservation_id", UNSET))

        reservation_ids = cast(list[int], d.pop("reservation_ids", UNSET))

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

        notes = d.pop("notes", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        patched_training_calendar_event = cls(
            id=id,
            title=title,
            group=group,
            group_id=group_id,
            group_name=group_name,
            sport_object=sport_object,
            sport_object_id=sport_object_id,
            sport_object_name=sport_object_name,
            sport_object_location=sport_object_location,
            trainer_price_per_hour=trainer_price_per_hour,
            object_price_per_hour=object_price_per_hour,
            child_price_per_hour=child_price_per_hour,
            group_members_count=group_members_count,
            reservation=reservation,
            reservation_id=reservation_id,
            reservation_ids=reservation_ids,
            start_time=start_time,
            end_time=end_time,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_training_calendar_event.additional_properties = d
        return patched_training_calendar_event

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
