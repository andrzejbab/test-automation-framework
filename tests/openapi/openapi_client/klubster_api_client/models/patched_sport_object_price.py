from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.day_type_enum import DayTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSportObjectPrice")


@_attrs_define
class PatchedSportObjectPrice:
    """
    Attributes:
        id (int | Unset):
        sport_object (int | Unset):
        day_type (DayTypeEnum | Unset): * `weekday` - Dni zwykłe
            * `weekend` - Weekend
        start_time (str | Unset):
        end_time (str | Unset):
        price (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    sport_object: int | Unset = UNSET
    day_type: DayTypeEnum | Unset = UNSET
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    price: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sport_object = self.sport_object

        day_type: str | Unset = UNSET
        if not isinstance(self.day_type, Unset):
            day_type = self.day_type.value

        start_time = self.start_time

        end_time = self.end_time

        price = self.price

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
        if day_type is not UNSET:
            field_dict["day_type"] = day_type
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if price is not UNSET:
            field_dict["price"] = price
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

        if not isinstance(self.day_type, Unset):
            files.append(("day_type", (None, str(self.day_type.value).encode(), "text/plain")))

        if not isinstance(self.start_time, Unset):
            files.append(("start_time", (None, str(self.start_time).encode(), "text/plain")))

        if not isinstance(self.end_time, Unset):
            files.append(("end_time", (None, str(self.end_time).encode(), "text/plain")))

        if not isinstance(self.price, Unset):
            files.append(("price", (None, str(self.price).encode(), "text/plain")))

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

        _day_type = d.pop("day_type", UNSET)
        day_type: DayTypeEnum | Unset
        if isinstance(_day_type, Unset):
            day_type = UNSET
        else:
            day_type = DayTypeEnum(_day_type)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        price = d.pop("price", UNSET)

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

        patched_sport_object_price = cls(
            id=id,
            sport_object=sport_object,
            day_type=day_type,
            start_time=start_time,
            end_time=end_time,
            price=price,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_sport_object_price.additional_properties = d
        return patched_sport_object_price

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
