from typing import Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.instance import (
    InstanceSearchList,
    InstanceDetail,
    InstanceCreateResult,
    InstanceConfig,
    batchOperationDetail,
)


class Instance:
    @staticmethod
    def search(
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
        result = send(
            "GET",
            "api/service/remote_service_instances",
            params={
                "daemonId": daemonId,
                "page": page,
                "page_size": page_size,
                "instance_name": instance_name,
                "status": status,
                "tag": tag,
            },
        )
        return InstanceSearchList(**result, daemonId=daemonId)

    @staticmethod
    def search_global(
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
        return send(
            "GET",
            "api/service/remote_services_instances_global",
            params={
                "page": page,
                "page_size": page_size,
                "instance_name": instance_name,
                "status": status,
            },
        )

    @staticmethod
    def detail(daemonId: str, uuid: str) -> InstanceDetail:
        """
        获取实例详细信息

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = send(
            "GET",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
        )
        return InstanceDetail(**result, daemonId=daemonId)

    @staticmethod
    def create(daemonId: str, config: dict[str, Any]) -> InstanceCreateResult:
        """
        创建实例

        :params daemonId: 节点的UUID
        :params config: 实例配置，缺失字段由 InstanceConfig 默认值补全
        """
        result = send(
            "POST",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data=InstanceConfig(**config).model_dump(),
        )
        return InstanceCreateResult(**result)

    @staticmethod
    def updateConfig(daemonId: str, uuid: str, config: dict[str, Any]) -> str:
        """
        更新实例配置（部分更新）

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params config: 要修改的配置字段
        """
        result = send(
            "PUT",
            ApiPool.INSTANCE,
            params={"uuid": uuid, "daemonId": daemonId},
            data=config,
        )
        return result["instanceUuid"]

    @staticmethod
    def delete(daemonId: str, uuids: list[str], deleteFile: bool = False) -> list[str]:
        """
        删除实例

        :params daemonId: 节点的UUID
        :params uuids: 实例UUID列表
        :params deleteFile: 是否删除关联文件
        """
        return send(
            "DELETE",
            ApiPool.INSTANCE,
            params={"daemonId": daemonId},
            data={"uuids": uuids, "deleteFile": deleteFile},
        )

    @staticmethod
    def start(daemonId: str, uuid: str) -> str:
        """
        启动实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/open",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def stop(daemonId: str, uuid: str) -> str:
        """
        停止实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/stop",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def restart(daemonId: str, uuid: str) -> str:
        """
        重启实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/restart",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def kill(daemonId: str, uuid: str) -> str:
        """
        强制关闭实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/kill",
            params={"daemonId": daemonId, "uuid": uuid},
        )
        return result["instanceUuid"]

    @staticmethod
    def batchOperation(
        instances: list[batchOperationDetail],
        operation: Literal["start", "stop", "restart", "kill"],
    ) -> bool:
        """
        批量操作多个实例

        :params instances: 实例信息列表
        :params operation: 操作类型
        """
        return send("POST", f"{ApiPool.INSTANCE}/multi_{operation}", data=instances)

    @staticmethod
    def update(daemonId: str, uuid: str) -> bool:
        """
        执行实例的更新任务

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        return send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/asynchronous",
            params={"daemonId": daemonId, "uuid": uuid, "task_name": "update"},
        )

    @staticmethod
    def command(daemonId: str, uuid: str, command: str) -> str:
        """
        向实例发送命令

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params command: 命令内容
        """
        result = send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/command",
            params={"daemonId": daemonId, "uuid": uuid, "command": command},
        )
        return result["instanceUuid"]

    @staticmethod
    def get_output(daemonId: str, uuid: str, size: int | None = None) -> str:
        """
        获取实例输出日志

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params size: 获取的输出大小 (1KB~2048KB)，未设置则返回全部
        """
        return send(
            "GET",
            f"{ApiPool.PROTECTED_INSTANCE}/outputlog",
            params={"daemonId": daemonId, "uuid": uuid, "size": size},
        )

    @staticmethod
    def reinstall(
        daemonId: str,
        uuid: str,
        targetUrl: str,
        title: str = "",
        description: str = "",
    ) -> bool:
        """
        重装实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params targetUrl: 重装文件URL
        :params title: 标题
        :params description: 描述
        """
        return send(
            "POST",
            f"{ApiPool.PROTECTED_INSTANCE}/install_instance",
            params={"uuid": uuid, "daemonId": daemonId},
            data={"targetUrl": targetUrl, "title": title, "description": description},
        )
