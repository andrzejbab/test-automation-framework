from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """
    Attributes:
        id (int):
        code (str):
        label (str):
        description (str):
        default_permissions (str):
        default_permission_labels (str):
    """

    id: int
    code: str
    label: str
    description: str
    default_permissions: str
    default_permission_labels: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        code = self.code

        label = self.label

        description = self.description

        default_permissions = self.default_permissions

        default_permission_labels = self.default_permission_labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "code": code,
                "label": label,
                "description": description,
                "default_permissions": default_permissions,
                "default_permission_labels": default_permission_labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        code = d.pop("code")

        label = d.pop("label")

        description = d.pop("description")

        default_permissions = d.pop("default_permissions")

        default_permission_labels = d.pop("default_permission_labels")

        role = cls(
            id=id,
            code=code,
            label=label,
            description=description,
            default_permissions=default_permissions,
            default_permission_labels=default_permission_labels,
        )

        role.additional_properties = d
        return role

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
