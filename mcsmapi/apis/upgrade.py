from __future__ import annotations
from typing import TYPE_CHECKING, Any
from mcsmapi.pool import ApiPool

if TYPE_CHECKING:
    from mcsmapi.request import Request


class Upgrade:
    def __init__(self, req: Request):
        self._req = req

    async def panel_info(self) -> Any:
        """
        获取面板版本与更新信息（仅管理员）
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.UPGRADE}/panel_info",
        )

    async def panel(self) -> Any:
        """
        触发面板自身更新（仅管理员）
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.UPGRADE}/panel",
        )

    async def daemon_info(self, uuid: str) -> Any:
        """
        获取节点更新信息（仅管理员）

        :param uuid: 节点UUID
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.UPGRADE}/daemon_info",
            params={"uuid": uuid},
        )

    async def daemon(self, uuid: str) -> Any:
        """
        触发节点自身更新（仅管理员）

        :param uuid: 节点UUID
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.UPGRADE}/daemon",
            params={"uuid": uuid},
        )
