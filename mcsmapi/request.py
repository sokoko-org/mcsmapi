from typing import Any
import httpx

from .exceptions import MCSMError


class Request:
    def __init__(self, mcsm_url: str = "", timeout: int = 5):
        self.mcsm_url = mcsm_url
        self.timeout = timeout
        self._client: httpx.AsyncClient | None = None
        self.apikey: str | None = None
        self.token: str | None = None

    def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self.mcsm_url,
                timeout=self.timeout,
                headers={"X-Requested-With": "XMLHttpRequest"},
            )
        return self._client

    async def close(self):
        """关闭底层连接"""
        if self._client is not None and not self._client.is_closed:
            await self._client.aclose()
            self._client = None

    async def set_timeout(self, timeout: int):
        """设置超时并重建连接"""
        self.timeout = timeout
        await self.close()

    def set_apikey(self, apikey: str):
        self.apikey = apikey

    def set_token(self, token: str):
        self.token = token

    async def send(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        data: Any = None,
    ) -> Any:
        """发送 HTTP 请求"""
        if params is None:
            params = {}
        if self.apikey is not None:
            params["apikey"] = self.apikey
        if self.token is not None:
            params["token"] = self.token

        client = self._get_client()
        kwargs: dict[str, Any] = {"params": params}
        if data is not None:
            kwargs["json"] = data

        response = await client.request(method, endpoint, **kwargs)
        try:
            response.raise_for_status()
            return response.json()["data"]
        except httpx.HTTPStatusError as e:
            raise MCSMError(
                response.status_code, response.json().get("data", response.text)
            ) from e

    async def upload(self, url: str, file: bytes) -> bool:
        """上传文件（使用绝对 URL）"""
        client = self._get_client()
        response = await client.post(url, files={"file": file})
        try:
            response.raise_for_status()
            return True
        except httpx.HTTPStatusError as e:
            raise MCSMError(
                response.status_code, response.json().get("data", response.text)
            ) from e
