"""
实例管理：搜索、启停、发送命令、文件操作
"""

import asyncio
from mcsmapi import MCSMAPI


async def main():
    mcsm = MCSMAPI("http://localhost:23333")
    await mcsm.login("admin", "password")

    # 获取节点列表
    daemons = await mcsm.daemon.config()
    daemon_id = daemons[0].uuid

    # 搜索实例
    result = await mcsm.instance.search(daemon_id, instance_name="Survival")
    print(f"找到 {len(result.data)} 个实例")

    if not result.data:
        await mcsm.close()
        return

    inst = result.data[0]
    print(f"实例: {inst.config.nickname} [{inst.status.name}]")

    # 启动 / 停止 / 重启 / 强制终止
    await inst.start()
    await inst.stop()
    await inst.restart()
    await inst.kill()

    # 发送命令
    await inst.command("say Hello from SDK!")

    # 获取输出
    output = await inst.get_output()
    print(output[-200:])

    # 部分更新配置（只修改传入的字段，不会重置其他字段）
    await inst.updateConfig({"nickname": "My Server", "stopCommand": "stop"})

    # 文件操作
    files = await inst.files(target=".")
    print(f"文件数: {files.total}")
    for f in files.items[:5]:
        print(f"  {f.name} ({f.size} bytes)")

    # 创建实例
    new = await mcsm.instance.create(daemon_id, {
        "nickname": "Test Server",
        "startCommand": "java -jar server.jar",
        "stopCommand": "stop",
        "type": "minecraft",
    })
    print(f"创建成功: {new.instanceUuid}")

    # 删除实例
    await mcsm.instance.delete(daemon_id, [new.instanceUuid], deleteFile=True)

    await mcsm.close()


asyncio.run(main())
