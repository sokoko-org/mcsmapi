from typing import Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.user import SearchUserModel, UserCreateResult


class User:
    @staticmethod
    async def search(
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
        result = await send(
            "GET",
            f"{ApiPool.AUTH}/search",
            params={
                "userName": username,
                "page": page,
                "pageSize": page_size,
                "role": role,
            },
        )
        return SearchUserModel(**result)

    @staticmethod
    async def create(username: str, password: str, permission: int = 1) -> UserCreateResult:
        """
        创建用户

        :params username: 用户名
        :params password: 密码
        :params permission: 权限等级
        """
        result = await send(
            "POST",
            ApiPool.AUTH,
            data={"username": username, "password": password, "permission": permission},
        )
        return UserCreateResult(**result)

    @staticmethod
    async def update(uuid: str, config: dict[str, Any]) -> bool:
        """
        更新用户信息（部分更新）

        :params uuid: 用户UUID
        :params config: 要修改的字段
        """
        return await send(
            "PUT",
            ApiPool.AUTH,
            data={"uuid": uuid, "config": config},
        )

    @staticmethod
    async def delete(uuids: list[str]) -> bool:
        """
        删除用户

        :params uuids: 用户UUID列表
        """
        return await send("DELETE", ApiPool.AUTH, data=uuids)