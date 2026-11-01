from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.models.user import SearchUserModel, UserCreateResult

if TYPE_CHECKING:
    from mcsmapi.request import Request


class User:
    def __init__(self, req: Request):
        self._req = req

    async def search(
        self,
        username: str = "",
        page: int = 1,
        page_size: int = 20,
        role: Literal[-1, 1, 10, ""] = "",
    ) -> SearchUserModel:
        """
        搜索用户

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

    async def create(self, username: str, password: str, permission: int = 1) -> UserCreateResult:
        """
        创建用户

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
        更新用户信息（部分更新）

        :params uuid: 用户UUID
        :params config: 要修改的字段
        """
        return await self._req.send(
            "PUT",
            ApiPool.AUTH,
            data={"uuid": uuid, "config": config},
        )

    async def delete(self, uuids: list[str]) -> bool:
        """
        删除用户

        :params uuids: 用户UUID列表
        """
        return await self._req.send("DELETE", ApiPool.AUTH, data=uuids)
