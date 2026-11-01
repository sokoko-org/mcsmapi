from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal
from pydantic import BaseModel, ConfigDict, PrivateAttr
from mcsmapi.models.instance import InstanceCreateResult, InstanceDetail, InstanceDeleteResult


if TYPE_CHECKING:
    from mcsmapi.request import Request
    from mcsmapi.models.instance import InstanceSearchList


class DaemonOperation(BaseModel):
    """节点操作基类"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    _req: Any = PrivateAttr(default=None)

    uuid: str
    """节点UUID"""

    def __init__(self, _req: Request | None = None, **data: Any):
        super().__init__(**data)
        self._req = _req

    async def search_instances(
        self,
        page: int = 1,
        page_size: int = 20,
        instance_name: str = "",
        status: Literal[-1, 0, 1, 2, 3, ""] = "",
    ) -> InstanceSearchList:
        """
        搜索当前节点的实例列表

        :params page: 页码
        :params page_size: 每页大小
        :params instance_name: 实例名称过滤
        :params status: 实例状态过滤
        """
        from mcsmapi.apis.instance import Instance

        return await Instance(self._req).search(
            self.uuid, page, page_size, instance_name, status
        )

    async def detail(self, instanceUuid: str) -> InstanceDetail:
        """
        获取当前节点上指定实例的详细信息

        :params instanceUuid: 实例UUID
        """
        from mcsmapi.apis.instance import Instance

        return await Instance(self._req).detail(self.uuid, instanceUuid)

    async def delete(self):
        """删除该节点"""
        from mcsmapi.apis.daemon import Daemon

        return await Daemon(self._req).delete(self.uuid)

    async def link(self):
        """连接该节点"""
        from mcsmapi.apis.daemon import Daemon

        return await Daemon(self._req).link(self.uuid)

    async def updateConfig(self, config: dict[str, Any]) -> bool:
        """
        更新节点配置（部分更新）

        :params config: 要修改的字段
        """
        from mcsmapi.apis.daemon import Daemon

        return await Daemon(self._req).update(self.uuid, config)

    async def createInstance(self, config: dict[str, Any]) -> InstanceCreateResult:
        """
        在当前节点创建实例

        :params config: 实例配置
        """
        from mcsmapi.apis.instance import Instance

        return await Instance(self._req).create(self.uuid, config)

    async def deleteInstance(self, uuids: list[str], deleteFile=False) -> InstanceDeleteResult:
        """
        删除当前节点的实例

        :params uuids: 实例UUID列表
        :params deleteFile: 是否删除关联文件
        """
        from mcsmapi.apis.instance import Instance

        return await Instance(self._req).delete(self.uuid, uuids, deleteFile)


class DaemonConfig(BaseModel):
    """节点配置信息"""

    ip: str = "localhost"
    """远程节点 IP"""
    port: int = 24444
    """远程节点端口"""
    prefix: str = ""
    """路径前缀"""
    remarks: str = ""
    """备注"""
    apiKey: str = ""
    """API Key"""


class DaemonStatus(DaemonOperation):
    """节点状态信息"""

    available: bool
    """节点可用状态"""
    ip: str
    """节点 IP"""
    port: int
    """节点端口"""
    prefix: str
    """路径前缀"""
    remarks: str
    """备注"""


