from typing import Any
import httpx
import urllib.parse

from mcsmapi.pool import ApiPool
from .exceptions import MCSMError


class Request:
    mcsm_url: str = ""
    timeout: int = 5
    _client: httpx.AsyncClient | None = None
    apikey: str | None = None
    token: str | None = None

    @classmethod
    def _get_client(cls) -> httpx.AsyncClient:
        if cls._client is None or cls._client.is_closed:
            cls._client = httpx.AsyncClient(timeout=cls.timeout)
        return cls._client

    @classmethod
    async def close(cls):
        """关闭底层连接"""
        if cls._client is not None and not cls._client.is_closed:
            await cls._client.aclose()
            cls._client = None

    @classmethod
    def set_mcsm_url(cls, url: str):
        cls.mcsm_url = url

    @classmethod
    def set_timeout(cls, timeout: int):
        cls.timeout = timeout
        # 更新已有 client 的超时
        if cls._client is not None and not cls._client.is_closed:
            cls._client = httpx.AsyncClient(timeout=cls.timeout)

    @classmethod
    def set_apikey(cls, apikey: str):
        cls.apikey = apikey

    @classmethod
    def set_token(cls, token: str):
        cls.token = token

    @classmethod
    async def send(
        cls,
        method: str,
        endpoint: str | ApiPool,
        params: dict | None = None,
        data: Any | None = None,
    ) -> Any:
        """发送 HTTP 请求"""
        if params is None:
            params = {}
        if data is None:
            data = {}
        if isinstance(endpoint, ApiPool):
            endpoint = endpoint.value

        url = urllib.parse.urljoin(cls.mcsm_url, endpoint)
        if cls.apikey is not None:
            params["apikey"] = cls.apikey
        if cls.token is not None:
            params["token"] = cls.token

        client = cls._get_client()
        response = await client.request(
            method.upper(),
            url,
            params=params,
            json=data,
        )
        try:
            response.raise_for_status()
            return response.json()["data"]
        except httpx.HTTPStatusError as e:
            raise MCSMError(
                response.status_code, response.json().get("data", response.text)
            ) from e

    @classmethod
    async def upload(cls, url: str, file: bytes) -> bool:
        """上传文件"""
        client = cls._get_client()
        response = await client.post(
            url,
            files={"file": file},
        )
        try:
            response.raise_for_status()
            return True
        except httpx.HTTPStatusError as e:
            raise MCSMError(
                response.status_code, response.json().get("data", response.text)
            ) from e


send = Request.send
upload = Request.upload
