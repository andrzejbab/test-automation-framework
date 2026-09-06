from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClubCalendarEvent")


@_attrs_define
class ClubCalendarEvent:
    """
    Attributes:
        id (int):
        title (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        created_by (int | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (str | Unset):
        location (str | Unset):
        all_day (bool | Unset):
    """

    id: int
    title: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    created_by: int | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    location: str | Unset = UNSET
    all_day: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        created_by: int | None
        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        location = self.location

        all_day = self.all_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "start_time": start_time,
                "end_time": end_time,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if all_day is not UNSET:
            field_dict["all_day"] = all_day

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        files.append(("start_time", (None, self.start_time.isoformat().encode(), "text/plain")))

        files.append(("end_time", (None, self.end_time.isoformat().encode(), "text/plain")))

        if isinstance(self.created_by, int):
            files.append(("created_by", (None, str(self.created_by).encode(), "text/plain")))
        else:
            files.append(("created_by", (None, str(self.created_by).encode(), "text/plain")))

        files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.location, Unset):
            files.append(("location", (None, str(self.location).encode(), "text/plain")))

        if not isinstance(self.all_day, Unset):
            files.append(("all_day", (None, str(self.all_day).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        end_time = datetime.datetime.fromisoformat(d.pop("end_time"))

        def _parse_created_by(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        created_by = _parse_created_by(d.pop("created_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        location = d.pop("location", UNSET)

        all_day = d.pop("all_day", UNSET)

        club_calendar_event = cls(
            id=id,
            title=title,
            start_time=start_time,
            end_time=end_time,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            location=location,
            all_day=all_day,
        )

        club_calendar_event.additional_properties = d
        return club_calendar_event

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
