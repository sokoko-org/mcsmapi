# Dashboard Data

## _class_ `Overview`

Get subclasses for operating dashboard data.

```python
api = mcsm.overview
```

---

### _method_ `overview()`

Get basic panel information.

#### Returns

- `OverviewModel`

#### Example

```python
overview = await api.overview()
print("Current server version:", overview.version)
```

### _method_ `logs(limit: int = 20)`

Get panel operation logs.

#### Parameters

- `limit`: Maximum number of log entries to return, defaults to 20.

#### Returns

- `list[LogDetail]`

#### Example

```python
logs = await api.logs(50)
for log in logs:
    print(log)
```

### _method_ `log_search(page: int = 1, page_size: int = 20, type: LogType | None = None, level: LogLevel | None = None, operator_name: str | None = None, start_time: int | None = None, end_time: int | None = None, keyword: str | None = None)`

Search panel logs with filters.

#### Parameters

- `page`: Page number, defaults to 1.
- `page_size`: Number of items per page, defaults to 20.
- `type`: Log type filter (`LogType` enum).
- `level`: Log level filter (`LogLevel` enum: `INFO`/`WARNING`/`ERROR`).
- `operator_name`: Operator name filter.
- `start_time`: Start timestamp filter.
- `end_time`: End timestamp filter.
- `keyword`: Keyword search filter.

#### Returns

- `LogSearchResult`: Search result model (contains `page`, `pageSize`, `maxPage`, `total`, `data` fields)

#### Example

```python
from mcsmapi.models.overview import LogType, LogLevel

result = await api.log_search(
    type=LogType.USER_LOGIN,
    level=LogLevel.INFO,
    page_size=10,
)
print(f"Total: {result.total}")
for log in result.data:
    print(log.operator_name, log.operation_level)
```

### _method_ `setting()`

Get panel settings.

#### Returns

- `dict[str, Any]`

#### Example

```python
settings = await api.setting()
```

### _method_ `update_setting(config: dict[str, Any])`

Update panel settings (partial update, only the provided fields are sent).

::: tip
This endpoint supports partial updates. Only the fields you provide will be modified; fields not included will remain unchanged.
:::

#### Parameters

- `config`: Settings fields to modify.

#### Returns

- `str`

#### Example

```python
await api.update_setting({"language": "en_us"})
```

### _method_ `layout()`

Get the current panel layout configuration.

#### Returns

- `dict[str, Any]`

#### Example

```python
layout = await api.layout()
```

### _method_ `set_layout(config: dict[str, Any])`

Set the panel layout configuration.

#### Parameters

- `config`: Layout configuration dictionary.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.set_layout({"theme": "dark"})
```

### _method_ `reset_layout()`

Reset the panel layout to default.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.reset_layout()
```

### _method_ `upload_assets(file: bytes)`

Upload asset files to the panel.

#### Parameters

- `file`: File content as bytes.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
with open("logo.png", "rb") as f:
    await api.upload_assets(f.read())
```
