from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aktualnosci_comment import AktualnosciComment
from ...models.aktualnosci_comment_create import AktualnosciCommentCreate
from ...types import UNSET, Response


def _get_kwargs(
    thread_id: int,
    *,
    body: AktualnosciCommentCreate | AktualnosciCommentCreate | AktualnosciCommentCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/aktualnosci/threads/{thread_id}/comments/".format(
            thread_id=quote(str(thread_id), safe=""),
        ),
    }

    if isinstance(body, AktualnosciCommentCreate):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AktualnosciCommentCreate):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AktualnosciCommentCreate):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AktualnosciComment | Any | None:
    if response.status_code == 201:
        response_201 = AktualnosciComment.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AktualnosciComment | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: int,
    *,
    client: AuthenticatedClient,
    body: AktualnosciCommentCreate | AktualnosciCommentCreate | AktualnosciCommentCreate | Unset = UNSET,
) -> Response[AktualnosciComment | Any]:
    """Add thread comment

    Args:
        thread_id (int):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AktualnosciComment | Any]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: int,
    *,
    client: AuthenticatedClient,
    body: AktualnosciCommentCreate | AktualnosciCommentCreate | AktualnosciCommentCreate | Unset = UNSET,
) -> AktualnosciComment | Any | None:
    """Add thread comment

    Args:
        thread_id (int):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AktualnosciComment | Any
    """

    return sync_detailed(
        thread_id=thread_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    thread_id: int,
    *,
    client: AuthenticatedClient,
    body: AktualnosciCommentCreate | AktualnosciCommentCreate | AktualnosciCommentCreate | Unset = UNSET,
) -> Response[AktualnosciComment | Any]:
    """Add thread comment

    Args:
        thread_id (int):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AktualnosciComment | Any]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: int,
    *,
    client: AuthenticatedClient,
    body: AktualnosciCommentCreate | AktualnosciCommentCreate | AktualnosciCommentCreate | Unset = UNSET,
) -> AktualnosciComment | Any | None:
    """Add thread comment

    Args:
        thread_id (int):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):
        body (AktualnosciCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AktualnosciComment | Any
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            client=client,
            body=body,
        )
    ).parsed
