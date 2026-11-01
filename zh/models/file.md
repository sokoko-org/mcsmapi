# 文件模型

## _class_ `FileType(IntEnum)`

文件类型

| 枚举项 | 枚举值 | 描述 |
| --- | --- | --- |
| `FOLDER` | 0 | 文件夹 |
| `FILE` | 1 | 文件 |

## _class_ `FileItem(BaseModel)`

文件信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `name` | str | 文件名 |
| `size` | int | 文件大小(字节) |
| `time` | str | 修改时间 |
| `mode` | int | 权限 (仅 Linux) |
| `type` | FileType | 文件类型 |
| `daemonId` | str | 节点 UUID (SDK 注入) |
| `uuid` | str | 实例 UUID (SDK 注入) |
| `target` | str | 所在路径 (SDK 注入) |

### 链式操作方法

所有方法均为 `async`，需要 `await` 调用。

| 方法 | 参数 | 返回 | 描述 |
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

文件列表

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `items` | list[FileItem] | 文件列表 |
| `page` | int | 当前页 |
| `pageSize` | int | 每页大小 |
| `total` | int | 总数 |
| `absolutePath` | str | 远程节点上的绝对路径 |
| `daemonId` | str | 节点 UUID (SDK 注入) |
| `uuid` | str | 实例 UUID (SDK 注入) |

### 链式操作方法

| 方法 | 参数 | 返回 | 描述 |
| --- | --- | --- | --- |
| `upload(file, upload_dir)` | file: bytes, upload_dir: str | bool | 上传文件 |
| `createFile(target)` | target: str | bool | 创建文件 |
| `createFolder(target)` | target: str | bool | 创建文件夹 |

## _class_ `RemoteMappingEndpoint(BaseModel)`

远程映射端点

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `addr` | str | 地址 |
| `prefix` | str | 前缀 |

## _class_ `RemoteMappingEntry(BaseModel)`

远程映射条目

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `from` | RemoteMappingEndpoint | 源端点 |
| `to` | RemoteMappingEndpoint | 目标端点 |

## _class_ `FileDownloadConfig(BaseModel)`

文件下载配置

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `password` | str | 文件下载密码 |
| `addr` | str | 文件下载地址 |
| `remoteMappings` | list[RemoteMappingEntry] | 远程端口映射 |

## _class_ `StreamChannelResult(BaseModel)`

数据流通道信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `password` | str | 通道密码 |
| `addr` | str | 通道地址 |
| `prefix` | str | 路径前缀 |
| `remoteMappings` | list[RemoteMappingEntry] | 远程端口映射 |
