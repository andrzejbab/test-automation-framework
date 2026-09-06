from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment


T = TypeVar("T", bound="DraftEmail")


@_attrs_define
class DraftEmail:
    """
    Attributes:
        id (int):
        sender (int):
        sender_name (str):
        recipients (list[int]):
        attachments (list[Attachment]):
        replies (str):
        sent_at (datetime.datetime):
        attachments_upload (list[str] | Unset):
        reply_to (int | None | Unset):
        is_starred_by (list[int] | Unset):
        is_read_by (list[int] | Unset):
        is_deleted_by (list[int] | Unset):
        is_draft_by (list[int] | Unset):
        is_archived_by (list[int] | Unset):
        subject (str | Unset):
        body (str | Unset):
        is_sent (bool | Unset):
    """

    id: int
    sender: int
    sender_name: str
    recipients: list[int]
    attachments: list[Attachment]
    replies: str
    sent_at: datetime.datetime
    attachments_upload: list[str] | Unset = UNSET
    reply_to: int | None | Unset = UNSET
    is_starred_by: list[int] | Unset = UNSET
    is_read_by: list[int] | Unset = UNSET
    is_deleted_by: list[int] | Unset = UNSET
    is_draft_by: list[int] | Unset = UNSET
    is_archived_by: list[int] | Unset = UNSET
    subject: str | Unset = UNSET
    body: str | Unset = UNSET
    is_sent: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sender = self.sender

        sender_name = self.sender_name

        recipients = self.recipients

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        replies = self.replies

        sent_at = self.sent_at.isoformat()

        attachments_upload: list[str] | Unset = UNSET
        if not isinstance(self.attachments_upload, Unset):
            attachments_upload = self.attachments_upload

        reply_to: int | None | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

        is_starred_by: list[int] | Unset = UNSET
        if not isinstance(self.is_starred_by, Unset):
            is_starred_by = self.is_starred_by

        is_read_by: list[int] | Unset = UNSET
        if not isinstance(self.is_read_by, Unset):
            is_read_by = self.is_read_by

        is_deleted_by: list[int] | Unset = UNSET
        if not isinstance(self.is_deleted_by, Unset):
            is_deleted_by = self.is_deleted_by

        is_draft_by: list[int] | Unset = UNSET
        if not isinstance(self.is_draft_by, Unset):
            is_draft_by = self.is_draft_by

        is_archived_by: list[int] | Unset = UNSET
        if not isinstance(self.is_archived_by, Unset):
            is_archived_by = self.is_archived_by

        subject = self.subject

        body = self.body

        is_sent = self.is_sent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sender": sender,
                "sender_name": sender_name,
                "recipients": recipients,
                "attachments": attachments,
                "replies": replies,
                "sent_at": sent_at,
            }
        )
        if attachments_upload is not UNSET:
            field_dict["attachments_upload"] = attachments_upload
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if is_starred_by is not UNSET:
            field_dict["is_starred_by"] = is_starred_by
        if is_read_by is not UNSET:
            field_dict["is_read_by"] = is_read_by
        if is_deleted_by is not UNSET:
            field_dict["is_deleted_by"] = is_deleted_by
        if is_draft_by is not UNSET:
            field_dict["is_draft_by"] = is_draft_by
        if is_archived_by is not UNSET:
            field_dict["is_archived_by"] = is_archived_by
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if is_sent is not UNSET:
            field_dict["is_sent"] = is_sent

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("sender", (None, str(self.sender).encode(), "text/plain")))

        files.append(("sender_name", (None, str(self.sender_name).encode(), "text/plain")))

        for recipients_item_element in self.recipients:
            files.append(("recipients", (None, str(recipients_item_element).encode(), "text/plain")))

        for attachments_item_element in self.attachments:
            files.append(
                ("attachments", (None, json.dumps(attachments_item_element.to_dict()).encode(), "application/json"))
            )

        files.append(("replies", (None, str(self.replies).encode(), "text/plain")))

        files.append(("sent_at", (None, self.sent_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.attachments_upload, Unset):
            for attachments_upload_item_element in self.attachments_upload:
                files.append(
                    ("attachments_upload", (None, str(attachments_upload_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.reply_to, Unset):
            if isinstance(self.reply_to, int):
                files.append(("reply_to", (None, str(self.reply_to).encode(), "text/plain")))
            else:
                files.append(("reply_to", (None, str(self.reply_to).encode(), "text/plain")))

        if not isinstance(self.is_starred_by, Unset):
            for is_starred_by_item_element in self.is_starred_by:
                files.append(("is_starred_by", (None, str(is_starred_by_item_element).encode(), "text/plain")))

        if not isinstance(self.is_read_by, Unset):
            for is_read_by_item_element in self.is_read_by:
                files.append(("is_read_by", (None, str(is_read_by_item_element).encode(), "text/plain")))

        if not isinstance(self.is_deleted_by, Unset):
            for is_deleted_by_item_element in self.is_deleted_by:
                files.append(("is_deleted_by", (None, str(is_deleted_by_item_element).encode(), "text/plain")))

        if not isinstance(self.is_draft_by, Unset):
            for is_draft_by_item_element in self.is_draft_by:
                files.append(("is_draft_by", (None, str(is_draft_by_item_element).encode(), "text/plain")))

        if not isinstance(self.is_archived_by, Unset):
            for is_archived_by_item_element in self.is_archived_by:
                files.append(("is_archived_by", (None, str(is_archived_by_item_element).encode(), "text/plain")))

        if not isinstance(self.subject, Unset):
            files.append(("subject", (None, str(self.subject).encode(), "text/plain")))

        if not isinstance(self.body, Unset):
            files.append(("body", (None, str(self.body).encode(), "text/plain")))

        if not isinstance(self.is_sent, Unset):
            files.append(("is_sent", (None, str(self.is_sent).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment import Attachment

        d = dict(src_dict)
        id = d.pop("id")

        sender = d.pop("sender")

        sender_name = d.pop("sender_name")

        recipients = cast(list[int], d.pop("recipients"))

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        replies = d.pop("replies")

        sent_at = datetime.datetime.fromisoformat(d.pop("sent_at"))

        attachments_upload = cast(list[str], d.pop("attachments_upload", UNSET))

        def _parse_reply_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        is_starred_by = cast(list[int], d.pop("is_starred_by", UNSET))

        is_read_by = cast(list[int], d.pop("is_read_by", UNSET))

        is_deleted_by = cast(list[int], d.pop("is_deleted_by", UNSET))

        is_draft_by = cast(list[int], d.pop("is_draft_by", UNSET))

        is_archived_by = cast(list[int], d.pop("is_archived_by", UNSET))

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        is_sent = d.pop("is_sent", UNSET)

        draft_email = cls(
            id=id,
            sender=sender,
            sender_name=sender_name,
            recipients=recipients,
            attachments=attachments,
            replies=replies,
            sent_at=sent_at,
            attachments_upload=attachments_upload,
            reply_to=reply_to,
            is_starred_by=is_starred_by,
            is_read_by=is_read_by,
            is_deleted_by=is_deleted_by,
            is_draft_by=is_draft_by,
            is_archived_by=is_archived_by,
            subject=subject,
            body=body,
            is_sent=is_sent,
        )

        draft_email.additional_properties = d
        return draft_email

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
