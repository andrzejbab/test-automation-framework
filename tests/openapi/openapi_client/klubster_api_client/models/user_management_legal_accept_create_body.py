from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UserManagementLegalAcceptCreateBody")


@_attrs_define
class UserManagementLegalAcceptCreateBody:
    """
    Attributes:
        accept_terms (bool):  Example: True.
        accept_privacy_policy (bool):  Example: True.
    """

    accept_terms: bool
    accept_privacy_policy: bool

    def to_dict(self) -> dict[str, Any]:
        accept_terms = self.accept_terms

        accept_privacy_policy = self.accept_privacy_policy

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accept_terms": accept_terms,
                "accept_privacy_policy": accept_privacy_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accept_terms = d.pop("accept_terms")

        accept_privacy_policy = d.pop("accept_privacy_policy")

        user_management_legal_accept_create_body = cls(
            accept_terms=accept_terms,
            accept_privacy_policy=accept_privacy_policy,
        )

        return user_management_legal_accept_create_body
