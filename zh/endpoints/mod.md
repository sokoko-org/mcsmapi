# 模组管理

## _class_ `Mod`

获取操作模组的子类

```python
api = mcsm.mod
```

---

### _method_ `mc_versions()`

获取可用的 Minecraft 版本列表

#### 返回

- `list`: Minecraft 版本列表

#### 例子

```python
versions = await api.mc_versions()
```

### _method_ `list(daemonId: str, uuid: str, page: int, pageSize: int, folder: str, search: str)`

获取实例的模组列表

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `page`: 页码
- `pageSize`: 每页条数
- `folder`: 模组文件夹路径
- `search`: 搜索关键词

#### 返回

- `ModListResult`: 模组列表结果模型

#### 例子

```python
result = await api.list("daemon-uuid", "instance-uuid",
    page=1, pageSize=20, folder="mods", search="")
```

### _method_ `info(hash: str)`

获取模组详细信息

#### 参数

- `hash`: 模组文件哈希值

#### 返回

- `ModInfoDetail`: 模组详情模型

### _method_ `search(query: str, offset: int, limit: int, source: str, version: str, type: str, loader: str, environment: str)`

搜索模组

#### 参数

- `query`: 搜索关键词
- `offset`: 偏移量
- `limit`: 返回条数
- `source`: 模组来源
- `version`: Minecraft 版本
- `type`: 模组类型
- `loader`: 模组加载器
- `environment`: 运行环境

#### 返回

- `ModSearchResult`: 搜索结果模型

#### 例子

```python
result = await api.search("fabric-api", offset=0, limit=20,
    source="", version="1.20.1", type="", loader="fabric", environment="")
```

### _method_ `versions(projectId: str, source: str)`

获取模组的版本列表

#### 参数

- `projectId`: 项目 ID
- `source`: 模组来源

#### 返回

- `list[ModVersion]`: 版本列表

### _method_ `download(daemonId: str, uuid: str, url: str, fileName: str, projectType: str, fallbackUrl: str, extraInfo: dict)`

下载模组到实例

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `url`: 下载地址
- `fileName`: 文件名
- `projectType`: 项目类型
- `fallbackUrl`: 备用下载地址
- `extraInfo`: 额外信息

#### 返回

- `bool`: 操作成功后返回 True

### _method_ `stop_transfer(daemonId: str, uuid: str, fileName: str, type: str)`

停止模组传输任务

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `fileName`: 文件名
- `type`: 任务类型

#### 返回

- `bool`: 操作成功后返回 True

### _method_ `config_files(daemonId: str, uuid: str, modId: str, type: str, fileName: str)`

获取模组配置文件列表

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `modId`: 模组 ID
- `type`: 模组类型
- `fileName`: 配置文件名

#### 返回

- `list`: 配置文件列表

### _method_ `toggle(daemonId: str, uuid: str, fileName: str)`

启用或禁用模组

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `fileName`: 模组文件名

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.toggle("daemon-uuid", "instance-uuid", "fabric-api-0.92.0.jar")
```

### _method_ `delete(daemonId: str, uuid: str, fileName: str)`

删除模组

#### 参数

- `daemonId`: 节点的 UUID
- `uuid`: 实例的 UUID
- `fileName`: 模组文件名

#### 返回

- `bool`: 操作成功后返回 True

### _method_ `batch_info(hashes: list[str])`

批量获取模组信息

#### 参数

- `hashes`: 模组文件哈希值列表

#### 返回

- `list`: 模组信息列表