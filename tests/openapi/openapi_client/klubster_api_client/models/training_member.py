from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingMember")


@_attrs_define
class TrainingMember:
    """
    Attributes:
        id (int):
        full_name (str):
        email (str):
        roles (str):
        first_name (str | Unset):
        last_name (str | Unset):
        phone (None | str | Unset):
    """

    id: int
    full_name: str
    email: str
    roles: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    phone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        full_name = self.full_name

        email = self.email

        roles = self.roles

        first_name = self.first_name

        last_name = self.last_name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "full_name": full_name,
                "email": email,
                "roles": roles,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("full_name", (None, str(self.full_name).encode(), "text/plain")))

        files.append(("email", (None, str(self.email).encode(), "text/plain")))

        files.append(("roles", (None, str(self.roles).encode(), "text/plain")))

        if not isinstance(self.first_name, Unset):
            files.append(("first_name", (None, str(self.first_name).encode(), "text/plain")))

        if not isinstance(self.last_name, Unset):
            files.append(("last_name", (None, str(self.last_name).encode(), "text/plain")))

        if not isinstance(self.phone, Unset):
            if isinstance(self.phone, str):
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))
            else:
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        full_name = d.pop("full_name")

        email = d.pop("email")

        roles = d.pop("roles")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        training_member = cls(
            id=id,
            full_name=full_name,
            email=email,
            roles=roles,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )

        training_member.additional_properties = d
        return training_member

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
