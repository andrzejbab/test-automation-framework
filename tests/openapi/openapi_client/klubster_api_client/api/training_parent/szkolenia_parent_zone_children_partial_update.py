from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_parent_child_update import PatchedParentChildUpdate
from ...models.szkolenia_parent_zone_children_partial_update_response_200 import (
    SzkoleniaParentZoneChildrenPartialUpdateResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    child_id: int,
    *,
    body: PatchedParentChildUpdate | PatchedParentChildUpdate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/szkolenia/parent-zone/children/{child_id}/".format(
            child_id=quote(str(child_id), safe=""),
        ),
    }

    if isinstance(body, PatchedParentChildUpdate):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"
    if isinstance(body, PatchedParentChildUpdate):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200 | None:
    if response.status_code == 200:
        response_200 = SzkoleniaParentZoneChildrenPartialUpdateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    child_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedParentChildUpdate | PatchedParentChildUpdate | Unset = UNSET,
) -> Response[Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200]:
    """Update child data in parent zone

     Supports multipart updates and optional email completion for placeholder child accounts.

    Args:
        child_id (int):
        body (PatchedParentChildUpdate | Unset):
        body (PatchedParentChildUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200]
    """

    kwargs = _get_kwargs(
        child_id=child_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    child_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedParentChildUpdate | PatchedParentChildUpdate | Unset = UNSET,
) -> Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200 | None:
    """Update child data in parent zone

     Supports multipart updates and optional email completion for placeholder child accounts.

    Args:
        child_id (int):
        body (PatchedParentChildUpdate | Unset):
        body (PatchedParentChildUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200
    """

    return sync_detailed(
        child_id=child_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    child_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedParentChildUpdate | PatchedParentChildUpdate | Unset = UNSET,
) -> Response[Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200]:
    """Update child data in parent zone

     Supports multipart updates and optional email completion for placeholder child accounts.

    Args:
        child_id (int):
        body (PatchedParentChildUpdate | Unset):
        body (PatchedParentChildUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200]
    """

    kwargs = _get_kwargs(
        child_id=child_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    child_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedParentChildUpdate | PatchedParentChildUpdate | Unset = UNSET,
) -> Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200 | None:
    """Update child data in parent zone

     Supports multipart updates and optional email completion for placeholder child accounts.

    Args:
        child_id (int):
        body (PatchedParentChildUpdate | Unset):
        body (PatchedParentChildUpdate | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SzkoleniaParentZoneChildrenPartialUpdateResponse200
    """

    return (
        await asyncio_detailed(
            child_id=child_id,
            client=client,
            body=body,
        )
    ).parsed
