from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClubPhoto")


@_attrs_define
class ClubPhoto:
    """
    Attributes:
        id (int):
        image (str):
        image_url (str):
        created_at (datetime.datetime):
        position (int | Unset):
    """

    id: int
    image: str
    image_url: str
    created_at: datetime.datetime
    position: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image = self.image

        image_url = self.image_url

        created_at = self.created_at.isoformat()

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "image": image,
                "image_url": image_url,
                "created_at": created_at,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        image = d.pop("image")

        image_url = d.pop("image_url")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        position = d.pop("position", UNSET)

        club_photo = cls(
            id=id,
            image=image,
            image_url=image_url,
            created_at=created_at,
            position=position,
        )

        club_photo.additional_properties = d
        return club_photo

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
