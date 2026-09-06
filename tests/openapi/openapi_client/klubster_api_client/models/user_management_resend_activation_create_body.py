from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UserManagementResendActivationCreateBody")


@_attrs_define
class UserManagementResendActivationCreateBody:
    """
    Attributes:
        email (str):  Example: admin.club@test.local.
    """

    email: str

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        user_management_resend_activation_create_body = cls(
            email=email,
        )

        return user_management_resend_activation_create_body
