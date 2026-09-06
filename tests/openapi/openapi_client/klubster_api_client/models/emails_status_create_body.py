from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.emails_status_create_body_action import EmailsStatusCreateBodyAction

T = TypeVar("T", bound="EmailsStatusCreateBody")


@_attrs_define
class EmailsStatusCreateBody:
    """
    Attributes:
        action (EmailsStatusCreateBodyAction):  Example: mark_as_read.
    """

    action: EmailsStatusCreateBodyAction

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = EmailsStatusCreateBodyAction(d.pop("action"))

        emails_status_create_body = cls(
            action=action,
        )

        return emails_status_create_body
