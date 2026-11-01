# 节点模型

## _class_ `DaemonOperation(BaseModel)`

节点操作基类

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | str | 节点 UUID |

### _method_ `search_instances(page, page_size, instance_name, status)`

搜索当前节点的实例列表

#### 参数

- `page`: 页码，默认 1
- `page_size`: 每页大小，默认 20
- `instance_name`: 实例名称过滤
- `status`: 实例状态过滤

#### 返回

- `InstanceSearchList`

### _method_ `detail(instanceUuid)`

获取当前节点上指定实例的详细信息

#### 参数

- `instanceUuid`: 实例 UUID

#### 返回

- `InstanceDetail`

### _method_ `delete()`

删除该节点

#### 返回

- `bool`

### _method_ `link()`

连接该节点

#### 返回

- `bool`

### _method_ `updateConfig(config)`

更新节点配置（部分更新）

#### 参数

- `config`: 要修改的字段 (dict)

#### 返回

- `bool`

### _method_ `createInstance(config)`

在当前节点创建实例

#### 参数

- `config`: 实例配置 (dict)

#### 返回

- `InstanceCreateResult`

### _method_ `deleteInstance(uuids, deleteFile)`

删除当前节点的实例

#### 参数

- `uuids`: 实例 UUID 列表
- `deleteFile`: 是否删除关联文件，默认 False

#### 返回

- `InstanceDeleteResult`

## _class_ `DaemonConfig(BaseModel)`

节点配置信息

| 字段名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `ip` | str | "localhost" | 远程节点 IP |
| `port` | int | 24444 | 远程节点端口 |
| `prefix` | str | "" | 路径前缀 |
| `remarks` | str | "" | 备注 |
| `apiKey` | str | "" | API Key |

## _class_ `DaemonStatus(DaemonOperation)`

节点状态信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `available` | bool | 节点可用状态 |
| `ip` | str | 节点 IP |
| `port` | int | 节点端口 |
| `prefix` | str | 路径前缀 |
| `remarks` | str | 备注 |
