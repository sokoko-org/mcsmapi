# Schedule Models

## _class_ `ScheduleActionType(Enum)`

Schedule action type

| Variant | Value | Description |
| --- | --- | --- |
| `COMMAND` | command | 发送命令 |
| `DELAY` | delay | 等待 x 秒 |
| `STOP` | stop | 停止实例 |
| `START` | start | 启动实例 |
| `RESTART` | restart | 重启实例 |
| `KILL` | kill | 强制停止实例 |

## _class_ `ScheduleType(IntEnum)`

Schedule type

| Variant | Value | Description |
| --- | --- | --- |
| `INTERVAL` | 1 | 间隔时间任务 |
| `CYCLE` | 2 | 周期时间任务 |
| `SPECIFY` | 3 | 指定时间任务 |

## _class_ `ScheduleAction(BaseModel)`

Schedule action type

| Field | Type | Description |
| --- | --- | --- |
| `type` | ScheduleActionType | 动作类型 |
| `payload` | str | 动作参数 |

## _class_ `SchedulePostBody(BaseModel)`

Schedule config params

| Field | Type | Description |
| --- | --- | --- |
| `name` | str | 计划任务名称 |
| `count` | int | 执行次数，-1 表无限 |
| `time` | str | 间隔秒数 (INTERVAL) 或 cron 字符串 (CYCLE/SPECIFY) |
| `actions` | list[ScheduleAction] | Schedule action type链 |
| `type` | ScheduleType | 任务类型 |

## _class_ `ScheduleDetail(SchedulePostBody)`

Schedule detail

| Field | Type | Description |
| --- | --- | --- |
| `instanceUuid` | str | 实例 UUID |
| `daemonId` | str | 节点 ID |

### _method_ `delete()`

Delete this schedule

#### 返回

- `bool`
