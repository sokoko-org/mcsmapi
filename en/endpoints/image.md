# Image

## _class_ `Image`

Get subclasses for Docker image operations.

```python
api = mcsm.image
```

---

### _method_ `images(daemonId: str)`

Get the image list.

#### Parameters

- `daemonId`: UUID of the daemon.

#### Returns

- `list[DockerImageItem]`

::: tip
For detailed field definitions, refer to [Docker API — ImageList](https://docs.docker.com/engine/api/v1.37/#tag/Image/operation/ImageList).
:::

#### Example

```python
images = await api.images("daemon-uuid")
for img in images:
    print(img)
```

### _method_ `containers(daemonId: str)`

Get the container list.

#### Parameters

- `daemonId`: UUID of the daemon.

#### Returns

- `list[DockerContainerItem]`

::: tip
For detailed field definitions, refer to [Docker API — ContainerList](https://docs.docker.com/engine/api/v1.37/#tag/Container/operation/ContainerList).
:::

#### Example

```python
containers = await api.containers("daemon-uuid")
for c in containers:
    print(c)
```

### _method_ `network(daemonId: str)`

Get the network interface list.

#### Parameters

- `daemonId`: UUID of the daemon.

#### Returns

- `list[DockerNetworkItem]`

::: tip
For detailed field definitions, refer to [Docker API — NetworkList](https://docs.docker.com/engine/api/v1.37/#tag/Network/operation/NetworkList).
:::

#### Example

```python
networks = await api.network("daemon-uuid")
for n in networks:
    print(n)
```

### _method_ `add(daemonId: str, dockerFile: str, name: str, tag: str)`

Build a new image from a Dockerfile.

#### Parameters

- `daemonId`: UUID of the daemon.
- `dockerFile`: Dockerfile content.
- `name`: Image name.
- `tag`: Image tag/version.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.add("daemon-uuid", "FROM openjdk:17\nCOPY . /app", "my-server", "latest")
```

### _method_ `delete(daemonId: str, imageId: str)`

Delete an image.

#### Parameters

- `daemonId`: UUID of the daemon.
- `imageId`: ID of the image to delete.

#### Returns

- `bool`: Returns `True` after successful operation.

#### Example

```python
await api.delete("daemon-uuid", "sha256:abc123...")
```

### _method_ `progress(daemonId: str)`

Get the image build progress.

#### Parameters

- `daemonId`: UUID of the daemon.

#### Returns

- `dict[str, int]`: `{container_name: status_code}`

| Status Code | Meaning              |
| ----------- | -------------------- |
| -1          | Image build failed   |
| 1           | Image building       |
| 2           | Image build complete |

#### Example

```python
progress = await api.progress("daemon-uuid")
for name, status in progress.items():
    print(name, status)
```

### _method_ `image_platforms(daemonId: str, imageName: str)`

Get available platforms for a local image.

#### Parameters

- `daemonId`: UUID of the daemon.
- `imageName`: Name of the image.

#### Returns

- `Any`

#### Example

```python
platforms = await api.image_platforms("daemon-uuid", "openjdk:17")
```

### _method_ `dockerhub_image_platforms(imageName: str)`

Get available platforms for a Docker Hub image.

#### Parameters

- `imageName`: Name of the Docker Hub image (e.g. `"openjdk:17"`).

#### Returns

- `list[str]`

#### Example

```python
platforms = await api.dockerhub_image_platforms("openjdk:17")
for p in platforms:
    print(p)
```