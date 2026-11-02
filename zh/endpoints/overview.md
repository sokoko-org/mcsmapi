# 仪表盘数据

## _class_ `Overview`

获取操作仪表盘数据的子类

```python
api = mcsm.overview
```

---

### _method_ `overview()`

获取面板基本信息

#### 返回

- `OverviewModel`: 面板概览信息模型

#### 例子

```python
overview = await api.overview()
print("服务端版本:", overview.version)
print("系统剩余内存:", overview.system.freemem)
```

### _method_ `logs(limit: int = 0)`

获取面板操作日志

#### 参数

- `limit`: 日志条数限制，默认为 0（不限制）

#### 返回

- `list[LogDetail]`: 日志详情列表

#### 例子

```python
logs = await api.logs(50)
for log in logs:
    print(log)
```

### _method_ `log_search(page: int = 1, page_size: int = 20, type: LogType | None = None, level: LogLevel | None = None, operator_name: str | None = None, start_time: int | None = None, end_time: int | None = None, keyword: str | None = None)`

搜索面板操作日志

#### 参数

- `page`: 页码
- `page_size`: 每页条数
- `type`: 操作类型过滤（`LogType` 枚举）
- `level`: 日志等级过滤（`LogLevel` 枚举：`INFO`/`WARNING`/`ERROR`）
- `operator_name`: 操作者用户名过滤
- `start_time`: 起始时间戳
- `end_time`: 结束时间戳
- `keyword`: 关键词搜索

#### 返回

- `LogSearchResult`: 搜索结果模型（包含 `page`, `pageSize`, `maxPage`, `total`, `data` 字段）

#### 例子

```python
from mcsmapi.models.overview import LogType, LogLevel

result = await api.log_search(
    page=1, page_size=20,
    type=LogType.USER_LOGIN,
    level=LogLevel.INFO,
)
print(f"总记录: {result.total}")
for log in result.data:
    print(log.operator_name, log.operation_level)
```

### _method_ `setting()`

获取面板全局设置

#### 返回

- `dict`: 面板设置信息

### _method_ `update_setting(config: dict[str, Any])`

更新面板全局设置（部分更新，只发送提供的字段）

::: tip
此接口支持部分更新，只需传入要修改的字段，未传入的字段不会被覆盖。
:::

#### 参数

- `config`: 要修改的配置字段

#### 返回

- `str`: 操作成功返回字符串

### _method_ `layout()`

获取面板布局配置

#### 返回

- `dict`: 布局配置

### _method_ `set_layout(config: dict[str, Any])`

设置面板布局配置

#### 参数

- `config`: 布局配置

#### 返回

- `bool`: 操作成功后返回 True

### _method_ `reset_layout()`

重置面板布局为默认配置

#### 返回

- `bool`: 操作成功后返回 True

### _method_ `upload_assets(file: bytes)`

上传面板资源文件

#### 参数

- `file`: 文件内容

#### 返回

- `bool`: 操作成功后返回 True

---

## 基本使用示例

### 获取系统概览信息

```python
overview = await api.overview()

print("服务端版本:", overview.version)
print("系统内存剩余:", overview.system.freemem)
print("系统负载平均值:", overview.system.loadavg)
print("MCSM 运行 CPU 占用率:", overview.process.cpu)
```

### 遍历所有远程守护进程

```python
overview = await api.overview()

for remote in overview.remote:
    print("备注名称:", remote.remarks)
    print("IP 地址:", remote.ip)
    print("端口号:", remote.port)
    print("是否可用:", remote.available)
    print("守护进程版本:", remote.version)
```