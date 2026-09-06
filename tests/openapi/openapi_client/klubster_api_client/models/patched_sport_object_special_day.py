from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.kind_enum import KindEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSportObjectSpecialDay")


@_attrs_define
class PatchedSportObjectSpecialDay:
    """
    Attributes:
        id (int | Unset):
        sport_object (int | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        start_time (None | str | Unset):
        end_time (None | str | Unset):
        kind (KindEnum | Unset): * `closed` - Zamknięte
            * `reserved` - Zarezerwowane
        label (str | Unset):
        notes (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    sport_object: int | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    start_time: None | str | Unset = UNSET
    end_time: None | str | Unset = UNSET
    kind: KindEnum | Unset = UNSET
    label: str | Unset = UNSET
    notes: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sport_object = self.sport_object

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        label = self.label

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
        if sport_object is not UNSET:
            field_dict["sport_object"] = sport_object
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
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

        if not isinstance(self.sport_object, Unset):
            files.append(("sport_object", (None, str(self.sport_object).encode(), "text/plain")))

        if not isinstance(self.start_date, Unset):
            files.append(("start_date", (None, self.start_date.isoformat().encode(), "text/plain")))

        if not isinstance(self.end_date, Unset):
            files.append(("end_date", (None, self.end_date.isoformat().encode(), "text/plain")))

        if not isinstance(self.start_time, Unset):
            if isinstance(self.start_time, str):
                files.append(("start_time", (None, str(self.start_time).encode(), "text/plain")))
            else:
                files.append(("start_time", (None, str(self.start_time).encode(), "text/plain")))

        if not isinstance(self.end_time, Unset):
            if isinstance(self.end_time, str):
                files.append(("end_time", (None, str(self.end_time).encode(), "text/plain")))
            else:
                files.append(("end_time", (None, str(self.end_time).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind.value).encode(), "text/plain")))

        if not isinstance(self.label, Unset):
            files.append(("label", (None, str(self.label).encode(), "text/plain")))

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

        sport_object = d.pop("sport_object", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)

        def _parse_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: KindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = KindEnum(_kind)

        label = d.pop("label", UNSET)

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

        patched_sport_object_special_day = cls(
            id=id,
            sport_object=sport_object,
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            kind=kind,
            label=label,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_sport_object_special_day.additional_properties = d
        return patched_sport_object_special_day

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
