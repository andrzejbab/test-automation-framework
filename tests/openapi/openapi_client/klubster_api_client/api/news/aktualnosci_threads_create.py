from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aktualnosci_thread import AktualnosciThread
from ...models.aktualnosci_thread_update import AktualnosciThreadUpdate
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: AktualnosciThreadUpdate | AktualnosciThreadUpdate | AktualnosciThreadUpdate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/aktualnosci/threads/",
    }

    if isinstance(body, AktualnosciThreadUpdate):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AktualnosciThreadUpdate):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AktualnosciThreadUpdate):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AktualnosciThread | Any | None:
    if response.status_code == 201:
        response_201 = AktualnosciThread.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AktualnosciThread | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AktualnosciThreadUpdate | AktualnosciThreadUpdate | AktualnosciThreadUpdate | Unset = UNSET,
) -> Response[AktualnosciThread | Any]:
    """Create thread

    Args:
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AktualnosciThread | Any]
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
    body: AktualnosciThreadUpdate | AktualnosciThreadUpdate | AktualnosciThreadUpdate | Unset = UNSET,
) -> AktualnosciThread | Any | None:
    """Create thread

    Args:
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AktualnosciThread | Any
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AktualnosciThreadUpdate | AktualnosciThreadUpdate | AktualnosciThreadUpdate | Unset = UNSET,
) -> Response[AktualnosciThread | Any]:
    """Create thread

    Args:
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AktualnosciThread | Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AktualnosciThreadUpdate | AktualnosciThreadUpdate | AktualnosciThreadUpdate | Unset = UNSET,
) -> AktualnosciThread | Any | None:
    """Create thread

    Args:
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):
        body (AktualnosciThreadUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AktualnosciThread | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
