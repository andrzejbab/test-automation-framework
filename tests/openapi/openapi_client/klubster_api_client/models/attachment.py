from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """
    Attributes:
        id (int):
        file (str):
        uploaded_at (datetime.datetime):
        club_id (int | None | Unset):
    """

    id: int
    file: str
    uploaded_at: datetime.datetime
    club_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file = self.file

        uploaded_at = self.uploaded_at.isoformat()

        club_id: int | None | Unset
        if isinstance(self.club_id, Unset):
            club_id = UNSET
        else:
            club_id = self.club_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "file": file,
                "uploaded_at": uploaded_at,
            }
        )
        if club_id is not UNSET:
            field_dict["club_id"] = club_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        file = d.pop("file")

        uploaded_at = datetime.datetime.fromisoformat(d.pop("uploaded_at"))

        def _parse_club_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        club_id = _parse_club_id(d.pop("club_id", UNSET))

        attachment = cls(
            id=id,
            file=file,
            uploaded_at=uploaded_at,
            club_id=club_id,
        )

        attachment.additional_properties = d
        return attachment

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
