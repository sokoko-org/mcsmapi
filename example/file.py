"""
文件管理：浏览、读写、上传下载、压缩解压
"""

import asyncio
from mcsmapi import MCSMAPI


async def main():
    mcsm = MCSMAPI("http://localhost:23333")
    await mcsm.login("admin", "password")

    daemons = await mcsm.daemon.config()
    daemon_id = daemons[0].uuid

    # 搜索实例
    result = await mcsm.instance.search(daemon_id)
    inst = result.data[0]

    # 浏览文件
    files = await mcsm.file.show(daemon_id, inst.instanceUuid)
    for f in files.items[:10]:
        kind = "📁" if f.type == 0 else "📄"
        print(f"  {kind} {f.name} ({f.size} bytes)")

    # 也可以通过实例对象直接操作
    files = await inst.files()

    # 读取文件内容
    text = await mcsm.file.content(daemon_id, inst.instanceUuid, "server.properties")
    print(text[:200])

    # 修改文件内容
    await mcsm.file.update(daemon_id, inst.instanceUuid, "server.properties", "motd=Hello!")

    # 创建文件和文件夹
    await mcsm.file.createFile(daemon_id, inst.instanceUuid, "notes.txt")
    await mcsm.file.createFolder(daemon_id, inst.instanceUuid, "backups")

    # FileItem 链式操作
    item = files.items[0]
    await item.rename("new_name.txt")
    await item.copy_to("/backup/new_name.txt")
    await item.delete()

    # 下载文件（获取下载 URL）
    url = await mcsm.file.download(daemon_id, inst.instanceUuid, "world.zip")
    print(f"下载地址: {url}")

    # 压缩
    await mcsm.file.zip(daemon_id, inst.instanceUuid, "backup.zip", ["world", "plugins"])

    # 解压
    await mcsm.file.unzip(daemon_id, inst.instanceUuid, "backup.zip", "/restore")

    # 从 URL 下载文件到实例
    task_id = await mcsm.file.download_from_url(
        daemon_id, inst.instanceUuid,
        url="https://example.com/plugin.jar",
        file_name="plugins/plugin.jar",
    )
    print(f"下载任务: {task_id}")

    await mcsm.close()


asyncio.run(main())
