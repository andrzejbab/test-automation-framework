from enum import Enum


class EmailsStatusCreateBodyAction(str, Enum):
    ARCHIVE = "archive"
    DELETE = "delete"
    MARK_AS_DRAFT = "mark_as_draft"
    MARK_AS_READ = "mark_as_read"
    MARK_AS_SENT = "mark_as_sent"
    MARK_AS_UNREAD = "mark_as_unread"
    RESTORE = "restore"
    STAR = "star"
    UNARCHIVE = "unarchive"
    UNSTAR = "unstar"

    def __str__(self) -> str:
        return str(self.value)
