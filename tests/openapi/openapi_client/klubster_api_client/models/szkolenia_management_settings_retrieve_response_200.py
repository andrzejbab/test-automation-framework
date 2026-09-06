from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SzkoleniaManagementSettingsRetrieveResponse200")


@_attrs_define
class SzkoleniaManagementSettingsRetrieveResponse200:
    """
    Attributes:
        training_hour_price (str | Unset):  Example: 120.00.
    """

    training_hour_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        training_hour_price = self.training_hour_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if training_hour_price is not UNSET:
            field_dict["training_hour_price"] = training_hour_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        training_hour_price = d.pop("training_hour_price", UNSET)

        szkolenia_management_settings_retrieve_response_200 = cls(
            training_hour_price=training_hour_price,
        )

        szkolenia_management_settings_retrieve_response_200.additional_properties = d
        return szkolenia_management_settings_retrieve_response_200

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
