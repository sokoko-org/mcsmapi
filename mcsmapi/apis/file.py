from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.models.file import FileDownloadConfig, FileList
import urllib.parse
import posixpath

if TYPE_CHECKING:
    from mcsmapi.request import Request


class File:
    def __init__(self, req: Request):
        self._req = req

    async def show(
        self,
        daemonId: str,
        uuid: str,
        target: str = ".",
        page: int = 0,
        page_size: int = 100,
        file_name: str = "",
    ) -> FileList:
        """
        获取文件列表

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 目标路径
        :params page: 页码
        :params page_size: 每页数量
        :params file_name: 文件名过滤
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.FILE}/list",
            params={
                "daemonId": daemonId,
                "uuid": uuid,
                "target": target,
                "page": page,
                "page_size": page_size,
                "file_name": file_name,
            },
        )
        # API 不返回 daemonId/uuid/target，由 SDK 注入以支持模型辅助方法
        return FileList(
            **result,
            daemonId=daemonId,
            uuid=uuid,
            _target=target,
            _req=self._req,
        )

    async def status(self, daemonId: str, uuid: str) -> dict[str, Any]:
        """
        获取文件管理器状态

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        """
        return await self._req.send(
            "GET",
            f"{ApiPool.FILE}/status",
            params={"daemonId": daemonId, "uuid": uuid},
        )

    async def content(self, daemonId: str, uuid: str, target: str) -> str:
        """
        获取文件内容

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 文件路径
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.FILE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )

    async def update(self, daemonId: str, uuid: str, target: str, text: str) -> bool:
        """
        更新文件内容

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 文件路径
        :params text: 新的文件内容
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.FILE}",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target, "text": text},
        )

    async def chmod(self, daemonId: str, uuid: str, target: str, chmod: int, deep: bool = False) -> bool:
        """
        修改文件权限 (仅 Linux)

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 文件路径
        :params chmod: 权限值 (如 755)
        :params deep: 是否递归修改
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.FILE}/chmod",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target, "chmod": chmod, "deep": deep},
        )

    async def chmod_batch(
        self, daemonId: str, uuid: str, targets: list[str], chmod: int, deep: bool = False
    ) -> bool:
        """
        批量修改文件权限 (仅 Linux)

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params targets: 文件路径列表
        :params chmod: 权限值 (如 755)
        :params deep: 是否递归修改
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.FILE}/chmod_batch",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets, "chmod": chmod, "deep": deep},
        )

    async def download(self, daemonId: str, uuid: str, file_name: str) -> str:
        """
        下载文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params file_name: 文件的实例内完整路径, eg: /backup/world.zip

        :returns: 文件下载URL
        """
        result = await self._req.send(
            "POST",
            f"{ApiPool.FILE}/download",
            params={"daemonId": daemonId, "uuid": uuid, "file_name": file_name},
        )
        result = FileDownloadConfig(**result)
        protocol = self._req.mcsm_url.split("://")[0]
        return f"{protocol}://{result.addr}/download/{result.password}/{urllib.parse.quote(file_name, safe='/')}"

    async def upload(self, daemonId: str, uuid: str, file: bytes, upload_dir: str) -> bool:
        """
        上传文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params file: 文件内容
        :params upload_dir: 上传目标路径
        """
        result = await self._req.send(
            "POST",
            f"{ApiPool.FILE}/upload",
            params={"daemonId": daemonId, "uuid": uuid, "upload_dir": upload_dir},
        )
        protocol = self._req.mcsm_url.split("://")[0]
        url = urllib.parse.urljoin(
            f"{protocol}://{result['addr']}",
            f"/upload/{result['password']}",
        )
        return await self._req.upload(url, file)

    async def copy_to(self, daemonId: str, uuid: str, copy_map: dict[str, str]) -> bool:
        """
        复制多个文件或文件夹到指定位置

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params copy_map: 复制映射 {源路径: 目标路径}
        """
        targets = [[source, target] for source, target in copy_map.items()]
        return await self._req.send(
            "POST",
            f"{ApiPool.FILE}/copy",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    async def copyOne(self, daemonId: str, uuid: str, source: str, target: str) -> bool:
        """
        复制单个文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 源路径
        :params target: 目标路径
        """
        return await self.copy_to(daemonId, uuid, {source: target})

    async def move(self, daemonId: str, uuid: str, copy_map: dict[str, str]) -> bool:
        """
        移动多个文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params copy_map: 移动映射 {源路径: 目标路径}
        """
        targets = [[source, target] for source, target in copy_map.items()]
        return await self._req.send(
            "PUT",
            f"{ApiPool.FILE}/move",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    async def moveOne(self, daemonId: str, uuid: str, source: str, target: str) -> bool:
        """
        移动单个文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 源路径
        :params target: 目标路径
        """
        return await self.move(daemonId, uuid, {source: target})

    async def rename(self, daemonId: str, uuid: str, source: str, new_name: str) -> bool:
        """
        重命名文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 源路径
        :params new_name: 新名称
        """
        directory = posixpath.dirname(source)
        target = posixpath.join(directory, new_name)
        return await self.moveOne(daemonId, uuid, source, target)

    async def zip(self, daemonId: str, uuid: str, source: str, targets: list[str]) -> bool:
        """
        压缩文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: 压缩后的文件路径
        :params targets: 需要压缩的文件路径列表
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.FILE}/compress",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"type": 1, "code": "utf-8", "source": source, "targets": targets},
        )

    async def unzip(
        self,
        daemonId: str,
        uuid: str,
        source: str,
        targets: str,
        code: Literal["utf-8", "gbk", "big5"] = "utf-8",
    ) -> bool:
        """
        解压缩 zip 文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params source: zip 文件路径
        :params targets: 解压目标路径
        :params code: 编码方式
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.FILE}/compress",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"type": 2, "code": code, "source": source, "targets": targets},
        )

    async def delete(self, daemonId: str, uuid: str, targets: list[str]) -> bool:
        """
        删除文件或文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params targets: 要删除的路径列表
        """
        return await self._req.send(
            "DELETE",
            ApiPool.FILE,
            params={"daemonId": daemonId, "uuid": uuid},
            data={"targets": targets},
        )

    async def createFile(self, daemonId: str, uuid: str, target: str) -> bool:
        """
        创建文件

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 文件路径
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.FILE}/touch",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )

    async def download_from_url(
        self,
        daemonId: str,
        uuid: str,
        url: str,
        file_name: str,
    ) -> str:
        """
        从 URL 下载文件到实例

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params url: 下载地址
        :params file_name: 保存的文件名

        :returns: 下载任务 ID
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.FILE}/download_from_url",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"url": url, "file_name": file_name},
        )

    async def download_from_url_stop(
        self,
        daemonId: str,
        uuid: str,
        taskId: str,
    ) -> bool:
        """
        停止从 URL 下载文件的任务

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params taskId: 下载任务 ID
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.FILE}/download_from_url_stop",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"taskId": taskId},
        )

    async def createFolder(self, daemonId: str, uuid: str, target: str) -> bool:
        """
        创建文件夹

        :params daemonId: 节点的UUID
        :params uuid: 实例的UUID
        :params target: 文件夹路径
        """
        return await self._req.send(
            "POST",
            f"{ApiPool.FILE}/mkdir",
            params={"daemonId": daemonId, "uuid": uuid},
            data={"target": target},
        )
