from pydantic import BaseModel


class JavaInfo(BaseModel):
    """Java 运行环境信息"""

    fullname: str = ""
    """完整名称（name_version）"""
    name: str = ""
    """Java 名称"""
    path: str | None = None
    """Java 路径"""
    installTime: int = 0
    """安装时间（Unix 时间戳）"""
    downloading: bool = False
    """是否正在下载"""
    version: str | None = None
    """Java 版本"""


class JavaRuntime(BaseModel):
    """Java 运行环境"""

    info: JavaInfo
    """运行环境信息"""
    path: str = ""
    """运行环境目录路径"""
    usingInstances: list[str] = []
    """正在使用的实例UUID列表"""
