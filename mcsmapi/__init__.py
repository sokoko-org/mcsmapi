import urllib.parse
from mcsmapi.pool import ApiPool
from mcsmapi.apis.file import File
from mcsmapi.apis.user import User
from mcsmapi.apis.image import Image
from mcsmapi.apis.daemon import Daemon
from mcsmapi.apis.instance import Instance
from mcsmapi.apis.overview import Overview
from mcsmapi.apis.schedule import Schedule
from mcsmapi.request import Request


class MCSMAPI:

    def __init__(self, url: str, timeout: int = 5):
        split_url = urllib.parse.urlsplit(url)
        mcsm_url = urllib.parse.urljoin(
            f"{split_url.scheme}://{split_url.netloc}", ""
        )
        self._req = Request(mcsm_url, timeout)

    async def login(self, username: str, password: str):
        self._req.set_token(
            await self._req.send(
                "POST",
                f"{ApiPool.AUTH}/login",
                data={"username": username, "password": password},
            )
        )
        self.authentication = "account"
        return self

    def login_with_apikey(self, apikey: str):
        self._req.set_apikey(apikey)
        self.authentication = "apikey"
        return self

    async def close(self):
        """关闭底层 HTTP 连接"""
        await self._req.close()

    @property
    def overview(self):
        return Overview(self._req)

    @property
    def instance(self):
        return Instance(self._req)

    @property
    def user(self):
        return User(self._req)

    @property
    def daemon(self):
        return Daemon(self._req)

    @property
    def file(self):
        return File(self._req)

    @property
    def image(self):
        return Image(self._req)

    @property
    def schedule(self):
        return Schedule(self._req)
