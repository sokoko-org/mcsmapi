import urllib.parse
from mcsmapi.pool import ApiPool
from mcsmapi.apis.file import File
from mcsmapi.apis.java import Java
from mcsmapi.apis.mod import Mod
from mcsmapi.apis.user import User
from mcsmapi.apis.image import Image
from mcsmapi.apis.daemon import Daemon
from mcsmapi.apis.instance import Instance
from mcsmapi.apis.overview import Overview
from mcsmapi.apis.schedule import Schedule
from mcsmapi.apis.upgrade import Upgrade
from mcsmapi.request import Request


class MCSMAPI:
    """MCSManager API 客户端

    支持 async context manager::

        async with MCSMAPI("http://localhost:23333") as mcsm:
            await mcsm.login("admin", "password")
            daemons = await mcsm.daemon.config()

    也可以手动管理::

        mcsm = MCSMAPI("http://localhost:23333")
        await mcsm.login("admin", "password")
        ...
        await mcsm.close()
    """

    def __init__(self, url: str, timeout: int = 5):
        split_url = urllib.parse.urlsplit(url)
        mcsm_url = urllib.parse.urljoin(
            f"{split_url.scheme}://{split_url.netloc}", ""
        )
        self._req = Request(mcsm_url, timeout)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        return False

    async def login(self, username: str, password: str):
        """
        使用账号密码登录面板。

        重复调用时，如果服务端 session 仍有效，MCSManager 会返回 `"Logined"`
        而非新 token。此时会先注销旧 session 再重新登录以获取有效 token。
        """
        result = await self._req.send(
            "POST",
            f"{ApiPool.AUTH}/login",
            data={"username": username, "password": password},
        )
        if result == "Logined":
            await self._req.send("GET", f"{ApiPool.AUTH}/logout")
            result = await self._req.send(
                "POST",
                f"{ApiPool.AUTH}/login",
                data={"username": username, "password": password},
            )
        self._req.set_token(result)
        self.authentication = "account"
        return self

    def login_with_apikey(self, apikey: str):
        """使用 API Key 认证（无需 await）"""
        self._req.set_apikey(apikey)
        self.authentication = "apikey"
        return self

    async def close(self):
        """关闭底层 HTTP 连接"""
        await self._req.close()

    @property
    def overview(self) -> Overview:
        try:
            return self._overview
        except AttributeError:
            self._overview = Overview(self._req)
            return self._overview

    @property
    def instance(self) -> Instance:
        try:
            return self._instance
        except AttributeError:
            self._instance = Instance(self._req)
            return self._instance

    @property
    def user(self) -> User:
        try:
            return self._user
        except AttributeError:
            self._user = User(self._req)
            return self._user

    @property
    def daemon(self) -> Daemon:
        try:
            return self._daemon
        except AttributeError:
            self._daemon = Daemon(self._req)
            return self._daemon

    @property
    def file(self) -> File:
        try:
            return self._file
        except AttributeError:
            self._file = File(self._req)
            return self._file

    @property
    def image(self) -> Image:
        try:
            return self._image
        except AttributeError:
            self._image = Image(self._req)
            return self._image

    @property
    def schedule(self) -> Schedule:
        try:
            return self._schedule
        except AttributeError:
            self._schedule = Schedule(self._req)
            return self._schedule

    @property
    def java(self) -> Java:
        try:
            return self._java
        except AttributeError:
            self._java = Java(self._req)
            return self._java

    @property
    def mod(self) -> Mod:
        try:
            return self._mod
        except AttributeError:
            self._mod = Mod(self._req)
            return self._mod

    @property
    def upgrade(self) -> Upgrade:
        try:
            return self._upgrade
        except AttributeError:
            self._upgrade = Upgrade(self._req)
            return self._upgrade
