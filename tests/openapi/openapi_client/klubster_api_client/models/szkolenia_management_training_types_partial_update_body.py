from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SzkoleniaManagementTrainingTypesPartialUpdateBody")


@_attrs_define
class SzkoleniaManagementTrainingTypesPartialUpdateBody:
    """
    Attributes:
        name (str | Unset):  Example: Technical training.
        price_per_hour (str | Unset):  Example: 90.00.
        training_hour_price (str | Unset):  Example: 120.00.
    """

    name: str | Unset = UNSET
    price_per_hour: str | Unset = UNSET
    training_hour_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        price_per_hour = self.price_per_hour

        training_hour_price = self.training_hour_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if price_per_hour is not UNSET:
            field_dict["price_per_hour"] = price_per_hour
        if training_hour_price is not UNSET:
            field_dict["training_hour_price"] = training_hour_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        price_per_hour = d.pop("price_per_hour", UNSET)

        training_hour_price = d.pop("training_hour_price", UNSET)

        szkolenia_management_training_types_partial_update_body = cls(
            name=name,
            price_per_hour=price_per_hour,
            training_hour_price=training_hour_price,
        )

        szkolenia_management_training_types_partial_update_body.additional_properties = d
        return szkolenia_management_training_types_partial_update_body

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
