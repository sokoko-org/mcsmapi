from __future__ import annotations
from typing import TYPE_CHECKING
from mcsmapi.pool import ApiPool
from mcsmapi.models.java import JavaRuntime

if TYPE_CHECKING:
    from mcsmapi.request import Request


class Java:
    def __init__(self, req: Request):
        self._req = req

    async def list(self, daemonId: str, instanceId: str) -> list[JavaRuntime]:
        """
        获取 Java 运行环境列表

        :param daemonId: 节点ID
        :param instanceId: 实例ID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.JAVA}/list",
            params={"daemonId": daemonId, "instanceId": instanceId},
        )
        return [JavaRuntime(**item) for item in result]

    async def add(self, daemonId: str, name: str, path: str) -> bool:
        """
        新增 Java 运行环境（仅管理员）

        :param daemonId: 节点ID
        :param name: Java 名称
        :param path: Java 路径
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.JAVA}/add",
            params={"daemonId": daemonId},
            data={"name": name, "path": path},
        )

    async def download(
        self, daemonId: str, instanceId: str, name: str, version: str
    ) -> bool:
        """
        下载 Java 运行环境（仅管理员）

        :param daemonId: 节点ID
        :param instanceId: 实例ID
        :param name: Java 名称
        :param version: Java 版本
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.JAVA}/download",
            params={"daemonId": daemonId, "instanceId": instanceId},
            data={"name": name, "version": version},
        )

    async def using(self, daemonId: str, instanceId: str, id: str) -> bool:
        """
        设置实例使用的 Java 运行环境

        :param daemonId: 节点ID
        :param instanceId: 实例ID
        :param id: Java 运行环境 ID
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.JAVA}/using",
            params={"daemonId": daemonId, "instanceId": instanceId},
            data={"id": id},
        )

    async def delete(self, daemonId: str, id: str) -> bool:
        """
        删除 Java 运行环境（仅管理员）

        :param daemonId: 节点ID
        :param id: Java 运行环境 ID
        """
        return await self._req.send(
            "DELETE",
            f"{ApiPool.JAVA}/delete",
            params={"daemonId": daemonId},
            data={"id": id},
        )
