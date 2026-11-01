# 实例模型

## _class_ `CRLFType(IntEnum)`

换行符

| 枚举项 | 枚举值 | 描述 |
| --- | --- | --- |
| `LF` | 0 | LF |
| `CR` | 1 | CR |
| `CRLF` | 2 | CRLF |

## _class_ `Status(IntEnum)`

实例状态

| 枚举项 | 枚举值 | 描述 |
| --- | --- | --- |
| `BUSY` | -1 | 维护中 |
| `STOP` | 0 | 未运行 |
| `STOPPING` | 1 | 停止中 |
| `STARTING` | 2 | 启动中 |
| `RUNNING` | 3 | 正在运行 |

## _class_ `BatchOperationDetail(TypedDict)`

批量操作的实例信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | str | 实例 UUID |
| `daemonId` | str | 节点 UUID |

## _class_ `TerminalOption(BaseModel)`

终端选项

| 字段名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `haveColor` | bool | False | 是否启用前端颜色渲染 |
| `pty` | bool | True | 是否使用伪终端 (PTY) |
| `ptyWindowCol` | int | 164 | PTY 窗口列数 |
| `ptyWindowRow` | int | 40 | PTY 窗口行数 |

## _class_ `EventTask(BaseModel)`

事件任务

| 字段名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `autoStart` | bool | False | 是否自动启动 |
| `autoRestart` | bool | False | 是否自动重启 |
| `autoRestartMaxTimes` | int | -1 | 自动重启最大次数 (-1 无限) |
| `ignore` | bool | False | 是否忽略 |

## _class_ `PingConfig(BaseModel)`

服务器 Ping 配置

| 字段名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `ip` | str | "" | 服务器 IP |
| `port` | int | 25565 | 端口 |
| `type` | int | 1 | Ping 类型 (0: UDP, 1: TCP) |

## _class_ `ExtraServiceConfig(BaseModel)`

额外服务配置

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `openFrpTunnelId` | str | OpenFrp 隧道 ID |
| `openFrpToken` | str | OpenFrp Token |

## _class_ `ActionCommand(BaseModel)`

操作命令

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `name` | str | 命令名称 |
| `command` | str | 命令内容 |

## _class_ `JavaConfig(BaseModel)`

Java 配置

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | str | Java 路径 ID |

## _class_ `InstanceConfig(BaseModel)`

实例配置信息

| 字段名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `nickname` | str | "Undefined" | 实例名称 |
| `startCommand` | str | "" | 启动命令 |
| `stopCommand` | str | "^C" | 停止命令 |
| `stopTimeout` | int | 0 | 停止超时时间(秒) |
| `cwd` | str | "" | 工作目录 |
| `ie` | str | "utf-8" | 输入编码 |
| `oe` | str | "utf-8" | 输出编码 |
| `createDatetime` | int | 0 | 创建时间 (Unix 时间戳) |
| `lastDatetime` | int | 0 | 最后修改时间 |
| `type` | str | "universal" | 实例类型 |
| `tag` | list[str] | [] | 实例标签 |
| `endTime` | int | 0 | 到期时间 (0 为不限制) |
| `fileCode` | str | "utf-8" | 文件编码 |
| `processType` | str | "general" | 进程类型 (general, docker) |
| `updateCommand` | str | "" | 更新命令 |
| `actionCommandList` | list[ActionCommand] | [] | 自定义操作命令列表 |
| `crlf` | CRLFType | CRLF | 换行符 |
| `docker` | DockerConfig | DockerConfig() | Docker 配置 |
| `enableRcon` | bool | False | 是否启用 RCON |
| `rconPassword` | str | "" | RCON 密码 |
| `rconPort` | int | 0 | RCON 端口 |
| `rconIp` | str | "" | RCON IP |
| `terminalOption` | TerminalOption | TerminalOption() | 终端选项 |
| `eventTask` | EventTask | EventTask() | 事件任务 |
| `pingConfig` | PingConfig | PingConfig() | Ping 配置 |
| `extraServiceConfig` | ExtraServiceConfig | ExtraServiceConfig() | 额外服务配置 |
| `runAs` | str | "" | 运行用户 |
| `category` | int | 0 | 分类 ID |
| `basePort` | int | 0 | 起始端口 |
| `java` | JavaConfig | JavaConfig() | Java 配置 |

## _class_ `InstanceDetail(BaseModel)`

实例详细信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `config` | InstanceConfig | 实例的配置信息 |
| `daemonId` | str | 所属的节点 UUID |
| `instanceUuid` | str | 实例 UUID |
| `started` | int | 启动次数 |
| `status` | Status | 实例状态 |

### 链式操作方法

所有方法均为 `async`，需要 `await` 调用。

| 方法 | 参数 | 返回 | 描述 |
| --- | --- | --- | --- |
| `start()` | - | str | 启动实例 |
| `stop()` | - | str | 停止实例 |
| `restart()` | - | str | 重启实例 |
| `kill()` | - | str | 强制关闭实例 |
| `delete(deleteFile=False)` | deleteFile: bool | InstanceDeleteResult | 删除实例 |
| `update()` | - | bool | 升级实例 |
| `updateConfig(config)` | config: dict | str | 更新配置（部分更新） |
| `reinstall(title, description)` | title, description: str | bool | 重装实例 |
| `command(command)` | command: str | str | 发送命令 |
| `get_output(size=None)` | size: int \| None | str | 获取输出 |
| `files(target, page, page_size, file_name)` | - | FileList | 获取文件列表 |
| `list_schedule()` | - | list[ScheduleDetail] | 获取计划任务列表 |
| `create_schedule(config)` | config: SchedulePostBody | bool | 创建计划任务 |

## _class_ `InstanceCreateResult(BaseModel)`

实例创建结果

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `instanceUuid` | str | 实例 UUID |
| `config` | InstanceConfig | 实例配置 |

## _class_ `InstanceSearchList(BaseModel)`

实例搜索列表

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `daemonId` | str | 所属节点 UUID |
| `pageSize` | int | 每页实例数量 |
| `maxPage` | int | 最大页数 |
| `data` | list[InstanceDetail] | 实例详细信息列表 |

## _class_ `InstanceDeleteItem(BaseModel)`

删除实例返回的单条信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `instanceUuid` | str | 实例 UUID |
| `nickname` | str | 实例名称 |

## _class_ `InstanceDeleteResult(BaseModel)`

实例删除结果

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `instanceUuids` | list[str] | 删除的实例 UUID 列表 |
| `instances` | list[InstanceDeleteItem] | 删除的实例详细信息 |
