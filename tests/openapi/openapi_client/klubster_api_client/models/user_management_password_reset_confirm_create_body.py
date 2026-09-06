from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UserManagementPasswordResetConfirmCreateBody")


@_attrs_define
class UserManagementPasswordResetConfirmCreateBody:
    """
    Attributes:
        password (str): New password for the user. Example: test_password.
    """

    password: str

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password")

        user_management_password_reset_confirm_create_body = cls(
            password=password,
        )

        return user_management_password_reset_confirm_create_body
