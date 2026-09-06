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


T = TypeVar("T", bound="PatchedDraftEmail")


@_attrs_define
class PatchedDraftEmail:
    """
    Attributes:
        id (int | Unset):
        sender (int | Unset):
        sender_name (str | Unset):
        recipients (list[int] | Unset):
        attachments (list[Attachment] | Unset):
        attachments_upload (list[str] | Unset):
        reply_to (int | None | Unset):
        replies (str | Unset):
        is_starred_by (list[int] | Unset):
        is_read_by (list[int] | Unset):
        is_deleted_by (list[int] | Unset):
        is_draft_by (list[int] | Unset):
        is_archived_by (list[int] | Unset):
        subject (str | Unset):
        body (str | Unset):
        sent_at (datetime.datetime | Unset):
        is_sent (bool | Unset):
    """

    id: int | Unset = UNSET
    sender: int | Unset = UNSET
    sender_name: str | Unset = UNSET
    recipients: list[int] | Unset = UNSET
    attachments: list[Attachment] | Unset = UNSET
    attachments_upload: list[str] | Unset = UNSET
    reply_to: int | None | Unset = UNSET
    replies: str | Unset = UNSET
    is_starred_by: list[int] | Unset = UNSET
    is_read_by: list[int] | Unset = UNSET
    is_deleted_by: list[int] | Unset = UNSET
    is_draft_by: list[int] | Unset = UNSET
    is_archived_by: list[int] | Unset = UNSET
    subject: str | Unset = UNSET
    body: str | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    is_sent: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sender = self.sender

        sender_name = self.sender_name

        recipients: list[int] | Unset = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        attachments_upload: list[str] | Unset = UNSET
        if not isinstance(self.attachments_upload, Unset):
            attachments_upload = self.attachments_upload

        reply_to: int | None | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

        replies = self.replies

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

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        is_sent = self.is_sent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if attachments_upload is not UNSET:
            field_dict["attachments_upload"] = attachments_upload
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if replies is not UNSET:
            field_dict["replies"] = replies
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
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if is_sent is not UNSET:
            field_dict["is_sent"] = is_sent

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.sender, Unset):
            files.append(("sender", (None, str(self.sender).encode(), "text/plain")))

        if not isinstance(self.sender_name, Unset):
            files.append(("sender_name", (None, str(self.sender_name).encode(), "text/plain")))

        if not isinstance(self.recipients, Unset):
            for recipients_item_element in self.recipients:
                files.append(("recipients", (None, str(recipients_item_element).encode(), "text/plain")))

        if not isinstance(self.attachments, Unset):
            for attachments_item_element in self.attachments:
                files.append(
                    ("attachments", (None, json.dumps(attachments_item_element.to_dict()).encode(), "application/json"))
                )

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

        if not isinstance(self.replies, Unset):
            files.append(("replies", (None, str(self.replies).encode(), "text/plain")))

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

        if not isinstance(self.sent_at, Unset):
            files.append(("sent_at", (None, self.sent_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.is_sent, Unset):
            files.append(("is_sent", (None, str(self.is_sent).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment import Attachment

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sender = d.pop("sender", UNSET)

        sender_name = d.pop("sender_name", UNSET)

        recipients = cast(list[int], d.pop("recipients", UNSET))

        _attachments = d.pop("attachments", UNSET)
        attachments: list[Attachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = Attachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        attachments_upload = cast(list[str], d.pop("attachments_upload", UNSET))

        def _parse_reply_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        replies = d.pop("replies", UNSET)

        is_starred_by = cast(list[int], d.pop("is_starred_by", UNSET))

        is_read_by = cast(list[int], d.pop("is_read_by", UNSET))

        is_deleted_by = cast(list[int], d.pop("is_deleted_by", UNSET))

        is_draft_by = cast(list[int], d.pop("is_draft_by", UNSET))

        is_archived_by = cast(list[int], d.pop("is_archived_by", UNSET))

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        _sent_at = d.pop("sent_at", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at, Unset):
            sent_at = UNSET
        else:
            sent_at = datetime.datetime.fromisoformat(_sent_at)

        is_sent = d.pop("is_sent", UNSET)

        patched_draft_email = cls(
            id=id,
            sender=sender,
            sender_name=sender_name,
            recipients=recipients,
            attachments=attachments,
            attachments_upload=attachments_upload,
            reply_to=reply_to,
            replies=replies,
            is_starred_by=is_starred_by,
            is_read_by=is_read_by,
            is_deleted_by=is_deleted_by,
            is_draft_by=is_draft_by,
            is_archived_by=is_archived_by,
            subject=subject,
            body=body,
            sent_at=sent_at,
            is_sent=is_sent,
        )

        patched_draft_email.additional_properties = d
        return patched_draft_email

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
