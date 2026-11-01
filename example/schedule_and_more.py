"""
计划任务 & 新增模块 (Schedule / Java / Mod / Upgrade)
"""

import asyncio
from mcsmapi import MCSMAPI
from mcsmapi.models.schedule import SchedulePostBody, ScheduleAction, ScheduleActionType, ScheduleType


async def main():
    mcsm = MCSMAPI("http://localhost:23333")
    await mcsm.login("admin", "password")

    daemons = await mcsm.daemon.config()
    daemon_id = daemons[0].uuid
    result = await mcsm.instance.search(daemon_id)
    inst = result.data[0]

    # --- 计划任务 ---
    tasks = await inst.list_schedule()
    print(f"计划任务数: {len(tasks)}")

    # 创建一个每30分钟自动重启的计划任务
    await inst.create_schedule(SchedulePostBody(
        name="auto-restart",
        count=-1,
        time="1800",
        type=ScheduleType.INTERVAL,
        actions=[
            ScheduleAction(type=ScheduleActionType.COMMAND, payload="say 服务器即将重启..."),
            ScheduleAction(type=ScheduleActionType.DELAY, payload="10"),
            ScheduleAction(type=ScheduleActionType.RESTART, payload=""),
        ],
    ))

    # --- Java 管理 ---
    javas = await mcsm.java.list(daemon_id, inst.instanceUuid)
    print(f"Java 运行环境: {javas}")

    # --- Mod 管理 ---
    versions = await mcsm.mod.mc_versions()
    print(f"MC 版本数: {len(versions) if isinstance(versions, list) else 'N/A'}")

    results = await mcsm.mod.search(query="fabric-api", limit=5)
    print(f"Mod 搜索结果: {results}")

    # --- 面板升级信息 ---
    info = await mcsm.upgrade.panel_info()
    print(f"面板更新信息: {info}")

    await mcsm.close()


asyncio.run(main())
