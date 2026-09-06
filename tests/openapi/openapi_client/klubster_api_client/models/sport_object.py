from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sport_object_extra import SportObjectExtra
    from ..models.sport_object_photo import SportObjectPhoto
    from ..models.sport_object_price import SportObjectPrice
    from ..models.sport_object_special_day import SportObjectSpecialDay


T = TypeVar("T", bound="SportObject")


@_attrs_define
class SportObject:
    """
    Attributes:
        id (int):
        club (int):
        name (str):
        special_days (list[SportObjectSpecialDay]):
        prices (list[SportObjectPrice]):
        extras (list[SportObjectExtra]):
        photos (list[SportObjectPhoto]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        type_ (TypeEnum | Unset): * `tennis_court` - Kort tenisowy
            * `fitness_studio` - Studio fitness
            * `gym` - Siłownia
            * `sports_hall` - Hala sportowa
            * `football_pitch` - Boisko piłkarskie
            * `swimming_pool` - Basen
            * `other` - Inne
        description (str | Unset):
        location (str | Unset):
        opening_time (str | Unset):
        closing_time (str | Unset):
        min_reservation_minutes (int | Unset):
        max_recurring_days (int | Unset):
        cancellation_window_minutes (int | Unset):
        belongs_to_club (bool | Unset):
        pay_in_club_only (bool | Unset):
        is_active (bool | Unset):
        upload_photos (list[str] | Unset):
    """

    id: int
    club: int
    name: str
    special_days: list[SportObjectSpecialDay]
    prices: list[SportObjectPrice]
    extras: list[SportObjectExtra]
    photos: list[SportObjectPhoto]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    type_: TypeEnum | Unset = UNSET
    description: str | Unset = UNSET
    location: str | Unset = UNSET
    opening_time: str | Unset = UNSET
    closing_time: str | Unset = UNSET
    min_reservation_minutes: int | Unset = UNSET
    max_recurring_days: int | Unset = UNSET
    cancellation_window_minutes: int | Unset = UNSET
    belongs_to_club: bool | Unset = UNSET
    pay_in_club_only: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    upload_photos: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        club = self.club

        name = self.name

        special_days = []
        for special_days_item_data in self.special_days:
            special_days_item = special_days_item_data.to_dict()
            special_days.append(special_days_item)

        prices = []
        for prices_item_data in self.prices:
            prices_item = prices_item_data.to_dict()
            prices.append(prices_item)

        extras = []
        for extras_item_data in self.extras:
            extras_item = extras_item_data.to_dict()
            extras.append(extras_item)

        photos = []
        for photos_item_data in self.photos:
            photos_item = photos_item_data.to_dict()
            photos.append(photos_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description = self.description

        location = self.location

        opening_time = self.opening_time

        closing_time = self.closing_time

        min_reservation_minutes = self.min_reservation_minutes

        max_recurring_days = self.max_recurring_days

        cancellation_window_minutes = self.cancellation_window_minutes

        belongs_to_club = self.belongs_to_club

        pay_in_club_only = self.pay_in_club_only

        is_active = self.is_active

        upload_photos: list[str] | Unset = UNSET
        if not isinstance(self.upload_photos, Unset):
            upload_photos = self.upload_photos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "club": club,
                "name": name,
                "special_days": special_days,
                "prices": prices,
                "extras": extras,
                "photos": photos,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if opening_time is not UNSET:
            field_dict["opening_time"] = opening_time
        if closing_time is not UNSET:
            field_dict["closing_time"] = closing_time
        if min_reservation_minutes is not UNSET:
            field_dict["min_reservation_minutes"] = min_reservation_minutes
        if max_recurring_days is not UNSET:
            field_dict["max_recurring_days"] = max_recurring_days
        if cancellation_window_minutes is not UNSET:
            field_dict["cancellation_window_minutes"] = cancellation_window_minutes
        if belongs_to_club is not UNSET:
            field_dict["belongs_to_club"] = belongs_to_club
        if pay_in_club_only is not UNSET:
            field_dict["pay_in_club_only"] = pay_in_club_only
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if upload_photos is not UNSET:
            field_dict["upload_photos"] = upload_photos

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("club", (None, str(self.club).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        for special_days_item_element in self.special_days:
            files.append(
                ("special_days", (None, json.dumps(special_days_item_element.to_dict()).encode(), "application/json"))
            )

        for prices_item_element in self.prices:
            files.append(("prices", (None, json.dumps(prices_item_element.to_dict()).encode(), "application/json")))

        for extras_item_element in self.extras:
            files.append(("extras", (None, json.dumps(extras_item_element.to_dict()).encode(), "application/json")))

        for photos_item_element in self.photos:
            files.append(("photos", (None, json.dumps(photos_item_element.to_dict()).encode(), "application/json")))

        files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.type_, Unset):
            files.append(("type", (None, str(self.type_.value).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.location, Unset):
            files.append(("location", (None, str(self.location).encode(), "text/plain")))

        if not isinstance(self.opening_time, Unset):
            files.append(("opening_time", (None, str(self.opening_time).encode(), "text/plain")))

        if not isinstance(self.closing_time, Unset):
            files.append(("closing_time", (None, str(self.closing_time).encode(), "text/plain")))

        if not isinstance(self.min_reservation_minutes, Unset):
            files.append(("min_reservation_minutes", (None, str(self.min_reservation_minutes).encode(), "text/plain")))

        if not isinstance(self.max_recurring_days, Unset):
            files.append(("max_recurring_days", (None, str(self.max_recurring_days).encode(), "text/plain")))

        if not isinstance(self.cancellation_window_minutes, Unset):
            files.append(
                ("cancellation_window_minutes", (None, str(self.cancellation_window_minutes).encode(), "text/plain"))
            )

        if not isinstance(self.belongs_to_club, Unset):
            files.append(("belongs_to_club", (None, str(self.belongs_to_club).encode(), "text/plain")))

        if not isinstance(self.pay_in_club_only, Unset):
            files.append(("pay_in_club_only", (None, str(self.pay_in_club_only).encode(), "text/plain")))

        if not isinstance(self.is_active, Unset):
            files.append(("is_active", (None, str(self.is_active).encode(), "text/plain")))

        if not isinstance(self.upload_photos, Unset):
            for upload_photos_item_element in self.upload_photos:
                files.append(("upload_photos", (None, str(upload_photos_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sport_object_extra import SportObjectExtra
        from ..models.sport_object_photo import SportObjectPhoto
        from ..models.sport_object_price import SportObjectPrice
        from ..models.sport_object_special_day import SportObjectSpecialDay

        d = dict(src_dict)
        id = d.pop("id")

        club = d.pop("club")

        name = d.pop("name")

        special_days = []
        _special_days = d.pop("special_days")
        for special_days_item_data in _special_days:
            special_days_item = SportObjectSpecialDay.from_dict(special_days_item_data)

            special_days.append(special_days_item)

        prices = []
        _prices = d.pop("prices")
        for prices_item_data in _prices:
            prices_item = SportObjectPrice.from_dict(prices_item_data)

            prices.append(prices_item)

        extras = []
        _extras = d.pop("extras")
        for extras_item_data in _extras:
            extras_item = SportObjectExtra.from_dict(extras_item_data)

            extras.append(extras_item)

        photos = []
        _photos = d.pop("photos")
        for photos_item_data in _photos:
            photos_item = SportObjectPhoto.from_dict(photos_item_data)

            photos.append(photos_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _type_ = d.pop("type", UNSET)
        type_: TypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TypeEnum(_type_)

        description = d.pop("description", UNSET)

        location = d.pop("location", UNSET)

        opening_time = d.pop("opening_time", UNSET)

        closing_time = d.pop("closing_time", UNSET)

        min_reservation_minutes = d.pop("min_reservation_minutes", UNSET)

        max_recurring_days = d.pop("max_recurring_days", UNSET)

        cancellation_window_minutes = d.pop("cancellation_window_minutes", UNSET)

        belongs_to_club = d.pop("belongs_to_club", UNSET)

        pay_in_club_only = d.pop("pay_in_club_only", UNSET)

        is_active = d.pop("is_active", UNSET)

        upload_photos = cast(list[str], d.pop("upload_photos", UNSET))

        sport_object = cls(
            id=id,
            club=club,
            name=name,
            special_days=special_days,
            prices=prices,
            extras=extras,
            photos=photos,
            created_at=created_at,
            updated_at=updated_at,
            type_=type_,
            description=description,
            location=location,
            opening_time=opening_time,
            closing_time=closing_time,
            min_reservation_minutes=min_reservation_minutes,
            max_recurring_days=max_recurring_days,
            cancellation_window_minutes=cancellation_window_minutes,
            belongs_to_club=belongs_to_club,
            pay_in_club_only=pay_in_club_only,
            is_active=is_active,
            upload_photos=upload_photos,
        )

        sport_object.additional_properties = d
        return sport_object

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
