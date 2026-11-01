# Daemon Models

## _class_ `DaemonOperation(BaseModel)`

Daemon operation base

| Field | Type | Description |
| --- | --- | --- |
| `uuid` | str | 节点 UUID |

### _method_ `search_instances(page, page_size, instance_name, status)`

Search instances on this node

#### 参数

- `page`: 页码，默认 1
- `page_size`: 每页大小，默认 20
- `instance_name`: 实例名称过滤
- `status`: Instance status过滤

#### 返回

- `InstanceSearchList`

### _method_ `detail(instanceUuid)`

Get instance detail on this node

#### 参数

- `instanceUuid`: 实例 UUID

#### 返回

- `InstanceDetail`

### _method_ `delete()`

Delete this node

#### 返回

- `bool`

### _method_ `link()`

Connect this node

#### 返回

- `bool`

### _method_ `updateConfig(config)`

Update node config (partial)

#### 参数

- `config`: 要修改的字段 (dict)

#### 返回

- `bool`

### _method_ `createInstance(config)`

Create instance on this node

#### 参数

- `config`: 实例配置 (dict)

#### 返回

- `InstanceCreateResult`

### _method_ `deleteInstance(uuids, deleteFile)`

Delete instances on this node

#### 参数

- `uuids`: 实例 UUID 列表
- `deleteFile`: 是否删除关联文件，默认 False

#### 返回

- `InstanceDeleteResult`

## _class_ `DaemonConfig(BaseModel)`

Daemon config

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `ip` | str | "localhost" | 远程节点 IP |
| `port` | int | 24444 | 远程节点端口 |
| `prefix` | str | "" | 路径前缀 |
| `remarks` | str | "" | 备注 |
| `apiKey` | str | "" | API Key |

## _class_ `DaemonStatus(DaemonOperation)`

Daemon status

| Field | Type | Description |
| --- | --- | --- |
| `available` | bool | 节点可用状态 |
| `ip` | str | 节点 IP |
| `port` | int | 节点端口 |
| `prefix` | str | 路径前缀 |
| `remarks` | str | 备注 |
