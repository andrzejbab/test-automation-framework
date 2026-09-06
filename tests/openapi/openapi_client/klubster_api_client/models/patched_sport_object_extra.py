from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSportObjectExtra")


@_attrs_define
class PatchedSportObjectExtra:
    """
    Attributes:
        id (int | Unset):
        sport_object (int | Unset):
        name (str | Unset):
        amount (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    sport_object: int | Unset = UNSET
    name: str | Unset = UNSET
    amount: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sport_object = self.sport_object

        name = self.name

        amount = self.amount

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
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
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

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.amount, Unset):
            files.append(("amount", (None, str(self.amount).encode(), "text/plain")))

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

        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

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

        patched_sport_object_extra = cls(
            id=id,
            sport_object=sport_object,
            name=name,
            amount=amount,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_sport_object_extra.additional_properties = d
        return patched_sport_object_extra

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
