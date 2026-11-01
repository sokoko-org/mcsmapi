from __future__ import annotations
from enum import IntEnum
from typing import TYPE_CHECKING, Any, Literal
from pydantic import BaseModel, ConfigDict, PrivateAttr, field_validator
import os

if TYPE_CHECKING:
    from mcsmapi.request import Request


class FileType(IntEnum):
    """文件类型"""

    FOLDER = 0
    FILE = 1


class FileItem(BaseModel):
    """文件信息"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    _req: Any = PrivateAttr(default=None)

    name: str
    """文件名"""
    size: int
    """文件大小(字节)"""
    time: str
    """修改时间"""
    mode: int
    """权限 (仅 Linux)"""
    type: FileType
    """文件类型"""
    daemonId: str = ""
    """节点UUID"""
    uuid: str = ""
    """实例UUID"""
    target: str = ""
    """所在路径"""
    file_name: str
    """文件列表过滤条件"""

    def __init__(self, _req: Request | None = None, **data: Any):
        super().__init__(**data)
        self._req = _req

    async def rename(self, newName: str):
        """重命名"""
        from mcsmapi.apis.file import File

        return await File(self._req).rename(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), newName
        )

    async def delete(self):
        """删除"""
        from mcsmapi.apis.file import File

        return await File(self._req).delete(
            self.daemonId, self.uuid, [os.path.join(self.target, self.name)]
        )

    async def copy_to(self, target: str):
        """复制到目标路径"""
        from mcsmapi.apis.file import File

        return await File(self._req).copyOne(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target
        )

    async def move(self, target: str):
        """移动到目标路径"""
        from mcsmapi.apis.file import File

        return await File(self._req).moveOne(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target
        )

    async def content(self):
        """获取文件内容"""
        from mcsmapi.apis.file import File

        return await File(self._req).content(
            self.daemonId, self.uuid, os.path.join(self.target, self.name)
        )

    async def zip(self, targets: list[str]):
        """压缩到指定位置"""
        from mcsmapi.apis.file import File

        return await File(self._req).zip(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), targets
        )

    async def unzip(self, target: str, code: Literal["utf-8", "gbk", "big5"] = "utf-8"):
        """解压到目标路径"""
        from mcsmapi.apis.file import File

        return await File(self._req).unzip(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), target, code
        )

    async def update(self, text: str):
        """更新文件内容"""
        from mcsmapi.apis.file import File

        return await File(self._req).update(
            self.daemonId, self.uuid, os.path.join(self.target, self.name), text
        )

    async def download(self):
        """获取下载URL"""
        from mcsmapi.apis.file import File

        return await File(self._req).download(
            self.daemonId, self.uuid, os.path.join(self.target, self.name)
        )


class FileList(BaseModel):
    """文件列表"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    _req: Any = PrivateAttr(default=None)

    items: list[FileItem]
    """文件列表"""
    page: int
    """当前页"""
    pageSize: int
    """每页大小"""
    total: int
    """总数"""
    absolutePath: str
    """远程节点上的绝对路径"""
    daemonId: str
    """节点UUID"""
    uuid: str
    """实例UUID"""
    target: str
    """目录路径"""

    def __init__(self, _req: Request | None = None, **data: Any):
        super().__init__(**data)
        self._req = _req
        for item in self.items:
            item._req = _req

    @field_validator("items", mode="before")
    @classmethod
    def fill_info(cls, v: Any, info) -> Any:
        """在验证 items 字段前填充基本信息"""
        if isinstance(info.data, dict):
            daemon_id = info.data.get("daemonId", "")
            uuid = info.data.get("uuid", "")
            target = info.data.get("target", "")
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        item["daemonId"] = daemon_id
                        item["uuid"] = uuid
                        item["target"] = target
        return v

    async def upload(self, file: bytes, upload_dir: str) -> bool:
        """上传文件"""
        from mcsmapi.apis.file import File

        return await File(self._req).upload(self.daemonId, self.uuid, file, upload_dir)

    async def createFile(self, target: str) -> bool:
        """创建文件"""
        from mcsmapi.apis.file import File

        return await File(self._req).createFile(self.daemonId, self.uuid, target)

    async def createFolder(self, target: str) -> bool:
        """创建文件夹"""
        from mcsmapi.apis.file import File

        return await File(self._req).createFolder(self.daemonId, self.uuid, target)


class FileDownloadConfig(BaseModel):

    password: str
    """文件下载密码"""
    addr: str
    """文件下载地址"""
