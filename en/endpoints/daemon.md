# Daemon

## _class_ `Daemon`

Get subclasses for daemon (node) operations.

```python
api = mcsm.daemon
```

---

### _method_ `config()`

Get configuration information for all daemons.

#### Returns

- `list[DaemonStatus]`: List of daemon configuration information.

#### Example

```python
daemons = await api.config()
for d in daemons:
    print(d.remarks, d.ip, d.port)
```

### _method_ `add(config: DaemonConfig)`

Add a new daemon.

#### Parameters

- `config`: Daemon configuration.

#### Returns

- `str`: UUID of the newly added daemon.

#### Example

```python
from mcsmapi.models.daemon import DaemonConfig

uuid = await api.add(DaemonConfig(ip="192.168.1.100", port=24444, apiKey="your-key"))
print("New daemon UUID:", uuid)
```

### _method_ `delete(daemonId: str)`

Delete a daemon.

#### Parameters

- `daemonId`: UUID of the daemon.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.delete("daemon-uuid")
```

### _method_ `link(daemonId: str)`

Connect to a daemon.

#### Parameters

- `daemonId`: UUID of the daemon.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.link("daemon-uuid")
```

### _method_ `update(daemonId: str, config: dict[str, Any])`

Update the configuration of a daemon (partial update, only the provided fields are sent).

::: tip
This endpoint supports partial updates. Only the fields you provide will be modified; fields not included will remain unchanged.
:::

#### Parameters

- `daemonId`: UUID of the daemon.
- `config`: Configuration fields to modify.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.update("daemon-uuid", {"remarks": "New nickname"})
```
