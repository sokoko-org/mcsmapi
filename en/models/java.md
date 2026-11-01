# Java Models

## _class_ `JavaInfo(BaseModel)`

Java runtime info

| Field | Type | Description |
| --- | --- | --- |
| `fullname` | str | 完整名称 (name_version) |
| `name` | str | Java 名称 |
| `path` | str \| None | Java 路径 |
| `installTime` | int | 安装时间（Unix 时间戳） |
| `downloading` | bool | 是否正在下载 |
| `version` | str \| None | Java 版本 |

## _class_ `JavaRuntime(BaseModel)`

Java runtime

| Field | Type | Description |
| --- | --- | --- |
| `info` | JavaInfo | 运行环境信息 |
| `path` | str | 运行环境目录路径 |
| `usingInstances` | list[str] | 正在使用的实例 UUID 列表 |
