from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.club_profile import ClubProfile
from ...models.patched_club_profile import PatchedClubProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchedClubProfile | PatchedClubProfile | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/club/profile/",
    }

    if isinstance(body, PatchedClubProfile):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"
    if isinstance(body, PatchedClubProfile):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ClubProfile | None:
    if response.status_code == 200:
        response_200 = ClubProfile.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ClubProfile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedClubProfile | PatchedClubProfile | Unset = UNSET,
) -> Response[Any | ClubProfile]:
    """Update club profile

    Args:
        body (PatchedClubProfile | Unset):
        body (PatchedClubProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClubProfile]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PatchedClubProfile | PatchedClubProfile | Unset = UNSET,
) -> Any | ClubProfile | None:
    """Update club profile

    Args:
        body (PatchedClubProfile | Unset):
        body (PatchedClubProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClubProfile
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedClubProfile | PatchedClubProfile | Unset = UNSET,
) -> Response[Any | ClubProfile]:
    """Update club profile

    Args:
        body (PatchedClubProfile | Unset):
        body (PatchedClubProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClubProfile]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PatchedClubProfile | PatchedClubProfile | Unset = UNSET,
) -> Any | ClubProfile | None:
    """Update club profile

    Args:
        body (PatchedClubProfile | Unset):
        body (PatchedClubProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClubProfile
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
