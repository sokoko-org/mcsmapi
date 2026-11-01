from __future__ import annotations
from enum import IntEnum
from typing import TYPE_CHECKING, Any, Literal
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr, field_validator
import posixpath

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
    """节点UUID（由 SDK 注入，API 不返回）"""
    uuid: str = ""
    """实例UUID（由 SDK 注入，API 不返回）"""
    target: str = ""
    """所在路径（由 SDK 注入，API 不返回）"""

    def __init__(self, _req: Request | None = None, **data: Any):
        super().__init__(**data)
        self._req = _req

    async def rename(self, newName: str):
        """重命名"""
        from mcsmapi.apis.file import File

        return await File(self._req).rename(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name), newName
        )

    async def delete(self):
        """删除"""
        from mcsmapi.apis.file import File

        return await File(self._req).delete(
            self.daemonId, self.uuid, [posixpath.join(self.target, self.name)]
        )

    async def copy_to(self, target: str):
        """复制到目标路径"""
        from mcsmapi.apis.file import File

        return await File(self._req).copyOne(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name), target
        )

    async def move(self, target: str):
        """移动到目标路径"""
        from mcsmapi.apis.file import File

        return await File(self._req).moveOne(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name), target
        )

    async def content(self):
        """获取文件内容"""
        from mcsmapi.apis.file import File

        return await File(self._req).content(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name)
        )

    async def zip(self, targets: list[str]):
        """压缩到指定位置"""
        from mcsmapi.apis.file import File

        return await File(self._req).zip(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name), targets
        )

    async def unzip(self, target: str, code: Literal["utf-8", "gbk", "big5"] = "utf-8"):
        """解压到目标路径"""
        from mcsmapi.apis.file import File

        return await File(self._req).unzip(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name), target, code
        )

    async def update(self, text: str):
        """更新文件内容"""
        from mcsmapi.apis.file import File

        return await File(self._req).update(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name), text
        )

    async def download(self):
        """获取下载URL"""
        from mcsmapi.apis.file import File

        return await File(self._req).download(
            self.daemonId, self.uuid, posixpath.join(self.target, self.name)
        )


class FileList(BaseModel):
    """文件列表

    API 返回的字段: items, page, pageSize, total, absolutePath
    SDK 注入的字段: daemonId, uuid（用于模型辅助方法）
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    _req: Any = PrivateAttr(default=None)
    _target: str = PrivateAttr(default="")

    # daemonId/uuid 必须定义在 items 之前，Pydantic v2 的 field_validator
    # 在 mode='before' 时 info.data 只包含已验证的字段
    daemonId: str = ""
    """节点UUID（由 SDK 注入）"""
    uuid: str = ""
    """实例UUID（由 SDK 注入）"""
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

    def __init__(
        self,
        _req: Request | None = None,
        _target: str = "",
        **data: Any,
    ):
        super().__init__(**data)
        self._req = _req
        self._target = _target
        # 向子 FileItem 注入 _req 和 target
        for item in self.items:
            item._req = _req
            item.target = _target

    @field_validator("items", mode="before")
    @classmethod
    def fill_info(cls, v: Any, info) -> Any:
        """在验证 items 字段前，将 SDK 注入的 daemonId/uuid 填充到每个 FileItem"""
        if isinstance(info.data, dict):
            daemon_id = info.data.get("daemonId", "")
            uuid = info.data.get("uuid", "")
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        item["daemonId"] = daemon_id
                        item["uuid"] = uuid
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


class RemoteMappingEndpoint(BaseModel):
    """远程映射端点"""
    addr: str = ""
    prefix: str = ""


class RemoteMappingEntry(BaseModel):
    """远程映射条目 (from -> to)"""
    from_: RemoteMappingEndpoint = Field(default_factory=RemoteMappingEndpoint, alias="from")
    to: RemoteMappingEndpoint = Field(default_factory=RemoteMappingEndpoint)

    model_config = ConfigDict(populate_by_name=True)


class FileDownloadConfig(BaseModel):
    """文件下载配置"""

    password: str
    """文件下载密码"""
    addr: str
    """文件下载地址"""
    remoteMappings: list[RemoteMappingEntry] = []
    """远程端口映射"""


class StreamChannelResult(BaseModel):
    """数据流通道信息"""

    password: str
    """通道密码"""
    addr: str
    """通道地址"""
    prefix: str = ""
    """路径前缀"""
    remoteMappings: list[RemoteMappingEntry] = []
    """远程端口映射"""
