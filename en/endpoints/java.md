# Java Management

## _class_ `Java`

Get subclasses for managing Java runtimes.

```python
api = mcsm.java
```

---

### _method_ `list(daemonId: str, instanceId: str)`

Get the list of available Java runtimes.

#### Parameters

- `daemonId`: UUID of the daemon.
- `instanceId`: UUID of the instance.

#### Returns

- `list[JavaRuntime]`

#### Example

```python
runtimes = await api.list("daemon-uuid", "instance-uuid")
for rt in runtimes:
    print(rt.name, rt.path)
```

### _method_ `add(daemonId: str, name: str, path: str)`

Add a custom Java runtime.

#### Parameters

- `daemonId`: UUID of the daemon.
- `name`: Display name for the runtime.
- `path`: File system path to the Java binary.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.add("daemon-uuid", "Java 21", "/usr/lib/jvm/java-21/bin/java")
```

### _method_ `download(daemonId: str, instanceId: str, name: str, version: str)`

Download and install a Java runtime.

#### Parameters

- `daemonId`: UUID of the daemon.
- `instanceId`: UUID of the instance.
- `name`: Name of the Java distribution.
- `version`: Java version string.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.download("daemon-uuid", "instance-uuid", "OpenJDK", "21")
```

### _method_ `using(daemonId: str, instanceId: str, id: str)`

Set the active Java runtime for an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `instanceId`: UUID of the instance.
- `id`: ID of the Java runtime to use.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.using("daemon-uuid", "instance-uuid", "runtime-id")
```

### _method_ `delete(daemonId: str, id: str)`

Delete a Java runtime.

#### Parameters

- `daemonId`: UUID of the daemon.
- `id`: ID of the Java runtime to delete.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.delete("daemon-uuid", "runtime-id")
```