from __future__ import annotations
from enum import IntEnum
from typing import TYPE_CHECKING, Any
from pydantic import BaseModel, ConfigDict, PrivateAttr

if TYPE_CHECKING:
    from mcsmapi.request import Request


class UserPermission(IntEnum):
    """用户权限级别"""

    BANNED = -1
    USER = 1
    ADMIN = 10


class UserInstances(BaseModel):
    """用户实例信息"""

    instanceUuid: str
    """实例UUID"""
    daemonId: str
    """节点ID"""


class UserCreateResult(BaseModel):
    """用户创建结果"""

    uuid: str
    """用户UUID"""
    userName: str
    """用户名"""
    permission: UserPermission
    """用户权限级别"""


class UserModel(BaseModel):
    """用户信息模型"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    _req: Any = PrivateAttr(default=None)

    uuid: str = ""
    """用户UUID"""
    userName: str = ""
    """用户名"""
    loginTime: str = ""
    """最后登录时间"""
    registerTime: str = ""
    """注册时间"""
    instances: list[UserInstances] = []
    """用户拥有的实例列表"""
    permission: UserPermission = UserPermission.USER
    """用户权限级别"""
    passWord: str = ""
    """用户密码 (搜索接口返回空字符串)"""
    open2FA: bool = False
    """是否启用双因素认证"""
    apiKey: str = ""
    """用户 API 密钥 (搜索接口返回掩码值)"""
    isInit: bool = False
    """是否为初始化用户"""
    secret: str = ""
    """2FA 密钥 (搜索接口返回掩码值)"""

    def __init__(self, _req: Request | None = None, **data: Any):
        super().__init__(**data)
        self._req = _req

    async def delete(self):
        """删除该用户"""
        from mcsmapi.apis.user import User

        return await User(self._req).delete([self.uuid])

    async def update(self, config: dict[str, Any]):
        """
        更新该用户的信息（部分更新，只发送提供的字段）

        :params config: 要修改的字段
        """
        from mcsmapi.apis.user import User

        return await User(self._req).update(self.uuid, config)


class SearchUserModel(BaseModel):
    """用户搜索结果"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    _req: Any = PrivateAttr(default=None)

    total: int
    """匹配的用户总数"""
    page: int
    """当前页码"""
    page_size: int
    """每页返回的用户数量"""
    max_page: int
    """最大可用页数"""
    data: list[UserModel]
    """用户信息列表"""

    def __init__(self, _req: Request | None = None, **data: Any):
        super().__init__(**data)
        self._req = _req
        for user in self.data:
            user._req = _req
