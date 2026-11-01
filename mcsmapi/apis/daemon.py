from typing import Any
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.daemon import (
    DaemonConfig,
    DaemonInfo,
    DaemonSystemInfo,
    DaemonStatus,
)


class Daemon:
    @staticmethod
    def config() -> list[DaemonStatus]:
        """获取全部节点配置信息"""
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_list",
        )
        return [DaemonStatus(**daemon) for daemon in daemons]

    @staticmethod
    def info() -> list[DaemonInfo]:
        """获取全部节点信息（含实例列表）"""
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services",
        )
        return [DaemonInfo(**daemon) for daemon in daemons]

    @staticmethod
    def system() -> list[DaemonSystemInfo]:
        """获取全部节点的系统信息"""
        daemons = send(
            "GET",
            f"{ApiPool.SERVICE}/remote_services_system",
        )
        return [DaemonSystemInfo(**daemon) for daemon in daemons]

    @staticmethod
    def add(config: DaemonConfig) -> str:
        """
        新增节点

        :params config: 节点配置信息
        """
        return send(
            "POST",
            f"{ApiPool.SERVICE}/remote_service",
            data=config.model_dump(),
        )

    @staticmethod
    def delete(daemonId: str) -> bool:
        """
        删除节点

        :params daemonId: 节点的UUID
        """
        return send(
            "DELETE", f"{ApiPool.SERVICE}/remote_service", params={"uuid": daemonId}
        )

    @staticmethod
    def link(daemonId: str) -> bool:
        """
        连接节点

        :params daemonId: 节点的UUID
        """
        return send(
            "GET", f"{ApiPool.SERVICE}/link_remote_service", params={"uuid": daemonId}
        )

    @staticmethod
    def update(daemonId: str, config: dict[str, Any]) -> bool:
        """
        更新节点配置（部分更新）

        :params daemonId: 节点的UUID
        :params config: 要修改的配置字段
        """
        return send(
            "PUT",
            f"{ApiPool.SERVICE}/remote_service",
            params={"uuid": daemonId},
            data=config,
        )
