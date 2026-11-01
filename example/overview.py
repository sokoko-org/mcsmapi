"""
基础示例：登录、获取仪表盘数据、遍历节点信息
"""

import asyncio
from mcsmapi import MCSMAPI


async def main():
    # 方式一：async with 自动管理连接
    async with MCSMAPI("http://localhost:23333") as mcsm:
        await mcsm.login("admin", "password")

        # 获取仪表盘概览
        data = await mcsm.overview.overview()
        print(f"面板版本: {data.version}")
        print(f"节点总数: {data.remoteCount.total}, 可用: {data.remoteCount.available}")

        # 遍历节点
        for remote in data.remote:
            print(f"  [{remote.remarks}] {remote.ip}:{remote.port}", end="")
            if remote.available and remote.system:
                print(f" - CPU {remote.system.cpuUsage:.1f}%")
            else:
                print(" - 离线")

    # 方式二：手动管理
    mcsm = MCSMAPI("http://localhost:23333")
    await mcsm.login("admin", "password")
    # ... 使用 ...
    await mcsm.close()

    # 方式三：API Key 认证（同步，无需 await）
    mcsm = MCSMAPI("http://localhost:23333")
    mcsm.login_with_apikey("your-api-key")
    data = await mcsm.overview.overview()
    print(f"面板版本: {data.version}")
    await mcsm.close()


asyncio.run(main())
