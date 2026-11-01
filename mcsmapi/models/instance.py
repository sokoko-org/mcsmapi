from enum import IntEnum
from typing import Any, TypedDict
from pydantic import BaseModel, field_validator
from mcsmapi.models.image import DockerConfig
from mcsmapi.models.schedule import ScheduleDetail, SchedulePostBody


class CRLFType(IntEnum):
    """换行符"""

    LF = 0
    CR = 1
    CRLF = 2


class Status(IntEnum):
    """实例状态"""

    BUSY = -1
    STOP = 0
    STOPPING = 1
    STARTING = 2
    RUNNING = 3


class batchOperationDetail(TypedDict):
    """批量操作的实例信息"""

    uuid: str
    """实例UUID"""
    daemonId: str
    """节点UUID"""


class TerminalOption(BaseModel):
    """终端选项"""

    haveColor: bool = False
    """是否启用前端颜色渲染"""
    pty: bool = True
    """是否使用伪终端 (PTY)"""
    ptyWindowCol: int = 164
    """PTY 窗口列数"""
    ptyWindowRow: int = 40
    """PTY 窗口行数"""


class EventTask(BaseModel):
    """事件任务"""

    autoStart: bool = False
    """是否自动启动"""
    autoRestart: bool = False
    """是否自动重启"""
    autoRestartMaxTimes: int = -1
    """自动重启最大次数(-1 为无限)"""
    ignore: bool = False
    """是否忽略该任务"""


class PingConfig(BaseModel):
    """服务器 Ping 配置"""

    ip: str = ""
    """服务器 IP 地址"""
    port: int = 25565
    """服务器端口"""
    type: int = 1
    """Ping 类型 (0: UDP, 1: TCP)"""


class ExtraServiceConfig(BaseModel):
    """额外服务配置"""

    openFrpTunnelId: str = ""
    """OpenFrp 隧道 ID"""
    openFrpToken: str = ""
    """OpenFrp Token"""


class ActionCommand(BaseModel):
    """操作命令"""

    name: str = ""
    """命令名称"""
    command: str = ""
    """命令内容"""


class InstanceConfig(BaseModel):
    """实例配置信息"""

    nickname: str = "New Name"
    """实例名称"""
    startCommand: str = ""
    """启动命令"""
    stopCommand: str = "^C"
    """停止命令"""
    stopTimeout: int = 0
    """停止超时时间(秒), 超时后强制终止进程"""
    cwd: str = ""
    """工作目录"""
    ie: str = "utf-8"
    """输入编码"""
    oe: str = "utf-8"
    """输出编码"""
    createDatetime: int = 0
    """创建时间 (Unix 时间戳)"""
    lastDatetime: int = 0
    """最后修改时间 (Unix 时间戳)"""
    type: str = "universal"
    """实例类型 (universal, minecraft 等)"""
    tag: list[str] = []
    """实例标签"""
    endTime: int = 0
    """实例到期时间 (Unix 时间戳, 0 为不限制)"""
    fileCode: str = "utf-8"
    """文件编码"""
    processType: str = "general"
    """进程类型 (general, docker)"""
    updateCommand: str = ""
    """更新命令"""
    actionCommandList: list[ActionCommand] = []
    """自定义操作命令列表"""
    crlf: CRLFType = CRLFType.CRLF
    """换行符"""
    docker: DockerConfig = DockerConfig()
    """Docker 相关配置"""
    enableRcon: bool = False
    """是否启用 RCON 远程控制"""
    rconPassword: str = ""
    """RCON 连接密码"""
    rconPort: int = 0
    """RCON 端口"""
    rconIp: str = ""
    """RCON IP 地址"""
    terminalOption: TerminalOption = TerminalOption()
    """终端选项配置"""
    eventTask: EventTask = EventTask()
    """事件任务配置"""
    pingConfig: PingConfig = PingConfig()
    """服务器 Ping 监测配置"""
    extraServiceConfig: ExtraServiceConfig = ExtraServiceConfig()
    """额外服务配置"""
    runAs: str = ""
    """运行该实例的系统用户，为空则使用启动面板的系统用户"""
    category: int = 0
    """分类 ID"""
    basePort: int = 0
    """分配的起始端口"""


class InstanceDetail(BaseModel):
    """实例详细信息"""

    config: InstanceConfig
    """实例的配置信息"""
    daemonId: str
    """所属的节点UUID"""
    instanceUuid: str
    """实例UUID"""
    started: int
    """实例的启动次数"""
    status: Status
    """实例状态"""

    def start(self):
        """启动该实例"""
        from mcsmapi.apis.instance import Instance

        return Instance.start(self.daemonId, self.instanceUuid)

    def stop(self):
        """停止该实例"""
        from mcsmapi.apis.instance import Instance

        return Instance.stop(self.daemonId, self.instanceUuid)

    def restart(self):
        """重启该实例"""
        from mcsmapi.apis.instance import Instance

        return Instance.restart(self.daemonId, self.instanceUuid)

    def kill(self):
        """强制关闭该实例"""
        from mcsmapi.apis.instance import Instance

        return Instance.kill(self.daemonId, self.instanceUuid)

    def delete(self, deleteFile: bool = False):
        """
        删除该实例

        :params deleteFile: 是否删除关联的文件
        """
        from mcsmapi.apis.instance import Instance

        return Instance.delete(self.daemonId, [self.instanceUuid], deleteFile)[0]

    def update(self):
        """升级实例"""
        from mcsmapi.apis.instance import Instance

        return Instance.update(self.daemonId, self.instanceUuid)

    def updateConfig(self, config: dict[str, Any]):
        """
        更新该实例配置（部分更新，只发送提供的字段）

        :params config: 要修改的配置字段
        """
        from mcsmapi.apis.instance import Instance

        return Instance.updateConfig(self.daemonId, self.instanceUuid, config)

    def reinstall(self, targetUrl: str, title: str = "", description: str = ""):
        """
        重装实例

        :params targetUrl: 重装文件的目标URL
        :params title: 重装文件的标题
        :params description: 重装文件的描述
        """
        from mcsmapi.apis.instance import Instance

        return Instance.reinstall(
            self.daemonId, self.instanceUuid, targetUrl, title, description
        )

    def command(self, command: str) -> str:
        """
        发送命令给实例

        :params command: 要发送的命令
        """
        from mcsmapi.apis.instance import Instance

        return Instance.command(self.daemonId, self.instanceUuid, command)

    def get_output(self, size: int | None = None) -> str:
        """
        获取实例的输出

        :params size: 要获取的输出大小
        """
        from mcsmapi.apis.instance import Instance

        return Instance.get_output(self.daemonId, self.instanceUuid, size)

    def files(
        self, target: str = "", page: int = 0, page_size: int = 100, file_name: str = ""
    ):
        """
        获取实例的文件列表

        :params target: 目标路径
        :params page: 页码
        :params page_size: 每页数量
        :params file_name: 文件名过滤
        """
        from mcsmapi.apis.file import File

        return File.show(
            self.daemonId, self.instanceUuid, target, page, page_size, file_name
        )

    def list_schedule(self) -> list[ScheduleDetail]:
        """获取实例的计划任务列表"""
        from mcsmapi.apis.schedule import Schedule

        return Schedule.list(self.daemonId, self.instanceUuid)

    def create_schedule(self, config: SchedulePostBody) -> bool:
        """
        创建计划任务

        :param config: 计划任务配置
        """
        from mcsmapi.apis.schedule import Schedule

        return Schedule.create(self.daemonId, self.instanceUuid, config)


class InstanceCreateResult(BaseModel):
    """实例创建结果"""

    instanceUuid: str
    """实例UUID"""
    config: InstanceConfig
    """实例的配置信息"""


class InstanceSearchList(BaseModel):
    """实例搜索列表"""

    pageSize: int = 0
    """每页的实例数量"""
    maxPage: int = 0
    """最大页数"""
    data: list[InstanceDetail] = []
    """实例详细信息列表"""
    daemonId: str = ""
    """所属的节点UUID"""

    @field_validator("data", mode="before")
    @classmethod
    def fill_daemon_id(cls, v: Any, info) -> Any:
        """在验证 data 字段前填充 daemonId"""
        if isinstance(info.data, dict):
            daemon_id = info.data.get("daemonId", "")
            if isinstance(v, list):
                for instance in v:
                    if isinstance(instance, dict):
                        instance["daemonId"] = daemon_id
        return v
