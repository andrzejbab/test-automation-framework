from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.club_photo import ClubPhoto
from ...models.patched_club_photo import PatchedClubPhoto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    photo_id: int,
    *,
    body: PatchedClubPhoto | PatchedClubPhoto | PatchedClubPhoto | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/club/profile/photos/{photo_id}/".format(
            photo_id=quote(str(photo_id), safe=""),
        ),
    }

    if isinstance(body, PatchedClubPhoto):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedClubPhoto):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedClubPhoto):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ClubPhoto | None:
    if response.status_code == 200:
        response_200 = ClubPhoto.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ClubPhoto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    photo_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedClubPhoto | PatchedClubPhoto | PatchedClubPhoto | Unset = UNSET,
) -> Response[Any | ClubPhoto]:
    """Update club photo

    Args:
        photo_id (int):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClubPhoto]
    """

    kwargs = _get_kwargs(
        photo_id=photo_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    photo_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedClubPhoto | PatchedClubPhoto | PatchedClubPhoto | Unset = UNSET,
) -> Any | ClubPhoto | None:
    """Update club photo

    Args:
        photo_id (int):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClubPhoto
    """

    return sync_detailed(
        photo_id=photo_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    photo_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedClubPhoto | PatchedClubPhoto | PatchedClubPhoto | Unset = UNSET,
) -> Response[Any | ClubPhoto]:
    """Update club photo

    Args:
        photo_id (int):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClubPhoto]
    """

    kwargs = _get_kwargs(
        photo_id=photo_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    photo_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedClubPhoto | PatchedClubPhoto | PatchedClubPhoto | Unset = UNSET,
) -> Any | ClubPhoto | None:
    """Update club photo

    Args:
        photo_id (int):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):
        body (PatchedClubPhoto | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClubPhoto
    """

    return (
        await asyncio_detailed(
            photo_id=photo_id,
            client=client,
            body=body,
        )
    ).parsed
