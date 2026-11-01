# Mod Management

## _class_ `Mod`

Get subclasses for managing mods and plugins.

```python
api = mcsm.mod
```

---

### _method_ `mc_versions()`

Get the list of available Minecraft versions.

#### Returns

- `list[str]`

#### Example

```python
versions = await api.mc_versions()
for v in versions:
    print(v)
```

### _method_ `list(daemonId: str, uuid: str, page: int = 1, pageSize: int = 50, folder: str | None = None, search: str | None = None)`

Get the list of installed mods for an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `page`: Page number, defaults to 1.
- `pageSize`: Number of items per page, defaults to 50.
- `folder`: Folder to search in.
- `search`: Search filter string.

#### Returns

- `ModListResult`

#### Example

```python
result = await api.list("daemon-uuid", "instance-uuid")
for mod in result.data:
    print(mod.fileName)
```

### _method_ `info(hash: str)`

Get detailed information for a single mod by its hash.

#### Parameters

- `hash`: File hash of the mod.

#### Returns

- `ModInfoDetail | None`

#### Example

```python
info = await api.info("abc123hash")
if info:
    print(info)
```

### _method_ `search(query: str = "", offset: int = 0, limit: int = 20, source: str = "all", version: str = "", type: str = "all", loader: str = "all", environment: str = "all")`

Search for mods from online sources.

#### Parameters

- `query`: Search query text.
- `offset`: Result offset, defaults to 0.
- `limit`: Maximum results, defaults to 20.
- `source`: Mod source (`"all"`, `"Modrinth"`, `"CurseForge"`, etc.).
- `version`: Minecraft version filter.
- `type`: Mod type filter (`"all"`, `"mod"`, `"plugin"`, etc.).
- `loader`: Mod loader filter (`"all"`, `"fabric"`, `"forge"`, etc.).
- `environment`: Environment filter (`"all"`, `"client"`, `"server"`, etc.).

#### Returns

- `ModSearchResult`

#### Example

```python
result = await api.search("WorldEdit", version="1.20.4", loader="fabric")
for hit in result.hits:
    print(hit.title, hit.description)
```

### _method_ `versions(projectId: str, source: str = "Modrinth")`

Get available versions for a mod project.

#### Parameters

- `projectId`: Project ID on the mod platform.
- `source`: Mod source, defaults to `"Modrinth"`.

#### Returns

- `list[ModVersion]`

#### Example

```python
versions = await api.versions("P7dR8mSH")
for v in versions:
    print(v.version_number)
```

### _method_ `download(daemonId: str, uuid: str, url: str, fileName: str, projectType: str, fallbackUrl: str | None = None, extraInfo: Any | None = None)`

Download and install a mod to an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `url`: Download URL for the mod file.
- `fileName`: File name to save as.
- `projectType`: Type of the project (e.g. `"mod"`, `"plugin"`).
- `fallbackUrl`: Fallback download URL.
- `extraInfo`: Additional metadata.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.download(
    "daemon-uuid", "instance-uuid",
    "https://cdn.modrinth.com/data/.../worldedit.jar",
    "worldedit.jar",
    "mod"
)
```

### _method_ `stop_transfer(daemonId: str, uuid: str, fileName: str, type: str)`

Stop a mod download/transfer in progress.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `fileName`: File name of the transfer to stop.
- `type`: Transfer type.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.stop_transfer("daemon-uuid", "instance-uuid", "worldedit.jar", "mod")
```

### _method_ `config_files(daemonId: str, uuid: str, modId: str, type: str, fileName: str)`

Get configuration files for a mod.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `modId`: Mod identifier.
- `type`: Mod type.
- `fileName`: Config file name.

#### Returns

- `Any`

#### Example

```python
configs = await api.config_files("daemon-uuid", "instance-uuid", "worldedit", "mod", "config.yml")
```

### _method_ `toggle(daemonId: str, uuid: str, fileName: str)`

Toggle a mod enabled/disabled.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `fileName`: File name of the mod to toggle.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.toggle("daemon-uuid", "instance-uuid", "worldedit.jar")
```

### _method_ `delete(daemonId: str, uuid: str, fileName: str)`

Delete a mod.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `fileName`: File name of the mod to delete.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.delete("daemon-uuid", "instance-uuid", "worldedit.jar")
```

### _method_ `batch_info(hashes: list[str])`

Get information for multiple mods by their hashes in batch.

#### Parameters

- `hashes`: List of mod file hashes.

#### Returns

- `Any`

#### Example

```python
infos = await api.batch_info(["hash1", "hash2", "hash3"])
```