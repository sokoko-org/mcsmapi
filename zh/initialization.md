# 初始化 MCSMAPI 对象

::: tip
后续的所有操作都默认你已经完成了此项配置
:::

## _class_ `MCSMAPI(url, timeout: int = 5)`

初始化 MCSMAPI 对象

### 参数

- `url`: MCSM 前端地址的 URL（包含协议头）
- `timeout`: 请求超时时间，默认为 5 秒

### 使用 `async with`（推荐）

```python
import asyncio
from mcsmapi import MCSMAPI

async def main():
    async with MCSMAPI("http://127.0.0.1:8080") as mcsm:
        await mcsm.login("username", "password")
        overview = await mcsm.overview.overview()
        print(overview.version)

asyncio.run(main())
```

### 手动管理生命周期

```python
import asyncio
from mcsmapi import MCSMAPI

async def main():
    mcsm = MCSMAPI("http://127.0.0.1:8080")
    try:
        await mcsm.login("username", "password")
        overview = await mcsm.overview.overview()
        print(overview.version)
    finally:
        await mcsm.close()

asyncio.run(main())
```

## 登录鉴权

大部分接口需要身份验证才能使用。

### 密码登录

#### _method_ `async login(username: str, password: str)`

使用用户名和密码登录面板。

##### 参数

- `username`: 用户名
- `password`: 密码

##### 例子

```python
await mcsm.login("username", "password")
```

::: warning
重复调用 `login()` 时，SDK 会自动注销当前 session 并重新登录以获取有效 token，无需手动处理。
:::

### 密钥登录

#### _method_ `login_with_apikey(apikey: str)`

使用 API Key 进行鉴权，此方法为同步方法，无需 `await`。

##### 参数

- `apikey`: 密钥

##### 例子

```python
mcsm.login_with_apikey("your-api-key")
```

## 完整示例

```python
import asyncio
from mcsmapi import MCSMAPI

async def main():
    async with MCSMAPI("http://127.0.0.1:8080") as mcsm:
        # 方式一：密码登录（异步）
        await mcsm.login("admin", "password")

        # 方式二：API Key 登录（同步）
        # mcsm.login_with_apikey("your-api-key")

        # 使用各端点
        overview = await mcsm.overview.overview()
        print("版本:", overview.version)

        users = await mcsm.user.search()
        print("用户数:", users.total)

asyncio.run(main())
```

## 快捷操作说明

`MCSMAPI` 对象中的每一个端点，都可在对应的模型中直接调用。

例如，你可以在 `User` 模型中，使用 `mcsm.user` 中的大部分方法。