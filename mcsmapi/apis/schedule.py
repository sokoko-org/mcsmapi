from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.schedule import ScheduleDetail, SchedulePostBody


class Schedule:

    @staticmethod
    async def list(daemonId: str, uuid: str) -> list[ScheduleDetail]:
        """
        获取实例计划任务列表

        :param daemonId: 节点ID
        :param uuid: 实例ID
        """
        result = await send(
            "GET",
            f"{ApiPool.SCHEDULE}",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return [ScheduleDetail(**r, daemonId=daemonId) for r in result]

    @staticmethod
    async def delete(daemonId: str, uuid: str, task_name: str) -> bool:
        """
        删除计划任务

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param task_name: 计划任务名称
        """
        return await send(
            "DELETE",
            f"{ApiPool.SCHEDULE}",
            params={"daemonId": daemonId, "uuid": uuid, "task_name": task_name},
        )

    @staticmethod
    async def create(daemonId: str, uuid: str, config: SchedulePostBody) -> bool:
        """
        创建计划任务

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param config: 计划任务配置
        """
        return await send(
            "POST",
            f"{ApiPool.SCHEDULE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data=config.model_dump(),
        )