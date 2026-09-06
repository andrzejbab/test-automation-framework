from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.club_photo import ClubPhoto


T = TypeVar("T", bound="ClubProfile")


@_attrs_define
class ClubProfile:
    """
    Attributes:
        id (int):
        photos (list[ClubPhoto]):
        current_storage_usage_mb (str):
        remaining_storage_mb (str):
        storage_limit_enabled (str):
        current_users_count (str):
        remaining_user_slots (str):
        user_limit_enabled (str):
        effective_user_limit (str):
        effective_storage_limit_mb (str):
        name (str):
        contact_email (str):
        contact_phone (str):
        location (str):
        logo (str | Unset):
        upload_photos (list[str] | Unset):
        opening_time_mon (None | str | Unset):
        closing_time_mon (None | str | Unset):
        opening_time_tue (None | str | Unset):
        closing_time_tue (None | str | Unset):
        opening_time_wed (None | str | Unset):
        closing_time_wed (None | str | Unset):
        opening_time_thu (None | str | Unset):
        closing_time_thu (None | str | Unset):
        opening_time_fri (None | str | Unset):
        closing_time_fri (None | str | Unset):
        opening_time_sat (None | str | Unset):
        closing_time_sat (None | str | Unset):
        opening_time_sun (None | str | Unset):
        closing_time_sun (None | str | Unset):
        user_limit (int | None | Unset): Maksymalna liczba użytkowników klubu. Brak wartości oznacza brak limitu.
        storage_limit_mb (int | None | Unset): Maksymalna przestrzeń dyskowa klubu (MB). Brak wartości oznacza brak
            limitu.
        website (None | str | Unset):
        closed_mon (bool | Unset):
        closed_tue (bool | Unset):
        closed_wed (bool | Unset):
        closed_thu (bool | Unset):
        closed_fri (bool | Unset):
        closed_sat (bool | Unset):
        closed_sun (bool | Unset):
        training_hour_price (str | Unset):
    """

    id: int
    photos: list[ClubPhoto]
    current_storage_usage_mb: str
    remaining_storage_mb: str
    storage_limit_enabled: str
    current_users_count: str
    remaining_user_slots: str
    user_limit_enabled: str
    effective_user_limit: str
    effective_storage_limit_mb: str
    name: str
    contact_email: str
    contact_phone: str
    location: str
    logo: str | Unset = UNSET
    upload_photos: list[str] | Unset = UNSET
    opening_time_mon: None | str | Unset = UNSET
    closing_time_mon: None | str | Unset = UNSET
    opening_time_tue: None | str | Unset = UNSET
    closing_time_tue: None | str | Unset = UNSET
    opening_time_wed: None | str | Unset = UNSET
    closing_time_wed: None | str | Unset = UNSET
    opening_time_thu: None | str | Unset = UNSET
    closing_time_thu: None | str | Unset = UNSET
    opening_time_fri: None | str | Unset = UNSET
    closing_time_fri: None | str | Unset = UNSET
    opening_time_sat: None | str | Unset = UNSET
    closing_time_sat: None | str | Unset = UNSET
    opening_time_sun: None | str | Unset = UNSET
    closing_time_sun: None | str | Unset = UNSET
    user_limit: int | None | Unset = UNSET
    storage_limit_mb: int | None | Unset = UNSET
    website: None | str | Unset = UNSET
    closed_mon: bool | Unset = UNSET
    closed_tue: bool | Unset = UNSET
    closed_wed: bool | Unset = UNSET
    closed_thu: bool | Unset = UNSET
    closed_fri: bool | Unset = UNSET
    closed_sat: bool | Unset = UNSET
    closed_sun: bool | Unset = UNSET
    training_hour_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        photos = []
        for photos_item_data in self.photos:
            photos_item = photos_item_data.to_dict()
            photos.append(photos_item)

        current_storage_usage_mb = self.current_storage_usage_mb

        remaining_storage_mb = self.remaining_storage_mb

        storage_limit_enabled = self.storage_limit_enabled

        current_users_count = self.current_users_count

        remaining_user_slots = self.remaining_user_slots

        user_limit_enabled = self.user_limit_enabled

        effective_user_limit = self.effective_user_limit

        effective_storage_limit_mb = self.effective_storage_limit_mb

        name = self.name

        contact_email = self.contact_email

        contact_phone = self.contact_phone

        location = self.location

        logo = self.logo

        upload_photos: list[str] | Unset = UNSET
        if not isinstance(self.upload_photos, Unset):
            upload_photos = self.upload_photos

        opening_time_mon: None | str | Unset
        if isinstance(self.opening_time_mon, Unset):
            opening_time_mon = UNSET
        else:
            opening_time_mon = self.opening_time_mon

        closing_time_mon: None | str | Unset
        if isinstance(self.closing_time_mon, Unset):
            closing_time_mon = UNSET
        else:
            closing_time_mon = self.closing_time_mon

        opening_time_tue: None | str | Unset
        if isinstance(self.opening_time_tue, Unset):
            opening_time_tue = UNSET
        else:
            opening_time_tue = self.opening_time_tue

        closing_time_tue: None | str | Unset
        if isinstance(self.closing_time_tue, Unset):
            closing_time_tue = UNSET
        else:
            closing_time_tue = self.closing_time_tue

        opening_time_wed: None | str | Unset
        if isinstance(self.opening_time_wed, Unset):
            opening_time_wed = UNSET
        else:
            opening_time_wed = self.opening_time_wed

        closing_time_wed: None | str | Unset
        if isinstance(self.closing_time_wed, Unset):
            closing_time_wed = UNSET
        else:
            closing_time_wed = self.closing_time_wed

        opening_time_thu: None | str | Unset
        if isinstance(self.opening_time_thu, Unset):
            opening_time_thu = UNSET
        else:
            opening_time_thu = self.opening_time_thu

        closing_time_thu: None | str | Unset
        if isinstance(self.closing_time_thu, Unset):
            closing_time_thu = UNSET
        else:
            closing_time_thu = self.closing_time_thu

        opening_time_fri: None | str | Unset
        if isinstance(self.opening_time_fri, Unset):
            opening_time_fri = UNSET
        else:
            opening_time_fri = self.opening_time_fri

        closing_time_fri: None | str | Unset
        if isinstance(self.closing_time_fri, Unset):
            closing_time_fri = UNSET
        else:
            closing_time_fri = self.closing_time_fri

        opening_time_sat: None | str | Unset
        if isinstance(self.opening_time_sat, Unset):
            opening_time_sat = UNSET
        else:
            opening_time_sat = self.opening_time_sat

        closing_time_sat: None | str | Unset
        if isinstance(self.closing_time_sat, Unset):
            closing_time_sat = UNSET
        else:
            closing_time_sat = self.closing_time_sat

        opening_time_sun: None | str | Unset
        if isinstance(self.opening_time_sun, Unset):
            opening_time_sun = UNSET
        else:
            opening_time_sun = self.opening_time_sun

        closing_time_sun: None | str | Unset
        if isinstance(self.closing_time_sun, Unset):
            closing_time_sun = UNSET
        else:
            closing_time_sun = self.closing_time_sun

        user_limit: int | None | Unset
        if isinstance(self.user_limit, Unset):
            user_limit = UNSET
        else:
            user_limit = self.user_limit

        storage_limit_mb: int | None | Unset
        if isinstance(self.storage_limit_mb, Unset):
            storage_limit_mb = UNSET
        else:
            storage_limit_mb = self.storage_limit_mb

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        closed_mon = self.closed_mon

        closed_tue = self.closed_tue

        closed_wed = self.closed_wed

        closed_thu = self.closed_thu

        closed_fri = self.closed_fri

        closed_sat = self.closed_sat

        closed_sun = self.closed_sun

        training_hour_price = self.training_hour_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "photos": photos,
                "current_storage_usage_mb": current_storage_usage_mb,
                "remaining_storage_mb": remaining_storage_mb,
                "storage_limit_enabled": storage_limit_enabled,
                "current_users_count": current_users_count,
                "remaining_user_slots": remaining_user_slots,
                "user_limit_enabled": user_limit_enabled,
                "effective_user_limit": effective_user_limit,
                "effective_storage_limit_mb": effective_storage_limit_mb,
                "name": name,
                "contact_email": contact_email,
                "contact_phone": contact_phone,
                "location": location,
            }
        )
        if logo is not UNSET:
            field_dict["logo"] = logo
        if upload_photos is not UNSET:
            field_dict["upload_photos"] = upload_photos
        if opening_time_mon is not UNSET:
            field_dict["opening_time_mon"] = opening_time_mon
        if closing_time_mon is not UNSET:
            field_dict["closing_time_mon"] = closing_time_mon
        if opening_time_tue is not UNSET:
            field_dict["opening_time_tue"] = opening_time_tue
        if closing_time_tue is not UNSET:
            field_dict["closing_time_tue"] = closing_time_tue
        if opening_time_wed is not UNSET:
            field_dict["opening_time_wed"] = opening_time_wed
        if closing_time_wed is not UNSET:
            field_dict["closing_time_wed"] = closing_time_wed
        if opening_time_thu is not UNSET:
            field_dict["opening_time_thu"] = opening_time_thu
        if closing_time_thu is not UNSET:
            field_dict["closing_time_thu"] = closing_time_thu
        if opening_time_fri is not UNSET:
            field_dict["opening_time_fri"] = opening_time_fri
        if closing_time_fri is not UNSET:
            field_dict["closing_time_fri"] = closing_time_fri
        if opening_time_sat is not UNSET:
            field_dict["opening_time_sat"] = opening_time_sat
        if closing_time_sat is not UNSET:
            field_dict["closing_time_sat"] = closing_time_sat
        if opening_time_sun is not UNSET:
            field_dict["opening_time_sun"] = opening_time_sun
        if closing_time_sun is not UNSET:
            field_dict["closing_time_sun"] = closing_time_sun
        if user_limit is not UNSET:
            field_dict["user_limit"] = user_limit
        if storage_limit_mb is not UNSET:
            field_dict["storage_limit_mb"] = storage_limit_mb
        if website is not UNSET:
            field_dict["website"] = website
        if closed_mon is not UNSET:
            field_dict["closed_mon"] = closed_mon
        if closed_tue is not UNSET:
            field_dict["closed_tue"] = closed_tue
        if closed_wed is not UNSET:
            field_dict["closed_wed"] = closed_wed
        if closed_thu is not UNSET:
            field_dict["closed_thu"] = closed_thu
        if closed_fri is not UNSET:
            field_dict["closed_fri"] = closed_fri
        if closed_sat is not UNSET:
            field_dict["closed_sat"] = closed_sat
        if closed_sun is not UNSET:
            field_dict["closed_sun"] = closed_sun
        if training_hour_price is not UNSET:
            field_dict["training_hour_price"] = training_hour_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.club_photo import ClubPhoto

        d = dict(src_dict)
        id = d.pop("id")

        photos = []
        _photos = d.pop("photos")
        for photos_item_data in _photos:
            photos_item = ClubPhoto.from_dict(photos_item_data)

            photos.append(photos_item)

        current_storage_usage_mb = d.pop("current_storage_usage_mb")

        remaining_storage_mb = d.pop("remaining_storage_mb")

        storage_limit_enabled = d.pop("storage_limit_enabled")

        current_users_count = d.pop("current_users_count")

        remaining_user_slots = d.pop("remaining_user_slots")

        user_limit_enabled = d.pop("user_limit_enabled")

        effective_user_limit = d.pop("effective_user_limit")

        effective_storage_limit_mb = d.pop("effective_storage_limit_mb")

        name = d.pop("name")

        contact_email = d.pop("contact_email")

        contact_phone = d.pop("contact_phone")

        location = d.pop("location")

        logo = d.pop("logo", UNSET)

        upload_photos = cast(list[str], d.pop("upload_photos", UNSET))

        def _parse_opening_time_mon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_time_mon = _parse_opening_time_mon(d.pop("opening_time_mon", UNSET))

        def _parse_closing_time_mon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_time_mon = _parse_closing_time_mon(d.pop("closing_time_mon", UNSET))

        def _parse_opening_time_tue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_time_tue = _parse_opening_time_tue(d.pop("opening_time_tue", UNSET))

        def _parse_closing_time_tue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_time_tue = _parse_closing_time_tue(d.pop("closing_time_tue", UNSET))

        def _parse_opening_time_wed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_time_wed = _parse_opening_time_wed(d.pop("opening_time_wed", UNSET))

        def _parse_closing_time_wed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_time_wed = _parse_closing_time_wed(d.pop("closing_time_wed", UNSET))

        def _parse_opening_time_thu(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_time_thu = _parse_opening_time_thu(d.pop("opening_time_thu", UNSET))

        def _parse_closing_time_thu(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_time_thu = _parse_closing_time_thu(d.pop("closing_time_thu", UNSET))

        def _parse_opening_time_fri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_time_fri = _parse_opening_time_fri(d.pop("opening_time_fri", UNSET))

        def _parse_closing_time_fri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_time_fri = _parse_closing_time_fri(d.pop("closing_time_fri", UNSET))

        def _parse_opening_time_sat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_time_sat = _parse_opening_time_sat(d.pop("opening_time_sat", UNSET))

        def _parse_closing_time_sat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_time_sat = _parse_closing_time_sat(d.pop("closing_time_sat", UNSET))

        def _parse_opening_time_sun(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_time_sun = _parse_opening_time_sun(d.pop("opening_time_sun", UNSET))

        def _parse_closing_time_sun(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing_time_sun = _parse_closing_time_sun(d.pop("closing_time_sun", UNSET))

        def _parse_user_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_limit = _parse_user_limit(d.pop("user_limit", UNSET))

        def _parse_storage_limit_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_limit_mb = _parse_storage_limit_mb(d.pop("storage_limit_mb", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        closed_mon = d.pop("closed_mon", UNSET)

        closed_tue = d.pop("closed_tue", UNSET)

        closed_wed = d.pop("closed_wed", UNSET)

        closed_thu = d.pop("closed_thu", UNSET)

        closed_fri = d.pop("closed_fri", UNSET)

        closed_sat = d.pop("closed_sat", UNSET)

        closed_sun = d.pop("closed_sun", UNSET)

        training_hour_price = d.pop("training_hour_price", UNSET)

        club_profile = cls(
            id=id,
            photos=photos,
            current_storage_usage_mb=current_storage_usage_mb,
            remaining_storage_mb=remaining_storage_mb,
            storage_limit_enabled=storage_limit_enabled,
            current_users_count=current_users_count,
            remaining_user_slots=remaining_user_slots,
            user_limit_enabled=user_limit_enabled,
            effective_user_limit=effective_user_limit,
            effective_storage_limit_mb=effective_storage_limit_mb,
            name=name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            location=location,
            logo=logo,
            upload_photos=upload_photos,
            opening_time_mon=opening_time_mon,
            closing_time_mon=closing_time_mon,
            opening_time_tue=opening_time_tue,
            closing_time_tue=closing_time_tue,
            opening_time_wed=opening_time_wed,
            closing_time_wed=closing_time_wed,
            opening_time_thu=opening_time_thu,
            closing_time_thu=closing_time_thu,
            opening_time_fri=opening_time_fri,
            closing_time_fri=closing_time_fri,
            opening_time_sat=opening_time_sat,
            closing_time_sat=closing_time_sat,
            opening_time_sun=opening_time_sun,
            closing_time_sun=closing_time_sun,
            user_limit=user_limit,
            storage_limit_mb=storage_limit_mb,
            website=website,
            closed_mon=closed_mon,
            closed_tue=closed_tue,
            closed_wed=closed_wed,
            closed_thu=closed_thu,
            closed_fri=closed_fri,
            closed_sat=closed_sat,
            closed_sun=closed_sun,
            training_hour_price=training_hour_price,
        )

        club_profile.additional_properties = d
        return club_profile

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
