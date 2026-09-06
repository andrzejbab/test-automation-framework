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


T = TypeVar("T", bound="TrainingGroup")


@_attrs_define
class TrainingGroup:
    """
    Attributes:
        id (int):
        name (str):
        training_type (str):
        coach (TrainingMember):
        players (list[TrainingMember]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        max_members (int | None | Unset):
        age_range (str | Unset):
        description (str | Unset):
        training_type_id (int | None | Unset):
        coach_id (int | None | Unset):
        player_ids (list[int] | Unset):
    """

    id: int
    name: str
    training_type: str
    coach: TrainingMember
    players: list[TrainingMember]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    max_members: int | None | Unset = UNSET
    age_range: str | Unset = UNSET
    description: str | Unset = UNSET
    training_type_id: int | None | Unset = UNSET
    coach_id: int | None | Unset = UNSET
    player_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        training_type = self.training_type

        coach = self.coach.to_dict()

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        max_members: int | None | Unset
        if isinstance(self.max_members, Unset):
            max_members = UNSET
        else:
            max_members = self.max_members

        age_range = self.age_range

        description = self.description

        training_type_id: int | None | Unset
        if isinstance(self.training_type_id, Unset):
            training_type_id = UNSET
        else:
            training_type_id = self.training_type_id

        coach_id: int | None | Unset
        if isinstance(self.coach_id, Unset):
            coach_id = UNSET
        else:
            coach_id = self.coach_id

        player_ids: list[int] | Unset = UNSET
        if not isinstance(self.player_ids, Unset):
            player_ids = self.player_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "training_type": training_type,
                "coach": coach,
                "players": players,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if max_members is not UNSET:
            field_dict["max_members"] = max_members
        if age_range is not UNSET:
            field_dict["age_range"] = age_range
        if description is not UNSET:
            field_dict["description"] = description
        if training_type_id is not UNSET:
            field_dict["training_type_id"] = training_type_id
        if coach_id is not UNSET:
            field_dict["coach_id"] = coach_id
        if player_ids is not UNSET:
            field_dict["player_ids"] = player_ids

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("id", (None, str(self.id).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("training_type", (None, str(self.training_type).encode(), "text/plain")))

        files.append(("coach", (None, json.dumps(self.coach.to_dict()).encode(), "application/json")))

        for players_item_element in self.players:
            files.append(("players", (None, json.dumps(players_item_element.to_dict()).encode(), "application/json")))

        files.append(("created_at", (None, self.created_at.isoformat().encode(), "text/plain")))

        files.append(("updated_at", (None, self.updated_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.max_members, Unset):
            if isinstance(self.max_members, int):
                files.append(("max_members", (None, str(self.max_members).encode(), "text/plain")))
            else:
                files.append(("max_members", (None, str(self.max_members).encode(), "text/plain")))

        if not isinstance(self.age_range, Unset):
            files.append(("age_range", (None, str(self.age_range).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.training_type_id, Unset):
            if isinstance(self.training_type_id, int):
                files.append(("training_type_id", (None, str(self.training_type_id).encode(), "text/plain")))
            else:
                files.append(("training_type_id", (None, str(self.training_type_id).encode(), "text/plain")))

        if not isinstance(self.coach_id, Unset):
            if isinstance(self.coach_id, int):
                files.append(("coach_id", (None, str(self.coach_id).encode(), "text/plain")))
            else:
                files.append(("coach_id", (None, str(self.coach_id).encode(), "text/plain")))

        if not isinstance(self.player_ids, Unset):
            for player_ids_item_element in self.player_ids:
                files.append(("player_ids", (None, str(player_ids_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.training_member import TrainingMember

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        training_type = d.pop("training_type")

        coach = TrainingMember.from_dict(d.pop("coach"))

        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = TrainingMember.from_dict(players_item_data)

            players.append(players_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_max_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_members = _parse_max_members(d.pop("max_members", UNSET))

        age_range = d.pop("age_range", UNSET)

        description = d.pop("description", UNSET)

        def _parse_training_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        training_type_id = _parse_training_type_id(d.pop("training_type_id", UNSET))

        def _parse_coach_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        coach_id = _parse_coach_id(d.pop("coach_id", UNSET))

        player_ids = cast(list[int], d.pop("player_ids", UNSET))

        training_group = cls(
            id=id,
            name=name,
            training_type=training_type,
            coach=coach,
            players=players,
            created_at=created_at,
            updated_at=updated_at,
            max_members=max_members,
            age_range=age_range,
            description=description,
            training_type_id=training_type_id,
            coach_id=coach_id,
            player_ids=player_ids,
        )

        training_group.additional_properties = d
        return training_group

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
