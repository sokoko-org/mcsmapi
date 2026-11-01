from __future__ import annotations
from typing import TYPE_CHECKING
from mcsmapi.pool import ApiPool
from mcsmapi.models.upgrade import UpgradeInfo, UpgradeResult

if TYPE_CHECKING:
    from mcsmapi.request import Request


class Upgrade:
    def __init__(self, req: Request):
        self._req = req

    async def panel_info(self) -> UpgradeInfo:
        """
        获取面板版本与更新信息（仅管理员）
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.UPGRADE}/panel_info",
        )
        return UpgradeInfo(**result)

    async def panel(self) -> UpgradeResult:
        """
        触发面板自身更新（仅管理员）
        """
        result = await self._req.send(
            "POST",
            f"{ApiPool.UPGRADE}/panel",
        )
        return UpgradeResult(**result)

    async def daemon_info(self, uuid: str) -> UpgradeInfo:
        """
        获取节点更新信息（仅管理员）

        :param uuid: 节点UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.UPGRADE}/daemon_info",
            params={"uuid": uuid},
        )
        return UpgradeInfo(**result)

    async def daemon(self, uuid: str) -> UpgradeResult:
        """
        触发节点自身更新（仅管理员）

        :param uuid: 节点UUID
        """
        result = await self._req.send(
            "POST",
            f"{ApiPool.UPGRADE}/daemon",
            params={"uuid": uuid},
        )
        return UpgradeResult(**result)
