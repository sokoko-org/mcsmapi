from pydantic import BaseModel


class UpgradeInfo(BaseModel):
    """面板/节点更新信息"""

    configured: bool
    """是否配置了更新源"""
    currentVersion: str
    """当前版本"""
    onlineVersion: str | None = None
    """在线最新版本"""
    onlineNotes: str | dict[str, str] | None = None
    """更新日志（字符串或 {locale: text} 字典）"""
    updateAvailable: bool
    """是否有可用更新"""
    updateSourceUrl: str = ""
    """使用的更新源地址"""
    error: str | None = None
    """获取更新信息时的错误"""


class UpgradeResult(BaseModel):
    """更新执行结果"""

    started: bool
    """是否已开始更新"""
    onlineVersion: str | None = None
    """更新的目标版本"""
    message: str | None = None
    """结果消息"""
