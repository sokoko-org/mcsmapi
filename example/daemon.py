"""
节点管理：查看节点、链式操作、创建/删除节点
"""

import asyncio
from mcsmapi import MCSMAPI
from mcsmapi.models.daemon import DaemonConfig


async def main():
    mcsm = MCSMAPI("http://localhost:23333")
    await mcsm.login("admin", "password")

    # 获取全部节点（含系统信息）
    nodes = await mcsm.daemon.system()
    for node in nodes:
        print(f"[{node.remarks}] {node.ip}:{node.port}")
        if node.available and node.system:
            mem_pct = node.system.memUsage * 100
            print(f"  CPU: {node.system.cpuUsage:.1f}%  内存: {mem_pct:.1f}%")
            if node.instance:
                print(f"  实例: {node.instance.running}/{node.instance.total} 运行中")

    # 链式操作：从节点对象直接搜索实例
    node = nodes[0]
    instances = await node.search_instances(page=1, page_size=10)
    for inst in instances.data:
        print(f"  实例: {inst.config.nickname} [{inst.status.name}]")

    # 新增节点
    daemon_id = await mcsm.daemon.add(DaemonConfig(
        ip="192.168.1.100",
        port=24444,
        remarks="Game Node 2",
    ))
    print(f"新增节点: {daemon_id}")

    # 部分更新节点配置
    await mcsm.daemon.update(daemon_id, {"remarks": "Renamed Node"})

    # 删除节点
    await mcsm.daemon.delete(daemon_id)

    await mcsm.close()


asyncio.run(main())
