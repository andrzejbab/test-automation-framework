from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_training_group import PatchedTrainingGroup
from ...models.training_group import TrainingGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: int,
    *,
    body: PatchedTrainingGroup | PatchedTrainingGroup | PatchedTrainingGroup | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/szkolenia/groups/{item_id}/".format(
            item_id=quote(str(item_id), safe=""),
        ),
    }

    if isinstance(body, PatchedTrainingGroup):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedTrainingGroup):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedTrainingGroup):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | TrainingGroup | None:
    if response.status_code == 200:
        response_200 = TrainingGroup.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | TrainingGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedTrainingGroup | PatchedTrainingGroup | PatchedTrainingGroup | Unset = UNSET,
) -> Response[Any | TrainingGroup]:
    """Update training group

    Args:
        item_id (int):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TrainingGroup]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedTrainingGroup | PatchedTrainingGroup | PatchedTrainingGroup | Unset = UNSET,
) -> Any | TrainingGroup | None:
    """Update training group

    Args:
        item_id (int):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TrainingGroup
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    item_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedTrainingGroup | PatchedTrainingGroup | PatchedTrainingGroup | Unset = UNSET,
) -> Response[Any | TrainingGroup]:
    """Update training group

    Args:
        item_id (int):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TrainingGroup]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedTrainingGroup | PatchedTrainingGroup | PatchedTrainingGroup | Unset = UNSET,
) -> Any | TrainingGroup | None:
    """Update training group

    Args:
        item_id (int):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):
        body (PatchedTrainingGroup | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TrainingGroup
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
