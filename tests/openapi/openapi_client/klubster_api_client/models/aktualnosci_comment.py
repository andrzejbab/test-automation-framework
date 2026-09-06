from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AktualnosciComment")


@_attrs_define
class AktualnosciComment:
    """
    Attributes:
        id (int):
        content (str):
        author (int | None):
        author_name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    content: str
    author: int | None
    author_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content = self.content

        author: int | None
        author = self.author

        author_name = self.author_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "content": content,
                "author": author,
                "author_name": author_name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        content = d.pop("content")

        def _parse_author(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        author = _parse_author(d.pop("author"))

        author_name = d.pop("author_name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        aktualnosci_comment = cls(
            id=id,
            content=content,
            author=author,
            author_name=author_name,
            created_at=created_at,
            updated_at=updated_at,
        )

        aktualnosci_comment.additional_properties = d
        return aktualnosci_comment

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
