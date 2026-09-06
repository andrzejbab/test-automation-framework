from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.permissions_enum import PermissionsEnum
from ..models.roles_enum import RolesEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """
    Attributes:
        id (int):
        email (str):
        username (str):
        has_login_account (str):
        uses_placeholder_email (str):
        parents (str):
        parents_details (str):
        profile_photo_url (str):
        roles (list[RolesEnum] | Unset):
        permissions (list[PermissionsEnum] | Unset):
        children (list[int] | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        phone (None | str | Unset):
        profile_photo (None | str | Unset):
        profile (int | None | Unset):
    """

    id: int
    email: str
    username: str
    has_login_account: str
    uses_placeholder_email: str
    parents: str
    parents_details: str
    profile_photo_url: str
    roles: list[RolesEnum] | Unset = UNSET
    permissions: list[PermissionsEnum] | Unset = UNSET
    children: list[int] | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    phone: None | str | Unset = UNSET
    profile_photo: None | str | Unset = UNSET
    profile: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        username = self.username

        has_login_account = self.has_login_account

        uses_placeholder_email = self.uses_placeholder_email

        parents = self.parents

        parents_details = self.parents_details

        profile_photo_url = self.profile_photo_url

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value
                roles.append(roles_item)

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        children: list[int] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children

        first_name = self.first_name

        last_name = self.last_name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        profile_photo: None | str | Unset
        if isinstance(self.profile_photo, Unset):
            profile_photo = UNSET
        else:
            profile_photo = self.profile_photo

        profile: int | None | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "username": username,
                "has_login_account": has_login_account,
                "uses_placeholder_email": uses_placeholder_email,
                "parents": parents,
                "parents_details": parents_details,
                "profile_photo_url": profile_photo_url,
            }
        )
        if roles is not UNSET:
            field_dict["roles"] = roles
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if children is not UNSET:
            field_dict["children"] = children
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if profile_photo is not UNSET:
            field_dict["profile_photo"] = profile_photo
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("email", (None, str(self.email).encode(), "text/plain")))

        files.append(("username", (None, str(self.username).encode(), "text/plain")))

        files.append(("has_login_account", (None, str(self.has_login_account).encode(), "text/plain")))

        files.append(("uses_placeholder_email", (None, str(self.uses_placeholder_email).encode(), "text/plain")))

        files.append(("parents", (None, str(self.parents).encode(), "text/plain")))

        files.append(("parents_details", (None, str(self.parents_details).encode(), "text/plain")))

        files.append(("profile_photo_url", (None, str(self.profile_photo_url).encode(), "text/plain")))

        if not isinstance(self.roles, Unset):
            for roles_item_element in self.roles:
                files.append(("roles", (None, str(roles_item_element.value).encode(), "text/plain")))

        if not isinstance(self.permissions, Unset):
            for permissions_item_element in self.permissions:
                files.append(("permissions", (None, str(permissions_item_element.value).encode(), "text/plain")))

        if not isinstance(self.children, Unset):
            for children_item_element in self.children:
                files.append(("children", (None, str(children_item_element).encode(), "text/plain")))

        if not isinstance(self.first_name, Unset):
            files.append(("first_name", (None, str(self.first_name).encode(), "text/plain")))

        if not isinstance(self.last_name, Unset):
            files.append(("last_name", (None, str(self.last_name).encode(), "text/plain")))

        if not isinstance(self.phone, Unset):
            if isinstance(self.phone, str):
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))
            else:
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))

        if not isinstance(self.profile_photo, Unset):
            if isinstance(self.profile_photo, str):
                files.append(("profile_photo", (None, str(self.profile_photo).encode(), "text/plain")))
            else:
                files.append(("profile_photo", (None, str(self.profile_photo).encode(), "text/plain")))

        if not isinstance(self.profile, Unset):
            if isinstance(self.profile, int):
                files.append(("profile", (None, str(self.profile).encode(), "text/plain")))
            else:
                files.append(("profile", (None, str(self.profile).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        username = d.pop("username")

        has_login_account = d.pop("has_login_account")

        uses_placeholder_email = d.pop("uses_placeholder_email")

        parents = d.pop("parents")

        parents_details = d.pop("parents_details")

        profile_photo_url = d.pop("profile_photo_url")

        _roles = d.pop("roles", UNSET)
        roles: list[RolesEnum] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = RolesEnum(roles_item_data)

                roles.append(roles_item)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[PermissionsEnum] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = PermissionsEnum(permissions_item_data)

                permissions.append(permissions_item)

        children = cast(list[int], d.pop("children", UNSET))

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_profile_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_photo = _parse_profile_photo(d.pop("profile_photo", UNSET))

        def _parse_profile(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        member = cls(
            id=id,
            email=email,
            username=username,
            has_login_account=has_login_account,
            uses_placeholder_email=uses_placeholder_email,
            parents=parents,
            parents_details=parents_details,
            profile_photo_url=profile_photo_url,
            roles=roles,
            permissions=permissions,
            children=children,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            profile_photo=profile_photo,
            profile=profile,
        )

        member.additional_properties = d
        return member

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
