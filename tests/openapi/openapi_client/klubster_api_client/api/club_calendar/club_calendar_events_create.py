from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.club_calendar_event import ClubCalendarEvent
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: ClubCalendarEvent | ClubCalendarEvent | ClubCalendarEvent | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/club-calendar/events/",
    }

    if isinstance(body, ClubCalendarEvent):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ClubCalendarEvent):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ClubCalendarEvent):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ClubCalendarEvent | None:
    if response.status_code == 201:
        response_201 = ClubCalendarEvent.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ClubCalendarEvent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ClubCalendarEvent | ClubCalendarEvent | ClubCalendarEvent | Unset = UNSET,
) -> Response[Any | ClubCalendarEvent]:
    """Create club calendar event

    Args:
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClubCalendarEvent]
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
    body: ClubCalendarEvent | ClubCalendarEvent | ClubCalendarEvent | Unset = UNSET,
) -> Any | ClubCalendarEvent | None:
    """Create club calendar event

    Args:
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClubCalendarEvent
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ClubCalendarEvent | ClubCalendarEvent | ClubCalendarEvent | Unset = UNSET,
) -> Response[Any | ClubCalendarEvent]:
    """Create club calendar event

    Args:
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClubCalendarEvent]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ClubCalendarEvent | ClubCalendarEvent | ClubCalendarEvent | Unset = UNSET,
) -> Any | ClubCalendarEvent | None:
    """Create club calendar event

    Args:
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):
        body (ClubCalendarEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClubCalendarEvent
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
