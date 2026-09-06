from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UserManagementTokenCreateBody")


@_attrs_define
class UserManagementTokenCreateBody:
    """
    Attributes:
        username (str):  Example: admin.club@test.local.
        password (str):  Example: test_password.
    """

    username: str
    password: str

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        user_management_token_create_body = cls(
            username=username,
            password=password,
        )

        return user_management_token_create_body
