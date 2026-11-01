from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.models.user import SearchUserModel, UserCreateResult

if TYPE_CHECKING:
    from mcsmapi.request import Request


class User:
    def __init__(self, req: Request):
        self._req = req

    async def info(self, advanced: bool = False) -> dict[str, Any]:
        """
        获取当前登录用户信息

        :params advanced: 是否返回高级数据（实例详情等）
        """
        return await self._req.send(
            "GET",
            ApiPool.AUTH,
            params={"advanced": str(advanced).lower()},
        )

    async def search(
        self,
        username: str = "",
        page: int = 1,
        page_size: int = 20,
        role: Literal[-1, 1, 10, ""] = "",
    ) -> SearchUserModel:
        """
        搜索用户（管理员）

        :params username: 用户名过滤，为空列出全部
        :params page: 页码
        :params page_size: 每页条数
        :params role: 权限过滤
        """
        result = await self._req.send(
            "GET",
            f"{ApiPool.AUTH}/search",
            params={
                "userName": username,
                "page": page,
                "pageSize": page_size,
                "role": role,
            },
        )
        return SearchUserModel(**result, _req=self._req)

    async def overview(self) -> list[dict[str, Any]]:
        """获取全部用户概览列表（管理员）"""
        return await self._req.send("GET", f"{ApiPool.AUTH}/overview")

    async def create(self, username: str, password: str, permission: int = 1) -> UserCreateResult:
        """
        创建用户（管理员）

        :params username: 用户名
        :params password: 密码
        :params permission: 权限等级
        """
        result = await self._req.send(
            "POST",
            ApiPool.AUTH,
            data={"username": username, "password": password, "permission": permission},
        )
        return UserCreateResult(**result)

    async def update(self, uuid: str, config: dict[str, Any]) -> bool:
        """
        更新用户信息（管理员，部分更新）

        :params uuid: 用户UUID
        :params config: 要修改的字段
        """
        return await self._req.send(
            "PUT",
            ApiPool.AUTH,
            data={"uuid": uuid, "config": config},
        )

    async def update_password(self, password: str) -> bool:
        """
        修改当前登录用户的密码

        :params password: 新密码
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.AUTH}/update",
            data={"passWord": password},
        )

    async def toggle_apikey(self, enable: bool) -> str:
        """
        生成或关闭当前用户的 API Key

        :params enable: True 生成新 Key，False 关闭
        :returns: 新 API Key（关闭时返回空字符串）
        """
        return await self._req.send(
            "PUT",
            f"{ApiPool.AUTH}/api",
            data={"enable": enable},
        )

    async def delete(self, uuids: list[str]) -> bool:
        """
        批量删除用户（管理员）

        :params uuids: 用户UUID列表
        """
        return await self._req.send("DELETE", ApiPool.AUTH, data=uuids)
