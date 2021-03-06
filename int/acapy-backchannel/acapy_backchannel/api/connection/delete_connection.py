from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.connection_module_response import ConnectionModuleResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    conn_id: str,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ConnectionModuleResponse]:
    if response.status_code == 200:
        response_200 = ConnectionModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnectionModuleResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    conn_id: str,
) -> Response[ConnectionModuleResponse]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    conn_id: str,
) -> Optional[ConnectionModuleResponse]:
    """ """

    return sync_detailed(
        client=client,
        conn_id=conn_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: str,
) -> Response[ConnectionModuleResponse]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    conn_id: str,
) -> Optional[ConnectionModuleResponse]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            conn_id=conn_id,
        )
    ).parsed
