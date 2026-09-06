from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSportObjectPhoto")


@_attrs_define
class PatchedSportObjectPhoto:
    """
    Attributes:
        id (int | Unset):
        image (str | Unset):
        image_url (str | Unset):
        position (int | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    image: str | Unset = UNSET
    image_url: str | Unset = UNSET
    position: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image = self.image

        image_url = self.image_url

        position = self.position

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if position is not UNSET:
            field_dict["position"] = position
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.image, Unset):
            files.append(("image", (None, str(self.image).encode(), "text/plain")))

        if not isinstance(self.image_url, Unset):
            files.append(("image_url", (None, str(self.image_url).encode(), "text/plain")))

        if not isinstance(self.position, Unset):
            files.append(("position", (None, str(self.position).encode(), "text/plain")))

        if not isinstance(self.created_at, Unset):
            files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        image_url = d.pop("image_url", UNSET)

        position = d.pop("position", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        patched_sport_object_photo = cls(
            id=id,
            image=image,
            image_url=image_url,
            position=position,
            created_at=created_at,
        )

        patched_sport_object_photo.additional_properties = d
        return patched_sport_object_photo

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
