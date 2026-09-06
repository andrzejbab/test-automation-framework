from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member import Member
from ...models.patched_member import PatchedMember
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_id: int,
    *,
    body: PatchedMember | PatchedMember | PatchedMember | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/club/members/update/{member_id}/".format(
            member_id=quote(str(member_id), safe=""),
        ),
    }

    if isinstance(body, PatchedMember):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedMember):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedMember):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Member | None:
    if response.status_code == 200:
        response_200 = Member.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Member]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    member_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | PatchedMember | PatchedMember | Unset = UNSET,
) -> Response[Any | Member]:
    """Update member

    Args:
        member_id (int):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Member]
    """

    kwargs = _get_kwargs(
        member_id=member_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | PatchedMember | PatchedMember | Unset = UNSET,
) -> Any | Member | None:
    """Update member

    Args:
        member_id (int):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Member
    """

    return sync_detailed(
        member_id=member_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    member_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | PatchedMember | PatchedMember | Unset = UNSET,
) -> Response[Any | Member]:
    """Update member

    Args:
        member_id (int):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Member]
    """

    kwargs = _get_kwargs(
        member_id=member_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMember | PatchedMember | PatchedMember | Unset = UNSET,
) -> Any | Member | None:
    """Update member

    Args:
        member_id (int):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):
        body (PatchedMember | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Member
    """

    return (
        await asyncio_detailed(
            member_id=member_id,
            client=client,
            body=body,
        )
    ).parsed
