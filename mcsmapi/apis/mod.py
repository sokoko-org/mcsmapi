from __future__ import annotations
from typing import TYPE_CHECKING, Any
from mcsmapi.pool import ApiPool
if TYPE_CHECKING:
    from mcsmapi.request import Request


class Mod:
    def __init__(self, req: Request):
        self._req = req

    async def mc_versions(self) -> Any:
        """
        获取 Minecraft 版本列表
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.MOD}/mc_versions",
        )

    async def list(
        self,
        daemonId: str,
        uuid: str,
        page: int = 1,
        pageSize: int = 50,
        folder: str | None = None,
        search: str | None = None,
    ) -> Any:
        """
        获取实例 Mod 列表

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param page: 页码
        :param pageSize: 每页数量
        :param folder: 文件夹路径
        :param search: 搜索关键词
        """
        params: dict[str, Any] = {
            "daemonId": daemonId,
            "uuid": uuid,
            "page": page,
            "pageSize": pageSize,
        }
        if folder is not None:
            params["folder"] = folder
        if search is not None:
            params["search"] = search
        return await self._req.send(
            "GET",
            f"{ApiPool.MOD}/list",
            params=params,
        )

    async def info(self, hash: str) -> Any:
        """
        获取 Mod 详细信息

        :param hash: Mod 文件哈希值
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.MOD}/info",
            params={"hash": hash},
        )

    async def search(
        self,
        query: str = "",
        offset: int = 0,
        limit: int = 20,
        source: str = "all",
        version: str = "",
        type: str = "all",
        loader: str = "all",
        environment: str = "all",
    ) -> Any:
        """
        搜索 Mod 资源

        :param query: 搜索关键词
        :param offset: 偏移量
        :param limit: 返回数量
        :param source: 资源来源
        :param version: Minecraft 版本
        :param type: 资源类型
        :param loader: 模组加载器
        :param environment: 运行环境
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.MOD}/search",
            params={
                "query": query,
                "offset": offset,
                "limit": limit,
                "source": source,
                "version": version,
                "type": type,
                "loader": loader,
                "environment": environment,
            },
        )

    async def versions(self, projectId: str, source: str = "Modrinth") -> Any:
        """
        获取 Mod 项目的版本列表

        :param projectId: 项目ID
        :param source: 资源来源
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.MOD}/versions",
            params={"projectId": projectId, "source": source},
        )

    async def download(
        self,
        daemonId: str,
        uuid: str,
        url: str,
        fileName: str,
        projectType: str,
        fallbackUrl: str | None = None,
        extraInfo: Any | None = None,
    ) -> Any:
        """
        下载 Mod 文件到实例

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param url: 下载地址
        :param fileName: 文件名
        :param projectType: 项目类型
        :param fallbackUrl: 备用下载地址
        :param extraInfo: 附加信息
        """
        body: dict[str, Any] = {
            "daemonId": daemonId,
            "uuid": uuid,
            "url": url,
            "fileName": fileName,
            "projectType": projectType,
        }
        if fallbackUrl is not None:
            body["fallbackUrl"] = fallbackUrl
        if extraInfo is not None:
            body["extraInfo"] = extraInfo
        return await self._req.send(
            "POST",
            f"{ApiPool.MOD}/download",
            data=body,
        )

    async def stop_transfer(
        self,
        daemonId: str,
        uuid: str,
        fileName: str,
        type: str,
    ) -> Any:
        """
        停止文件传输任务

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param fileName: 文件名
        :param type: 任务类型
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.MOD}/stop_transfer",
            data={
                "daemonId": daemonId,
                "uuid": uuid,
                "fileName": fileName,
                "type": type,
            },
        )

    async def config_files(
        self,
        daemonId: str,
        uuid: str,
        modId: str,
        type: str,
        fileName: str,
    ) -> Any:
        """
        获取 Mod 配置文件列表

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param modId: Mod ID
        :param type: 类型
        :param fileName: 文件名
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.MOD}/config_files",
            params={
                "daemonId": daemonId,
                "uuid": uuid,
                "modId": modId,
                "type": type,
                "fileName": fileName,
            },
        )

    async def toggle(self, daemonId: str, uuid: str, fileName: str) -> Any:
        """
        启用/禁用 Mod

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param fileName: 文件名
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.MOD}/toggle",
            data={
                "daemonId": daemonId,
                "uuid": uuid,
                "fileName": fileName,
            },
        )

    async def delete(self, daemonId: str, uuid: str, fileName: str) -> Any:
        """
        删除 Mod 文件

        :param daemonId: 节点ID
        :param uuid: 实例ID
        :param fileName: 文件名
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.MOD}/delete",
            data={
                "daemonId": daemonId,
                "uuid": uuid,
                "fileName": fileName,
            },
        )

    async def batch_info(self, hashes: list[str]) -> Any:
        """
        批量获取 Mod 信息

        :param hashes: Mod 文件哈希值列表
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.MOD}/batch_info",
            data={"hashes": hashes},
        )
