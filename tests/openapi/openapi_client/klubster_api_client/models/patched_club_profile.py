from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.club_photo import ClubPhoto


T = TypeVar("T", bound="PatchedClubProfile")


@_attrs_define
class PatchedClubProfile:
    """
    Attributes:
        id (int | Unset):
        logo (str | Unset):
        photos (list[ClubPhoto] | Unset):
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
        current_storage_usage_mb (str | Unset):
        remaining_storage_mb (str | Unset):
        storage_limit_enabled (str | Unset):
        current_users_count (str | Unset):
        remaining_user_slots (str | Unset):
        user_limit_enabled (str | Unset):
        effective_user_limit (str | Unset):
        effective_storage_limit_mb (str | Unset):
        name (str | Unset):
        user_limit (int | None | Unset): Maksymalna liczba użytkowników klubu. Brak wartości oznacza brak limitu.
        storage_limit_mb (int | None | Unset): Maksymalna przestrzeń dyskowa klubu (MB). Brak wartości oznacza brak
            limitu.
        contact_email (str | Unset):
        website (None | str | Unset):
        contact_phone (str | Unset):
        location (str | Unset):
        closed_mon (bool | Unset):
        closed_tue (bool | Unset):
        closed_wed (bool | Unset):
        closed_thu (bool | Unset):
        closed_fri (bool | Unset):
        closed_sat (bool | Unset):
        closed_sun (bool | Unset):
        training_hour_price (str | Unset):
    """

    id: int | Unset = UNSET
    logo: str | Unset = UNSET
    photos: list[ClubPhoto] | Unset = UNSET
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
    current_storage_usage_mb: str | Unset = UNSET
    remaining_storage_mb: str | Unset = UNSET
    storage_limit_enabled: str | Unset = UNSET
    current_users_count: str | Unset = UNSET
    remaining_user_slots: str | Unset = UNSET
    user_limit_enabled: str | Unset = UNSET
    effective_user_limit: str | Unset = UNSET
    effective_storage_limit_mb: str | Unset = UNSET
    name: str | Unset = UNSET
    user_limit: int | None | Unset = UNSET
    storage_limit_mb: int | None | Unset = UNSET
    contact_email: str | Unset = UNSET
    website: None | str | Unset = UNSET
    contact_phone: str | Unset = UNSET
    location: str | Unset = UNSET
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

        logo = self.logo

        photos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = []
            for photos_item_data in self.photos:
                photos_item = photos_item_data.to_dict()
                photos.append(photos_item)

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

        current_storage_usage_mb = self.current_storage_usage_mb

        remaining_storage_mb = self.remaining_storage_mb

        storage_limit_enabled = self.storage_limit_enabled

        current_users_count = self.current_users_count

        remaining_user_slots = self.remaining_user_slots

        user_limit_enabled = self.user_limit_enabled

        effective_user_limit = self.effective_user_limit

        effective_storage_limit_mb = self.effective_storage_limit_mb

        name = self.name

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

        contact_email = self.contact_email

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        contact_phone = self.contact_phone

        location = self.location

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if logo is not UNSET:
            field_dict["logo"] = logo
        if photos is not UNSET:
            field_dict["photos"] = photos
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
        if current_storage_usage_mb is not UNSET:
            field_dict["current_storage_usage_mb"] = current_storage_usage_mb
        if remaining_storage_mb is not UNSET:
            field_dict["remaining_storage_mb"] = remaining_storage_mb
        if storage_limit_enabled is not UNSET:
            field_dict["storage_limit_enabled"] = storage_limit_enabled
        if current_users_count is not UNSET:
            field_dict["current_users_count"] = current_users_count
        if remaining_user_slots is not UNSET:
            field_dict["remaining_user_slots"] = remaining_user_slots
        if user_limit_enabled is not UNSET:
            field_dict["user_limit_enabled"] = user_limit_enabled
        if effective_user_limit is not UNSET:
            field_dict["effective_user_limit"] = effective_user_limit
        if effective_storage_limit_mb is not UNSET:
            field_dict["effective_storage_limit_mb"] = effective_storage_limit_mb
        if name is not UNSET:
            field_dict["name"] = name
        if user_limit is not UNSET:
            field_dict["user_limit"] = user_limit
        if storage_limit_mb is not UNSET:
            field_dict["storage_limit_mb"] = storage_limit_mb
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
        if website is not UNSET:
            field_dict["website"] = website
        if contact_phone is not UNSET:
            field_dict["contact_phone"] = contact_phone
        if location is not UNSET:
            field_dict["location"] = location
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.logo, Unset):
            files.append(("logo", (None, str(self.logo).encode(), "text/plain")))

        if not isinstance(self.photos, Unset):
            for photos_item_element in self.photos:
                files.append(("photos", (None, json.dumps(photos_item_element.to_dict()).encode(), "application/json")))

        if not isinstance(self.upload_photos, Unset):
            for upload_photos_item_element in self.upload_photos:
                files.append(("upload_photos", (None, str(upload_photos_item_element).encode(), "text/plain")))

        if not isinstance(self.opening_time_mon, Unset):
            if isinstance(self.opening_time_mon, str):
                files.append(("opening_time_mon", (None, str(self.opening_time_mon).encode(), "text/plain")))
            else:
                files.append(("opening_time_mon", (None, str(self.opening_time_mon).encode(), "text/plain")))

        if not isinstance(self.closing_time_mon, Unset):
            if isinstance(self.closing_time_mon, str):
                files.append(("closing_time_mon", (None, str(self.closing_time_mon).encode(), "text/plain")))
            else:
                files.append(("closing_time_mon", (None, str(self.closing_time_mon).encode(), "text/plain")))

        if not isinstance(self.opening_time_tue, Unset):
            if isinstance(self.opening_time_tue, str):
                files.append(("opening_time_tue", (None, str(self.opening_time_tue).encode(), "text/plain")))
            else:
                files.append(("opening_time_tue", (None, str(self.opening_time_tue).encode(), "text/plain")))

        if not isinstance(self.closing_time_tue, Unset):
            if isinstance(self.closing_time_tue, str):
                files.append(("closing_time_tue", (None, str(self.closing_time_tue).encode(), "text/plain")))
            else:
                files.append(("closing_time_tue", (None, str(self.closing_time_tue).encode(), "text/plain")))

        if not isinstance(self.opening_time_wed, Unset):
            if isinstance(self.opening_time_wed, str):
                files.append(("opening_time_wed", (None, str(self.opening_time_wed).encode(), "text/plain")))
            else:
                files.append(("opening_time_wed", (None, str(self.opening_time_wed).encode(), "text/plain")))

        if not isinstance(self.closing_time_wed, Unset):
            if isinstance(self.closing_time_wed, str):
                files.append(("closing_time_wed", (None, str(self.closing_time_wed).encode(), "text/plain")))
            else:
                files.append(("closing_time_wed", (None, str(self.closing_time_wed).encode(), "text/plain")))

        if not isinstance(self.opening_time_thu, Unset):
            if isinstance(self.opening_time_thu, str):
                files.append(("opening_time_thu", (None, str(self.opening_time_thu).encode(), "text/plain")))
            else:
                files.append(("opening_time_thu", (None, str(self.opening_time_thu).encode(), "text/plain")))

        if not isinstance(self.closing_time_thu, Unset):
            if isinstance(self.closing_time_thu, str):
                files.append(("closing_time_thu", (None, str(self.closing_time_thu).encode(), "text/plain")))
            else:
                files.append(("closing_time_thu", (None, str(self.closing_time_thu).encode(), "text/plain")))

        if not isinstance(self.opening_time_fri, Unset):
            if isinstance(self.opening_time_fri, str):
                files.append(("opening_time_fri", (None, str(self.opening_time_fri).encode(), "text/plain")))
            else:
                files.append(("opening_time_fri", (None, str(self.opening_time_fri).encode(), "text/plain")))

        if not isinstance(self.closing_time_fri, Unset):
            if isinstance(self.closing_time_fri, str):
                files.append(("closing_time_fri", (None, str(self.closing_time_fri).encode(), "text/plain")))
            else:
                files.append(("closing_time_fri", (None, str(self.closing_time_fri).encode(), "text/plain")))

        if not isinstance(self.opening_time_sat, Unset):
            if isinstance(self.opening_time_sat, str):
                files.append(("opening_time_sat", (None, str(self.opening_time_sat).encode(), "text/plain")))
            else:
                files.append(("opening_time_sat", (None, str(self.opening_time_sat).encode(), "text/plain")))

        if not isinstance(self.closing_time_sat, Unset):
            if isinstance(self.closing_time_sat, str):
                files.append(("closing_time_sat", (None, str(self.closing_time_sat).encode(), "text/plain")))
            else:
                files.append(("closing_time_sat", (None, str(self.closing_time_sat).encode(), "text/plain")))

        if not isinstance(self.opening_time_sun, Unset):
            if isinstance(self.opening_time_sun, str):
                files.append(("opening_time_sun", (None, str(self.opening_time_sun).encode(), "text/plain")))
            else:
                files.append(("opening_time_sun", (None, str(self.opening_time_sun).encode(), "text/plain")))

        if not isinstance(self.closing_time_sun, Unset):
            if isinstance(self.closing_time_sun, str):
                files.append(("closing_time_sun", (None, str(self.closing_time_sun).encode(), "text/plain")))
            else:
                files.append(("closing_time_sun", (None, str(self.closing_time_sun).encode(), "text/plain")))

        if not isinstance(self.current_storage_usage_mb, Unset):
            files.append(
                ("current_storage_usage_mb", (None, str(self.current_storage_usage_mb).encode(), "text/plain"))
            )

        if not isinstance(self.remaining_storage_mb, Unset):
            files.append(("remaining_storage_mb", (None, str(self.remaining_storage_mb).encode(), "text/plain")))

        if not isinstance(self.storage_limit_enabled, Unset):
            files.append(("storage_limit_enabled", (None, str(self.storage_limit_enabled).encode(), "text/plain")))

        if not isinstance(self.current_users_count, Unset):
            files.append(("current_users_count", (None, str(self.current_users_count).encode(), "text/plain")))

        if not isinstance(self.remaining_user_slots, Unset):
            files.append(("remaining_user_slots", (None, str(self.remaining_user_slots).encode(), "text/plain")))

        if not isinstance(self.user_limit_enabled, Unset):
            files.append(("user_limit_enabled", (None, str(self.user_limit_enabled).encode(), "text/plain")))

        if not isinstance(self.effective_user_limit, Unset):
            files.append(("effective_user_limit", (None, str(self.effective_user_limit).encode(), "text/plain")))

        if not isinstance(self.effective_storage_limit_mb, Unset):
            files.append(
                ("effective_storage_limit_mb", (None, str(self.effective_storage_limit_mb).encode(), "text/plain"))
            )

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.user_limit, Unset):
            if isinstance(self.user_limit, int):
                files.append(("user_limit", (None, str(self.user_limit).encode(), "text/plain")))
            else:
                files.append(("user_limit", (None, str(self.user_limit).encode(), "text/plain")))

        if not isinstance(self.storage_limit_mb, Unset):
            if isinstance(self.storage_limit_mb, int):
                files.append(("storage_limit_mb", (None, str(self.storage_limit_mb).encode(), "text/plain")))
            else:
                files.append(("storage_limit_mb", (None, str(self.storage_limit_mb).encode(), "text/plain")))

        if not isinstance(self.contact_email, Unset):
            files.append(("contact_email", (None, str(self.contact_email).encode(), "text/plain")))

        if not isinstance(self.website, Unset):
            if isinstance(self.website, str):
                files.append(("website", (None, str(self.website).encode(), "text/plain")))
            else:
                files.append(("website", (None, str(self.website).encode(), "text/plain")))

        if not isinstance(self.contact_phone, Unset):
            files.append(("contact_phone", (None, str(self.contact_phone).encode(), "text/plain")))

        if not isinstance(self.location, Unset):
            files.append(("location", (None, str(self.location).encode(), "text/plain")))

        if not isinstance(self.closed_mon, Unset):
            files.append(("closed_mon", (None, str(self.closed_mon).encode(), "text/plain")))

        if not isinstance(self.closed_tue, Unset):
            files.append(("closed_tue", (None, str(self.closed_tue).encode(), "text/plain")))

        if not isinstance(self.closed_wed, Unset):
            files.append(("closed_wed", (None, str(self.closed_wed).encode(), "text/plain")))

        if not isinstance(self.closed_thu, Unset):
            files.append(("closed_thu", (None, str(self.closed_thu).encode(), "text/plain")))

        if not isinstance(self.closed_fri, Unset):
            files.append(("closed_fri", (None, str(self.closed_fri).encode(), "text/plain")))

        if not isinstance(self.closed_sat, Unset):
            files.append(("closed_sat", (None, str(self.closed_sat).encode(), "text/plain")))

        if not isinstance(self.closed_sun, Unset):
            files.append(("closed_sun", (None, str(self.closed_sun).encode(), "text/plain")))

        if not isinstance(self.training_hour_price, Unset):
            files.append(("training_hour_price", (None, str(self.training_hour_price).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.club_photo import ClubPhoto

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        logo = d.pop("logo", UNSET)

        _photos = d.pop("photos", UNSET)
        photos: list[ClubPhoto] | Unset = UNSET
        if _photos is not UNSET:
            photos = []
            for photos_item_data in _photos:
                photos_item = ClubPhoto.from_dict(photos_item_data)

                photos.append(photos_item)

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

        current_storage_usage_mb = d.pop("current_storage_usage_mb", UNSET)

        remaining_storage_mb = d.pop("remaining_storage_mb", UNSET)

        storage_limit_enabled = d.pop("storage_limit_enabled", UNSET)

        current_users_count = d.pop("current_users_count", UNSET)

        remaining_user_slots = d.pop("remaining_user_slots", UNSET)

        user_limit_enabled = d.pop("user_limit_enabled", UNSET)

        effective_user_limit = d.pop("effective_user_limit", UNSET)

        effective_storage_limit_mb = d.pop("effective_storage_limit_mb", UNSET)

        name = d.pop("name", UNSET)

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

        contact_email = d.pop("contact_email", UNSET)

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        contact_phone = d.pop("contact_phone", UNSET)

        location = d.pop("location", UNSET)

        closed_mon = d.pop("closed_mon", UNSET)

        closed_tue = d.pop("closed_tue", UNSET)

        closed_wed = d.pop("closed_wed", UNSET)

        closed_thu = d.pop("closed_thu", UNSET)

        closed_fri = d.pop("closed_fri", UNSET)

        closed_sat = d.pop("closed_sat", UNSET)

        closed_sun = d.pop("closed_sun", UNSET)

        training_hour_price = d.pop("training_hour_price", UNSET)

        patched_club_profile = cls(
            id=id,
            logo=logo,
            photos=photos,
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
            current_storage_usage_mb=current_storage_usage_mb,
            remaining_storage_mb=remaining_storage_mb,
            storage_limit_enabled=storage_limit_enabled,
            current_users_count=current_users_count,
            remaining_user_slots=remaining_user_slots,
            user_limit_enabled=user_limit_enabled,
            effective_user_limit=effective_user_limit,
            effective_storage_limit_mb=effective_storage_limit_mb,
            name=name,
            user_limit=user_limit,
            storage_limit_mb=storage_limit_mb,
            contact_email=contact_email,
            website=website,
            contact_phone=contact_phone,
            location=location,
            closed_mon=closed_mon,
            closed_tue=closed_tue,
            closed_wed=closed_wed,
            closed_thu=closed_thu,
            closed_fri=closed_fri,
            closed_sat=closed_sat,
            closed_sun=closed_sun,
            training_hour_price=training_hour_price,
        )

        patched_club_profile.additional_properties = d
        return patched_club_profile

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
