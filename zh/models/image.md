# 镜像模型

::: tip
Docker 相关模型详细定义参考:

- [Image API](https://docs.docker.com/engine/api/v1.37/#tag/Image/operation/ImageList)
- [Network API](https://docs.docker.com/engine/api/v1.37/#tag/Network/operation/NetworkList)
- [Container API](https://docs.docker.com/engine/api/v1.37/#tag/Container/operation/ContainerList)
:::

## _class_ `DockerConfig(BaseModel)`

Docker 容器配置

| 字段名 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `containerName` | str | "" | 容器名称 |
| `image` | str | "" | 镜像名称 |
| `updateCommandImage` | str | "HOST" | 更新命令使用的镜像 |
| `ports` | list[str] | [] | 端口映射, eg: ["25565:25565/tcp"] |
| `extraVolumes` | list[str] | [] | 额外挂载卷 |
| `memory` | int | 0 | 内存(MB) |
| `memorySwap` | int \| None | None | swap 内存(MB) |
| `memorySwappiness` | int \| None | None | 虚拟内存倾向(0-100) |
| `networkMode` | str | "bridge" | 网络模式 |
| `networkAliases` | list[str] | [] | 网络别名 |
| `maxSpace` | int | 0 | 最大磁盘空间(MB) |
| `network` | int | 0 | 网络限速 |
| `io` | int | 0 | IO 限制 |
| `cpusetCpus` | str | "" | 绑定 CPU 核心 |
| `cpuUsage` | int | 0 | CPU 限制(%) |
| `workingDir` | str | "/data" | 工作目录 |
| `env` | list[str] | [] | 环境变量 |
| `labels` | list[str] | [] | 容器标签 |
| `changeWorkdir` | bool | True | 是否更变默认工作目录 |
| `uploadSpeedLimit` | int | 0 | 上传速度限制 |
| `downloadSpeedLimit` | int | 0 | 下载速度限制 |
| `capAdd` | list[str] | [] | 添加的 capabilities |
| `capDrop` | list[str] | [] | 移除的 capabilities |
| `devices` | list[str] | [] | 映射设备 |
| `privileged` | bool | False | 特权模式 |
| `gpuEnabled` | bool | False | 启用 GPU |
| `gpuCount` | int | -1 | GPU 数量 (-1 全部) |
| `gpuDeviceIds` | list[str] | [] | GPU 设备 ID |
| `gpuDriver` | str | "nvidia" | GPU 驱动 |
| `deviceReadBps` | list[str] | [] | 设备读取速率限制 |
| `deviceWriteBps` | list[str] | [] | 设备写入速率限制 |

## _class_ `DockerImageItem(BaseModel)`

Docker 镜像信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `Id` | str | 镜像 ID |
| `ParentId` | str | 父镜像 ID |
| `RepoTags` | list[str] | 仓库标签 |
| `RepoDigests` | list[str] | 镜像摘要 |
| `Created` | int | 创建时间 |
| `Size` | int | 大小(字节) |
| `VirtualSize` | int | 虚拟大小 |
| `SharedSize` | int | 共享空间 |
| `Labels` | dict[str, str] | 标签 |
| `Containers` | int | 容器数量 |

## _class_ `DockerContainerItemPort(BaseModel)`

容器端口映射

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `PrivatePort` | int | 内部端口 |
| `PublicPort` | int \| None | 宿主机端口 |
| `Type` | Literal["tcp", "udp"] | 端口类型 |

## _class_ `DockerContainerItemNetworkSettingsNetwork(BaseModel)`

容器网络信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `NetworkID` | str | 网络 ID |
| `EndpointID` | str | 端点 ID |
| `Gateway` | str | 网关 |
| `IPAddress` | str | IP 地址 |
| `IPPrefixLen` | int | 前缀长度 |
| `IPv6Gateway` | str | IPv6 网关 |
| `GlobalIPv6Address` | str | IPv6 地址 |
| `GlobalIPv6PrefixLen` | int | IPv6 前缀长度 |
| `MacAddress` | str | MAC 地址 |

## _class_ `DockerContainerItemNetworkSettings(BaseModel)`

容器网络配置

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `Networks` | dict[str, ...Network] | 所有网络 |

## _class_ `DockerContainerItemMount(BaseModel)`

容器挂载点

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `Name` | str | 挂载名称 |
| `Source` | str | 源路径 |
| `Destination` | str | 目标路径 |
| `Driver` | str | 驱动 |
| `Mode` | str | 模式 |
| `RW` | bool | 读写 |
| `Propagation` | str | 传播模式 |

## _class_ `DockerContainerItemHostConfig(BaseModel)`

宿主机配置

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `NetworkMode` | str | 网络模式 |

## _class_ `DockerContainerItem(BaseModel)`

Docker 容器详细信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `Id` | str | 容器 ID |
| `Names` | list[str] | 名称列表 |
| `Image` | str | 镜像名称 |
| `ImageID` | str | 镜像 ID |
| `Command` | str | 启动命令 |
| `Created` | int | 创建时间 |
| `State` | str | 容器状态 |
| `Status` | str | 状态描述 |
| `Ports` | list[...Port] | 端口映射 |
| `Labels` | dict[str, str] | 标签 |
| `SizeRw` | int | 读写层大小 |
| `SizeRootFs` | int | 根文件系统大小 |
| `HostConfig` | ...HostConfig | 宿主机配置 |
| `NetworkSettings` | ...NetworkSettings | 网络配置 |
| `Mounts` | list[...Mount] | 挂载信息 |

## _class_ `DockerNetworkItemIPAMConfig(BaseModel)`

IPAM 配置

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `Subnet` | str | 子网地址 |

## _class_ `DockerNetworkItemIPAM(BaseModel)`

IPAM 管理

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `Driver` | str | 驱动类型 |
| `Config` | list[...IPAMConfig] | 配置 |

## _class_ `DockerNetworkItem(BaseModel)`

Docker 网络信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `Name` | str | 网络名称 |
| `Id` | str | 网络 ID |
| `Created` | str | 创建时间 |
| `Scope` | str | 作用范围 |
| `Driver` | str | 驱动类型 |
| `EnableIPv6` | bool | 启用 IPv6 |
| `Internal` | bool | 内部网络 |
| `Attachable` | bool | 可附加 |
| `Ingress` | bool | 入口网络 |
| `IPAM` | ...IPAM | IPAM 配置 |
| `Options` | dict[str, str] | 网络选项 |
| `Containers` | dict[str, dict] | 容器信息 |
