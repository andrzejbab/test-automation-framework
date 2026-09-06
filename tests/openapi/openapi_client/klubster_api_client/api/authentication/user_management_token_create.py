from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_management_token_create_body import UserManagementTokenCreateBody
from ...models.user_management_token_create_response_200 import UserManagementTokenCreateResponse200
from ...models.user_management_token_create_response_401 import UserManagementTokenCreateResponse401
from ...models.user_management_token_create_response_500 import UserManagementTokenCreateResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserManagementTokenCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/user_management/token/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UserManagementTokenCreateResponse200
    | UserManagementTokenCreateResponse401
    | UserManagementTokenCreateResponse500
    | None
):
    if response.status_code == 200:
        response_200 = UserManagementTokenCreateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UserManagementTokenCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = UserManagementTokenCreateResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UserManagementTokenCreateResponse200 | UserManagementTokenCreateResponse401 | UserManagementTokenCreateResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserManagementTokenCreateBody | Unset = UNSET,
) -> Response[
    UserManagementTokenCreateResponse200 | UserManagementTokenCreateResponse401 | UserManagementTokenCreateResponse500
]:
    """Obtain JWT token pair

     Authenticate user and return JWT access and refresh tokens.

    Args:
        body (UserManagementTokenCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserManagementTokenCreateResponse200 | UserManagementTokenCreateResponse401 | UserManagementTokenCreateResponse500]
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
    client: AuthenticatedClient | Client,
    body: UserManagementTokenCreateBody | Unset = UNSET,
) -> (
    UserManagementTokenCreateResponse200
    | UserManagementTokenCreateResponse401
    | UserManagementTokenCreateResponse500
    | None
):
    """Obtain JWT token pair

     Authenticate user and return JWT access and refresh tokens.

    Args:
        body (UserManagementTokenCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserManagementTokenCreateResponse200 | UserManagementTokenCreateResponse401 | UserManagementTokenCreateResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserManagementTokenCreateBody | Unset = UNSET,
) -> Response[
    UserManagementTokenCreateResponse200 | UserManagementTokenCreateResponse401 | UserManagementTokenCreateResponse500
]:
    """Obtain JWT token pair

     Authenticate user and return JWT access and refresh tokens.

    Args:
        body (UserManagementTokenCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserManagementTokenCreateResponse200 | UserManagementTokenCreateResponse401 | UserManagementTokenCreateResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserManagementTokenCreateBody | Unset = UNSET,
) -> (
    UserManagementTokenCreateResponse200
    | UserManagementTokenCreateResponse401
    | UserManagementTokenCreateResponse500
    | None
):
    """Obtain JWT token pair

     Authenticate user and return JWT access and refresh tokens.

    Args:
        body (UserManagementTokenCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserManagementTokenCreateResponse200 | UserManagementTokenCreateResponse401 | UserManagementTokenCreateResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
