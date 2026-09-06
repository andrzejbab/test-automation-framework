from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserManagementRegisterCreateBody")


@_attrs_define
class UserManagementRegisterCreateBody:
    """
    Attributes:
        email (str):  Example: admin.club@test.local.
        password (str):  Example: test_password.
        accept_terms (bool):  Example: True.
        accept_privacy_policy (bool):  Example: True.
        abonament (str | Unset):  Example: basic.
    """

    email: str
    password: str
    accept_terms: bool
    accept_privacy_policy: bool
    abonament: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        accept_terms = self.accept_terms

        accept_privacy_policy = self.accept_privacy_policy

        abonament = self.abonament

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
                "accept_terms": accept_terms,
                "accept_privacy_policy": accept_privacy_policy,
            }
        )
        if abonament is not UNSET:
            field_dict["abonament"] = abonament

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        accept_terms = d.pop("accept_terms")

        accept_privacy_policy = d.pop("accept_privacy_policy")

        abonament = d.pop("abonament", UNSET)

        user_management_register_create_body = cls(
            email=email,
            password=password,
            accept_terms=accept_terms,
            accept_privacy_policy=accept_privacy_policy,
            abonament=abonament,
        )

        user_management_register_create_body.additional_properties = d
        return user_management_register_create_body

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
