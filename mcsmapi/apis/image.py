from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.image import DockerImageItem, DockerContainerItem, DockerNetworkItem


class Image:
    @staticmethod
    async def images(daemonId: str) -> list[DockerImageItem]:
        """
        获取镜像列表

        :params daemonId: 节点的UUID
        """
        result = await send(
            "GET",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId},
        )
        return [DockerImageItem(**item) for item in result]

    @staticmethod
    async def containers(daemonId: str) -> list[DockerContainerItem]:
        """
        获取容器列表

        :params daemonId: 节点的UUID
        """
        result = await send(
            "GET",
            f"{ApiPool.IMAGE}/containers",
            params={"daemonId": daemonId},
        )
        return [DockerContainerItem(**item) for item in result]

    @staticmethod
    async def network(daemonId: str) -> list[DockerNetworkItem]:
        """
        获取网络接口列表

        :params daemonId: 节点的UUID
        """
        result = await send(
            "GET",
            f"{ApiPool.IMAGE}/networkModes",
            params={"daemonId": daemonId},
        )
        return [DockerNetworkItem(**item) for item in result]

    @staticmethod
    async def add(daemonId: str, dockerFile: str, name: str, tag: str) -> bool:
        """
        新增一个镜像

        :params daemonId: 节点的UUID
        :params dockerFile: DockerFile 内容
        :params name: 镜像名称
        :params tag: 镜像版本
        """
        return await send(
            "POST",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId},
            data={"dockerFile": dockerFile, "name": name, "tag": tag},
        )

    @staticmethod
    async def delete(daemonId: str, imageId: str) -> bool:
        """
        删除指定镜像

        :params daemonId: 节点的UUID
        :params imageId: 镜像 ID
        """
        return await send(
            "DELETE",
            f"{ApiPool.IMAGE}/image",
            params={"daemonId": daemonId, "imageId": imageId},
        )

    @staticmethod
    async def progress(daemonId: str) -> dict[str, int]:
        """
        获取镜像构建进度

        :params daemonId: 节点的UUID

        :returns: {容器名称: 当前状态} (-1: 失败, 1: 构建中, 2: 完成)
        """
        return await send(
            "GET",
            f"{ApiPool.IMAGE}/progress",
            params={"daemonId": daemonId},
        )