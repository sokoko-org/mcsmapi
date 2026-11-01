from enum import Enum
from typing import Literal
from pydantic import BaseModel
from mcsmapi.models.common import CpuMemChart, InstanceStat, ProcessInfo



class SystemUser(BaseModel):
    """系统用户信息"""

    uid: int
    """用户 ID"""
    gid: int
    """用户组 ID"""
    username: str
    """用户名"""
    homedir: str
    """主目录"""
    shell: str | None
    """默认 Shell"""


class SystemInfo(BaseModel):
    """系统信息"""

    user: SystemUser
    """当前登录用户"""
    time: int
    """系统当前时间 (Unix 时间戳)"""
    totalmem: int
    """总内存(字节)"""
    freemem: int
    """空闲内存(字节)"""
    type: str
    """操作系统类型"""
    version: str
    """操作系统版本"""
    node: str
    """NodeJS 版本"""
    hostname: str
    """主机名"""
    loadavg: tuple[float, float, float]
    """系统负载平均值 (1/5/15 分钟)"""
    platform: str
    """操作系统平台"""
    release: str
    """系统发行版本"""
    uptime: float
    """系统运行时间(秒)"""
    cpu: float
    """CPU 使用率(%)"""


class RecordInfo(BaseModel):
    """安全记录"""

    logined: int
    """登录成功次数"""
    illegalAccess: int
    """非法访问次数"""
    banips: int
    """被封禁 IP 数量"""
    loginFailed: int
    """登录失败次数"""


class RequestChart(BaseModel):
    """请求量趋势"""

    value: int
    """接口请求量"""
    totalInstance: int
    """总实例数"""
    runningInstance: int
    """运行中实例数"""


class ChartInfo(BaseModel):
    """图表数据"""

    system: list[CpuMemChart]
    """系统资源使用趋势"""
    request: list[RequestChart]
    """请求量趋势"""


class RemoteCountInfo(BaseModel):
    """远程节点统计"""

    total: int
    """节点总数"""
    available: int
    """可用节点数"""


class OverviewRemoteSetting(BaseModel):
    """概览中的节点配置"""

    language: str = ""
    """节点语言"""
    uploadSpeedRate: int = 0
    """上传速度限制"""
    downloadSpeedRate: int = 0
    """下载速度限制"""
    portRangeStart: int = 0
    """端口范围起始"""
    portRangeEnd: int = 0
    """端口范围结束"""
    portAssignInterval: int = 0
    """端口分配间隔"""
    port: int = 0
    """节点端口"""
    maxDownloadFromUrlFileCount: int = 0
    """允许同时下载的远程任务数"""


class OverviewRemoteSystem(BaseModel):
    """概览中的节点系统信息"""

    type: str = ""
    """系统类型"""
    hostname: str = ""
    """主机名"""
    platform: str = ""
    """平台"""
    release: str = ""
    """系统版本"""
    uptime: float = 0
    """运行时间（秒）"""
    cwd: str = ""
    """工作路径"""
    loadavg: tuple[float, float, float] = (0, 0, 0)
    """负载平均值"""
    freemem: int = 0
    """空闲内存（字节）"""
    cpuUsage: float = 0
    """CPU 使用率"""
    memUsage: float = 0
    """内存使用率"""
    totalmem: int = 0
    """内存总量（字节）"""


class OverviewRemote(BaseModel):
    """概览中的远程节点信息"""

    uuid: str = ""
    """节点UUID"""
    ip: str = ""
    """节点 IP"""
    port: int = 0
    """节点端口"""
    prefix: str = ""
    """路径前缀"""
    available: bool = False
    """节点可用状态"""
    remarks: str = ""
    """备注"""
    version: str | None = None
    """节点版本"""
    process: ProcessInfo | None = None
    """进程信息"""
    instance: InstanceStat | None = None
    """实例统计"""
    system: OverviewRemoteSystem | None = None
    """系统信息"""
    cpuMemChart: list[CpuMemChart] | None = None
    """CPU/内存使用趋势"""
    config: OverviewRemoteSetting | None = None
    """节点配置"""
    remoteMappings: list | None = None
    """远程端口映射"""


class OverviewModel(BaseModel):
    """系统概览"""

    version: str
    """面板版本"""
    specifiedDaemonVersion: str
    """指定的节点版本"""
    system: SystemInfo
    """系统信息"""
    record: RecordInfo
    """安全记录"""
    process: ProcessInfo
    """进程状态"""
    chart: ChartInfo
    """图表数据"""
    remoteCount: RemoteCountInfo
    """远程节点统计"""
    remote: list[OverviewRemote]
    """远程节点详细信息"""


class LogType(Enum):
    """操作类型"""

    # 系统
    SYSTEM_CONFIG_CHANGE = "system_config_change"
    """系统配置修改"""

    # 用户
    USER_LOGIN = "user_login"
    """用户登录"""
    USER_CONFIG_CHANGE = "user_config_change"
    """修改用户配置"""
    USER_DELETE = "user_delete"
    """删除用户"""
    USER_CREATE = "user_create"
    """创建用户"""
    USER_APIKEY_CHANGE = "user_apikey_change"
    """修改用户 API Key"""

    # 节点
    DAEMON_CONFIG_CHANGE = "daemon_config_change"
    """修改节点配置"""
    DAEMON_REMOVE = "daemon_remove"
    """删除节点"""
    DAEMON_CREATE = "daemon_create"
    """创建节点"""

    # 实例计划任务
    INSTANCE_TASK_DELETE = "instance_task_delete"
    """删除计划任务"""
    INSTANCE_TASK_CREATE = "instance_task_create"
    """创建计划任务"""

    # 实例文件
    INSTANCE_FILE_DELETE = "instance_file_delete"
    """删除文件"""
    INSTANCE_FILE_DOWNLOAD = "instance_file_download"
    """下载文件"""
    INSTANCE_FILE_UPDATE = "instance_file_update"
    """更新文件"""
    INSTANCE_FILE_UPLOAD = "instance_file_upload"
    """上传文件"""
    INSTANCE_FILE_COMPRESS = "instance_file_compress"
    """压缩文件"""
    INSTANCE_FILE_DECOMPRESS = "instance_file_decompress"
    """解压文件"""
    INSTANCE_FILE_MOVE = "instance_file_move"
    """移动文件"""
    INSTANCE_FILE_RENAME = "instance_file_rename"
    """重命名文件"""
    INSTANCE_FILE_DOWNLOAD_FROM_URL = "instance_file_download_from_url"
    """从 URL 下载文件到实例"""

    # 实例操作
    INSTANCE_DELETE = "instance_delete"
    """删除实例"""
    INSTANCE_CREATE = "instance_create"
    """创建实例"""
    INSTANCE_CONFIG_CHANGE = "instance_config_change"
    """修改实例配置"""
    INSTANCE_KILL = "instance_kill"
    """强制停止实例"""
    INSTANCE_UPDATE = "instance_update"
    """更新实例"""
    INSTANCE_RESTART = "instance_restart"
    """重启实例"""
    INSTANCE_STOP = "instance_stop"
    """停止实例"""
    INSTANCE_START = "instance_start"
    """启动实例"""

    # SSO
    SSO_AUTH_FAILED = "sso_auth_failed"
    """SSO 认证失败"""
    SSO_BIND = "sso_bind"
    """SSO 绑定"""
    SSO_BIND_CURRENT = "sso_bind_current"
    """SSO 绑定当前用户"""
    SSO_UNBIND = "sso_unbind"
    """SSO 解绑"""


class LogDetail(BaseModel):
    """操作日志详情"""

    operation_id: str
    """操作者UUID"""
    operator_name: str | None = None
    """操作者用户名"""
    operation_time: str
    """操作时间戳"""
    operator_ip: str
    """操作者IP"""
    operation_level: Literal["info", "warning", "error", "unknown"]
    """日志等级"""
    type: LogType
    """操作类型"""
    instance_name: str | None = None
    """实例名称"""
    instance_id: str | None = None
    """实例ID"""
    daemon_id: str | None = None
    """节点ID"""
    login_result: bool | None = None
    """登录结果"""
    file: list[str] | str | None = None
    """被操作的文件"""
    task_name: str | None = None
    """任务名称"""
