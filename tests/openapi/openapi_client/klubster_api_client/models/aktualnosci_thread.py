from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aktualnosci_comment import AktualnosciComment


T = TypeVar("T", bound="AktualnosciThread")


@_attrs_define
class AktualnosciThread:
    """
    Attributes:
        id (int):
        content (str):
        author (int | None):
        author_name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        comments (list[AktualnosciComment]):
        title (str | Unset):
        external_link (None | str | Unset):
    """

    id: int
    content: str
    author: int | None
    author_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    comments: list[AktualnosciComment]
    title: str | Unset = UNSET
    external_link: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content = self.content

        author: int | None
        author = self.author

        author_name = self.author_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        title = self.title

        external_link: None | str | Unset
        if isinstance(self.external_link, Unset):
            external_link = UNSET
        else:
            external_link = self.external_link

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
                "comments": comments,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if external_link is not UNSET:
            field_dict["external_link"] = external_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aktualnosci_comment import AktualnosciComment

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

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = AktualnosciComment.from_dict(comments_item_data)

            comments.append(comments_item)

        title = d.pop("title", UNSET)

        def _parse_external_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_link = _parse_external_link(d.pop("external_link", UNSET))

        aktualnosci_thread = cls(
            id=id,
            content=content,
            author=author,
            author_name=author_name,
            created_at=created_at,
            updated_at=updated_at,
            comments=comments,
            title=title,
            external_link=external_link,
        )

        aktualnosci_thread.additional_properties = d
        return aktualnosci_thread

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
