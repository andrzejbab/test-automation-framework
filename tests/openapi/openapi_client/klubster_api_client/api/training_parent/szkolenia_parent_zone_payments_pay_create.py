from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.parent_training_payment import ParentTrainingPayment
from ...models.szkolenia_parent_zone_payments_pay_create_body import SzkoleniaParentZonePaymentsPayCreateBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    payment_id: int,
    *,
    body: SzkoleniaParentZonePaymentsPayCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/szkolenia/parent-zone/payments/{payment_id}/pay/".format(
            payment_id=quote(str(payment_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ParentTrainingPayment | None:
    if response.status_code == 200:
        response_200 = ParentTrainingPayment.from_dict(response.json())

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
) -> Response[Any | ParentTrainingPayment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    payment_id: int,
    *,
    client: AuthenticatedClient,
    body: SzkoleniaParentZonePaymentsPayCreateBody | Unset = UNSET,
) -> Response[Any | ParentTrainingPayment]:
    """Pay single training payment

    Args:
        payment_id (int):
        body (SzkoleniaParentZonePaymentsPayCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ParentTrainingPayment]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    payment_id: int,
    *,
    client: AuthenticatedClient,
    body: SzkoleniaParentZonePaymentsPayCreateBody | Unset = UNSET,
) -> Any | ParentTrainingPayment | None:
    """Pay single training payment

    Args:
        payment_id (int):
        body (SzkoleniaParentZonePaymentsPayCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ParentTrainingPayment
    """

    return sync_detailed(
        payment_id=payment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    payment_id: int,
    *,
    client: AuthenticatedClient,
    body: SzkoleniaParentZonePaymentsPayCreateBody | Unset = UNSET,
) -> Response[Any | ParentTrainingPayment]:
    """Pay single training payment

    Args:
        payment_id (int):
        body (SzkoleniaParentZonePaymentsPayCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ParentTrainingPayment]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    payment_id: int,
    *,
    client: AuthenticatedClient,
    body: SzkoleniaParentZonePaymentsPayCreateBody | Unset = UNSET,
) -> Any | ParentTrainingPayment | None:
    """Pay single training payment

    Args:
        payment_id (int):
        body (SzkoleniaParentZonePaymentsPayCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ParentTrainingPayment
    """

    return (
        await asyncio_detailed(
            payment_id=payment_id,
            client=client,
            body=body,
        )
    ).parsed
