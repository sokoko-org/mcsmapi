# 节点

## _class_ `Daemon`

获取操作节点的子类

```python
api = mcsm.daemon
```

---

### _method_ `config()`

获取全部节点配置信息

#### 返回

- `list[DaemonStatus]`: 节点的配置信息列表

#### 例子

```python
daemons = await api.config()
for d in daemons:
    print(d)
```

### _method_ `add(config: DaemonConfig)`

新增一个节点

#### 参数

- `config`: 节点的配置信息

#### 返回

- `str`: 新增节点的 UUID

#### 例子

```python
from mcsmapi.models.daemon import DaemonConfig

daemon_id = await api.add(DaemonConfig(
    ip="127.0.0.1",
    port=24444,
    remarks="新节点"
))
print("新节点 ID:", daemon_id)
```

### _method_ `delete(daemonId: str)`

删除一个节点

#### 参数

- `daemonId`: 节点的 UUID

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.delete("daemon-uuid")
```

### _method_ `link(daemonId: str)`

连接一个节点

#### 参数

- `daemonId`: 节点的 UUID

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.link("daemon-uuid")
```

### _method_ `update(daemonId: str, config: dict[str, Any])`

更新一个节点的配置（部分更新，只发送提供的字段）

::: tip
此接口支持部分更新，只需传入要修改的字段，未传入的字段不会被覆盖。
:::

#### 参数

- `daemonId`: 节点的 UUID
- `config`: 要修改的配置字段

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.update("daemon-uuid", {"remarks": "新的备注名"})
```