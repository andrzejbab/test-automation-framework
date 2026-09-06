from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sport_object_reservation import SportObjectReservation
from ...models.sports_reservations_create_body import SportsReservationsCreateBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SportsReservationsCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/sports-reservations/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SportObjectReservation | None:
    if response.status_code == 201:
        response_201 = SportObjectReservation.from_dict(response.json())

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
) -> Response[Any | SportObjectReservation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SportsReservationsCreateBody | Unset = UNSET,
) -> Response[Any | SportObjectReservation]:
    """Create sport object reservation

     Creates a reservation in current user club. Optional send_confirmation_email flag controls
    notification sending.

    Args:
        body (SportsReservationsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SportObjectReservation]
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
    body: SportsReservationsCreateBody | Unset = UNSET,
) -> Any | SportObjectReservation | None:
    """Create sport object reservation

     Creates a reservation in current user club. Optional send_confirmation_email flag controls
    notification sending.

    Args:
        body (SportsReservationsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SportObjectReservation
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SportsReservationsCreateBody | Unset = UNSET,
) -> Response[Any | SportObjectReservation]:
    """Create sport object reservation

     Creates a reservation in current user club. Optional send_confirmation_email flag controls
    notification sending.

    Args:
        body (SportsReservationsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SportObjectReservation]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SportsReservationsCreateBody | Unset = UNSET,
) -> Any | SportObjectReservation | None:
    """Create sport object reservation

     Creates a reservation in current user club. Optional send_confirmation_email flag controls
    notification sending.

    Args:
        body (SportsReservationsCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SportObjectReservation
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
