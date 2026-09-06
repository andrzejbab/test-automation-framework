from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingType")


@_attrs_define
class TrainingType:
    """
    Attributes:
        id (int):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        price_per_hour (str | Unset):
        is_active (bool | Unset):
    """

    id: int
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    price_per_hour: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        price_per_hour = self.price_per_hour

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if price_per_hour is not UNSET:
            field_dict["price_per_hour"] = price_per_hour
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.price_per_hour, Unset):
            files.append(("price_per_hour", (None, str(self.price_per_hour).encode(), "text/plain")))

        if not isinstance(self.is_active, Unset):
            files.append(("is_active", (None, str(self.is_active).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        price_per_hour = d.pop("price_per_hour", UNSET)

        is_active = d.pop("is_active", UNSET)

        training_type = cls(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            price_per_hour=price_per_hour,
            is_active=is_active,
        )

        training_type.additional_properties = d
        return training_type

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
