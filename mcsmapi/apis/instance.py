from __future__ import annotations
import json
from typing import TYPE_CHECKING, Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.models.instance import (
    InstanceSearchList,
    InstanceDetail,
    InstanceCreateResult,
    InstanceConfig,
    InstanceDeleteResult,
    BatchOperationDetail,
)
from mcsmapi.models.file import StreamChannelResult

if TYPE_CHECKING:
    from mcsmapi.request import Request


class Instance:
    def __init__(self, req: Request):
        self._req = req

    async def search(
        self,
        daemonId: str,
        page: int = 1,
        page_size: int = 20,
        instance_name: str = "",
        status: Literal[-1, 0, 1, 2, 3, ""] = "",
        tag: list[str] | None = None,
    ) -> InstanceSearchList:
        """
        搜索指定节点的实例

        :params daemonId: 节点的UUID
        :params page: 页码
        :params page_size: 每页大小
        :params instance_name: 实例名称过滤
        :params status: 实例状态过滤
        :params tag: 标签过滤
        """
        if tag is None:
            tag = []
        result = await self._req.send(
            "GET",
            "api/service/remote_service_instances",
            params={
                "daemonId": daemonId,
                "page": page,
                "page_size": page_size,
                "instance_name": instance_name,
                "status": status,
                "tag": json.dumps(tag),
            },
        )
        return InstanceSearchList(**result, daemonId=daemonId, _req=self._req)

    async def search_global(
        self,
        page: int = 1,
        page_size: int = 20,
        instance_name: str = "",
        status: Literal[-1, 0, 1, 2, 3, ""] = "",
    ) -> dict[str, Any]:
        """
        跨所有节点搜索实例

        :params page: 页码
        :params page_size: 每页大小
        :params instance_name: 实例名称过滤
        :params status: 实例状态过滤

        :returns: {daemonId: {instances, maxPage, page}}
        """
        return await self._req.send(
            "GET",
            "api/service/remote_services_instances_global",
            params={
                "page": page,
                "page_size": page_size,
                "instance_name": instance_name,
                "status": status,
            },
        )

    async def detail(self, daemonId: str, uuid: str) -> InstanceDetail:
        """
        获取实例详细信息

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = await self._req.send(
            "GET",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
        )
        return InstanceDetail(**result, daemonId=daemonId, _req=self._req)

    async def create(self, daemonId: str, config: dict[str, Any]) -> InstanceCreateResult:
        """
        创建实例

        :params daemonId: 节点的UUID
        :params config: 实例配置，缺失字段由 InstanceConfig 默认值补全
        """
        result = await self._req.send(
            "POST",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data=InstanceConfig(**config).model_dump(),
        )
        return InstanceCreateResult(**result)

    async def updateConfig(self, daemonId: str, uuid: str, config: dict[str, Any]) -> str:
        """
        更新实例配置（部分更新）

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params config: 要修改的配置字段
        """
        result = await self._req.send(
            "PUT",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
            data=config,
        )
        return result["instanceUuid"]

    async def delete(self, daemonId: str, uuids: list[str], deleteFile: bool = False) -> InstanceDeleteResult:
        """
        删除实例

        :params daemonId: 节点的UUID
        :params uuids: 实例UUID列表
        :params deleteFile: 是否删除关联文件
        """
        result = await self._req.send(
            "DELETE",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data={"uuids": uuids, "deleteFile": deleteFile},
        )
        return InstanceDeleteResult(**result)

    async def start(self, daemonId: str, uuid: str) -> str:
        """
        启动实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/open",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    async def stop(self, daemonId: str, uuid: str) -> str:
        """
        停止实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/stop",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    async def restart(self, daemonId: str, uuid: str) -> str:
        """
        重启实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/restart",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    async def kill(self, daemonId: str, uuid: str) -> str:
        """
        强制关闭实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/kill",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    async def batchOperation(
        self,
        instances: list[BatchOperationDetail],
        operation: Literal["start", "stop", "restart", "kill"],
    ) -> bool:
        """
        批量操作多个实例

        :params instances: 实例信息列表
        :params operation: 操作类型
        """
        return await self._req.send("POST", f"{ApiPool.INSTANCE}/multi_{operation}", data=instances)

    async def update(self, daemonId: str, uuid: str) -> bool:
        """
        执行实例的更新任务

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/asynchronous",
            params={"daemonId": daemonId, "uuid": uuid, "task_name": "update"},
        )

    async def command(self, daemonId: str, uuid: str, command: str) -> str:
        """
        向实例发送命令

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params command: 命令内容
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/command",
            params={"daemonId": daemonId, "uuid": uuid, "command": command},
        )
        return result["instanceUuid"]

    async def get_output(self, daemonId: str, uuid: str, size: int | None = None) -> str:
        """
        获取实例输出日志

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params size: 获取的输出大小 (1KB~2048KB)，未设置则返回全部
        """
        params: dict[str, Any] = {"daemonId": daemonId, "uuid": uuid}
        if size is not None:
            params["size"] = size
        return await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/outputlog",
            params=params,
        )

    async def reinstall(
        self,
        daemonId: str,
        uuid: str,
        title: str,
        description: str,
    ) -> bool:
        """
        重装实例（通过应用市场预设）

        服务端使用 title + description 匹配应用市场中的预设配置。

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params title: 预设标题（需与应用市场一致）
        :params description: 预设描述（需与应用市场一致）
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/install_instance",
            params={"uuid": uuid, "daemonId": daemonId},
            data={"title": title, "description": description},
        )


    async def quick_install_list(self) -> list[dict[str, Any]]:
        """获取应用市场快速安装列表"""
        return await self._req.send(
            "GET",
            f"{ApiPool.INSTANCE}/quick_install_list",
        )

    async def process_config_list(
        self, daemonId: str, uuid: str, files: list[str]
    ) -> list[dict[str, Any]]:
        """
        获取实例的配置文件列表

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params files: 要查询的配置文件路径列表
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/process_config/list",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"files": files},
        )

    async def process_config_get(
        self, daemonId: str, uuid: str, fileName: str, type: str = ""
    ) -> Any:
        """
        获取实例的指定配置文件内容

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params fileName: 配置文件名
        :params type: 配置文件类型
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/process_config/file",
            params={
                "daemonId": daemonId,
                "uuid": uuid,
                "fileName": fileName,
                "type": type,
            },
        )

    async def process_config_update(
        self, daemonId: str, uuid: str, fileName: str, config: Any, type: str = ""
    ) -> Any:
        """
        更新实例的指定配置文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params fileName: 配置文件名
        :params config: 新的配置内容
        :params type: 配置文件类型
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.PROTECTED_INSTANCE}/process_config/file",
            params={
                "daemonId": daemonId,
                "uuid": uuid,
                "fileName": fileName,
                "type": type,
            },
            data=config,
        )

    async def stop_asynchronous(self, daemonId: str, uuid: str, taskId: str = "") -> bool:
        """
        停止异步任务

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params taskId: 任务ID
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/stop_asynchronous",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"taskId": taskId} if taskId else {},
        )

    async def query_asynchronous(
        self, daemonId: str, uuid: str, task_name: str = "", taskId: str = ""
    ) -> Any:
        """
        查询异步任务状态

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params task_name: 任务名称
        :params taskId: 任务ID
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/query_asynchronous",
            params={"daemonId": daemonId, "uuid": uuid, "task_name": task_name},
            data={"taskId": taskId} if taskId else {},
        )

    async def stream_channel(self, daemonId: str, uuid: str) -> StreamChannelResult:
        """
        请求建立数据流通道

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = await self._req.send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/stream_channel",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return StreamChannelResult(**result)
