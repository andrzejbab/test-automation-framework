from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.day_type_enum import DayTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SportObjectPrice")


@_attrs_define
class SportObjectPrice:
    """
    Attributes:
        id (int):
        sport_object (int):
        start_time (str):
        end_time (str):
        price (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        day_type (DayTypeEnum | Unset): * `weekday` - Dni zwykłe
            * `weekend` - Weekend
    """

    id: int
    sport_object: int
    start_time: str
    end_time: str
    price: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    day_type: DayTypeEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sport_object = self.sport_object

        start_time = self.start_time

        end_time = self.end_time

        price = self.price

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        day_type: str | Unset = UNSET
        if not isinstance(self.day_type, Unset):
            day_type = self.day_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sport_object": sport_object,
                "start_time": start_time,
                "end_time": end_time,
                "price": price,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if day_type is not UNSET:
            field_dict["day_type"] = day_type

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("sport_object", (None, str(self.sport_object).encode(), "text/plain")))

        files.append(("start_time", (None, str(self.start_time).encode(), "text/plain")))

        files.append(("end_time", (None, str(self.end_time).encode(), "text/plain")))

        files.append(("price", (None, str(self.price).encode(), "text/plain")))

        files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.day_type, Unset):
            files.append(("day_type", (None, str(self.day_type.value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sport_object = d.pop("sport_object")

        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        price = d.pop("price")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _day_type = d.pop("day_type", UNSET)
        day_type: DayTypeEnum | Unset
        if isinstance(_day_type, Unset):
            day_type = UNSET
        else:
            day_type = DayTypeEnum(_day_type)

        sport_object_price = cls(
            id=id,
            sport_object=sport_object,
            start_time=start_time,
            end_time=end_time,
            price=price,
            created_at=created_at,
            updated_at=updated_at,
            day_type=day_type,
        )

        sport_object_price.additional_properties = d
        return sport_object_price

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
