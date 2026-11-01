from typing import Any
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.overview import OverviewModel, LogDetail


class Overview:
    @staticmethod
    def overview() -> OverviewModel:
        """获取面板基本信息"""
        result = send("GET", ApiPool.OVERVIEW)
        return OverviewModel(**result)

    @staticmethod
    def logs(limit: int = 20) -> list[LogDetail]:
        """
        获取面板操作日志

        :params limit: 返回的日志条数 (1-200)
        """
        result = send("GET", ApiPool.LOG, params={"limit": limit})
        return [LogDetail(**item) for item in result]

    @staticmethod
    def log_search(
        page: int = 1,
        page_size: int = 20,
        type: str | None = None,
        level: str | None = None,
        operator_name: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        keyword: str | None = None,
    ) -> dict[str, Any]:
        """
        分页搜索操作日志

        :params page: 页码
        :params page_size: 每页条数 (1-100)
        :params type: 操作类型过滤
        :params level: 日志等级过滤 (info/warning/error)
        :params operator_name: 操作者用户名过滤
        :params start_time: 起始时间戳
        :params end_time: 结束时间戳
        :params keyword: 关键词搜索
        """
        params: dict[str, Any] = {"page": page, "page_size": page_size}
        if type is not None:
            params["type"] = type
        if level is not None:
            params["level"] = level
        if operator_name is not None:
            params["operator_name"] = operator_name
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
        if keyword is not None:
            params["keyword"] = keyword
        return send("GET", f"{ApiPool.LOG}/search", params=params)

    @staticmethod
    def setting() -> dict[str, Any]:
        """获取面板配置项 (管理员)"""
        return send("GET", f"{ApiPool.OVERVIEW}/setting")

    @staticmethod
    def update_setting(config: dict[str, Any]) -> str:
        """
        更新面板配置项（部分更新，只发送提供的字段）

        :params config: 要修改的配置字段
        """
        return send("PUT", f"{ApiPool.OVERVIEW}/setting", data=config)
