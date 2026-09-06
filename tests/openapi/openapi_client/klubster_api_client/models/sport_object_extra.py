from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="SportObjectExtra")


@_attrs_define
class SportObjectExtra:
    """
    Attributes:
        id (int):
        sport_object (int):
        name (str):
        amount (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    sport_object: int
    name: str
    amount: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sport_object = self.sport_object

        name = self.name

        amount = self.amount

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sport_object": sport_object,
                "name": name,
                "amount": amount,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("sport_object", (None, str(self.sport_object).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("amount", (None, str(self.amount).encode(), "text/plain")))

        files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sport_object = d.pop("sport_object")

        name = d.pop("name")

        amount = d.pop("amount")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        sport_object_extra = cls(
            id=id,
            sport_object=sport_object,
            name=name,
            amount=amount,
            created_at=created_at,
            updated_at=updated_at,
        )

        sport_object_extra.additional_properties = d
        return sport_object_extra

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
