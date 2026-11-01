# 计划任务模型

## _class_ `ScheduleActionType(Enum)`

计划任务动作

| 枚举项 | 枚举值 | 描述 |
| --- | --- | --- |
| `COMMAND` | command | 发送命令 |
| `DELAY` | delay | 等待 x 秒 |
| `STOP` | stop | 停止实例 |
| `START` | start | 启动实例 |
| `RESTART` | restart | 重启实例 |
| `KILL` | kill | 强制停止实例 |

## _class_ `ScheduleType(IntEnum)`

计划任务类型

| 枚举项 | 枚举值 | 描述 |
| --- | --- | --- |
| `INTERVAL` | 1 | 间隔时间任务 |
| `CYCLE` | 2 | 周期时间任务 |
| `SPECIFY` | 3 | 指定时间任务 |

## _class_ `ScheduleAction(BaseModel)`

计划任务动作

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `type` | ScheduleActionType | 动作类型 |
| `payload` | str | 动作参数 |

## _class_ `SchedulePostBody(BaseModel)`

计划任务配置参数

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `name` | str | 计划任务名称 |
| `count` | int | 执行次数，-1 表无限 |
| `time` | str | 间隔秒数 (INTERVAL) 或 cron 字符串 (CYCLE/SPECIFY) |
| `actions` | list[ScheduleAction] | 计划任务动作链 |
| `type` | ScheduleType | 任务类型 |

## _class_ `ScheduleDetail(SchedulePostBody)`

计划任务信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `instanceUuid` | str | 实例 UUID |
| `daemonId` | str | 节点 ID |

### _method_ `delete()`

删除该计划任务

#### 返回

- `bool`
