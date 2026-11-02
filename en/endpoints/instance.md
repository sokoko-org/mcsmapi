# Instance

## _class_ `Instance`

Get subclasses for instance operations.

```python
api = mcsm.instance
```

---

### _method_ `search(daemonId: str, page: int = 1, page_size: int = 20, instance_name: str = "", status: Status | Literal[""] = "", tag: list[str] | None = None)`

Search for instance information on a specific daemon.

#### Parameters

- `daemonId`: UUID of the daemon.
- `page`: Page number, defaults to 1.
- `page_size`: Number of items per page, defaults to 20.
- `instance_name`: Instance name filter.
- `status`: Instance status filter.
- `tag`: List of tags for filtering.

#### Returns

- `InstanceSearchList`

#### Example

```python
result = await api.search("daemon-uuid", instance_name="survival")
for inst in result.data:
    print(inst.config.nickname)
```

### _method_ `search_global(page: int = 1, page_size: int = 20, instance_name: str = "", status: Status | Literal[\"\"] = "")`

Search for instances across all daemons.

#### Parameters

- `page`: Page number, defaults to 1.
- `page_size`: Number of items per page, defaults to 20.
- `instance_name`: Instance name filter.
- `status`: Instance status filter.

#### Returns

- `dict[str, Any]`

#### Example

```python
result = await api.search_global(instance_name="lobby")
```

### _method_ `detail(daemonId: str, uuid: str)`

Get detailed information of a specific instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `InstanceDetail`

#### Example

```python
detail = await api.detail("daemon-uuid", "instance-uuid")
print(detail.config.nickname, detail.status)
```

### _method_ `create(daemonId: str, config: dict[str, Any])`

Create a new instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `config`: Configuration of the new instance, provided as a dictionary. Missing values are filled with default values from the `InstanceConfig` model.

#### Returns

- `InstanceCreateResult`

#### Example

```python
result = await api.create("daemon-uuid", {
    "nickname": "My Server",
    "startCommand": "java -jar server.jar",
    "type": 6
})
print("Created:", result.instanceUuid)
```

### _method_ `updateConfig(daemonId: str, uuid: str, config: dict[str, Any])`

Update the configuration of an instance (partial update, only the provided fields are sent).

::: tip
This endpoint supports partial updates. Only the fields you provide will be modified; fields not included will remain unchanged.
:::

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `config`: Configuration fields to modify.

#### Returns

- `str`: UUID of the instance whose configuration was updated.

#### Example

```python
uuid = await api.updateConfig("daemon-uuid", "instance-uuid", {"nickname": "Renamed"})
```

### _method_ `delete(daemonId: str, uuids: list[str], deleteFile: bool = False)`

Delete instances.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuids`: List of UUIDs of instances to delete.
- `deleteFile`: Whether to delete instance files, defaults to `False`.

#### Returns

- `InstanceDeleteResult`

#### Example

```python
result = await api.delete("daemon-uuid", ["uuid1", "uuid2"], deleteFile=True)
```

### _method_ `start(daemonId: str, uuid: str)`

Start an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `str`: UUID of the started instance.

#### Example

```python
await api.start("daemon-uuid", "instance-uuid")
```

### _method_ `stop(daemonId: str, uuid: str)`

Stop an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `str`: UUID of the stopped instance.

#### Example

```python
await api.stop("daemon-uuid", "instance-uuid")
```

### _method_ `restart(daemonId: str, uuid: str)`

Restart an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `str`: UUID of the restarted instance.

#### Example

```python
await api.restart("daemon-uuid", "instance-uuid")
```

### _method_ `kill(daemonId: str, uuid: str)`

Forcefully stop an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `str`: UUID of the killed instance.

#### Example

```python
await api.kill("daemon-uuid", "instance-uuid")
```

### _method_ `batchOperation(instances: list[BatchOperationDetail], operation: Literal["start", "stop", "restart", "kill"])`

Perform batch operations on instances.

#### Parameters

- `instances`: List of instances to operate on.
- `operation`: Type of operation (`"start"`, `"stop"`, `"restart"`, or `"kill"`).

#### Returns

- `bool`: Returns `True` if the operation is successful.

#### Example

```python
from mcsmapi.models.instance import BatchOperationDetail

await api.batchOperation([
    BatchOperationDetail(uuid="uuid1", daemonId="daemon1"),
    BatchOperationDetail(uuid="uuid2", daemonId="daemon1"),
], "start")
```

### _method_ `update(daemonId: str, uuid: str)`

Update an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `bool`: Returns `True` if the operation is successful.

#### Example

```python
await api.update("daemon-uuid", "instance-uuid")
```

### _method_ `command(daemonId: str, uuid: str, command: str)`

Send a command to an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `command`: Command to send.

#### Returns

- `str`: UUID of the operated instance.

#### Example

```python
await api.command("daemon-uuid", "instance-uuid", "say Hello World")
```

### _method_ `get_output(daemonId: str, uuid: str, size: int | None = None)`

Get instance output log.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `size`: Size of output to retrieve, in KB (1KB ~ 2048KB). If not set, all logs are returned.

#### Returns

- `str`: Log content.

#### Example

```python
output = await api.get_output("daemon-uuid", "instance-uuid", size=100)
print(output)
```

### _method_ `reinstall(daemonId: str, uuid: str, title: str, description: str)`

Reinstall an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `title`: Title of the reinstallation.
- `description`: Description of the reinstallation.

#### Returns

- `bool`: Returns `True` if the operation is successful.

#### Example

```python
await api.reinstall("daemon-uuid", "instance-uuid", "Paper 1.20.4", "Reinstall with Paper")
```

### _method_ `quick_install_list()`

Get the list of available quick-install templates.

#### Returns

- `list[dict[str, Any]]`

#### Example

```python
templates = await api.quick_install_list()
for t in templates:
    print(t)
```

### _method_ `process_config_list(daemonId: str, uuid: str, files: list[str])`

Get the list of process configuration files.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `files`: List of file paths to query.

#### Returns

- `list[dict[str, Any]]`

#### Example

```python
configs = await api.process_config_list("daemon-uuid", "instance-uuid", ["server.properties"])
```

### _method_ `process_config_get(daemonId: str, uuid: str, fileName: str, type: str = "")`

Get the content of a process configuration file.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `fileName`: Name of the configuration file.
- `type`: Configuration type, defaults to empty string.

#### Returns

- `Any`

#### Example

```python
config = await api.process_config_get("daemon-uuid", "instance-uuid", "server.properties")
```

### _method_ `process_config_update(daemonId: str, uuid: str, fileName: str, config: Any, type: str = "")`

Update a process configuration file.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `fileName`: Name of the configuration file.
- `config`: New configuration content.
- `type`: Configuration type, defaults to empty string.

#### Returns

- `Any`

#### Example

```python
await api.process_config_update("daemon-uuid", "instance-uuid", "server.properties", {"max-players": "50"})
```

### _method_ `stop_asynchronous(daemonId: str, uuid: str, taskId: str = "")`

Stop an asynchronous task on an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `taskId`: Task ID, defaults to empty string.

#### Returns

- `bool`: Returns `True` if the operation is successful.

#### Example

```python
await api.stop_asynchronous("daemon-uuid", "instance-uuid", "task-id")
```

### _method_ `query_asynchronous(daemonId: str, uuid: str, task_name: str = "", taskId: str = "")`

Query the status of an asynchronous task.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `task_name`: Name of the task.
- `taskId`: Task ID.

#### Returns

- `Any`

#### Example

```python
status = await api.query_asynchronous("daemon-uuid", "instance-uuid", taskId="task-id")
```

### _method_ `stream_channel(daemonId: str, uuid: str)`

Open a stream channel for an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `StreamChannelResult`

#### Example

```python
channel = await api.stream_channel("daemon-uuid", "instance-uuid")
print(channel)
```

### _method_ `updateConfigUser(daemonId: str, uuid: str, config: dict[str, Any])`

Update instance configuration as a non-admin user.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `config`: New configuration, provided as a dictionary.

#### Returns

- `str`: UUID of the instance whose configuration was updated.

#### Example

```python
uuid = await api.updateConfigUser("daemon-uuid", "instance-uuid", {"nickname": "My Server"})
```