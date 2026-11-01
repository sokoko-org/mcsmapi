from __future__ import annotations
from typing import TYPE_CHECKING, Any
from mcsmapi.pool import ApiPool
from mcsmapi.models.daemon import (
    DaemonConfig,
    DaemonStatus,
)

if TYPE_CHECKING:
    from mcsmapi.request import Request


class Daemon:
    def __init__(self, req: Request):
        self._req = req

    async def config(self) -> list[DaemonStatus]:
        """获取全部节点配置信息"""
        daemons = await self._req.send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_list",
        )
        return [DaemonStatus(**daemon, _req=self._req) for daemon in daemons]



    async def add(self, config: DaemonConfig) -> str:
        """
        新增节点

        :params config: 节点配置信息
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.SERVICE}/remote_service",
            data=config.model_dump(),
        )

    async def delete(self, daemonId: str) -> bool:
        """
        删除节点

        :params daemonId: 节点的UUID
        """
        return await self._req.send(
            "DELETE", f"{ApiPool.SERVICE}/remote_service", params={"uuid": daemonId}
        )

    async def link(self, daemonId: str) -> bool:
        """
        连接节点

        :params daemonId: 节点的UUID
        """
        return await self._req.send(
            "GET", f"{ApiPool.SERVICE}/link_remote_service", params={"uuid": daemonId}
        )

    async def update(self, daemonId: str, config: dict[str, Any]) -> bool:
        """
        更新节点配置（部分更新）

        :params daemonId: 节点的UUID
        :params config: 要修改的配置字段
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.SERVICE}/remote_service",
            params={"uuid": daemonId},
            data=config,
        )
