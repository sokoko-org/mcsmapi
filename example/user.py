"""
用户管理：搜索、创建、更新、删除用户
"""

import asyncio
from mcsmapi import MCSMAPI


async def main():
    mcsm = MCSMAPI("http://localhost:23333")
    await mcsm.login("admin", "password")

    # 搜索全部用户
    users = await mcsm.user.search()
    for u in users.data:
        print(f"{u.userName} (权限: {u.permission.name})")

    # 按权限搜索管理员
    admins = await mcsm.user.search(role=10)
    print(f"管理员数量: {admins.total}")

    # 创建新用户
    result = await mcsm.user.create("player1", "SecurePass123#")
    print(f"创建用户: {result.userName} ({result.uuid})")

    # 更新用户权限（部分更新）
    await mcsm.user.update(result.uuid, {"permission": 1})

    # 删除用户
    await mcsm.user.delete([result.uuid])

    # 修改当前用户密码
    # await mcsm.user.update_password("NewPassword456#")

    # API Key 管理
    # api_key = await mcsm.user.toggle_apikey(True)
    # print(f"API Key: {api_key}")

    await mcsm.close()


asyncio.run(main())
