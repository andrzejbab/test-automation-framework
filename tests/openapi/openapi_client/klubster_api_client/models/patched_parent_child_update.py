from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedParentChildUpdate")


@_attrs_define
class PatchedParentChildUpdate:
    """
    Attributes:
        phone (None | str | Unset):
        profile_photo (str | Unset):
        email (str | Unset):
    """

    phone: None | str | Unset = UNSET
    profile_photo: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        profile_photo = self.profile_photo

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone is not UNSET:
            field_dict["phone"] = phone
        if profile_photo is not UNSET:
            field_dict["profile_photo"] = profile_photo
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.phone, Unset):
            if isinstance(self.phone, str):
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))
            else:
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))

        if not isinstance(self.profile_photo, Unset):
            files.append(("profile_photo", (None, str(self.profile_photo).encode(), "text/plain")))

        if not isinstance(self.email, Unset):
            files.append(("email", (None, str(self.email).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        profile_photo = d.pop("profile_photo", UNSET)

        email = d.pop("email", UNSET)

        patched_parent_child_update = cls(
            phone=phone,
            profile_photo=profile_photo,
            email=email,
        )

        patched_parent_child_update.additional_properties = d
        return patched_parent_child_update

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
