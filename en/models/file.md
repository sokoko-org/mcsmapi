# File Models

## _class_ `FileType(IntEnum)`

File type

| Variant | Value | Description |
| --- | --- | --- |
| `FOLDER` | 0 | 文件夹 |
| `FILE` | 1 | 文件 |

## _class_ `FileItem(BaseModel)`

File info

| Field | Type | Description |
| --- | --- | --- |
| `name` | str | 文件名 |
| `size` | int | 文件大小(字节) |
| `time` | str | 修改时间 |
| `mode` | int | 权限 (仅 Linux) |
| `type` | FileType | File type |
| `daemonId` | str | 节点 UUID (SDK 注入) |
| `uuid` | str | 实例 UUID (SDK 注入) |
| `target` | str | 所在路径 (SDK 注入) |

### Chain methods

All methods are `async` and require `await`.

| Method | Parameters | Return | Description |
| --- | --- | --- | --- |
| `rename(newName)` | newName: str | bool | 重命名 |
| `delete()` | - | bool | 删除 |
| `copy_to(target)` | target: str | bool | 复制到目标路径 |
| `move(target)` | target: str | bool | 移动到目标路径 |
| `content()` | - | str | 获取文件内容 |
| `zip(targets)` | targets: list[str] | bool | 压缩 |
| `unzip(target, code)` | target: str, code: str | bool | 解压 |
| `update(text)` | text: str | bool | 更新文件内容 |
| `download()` | - | FileDownloadConfig | 获取下载配置 |

## _class_ `FileList(BaseModel)`

File list

| Field | Type | Description |
| --- | --- | --- |
| `items` | list[FileItem] | File list |
| `page` | int | 当前页 |
| `pageSize` | int | 每页大小 |
| `total` | int | 总数 |
| `absolutePath` | str | 远程节点上的绝对路径 |
| `daemonId` | str | 节点 UUID (SDK 注入) |
| `uuid` | str | 实例 UUID (SDK 注入) |

### Chain methods

| Method | Parameters | Return | Description |
| --- | --- | --- | --- |
| `upload(file, upload_dir)` | file: bytes, upload_dir: str | bool | 上传文件 |
| `createFile(target)` | target: str | bool | 创建文件 |
| `createFolder(target)` | target: str | bool | 创建文件夹 |

## _class_ `RemoteMappingEndpoint(BaseModel)`

Remote mapping endpoint

| Field | Type | Description |
| --- | --- | --- |
| `addr` | str | 地址 |
| `prefix` | str | 前缀 |

## _class_ `RemoteMappingEntry(BaseModel)`

Remote mapping entry

| Field | Type | Description |
| --- | --- | --- |
| `from` | RemoteMappingEndpoint | 源端点 |
| `to` | RemoteMappingEndpoint | 目标端点 |

## _class_ `FileDownloadConfig(BaseModel)`

File download config

| Field | Type | Description |
| --- | --- | --- |
| `password` | str | 文件下载密码 |
| `addr` | str | 文件下载地址 |
| `remoteMappings` | list[RemoteMappingEntry] | 远程端口映射 |

## _class_ `StreamChannelResult(BaseModel)`

Stream channel result

| Field | Type | Description |
| --- | --- | --- |
| `password` | str | 通道密码 |
| `addr` | str | 通道地址 |
| `prefix` | str | 路径前缀 |
| `remoteMappings` | list[RemoteMappingEntry] | 远程端口映射 |
