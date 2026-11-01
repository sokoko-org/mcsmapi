from __future__ import annotations
from typing import TYPE_CHECKING
from mcsmapi.pool import ApiPool
from typing import Any
from mcsmapi.models.image import DockerImageItem, DockerContainerItem, DockerNetworkItem

if TYPE_CHECKING:
    from mcsmapi.request import Request


class Image:
    def __init__(self, req: Request):
        self._req = req

    async def images(self, daemonId: str) -> list[DockerImageItem]:
        """
        获取镜像列表

        :params daemonId: 节点的UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId},
        )
        return [DockerImageItem(**item) for item in result]

    async def containers(self, daemonId: str) -> list[DockerContainerItem]:
        """
        获取容器列表

        :params daemonId: 节点的UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.IMAGE}/containers",
            params={"daemonId": daemonId},
        )
        return [DockerContainerItem(**item) for item in result]

    async def network(self, daemonId: str) -> list[DockerNetworkItem]:
        """
        获取网络接口列表

        :params daemonId: 节点的UUID
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.IMAGE}/networkModes",
            params={"daemonId": daemonId},
        )
        return [DockerNetworkItem(**item) for item in result]

    async def add(self, daemonId: str, dockerFile: str, name: str, tag: str) -> bool:
        """
        新增一个镜像

        :params daemonId: 节点的UUID
        :params dockerFile: DockerFile 内容
        :params name: 镜像名称
        :params tag: 镜像版本
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId},
            data={"dockerFile": dockerFile, "name": name, "tag": tag},
        )

    async def delete(self, daemonId: str, imageId: str) -> bool:
        """
        删除指定镜像

        :params daemonId: 节点的UUID
        :params imageId: 镜像 ID
        """
        return await self._req.send(
            "DELETE",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId, "imageId": imageId},
        )

    async def progress(self, daemonId: str) -> dict[str, int]:
        """
        获取镜像构建进度

        :params daemonId: 节点的UUID

        :returns: {容器名称: 当前状态} (-1: 失败, 1: 构建中, 2: 完成)
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.IMAGE}/progress",
            params={"daemonId": daemonId},
        )

    async def image_platforms(self, daemonId: str, imageName: str) -> Any:
        """
        获取镜像支持的平台架构（通过节点查询）

        :params daemonId: 节点的UUID
        :params imageName: 镜像名称
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.IMAGE}/image_platforms",
            params={"daemonId": daemonId},
            data={"imageName": imageName},
        )

    async def dockerhub_image_platforms(self, imageName: str) -> list[str]:
        """
        获取 DockerHub 镜像支持的平台架构（面板代理请求）

        :params imageName: 镜像名称 (如 ubuntu:latest)
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.IMAGE}/dockerhub_image_platforms",
            data={"imageName": imageName},
        )
