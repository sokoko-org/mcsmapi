# Java 环境

## _class_ `Java`

获取操作 Java 环境的子类

```python
api = mcsm.java
```

---

### _method_ `list(daemonId: str, instanceId: str)`

获取节点上的 Java 环境列表

#### 参数

- `daemonId`: 节点的 UUID
- `instanceId`: 实例的 UUID

#### 返回

- `list[JavaRuntime]`: Java 运行时列表

#### 例子

```python
javas = await api.list("daemon-uuid", "instance-uuid")
for j in javas:
    print(j.name, j.path)
```

### _method_ `add(daemonId: str, name: str, path: str)`

手动添加 Java 环境

#### 参数

- `daemonId`: 节点的 UUID
- `name`: Java 名称
- `path`: Java 可执行文件路径

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.add("daemon-uuid", "Java 17", "/usr/lib/jvm/java-17/bin/java")
```

### _method_ `download(daemonId: str, instanceId: str, name: str, version: str)`

下载安装 Java 环境

#### 参数

- `daemonId`: 节点的 UUID
- `instanceId`: 实例的 UUID
- `name`: Java 发行版名称
- `version`: Java 版本

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.download("daemon-uuid", "instance-uuid", "Adoptium", "17")
```

### _method_ `using(daemonId: str, instanceId: str, id: str)`

设置实例使用的 Java 环境

#### 参数

- `daemonId`: 节点的 UUID
- `instanceId`: 实例的 UUID
- `id`: Java 环境 ID

#### 返回

- `bool`: 操作成功后返回 True

### _method_ `delete(daemonId: str, id: str)`

删除 Java 环境

#### 参数

- `daemonId`: 节点的 UUID
- `id`: Java 环境 ID

#### 返回

- `bool`: 操作成功后返回 True