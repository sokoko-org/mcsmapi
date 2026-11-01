# Scheduled Tasks

## _class_ `Schedule`

Get subclasses for managing scheduled tasks.

```python
api = mcsm.schedule
```

---

### _method_ `list(daemonId: str, uuid: str)`

Retrieve the list of scheduled tasks for an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `list[ScheduleDetail]`

#### Example

```python
tasks = await api.list("daemon-uuid", "instance-uuid")
for task in tasks:
    print(task.name)
```

### _method_ `delete(daemonId: str, uuid: str, task_name: str)`

Delete a scheduled task.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `task_name`: Name of the scheduled task.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.delete("daemon-uuid", "instance-uuid", "auto-restart")
```

### _method_ `create(daemonId: str, uuid: str, config: SchedulePostBody)`

Create a scheduled task.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `config`: Scheduled task configuration.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
from mcsmapi.models.schedule import SchedulePostBody, ScheduleAction, ScheduleType

task = SchedulePostBody(
    name="auto-restart",
    action=ScheduleAction.RESTART,
    type=ScheduleType.INTERVAL,
    time="3600"
)
await api.create("daemon-uuid", "instance-uuid", task)
```