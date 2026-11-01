# 镜像

## _class_ `Image`

获取操作镜像的子类

```python
api = mcsm.image
```

---

### _method_ `images(daemonId: str)`

获取镜像列表

#### 参数

- `daemonId`: 节点的 UUID

#### 返回

- `list[DockerImageItem]`: 镜像列表详情的模型列表

::: tip
详细定义参考 https://docs.docker.com/engine/api/v1.37/#tag/Image/operation/ImageList

字段含义以 Docker 文档为准
:::

### _method_ `containers(daemonId: str)`

获取容器列表

#### 参数

- `daemonId`: 节点的 UUID

#### 返回

- `list[DockerContainerItem]`: 容器列表详情的模型列表

::: tip
详细定义参考 https://docs.docker.com/engine/api/v1.37/#tag/Container/operation/ContainerList

字段含义以 Docker 文档为准
:::

### _method_ `network(daemonId: str)`

获取网络接口列表

#### 参数

- `daemonId`: 节点的 UUID

#### 返回

- `list[DockerNetworkItem]`: 网络接口列表详情的模型列表

::: tip
详细定义参考 https://docs.docker.com/engine/api/v1.37/#tag/Network/operation/NetworkList

字段含义以 Docker 文档为准
:::

### _method_ `add(daemonId: str, dockerFile: str, name: str, tag: str)`

新增一个镜像

#### 参数

- `daemonId`: 节点的 UUID
- `dockerFile`: Dockerfile 配置内容
- `name`: 镜像名称
- `tag`: 镜像版本标签

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.add("daemon-uuid", "FROM ubuntu:22.04", "myimage", "latest")
```

### _method_ `delete(daemonId: str, imageId: str)`

删除指定镜像

#### 参数

- `daemonId`: 节点的 UUID
- `imageId`: 镜像 ID

#### 返回

- `bool`: 操作成功后返回 True

#### 例子

```python
await api.delete("daemon-uuid", "sha256:abc123...")
```

### _method_ `progress(daemonId: str)`

获取镜像构建进度

#### 参数

- `daemonId`: 节点的 UUID

#### 返回

- `dict[str, int]`: `{容器名称: 当前状态}`

| 状态码 | 含义         |
| ------ | ------------ |
| -1     | 镜像构建失败 |
| 1      | 镜像构建中   |
| 2      | 镜像构建完成 |

### _method_ `image_platforms(daemonId: str, imageName: str)`

获取指定镜像支持的平台列表

#### 参数

- `daemonId`: 节点的 UUID
- `imageName`: 镜像名称

#### 返回

- `list`: 支持的平台列表

#### 例子

```python
platforms = await api.image_platforms("daemon-uuid", "ubuntu:22.04")
```

### _method_ `dockerhub_image_platforms(imageName: str)`

从 Docker Hub 获取指定镜像支持的平台列表

#### 参数

- `imageName`: 镜像名称

#### 返回

- `list`: 支持的平台列表

#### 例子

```python
platforms = await api.dockerhub_image_platforms("nginx:latest")
```