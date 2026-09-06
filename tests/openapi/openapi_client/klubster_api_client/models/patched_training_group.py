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
    from ..models.training_member import TrainingMember


T = TypeVar("T", bound="PatchedTrainingGroup")


@_attrs_define
class PatchedTrainingGroup:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        max_members (int | None | Unset):
        age_range (str | Unset):
        description (str | Unset):
        training_type (str | Unset):
        training_type_id (int | None | Unset):
        coach (TrainingMember | Unset):
        coach_id (int | None | Unset):
        players (list[TrainingMember] | Unset):
        player_ids (list[int] | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    max_members: int | None | Unset = UNSET
    age_range: str | Unset = UNSET
    description: str | Unset = UNSET
    training_type: str | Unset = UNSET
    training_type_id: int | None | Unset = UNSET
    coach: TrainingMember | Unset = UNSET
    coach_id: int | None | Unset = UNSET
    players: list[TrainingMember] | Unset = UNSET
    player_ids: list[int] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        max_members: int | None | Unset
        if isinstance(self.max_members, Unset):
            max_members = UNSET
        else:
            max_members = self.max_members

        age_range = self.age_range

        description = self.description

        training_type = self.training_type

        training_type_id: int | None | Unset
        if isinstance(self.training_type_id, Unset):
            training_type_id = UNSET
        else:
            training_type_id = self.training_type_id

        coach: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coach, Unset):
            coach = self.coach.to_dict()

        coach_id: int | None | Unset
        if isinstance(self.coach_id, Unset):
            coach_id = UNSET
        else:
            coach_id = self.coach_id

        players: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)

        player_ids: list[int] | Unset = UNSET
        if not isinstance(self.player_ids, Unset):
            player_ids = self.player_ids

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if max_members is not UNSET:
            field_dict["max_members"] = max_members
        if age_range is not UNSET:
            field_dict["age_range"] = age_range
        if description is not UNSET:
            field_dict["description"] = description
        if training_type is not UNSET:
            field_dict["training_type"] = training_type
        if training_type_id is not UNSET:
            field_dict["training_type_id"] = training_type_id
        if coach is not UNSET:
            field_dict["coach"] = coach
        if coach_id is not UNSET:
            field_dict["coach_id"] = coach_id
        if players is not UNSET:
            field_dict["players"] = players
        if player_ids is not UNSET:
            field_dict["player_ids"] = player_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.max_members, Unset):
            if isinstance(self.max_members, int):
                files.append(("max_members", (None, str(self.max_members).encode(), "text/plain")))
            else:
                files.append(("max_members", (None, str(self.max_members).encode(), "text/plain")))

        if not isinstance(self.age_range, Unset):
            files.append(("age_range", (None, str(self.age_range).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.training_type, Unset):
            files.append(("training_type", (None, str(self.training_type).encode(), "text/plain")))

        if not isinstance(self.training_type_id, Unset):
            if isinstance(self.training_type_id, int):
                files.append(("training_type_id", (None, str(self.training_type_id).encode(), "text/plain")))
            else:
                files.append(("training_type_id", (None, str(self.training_type_id).encode(), "text/plain")))

        if not isinstance(self.coach, Unset):
            files.append(("coach", (None, json.dumps(self.coach.to_dict()).encode(), "application/json")))

        if not isinstance(self.coach_id, Unset):
            if isinstance(self.coach_id, int):
                files.append(("coach_id", (None, str(self.coach_id).encode(), "text/plain")))
            else:
                files.append(("coach_id", (None, str(self.coach_id).encode(), "text/plain")))

        if not isinstance(self.players, Unset):
            for players_item_element in self.players:
                files.append(
                    ("players", (None, json.dumps(players_item_element.to_dict()).encode(), "application/json"))
                )

        if not isinstance(self.player_ids, Unset):
            for player_ids_item_element in self.player_ids:
                files.append(("player_ids", (None, str(player_ids_item_element).encode(), "text/plain")))

        if not isinstance(self.created_at, Unset):
            files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.updated_at, Unset):
            files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.training_member import TrainingMember

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_max_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_members = _parse_max_members(d.pop("max_members", UNSET))

        age_range = d.pop("age_range", UNSET)

        description = d.pop("description", UNSET)

        training_type = d.pop("training_type", UNSET)

        def _parse_training_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        training_type_id = _parse_training_type_id(d.pop("training_type_id", UNSET))

        _coach = d.pop("coach", UNSET)
        coach: TrainingMember | Unset
        if isinstance(_coach, Unset):
            coach = UNSET
        else:
            coach = TrainingMember.from_dict(_coach)

        def _parse_coach_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        coach_id = _parse_coach_id(d.pop("coach_id", UNSET))

        _players = d.pop("players", UNSET)
        players: list[TrainingMember] | Unset = UNSET
        if _players is not UNSET:
            players = []
            for players_item_data in _players:
                players_item = TrainingMember.from_dict(players_item_data)

                players.append(players_item)

        player_ids = cast(list[int], d.pop("player_ids", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        patched_training_group = cls(
            id=id,
            name=name,
            max_members=max_members,
            age_range=age_range,
            description=description,
            training_type=training_type,
            training_type_id=training_type_id,
            coach=coach,
            coach_id=coach_id,
            players=players,
            player_ids=player_ids,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_training_group.additional_properties = d
        return patched_training_group

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
