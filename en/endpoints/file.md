# File

## _class_ `File`

Get subclasses for file operations.

```python
api = mcsm.file
```

---

### _method_ `show(daemonId: str, uuid: str, target: str = ".", page: int = 0, page_size: int = 100, file_name: str = "")`

Get the file list.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `target`: Target directory path, defaults to `"."`.
- `page`: Page number for pagination, defaults to 0.
- `page_size`: Page size, defaults to 100.
- `file_name`: Filter files or folders whose names contain the specified string.

#### Returns

- `FileList`

#### Example

```python
files = await api.show("daemon-uuid", "instance-uuid", target="/")
for f in files.items:
    print(f.name, f.size)
```

### _method_ `status(daemonId: str, uuid: str)`

Get the file management status of an instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.

#### Returns

- `dict[str, Any]`

#### Example

```python
status = await api.status("daemon-uuid", "instance-uuid")
```

### _method_ `content(daemonId: str, uuid: str, target: str)`

Get file content.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `target`: Target file path.

#### Returns

- `str`: Content of the file.

#### Example

```python
text = await api.content("daemon-uuid", "instance-uuid", "/server.properties")
print(text)
```

### _method_ `update(daemonId: str, uuid: str, target: str, text: str)`

Update file content.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `target`: Target file path.
- `text`: New file content.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.update("daemon-uuid", "instance-uuid", "/server.properties", "max-players=50\n")
```

### _method_ `chmod(daemonId: str, uuid: str, target: str, chmod: int, deep: bool = False)`

Change file permissions.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `target`: Target file or folder path.
- `chmod`: Permission mode (e.g. `755`).
- `deep`: Whether to apply recursively, defaults to `False`.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.chmod("daemon-uuid", "instance-uuid", "/start.sh", 755)
```

### _method_ `chmod_batch(daemonId: str, uuid: str, targets: list[str], chmod: int, deep: bool = False)`

Change permissions for multiple files or folders.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `targets`: List of target file or folder paths.
- `chmod`: Permission mode.
- `deep`: Whether to apply recursively, defaults to `False`.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.chmod_batch("daemon-uuid", "instance-uuid", ["/start.sh", "/stop.sh"], 755)
```

### _method_ `download(daemonId: str, uuid: str, file_name: str)`

Get a download URL for a file.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `file_name`: Full path within the instance of the file to download, e.g. `/backup/world.zip`.

#### Returns

- `str`: File download URL.

#### Example

```python
url = await api.download("daemon-uuid", "instance-uuid", "/backup/world.zip")
print("Download URL:", url)
```

### _method_ `upload(daemonId: str, uuid: str, file: bytes, upload_dir: str)`

Upload a file.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `file`: Content of the file to upload.
- `upload_dir`: Target directory to upload the file to.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
with open("plugin.jar", "rb") as f:
    await api.upload("daemon-uuid", "instance-uuid", f.read(), "/plugins")
```

### _method_ `copy_to(daemonId: str, uuid: str, copy_map: dict[str, str])`

Copy multiple files or folders to specified locations.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `copy_map`: Copy mapping, format: `{source_path: target_path}`.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.copy_to("daemon-uuid", "instance-uuid", {
    "/world": "/backup/world",
    "/config.yml": "/backup/config.yml"
})
```

### _method_ `copyOne(daemonId: str, uuid: str, source: str, target: str)`

Copy a single file or folder.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `source`: Source path.
- `target`: Target path.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.copyOne("daemon-uuid", "instance-uuid", "/world", "/backup/world")
```

### _method_ `move(daemonId: str, uuid: str, copy_map: dict[str, str])`

Move multiple files or folders to specified locations.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `copy_map`: Move mapping, format: `{source_path: target_path}`.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.move("daemon-uuid", "instance-uuid", {
    "/old_world": "/worlds/old_world"
})
```

### _method_ `moveOne(daemonId: str, uuid: str, source: str, target: str)`

Move a single file or folder.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `source`: Source path.
- `target`: Target path.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.moveOne("daemon-uuid", "instance-uuid", "/world", "/worlds/world")
```

### _method_ `rename(daemonId: str, uuid: str, source: str, new_name: str)`

Rename a file or folder.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `source`: Path of the source file or folder.
- `new_name`: New name.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.rename("daemon-uuid", "instance-uuid", "/world", "world_backup")
```

### _method_ `zip(daemonId: str, uuid: str, source: str, targets: list[str])`

Compress files or folders.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `source`: Target archive file path.
- `targets`: Paths of the files to compress.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.zip("daemon-uuid", "instance-uuid", "/backup.zip", ["/world", "/config.yml"])
```

### _method_ `unzip(daemonId: str, uuid: str, source: str, targets: str, code: Literal["utf-8", "gbk", "big5"] = "utf-8")`

Unzip a file to the target location.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `source`: Path of the zip file.
- `targets`: Target directory to unzip to.
- `code`: Encoding of the compressed file, defaults to `"utf-8"`.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.unzip("daemon-uuid", "instance-uuid", "/backup.zip", "/restored")
```

### _method_ `delete(daemonId: str, uuid: str, targets: list[str])`

Delete files or folders.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `targets`: Paths of the files or folders to delete.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.delete("daemon-uuid", "instance-uuid", ["/old_logs", "/temp"])
```

### _method_ `createFile(daemonId: str, uuid: str, target: str)`

Create a file.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `target`: File path including filename.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.createFile("daemon-uuid", "instance-uuid", "/config/custom.yml")
```

### _method_ `download_from_url(daemonId: str, uuid: str, url: str, file_name: str)`

Download a file from a URL to the instance.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `url`: URL to download from.
- `file_name`: Target file name to save as.

#### Returns

- `str`: Task ID for the download.

#### Example

```python
task_id = await api.download_from_url("daemon-uuid", "instance-uuid", "https://example.com/plugin.jar", "plugin.jar")
```

### _method_ `download_from_url_stop(daemonId: str, uuid: str, taskId: str)`

Stop a URL download task.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `taskId`: Task ID returned by `download_from_url`.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.download_from_url_stop("daemon-uuid", "instance-uuid", "task-id")
```

### _method_ `createFolder(daemonId: str, uuid: str, target: str)`

Create a folder.

#### Parameters

- `daemonId`: UUID of the daemon.
- `uuid`: UUID of the instance.
- `target`: Target folder path.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.createFolder("daemon-uuid", "instance-uuid", "/backups")
```