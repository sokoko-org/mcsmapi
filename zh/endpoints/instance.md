# 实例

## _class_ `Instance`

获取操作实例的子类

```python
api = mcsm.instance
```

---

### _method_ `search(daemonId: str, page: int = 1, page_size: int = 20, instance_name: str = "", status: Status | Literal[""] = "", tag: list[str] | None = None)`

根据指定的参数搜索实例信息

#### 参数

- `daemonId`: 节点的 UUID
- `page`: 页码，用于指示返回数据的第几页
- `page_size`: 每页数据条数，默认为 20
- `instance_name`: 用于过滤的实例名称
- `status`: 用于过滤的实例状态
- `tag`: 用于过滤的实例标签列表

#### 返回

- `InstanceSearchList`: 搜索结果模型

#### 例子

```python
result = await api.search("daemon-uuid", page=1, page_size=10)
for inst in result.data:
    print(inst.config.nickname, inst.status)
```

### _method_ `search_global(page: int = 1, page_size: int = 20, instance_name: str = "", status: Status | Literal[\"\"] = "")`

在所有节点中全局搜索实例

#### 参数

- `page`: 页码
- `page_size`: 每页数据条数，默认为 20
- `instance_name`: 用于过滤的实例名称
- `status`: 用于过滤的实例状态

#### 返回

- `dict`: `{daemonId: {instances, maxPage, page}}`

#### 例子

```python
result = await api.search_global(instance_name="survival")
```

### _method_ `detail(daemonId: str, uuid: str)`

获取指定实例的详细信息

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID

#### 返回

- `InstanceDetail`: 实例详细信息模型

#### 例子

```python
detail = await api.detail("daemon-uuid", "instance-uuid")
print(detail.config.nickname)
```

### _method_ `create(daemonId: str, config: dict[str, Any])`

创建新实例

#### 参数

- `daemonId`: 节点的 UUID
- `config`: 新实例的配置，以字典形式提供，缺失内容由 `InstanceConfig` 模型提供默认值

#### 返回

- `InstanceCreateResult`: 一个包含新创建实例信息的结果对象

#### 例子

```python
result = await api.create("daemon-uuid", {
    "nickname": "Survival Server",
    "startCommand": "java -jar server.jar"
})
print("新实例 UUID:", result.instanceUuid)
```

### _method_ `updateConfig(daemonId: str, uuid: str, config: dict[str, Any])`

更新实例配置（部分更新，只发送提供的字段）

::: tip
此接口支持部分更新，只需传入要修改的字段，未传入的字段不会被覆盖。
:::

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `config`: 要修改的配置字段

#### 返回

- `str`: 被更新配置的实例 UUID

#### 例子

```python
uuid = await api.updateConfig("daemon-uuid", "instance-uuid", {
    "nickname": "新名称"
})
```

### _method_ `delete(daemonId: str, uuids: list[str], deleteFile: bool = False)`

删除实例

#### 参数

- `daemonId`: 节点的 UUID
- `uuids`: 要删除的实例 UUID 列表
- `deleteFile`: 是否删除实例文件

#### 返回

- `InstanceDeleteResult`: 删除结果模型

#### 例子

```python
result = await api.delete("daemon-uuid", ["uuid1", "uuid2"], deleteFile=True)
```

### _method_ `start(daemonId: str, uuid: str)`

启动实例

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 要启动的实例 UUID

#### 返回

- `str`: 被启动的实例的 UUID

#### 例子

```python
uuid = await api.start("daemon-uuid", "instance-uuid")
```

### _method_ `stop(daemonId: str, uuid: str)`

关闭实例

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 要关闭的实例 UUID

#### 返回

- `str`: 被关闭的实例的 UUID

### _method_ `restart(daemonId: str, uuid: str)`

重启实例

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 要重启的实例 UUID

#### 返回

- `str`: 被重启的实例的 UUID

### _method_ `kill(daemonId: str, uuid: str)`

强制关闭实例

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 要停止的实例 UUID

#### 返回

- `str`: 被停止的实例的 UUID

### _method_ `batchOperation(instances: list[BatchOperationDetail], operation: Literal["start", "stop", "restart", "kill"])`

批量操作实例

#### 参数

- `instances`: 批量操作的实例列表
- `operation`: 操作类型

#### 返回

- `bool`: 操作成功返回 True

#### 例子

```python
from mcsmapi.models.instance import BatchOperationDetail

await api.batchOperation([
    BatchOperationDetail(daemonId="d1", uuid="u1"),
    BatchOperationDetail(daemonId="d1", uuid="u2"),
], operation="start")
```

### _method_ `update(daemonId: str, uuid: str)`

执行实例的更新任务

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID

#### 返回

- `bool`: 操作成功返回 True

### _method_ `command(daemonId: str, uuid: str, command: str)`

向实例发送命令

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `command`: 命令内容

#### 返回

- `str`: 被操作的实例的 UUID

#### 例子

```python
uuid = await api.command("daemon-uuid", "instance-uuid", "say Hello")
```

### _method_ `get_output(daemonId: str, uuid: str, size: int | None = None)`

获取实例输出日志

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `size`: 获取的输出大小：1KB ~ 2048KB，未设置则返回所有日志

#### 返回

- `str`: 日志内容

#### 例子

```python
output = await api.get_output("daemon-uuid", "instance-uuid", size=100)
print(output)
```

### _method_ `reinstall(daemonId: str, uuid: str, title: str, description: str)`

重装实例（通过应用商城预设）

使用 `title` + `description` 匹配应用商城中的预设配置。

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `title`: 预设标题（需与应用商城一致）
- `description`: 预设描述（需与应用商城一致）

#### 返回

- `bool`: 操作成功返回 True

#### 例子

```python
await api.reinstall("daemon-uuid", "instance-uuid",
    title="Vanilla", description="Minecraft 原版服务端")
```

### _method_ `quick_install_list()`

获取应用商城快速安装列表

#### 返回

- `list`: 可安装的应用列表

### _method_ `process_config_list(daemonId: str, uuid: str, files: list[str])`

获取实例的配置文件列表

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `files`: 要查询的配置文件路径列表

#### 返回

- `list`: 配置文件列表

### _method_ `process_config_get(daemonId: str, uuid: str, fileName: str, type: str)`

获取实例的指定配置文件内容

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `fileName`: 配置文件名
- `type`: 配置文件类型

#### 返回

- `dict`: 配置文件内容

### _method_ `process_config_update(daemonId: str, uuid: str, fileName: str, config: dict, type: str)`

更新实例的指定配置文件

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `fileName`: 配置文件名
- `config`: 新的配置内容
- `type`: 配置文件类型

#### 返回

- `bool`: 操作成功返回 True

### _method_ `stop_asynchronous(daemonId: str, uuid: str, taskId: str)`

停止异步任务

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `taskId`: 任务 ID

#### 返回

- `bool`: 操作成功返回 True

### _method_ `query_asynchronous(daemonId: str, uuid: str, task_name: str, taskId: str)`

查询异步任务状态

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `task_name`: 任务名称
- `taskId`: 任务 ID

#### 返回

- `dict`: 任务状态信息

### _method_ `stream_channel(daemonId: str, uuid: str)`

创建数据流通道

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID

#### 返回

- `StreamChannelResult`: 通道信息

### _method_ `updateConfigUser(daemonId: str, uuid: str, config: dict[str, Any])`

更新实例配置（普通用户权限）

与 `updateConfig` 的区别：此接口普通用户也可调用，但仅允许修改部分安全字段（如 `pingConfig`、`eventTask`、`terminalOption` 等），不允许修改 `startCommand` 等核心配置。

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `config`: 要修改的配置字段

#### 返回

- `bool`: 操作成功返回 True