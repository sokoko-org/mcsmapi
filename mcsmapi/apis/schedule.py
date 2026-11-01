from __future__ import annotations
from typing import TYPE_CHECKING
from mcsmapi.pool import ApiPool
from mcsmapi.models.schedule import ScheduleDetail, SchedulePostBody

if TYPE_CHECKING:
    from mcsmapi.request import Request


class Schedule:
    def __init__(self, req: Request):
        self._req = req

    async def list(self, daemonId: str, uuid: str) -> list[ScheduleDetail]:
        """
        获取实例计划任务列表

        :param daemonId: 节点ID
        :param uuid: 实例ID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.SCHEDULE}",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return [ScheduleDetail(**r, daemonId=daemonId, _req=self._req) for r in result]

    async def delete(self, daemonId: str, uuid: str, task_name: str) -> bool:
        """
        删除计划任务

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param task_name: 计划任务名称
        """
        return await self._req.send(
            "DELETE",
            f"{ApiPool.SCHEDULE}",
            params={"daemonId": daemonId, "uuid": uuid, "task_name": task_name},
        )

    async def create(self, daemonId: str, uuid: str, config: SchedulePostBody) -> bool:
        """
        创建计划任务

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param config: 计划任务配置
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.SCHEDULE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data=config.model_dump(),
        )
