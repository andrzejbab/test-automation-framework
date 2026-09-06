from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserProfileUpdate")


@_attrs_define
class PatchedUserProfileUpdate:
    """
    Attributes:
        email (str | Unset):
        abonament (str | Unset):
        user_type (str | Unset):
    """

    email: str | Unset = UNSET
    abonament: str | Unset = UNSET
    user_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        abonament = self.abonament

        user_type = self.user_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if abonament is not UNSET:
            field_dict["abonament"] = abonament
        if user_type is not UNSET:
            field_dict["user_type"] = user_type

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.email, Unset):
            files.append(("email", (None, str(self.email).encode(), "text/plain")))

        if not isinstance(self.abonament, Unset):
            files.append(("abonament", (None, str(self.abonament).encode(), "text/plain")))

        if not isinstance(self.user_type, Unset):
            files.append(("user_type", (None, str(self.user_type).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        abonament = d.pop("abonament", UNSET)

        user_type = d.pop("user_type", UNSET)

        patched_user_profile_update = cls(
            email=email,
            abonament=abonament,
            user_type=user_type,
        )

        patched_user_profile_update.additional_properties = d
        return patched_user_profile_update

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
