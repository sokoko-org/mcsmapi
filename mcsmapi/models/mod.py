from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class ModSearchHit(BaseModel):
    """Mod 搜索结果条目"""

    id: str = ""
    """项目 ID"""
    slug: str = ""
    """项目 slug"""
    title: str = ""
    """项目标题"""
    description: str = ""
    """项目简介"""
    icon_url: str = ""
    """图标 URL"""
    author: str = ""
    """作者"""
    downloads: int = 0
    """下载量"""
    updated: str = ""
    """最后更新时间"""
    categories: list[str] = []
    """分类列表"""
    version_number: str = ""
    """最新版本号"""
    game_versions: list[str] = []
    """支持的游戏版本"""
    display_categories: list[str] = []
    """显示分类"""
    source: str = ""
    """资源来源"""
    project_type: str = ""
    """项目类型"""


class ModSearchResult(BaseModel):
    """Mod 搜索结果"""

    hits: list[ModSearchHit] = []
    """搜索结果列表"""
    total_hits: int = 0
    """总匹配数"""


class ModVersionFile(BaseModel):
    """Mod 版本文件"""

    url: str = ""
    """下载地址"""
    filename: str = ""
    """文件名"""
    primary: bool = False
    """是否为主文件"""


class ModVersion(BaseModel):
    """Mod 版本信息"""

    id: str = ""
    """版本 ID"""
    name: str | None = None
    """版本名称"""
    version_number: str = ""
    """版本号"""
    game_versions: list[str] = []
    """支持的游戏版本"""
    loaders: list[str] = []
    """支持的加载器"""
    project_type: str = ""
    """项目类型"""
    files: list[ModVersionFile] = []
    """版本文件列表"""


class ModInfoDetail(BaseModel):
    """Mod 详细信息（通过哈希查询）"""

    version: Any = None
    """Modrinth 版本数据"""
    project: Any = None
    """Modrinth 项目数据"""


class ModFileItem(BaseModel):
    """实例 Mod 文件条目"""

    fileName: str = ""
    """文件名"""
    size: int = 0
    """文件大小（字节）"""
    enable: bool = True
    """是否启用"""
    hash: str = ""
    """文件哈希（sha1）"""


class ModListResult(BaseModel):
    """实例 Mod 列表"""

    items: list[ModFileItem] = []
    """Mod 文件列表"""
    page: int = 1
    """当前页"""
    pageSize: int = 50
    """每页大小"""
    total: int = 0
    """总数"""
