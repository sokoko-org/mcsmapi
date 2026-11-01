from typing import Any
from pydantic import BaseModel
from mcsmapi.models.instance import InstanceCreateResult, InstanceDetail
from mcsmapi.models.common import ProcessInfo, InstanceStat, CpuMemChart


class SystemInfo(BaseModel):
    """节点系统信息"""

    type: str
    """系统类型"""
    hostname: str
    """主机名"""
    platform: str
    """平台架构"""
    release: str
    """系统版本"""
    uptime: float
    """系统运行时间(秒)"""
    cwd: str
    """远程节点运行路径"""
    loadavg: tuple[float, float, float]
    """系统负载平均值 (1/5/15 分钟)"""
    freemem: int
    """可用内存(字节)"""
    cpuUsage: float
    """CPU 使用率"""
    memUsage: float
    """内存使用率"""
    totalmem: int
    """内存总量(字节)"""


class DaemonSetting(BaseModel):
    """节点系统配置"""

    language: str
    """节点语言"""
    uploadSpeedRate: int
    """上传速度限制(0 不限制, 限制为 n*64 KB/s)"""
    downloadSpeedRate: int
    """下载速度限制(0 不限制, 限制为 n*64 KB/s)"""
    portRangeStart: int
    """端口范围起始值"""
    portRangeEnd: int
    """端口范围结束值"""
    portAssignInterval: int
    """端口分配间隔"""
    port: int
    """节点监听端口"""
    maxDownloadFromUrlFileCount: int
    """允许同时下载的远程任务数量"""


class DaemonOperation(BaseModel):
    uuid: str
    """节点UUID"""

    async def delete(self):
        """删除该节点"""
        from mcsmapi.apis.daemon import Daemon

        return await Daemon.delete(self.uuid)

    async def link(self):
        """连接该节点"""
        from mcsmapi.apis.daemon import Daemon

        return await Daemon.link(self.uuid)

    async def updateConfig(self, config: dict[str, Any]) -> bool:
        """
        更新节点配置（部分更新）

        :params config: 要修改的字段
        """
        from mcsmapi.apis.daemon import Daemon

        return await Daemon.update(self.uuid, config)

    async def createInstance(self, config: dict[str, Any]) -> InstanceCreateResult:
        """
        在当前节点创建实例

        :params config: 实例配置
        """
        from mcsmapi.apis.instance import Instance
        from .instance import InstanceConfig

        return await Instance.create(self.uuid, InstanceConfig(**config).model_dump())

    async def deleteInstance(self, uuids: list[str], deleteFile=False) -> list[str]:
        """
        删除当前节点的实例

        :params uuids: 实例UUID列表
        :params deleteFile: 是否删除关联文件
        """
        from mcsmapi.apis.instance import Instance

        return await Instance.delete(self.uuid, uuids, deleteFile)


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


class DaemonSystemInfo(DaemonStatus):
    """节点系统信息"""

    version: str | None = None
    """节点版本"""
    process: ProcessInfo | None = None
    """进程信息"""
    instance: InstanceStat | None = None
    """实例统计"""
    system: SystemInfo | None = None
    """系统信息"""
    cpuMemChart: list[CpuMemChart] | None = None
    """CPU/内存使用趋势"""
    config: DaemonSetting | None = None
    """节点配置"""


class DaemonInfo(DaemonStatus):
    """节点信息（含实例列表）"""

    instances: list[InstanceDetail]
    """实例列表"""