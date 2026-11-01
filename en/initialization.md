# Initializing the MCSMAPI Object

::: tip
All subsequent operations assume you have completed this configuration.
:::

## _class_ `MCSMAPI(url: str, timeout: int = 5)`

Initialize the MCSMAPI client.

### Parameters

- `url`: The URL of the MCSM frontend (including the protocol).
- `timeout`: Request timeout in seconds, defaults to 5.

### Using `async with` (recommended)

```python
import asyncio
from mcsmapi import MCSMAPI

async def main():
    async with MCSMAPI("http://127.0.0.1:23333") as mcsm:
        await mcsm.login("username", "password")
        daemons = await mcsm.daemon.config()
        print(daemons)

asyncio.run(main())
```

The client is automatically closed when the `async with` block exits.

### Manual style

```python
import asyncio
from mcsmapi import MCSMAPI

async def main():
    mcsm = MCSMAPI("http://127.0.0.1:23333")
    await mcsm.login("username", "password")
    daemons = await mcsm.daemon.config()
    print(daemons)
    await mcsm.close()

asyncio.run(main())
```

::: warning
When using the manual style, always call `await mcsm.close()` when you are done to release the underlying httpx connection pool.
:::

## Authentication

Most APIs require authentication to be used.

### Password Login

#### _method_ `login(username: str, password: str)`

This method is **async** — you must `await` it.

If you call `login()` again on an already-authenticated instance, the previous session is replaced automatically.

##### Parameters

- `username`: Your username.
- `password`: Your password.

##### Example

```python
await mcsm.login("username", "password")
```

### API Key Login

#### _method_ `login_with_apikey(apikey: str)`

This method is **sync** — no `await` needed.

##### Parameters

- `apikey`: Your API key.

##### Example

```python
mcsm.login_with_apikey("your-api-key")
```

## Accessing Endpoints

Every endpoint group is exposed as a `cached_property` on the `MCSMAPI` instance:

```python
mcsm.overview   # Overview
mcsm.daemon     # Daemon
mcsm.instance   # Instance
mcsm.user       # User
mcsm.file       # File
mcsm.image      # Image
mcsm.schedule   # Schedule
mcsm.java       # Java
mcsm.mod        # Mod
mcsm.upgrade    # Upgrade
```

All methods on these endpoint objects are `async` and must be called with `await`.

## Complete Example

```python
import asyncio
from mcsmapi import MCSMAPI

async def main():
    async with MCSMAPI("http://127.0.0.1:23333") as mcsm:
        await mcsm.login("admin", "password")

        # Get panel overview
        info = await mcsm.overview.overview()
        print("Panel version:", info.version)

        # List all daemons
        daemons = await mcsm.daemon.config()
        for d in daemons:
            print("Daemon:", d.remarks, d.ip)

        # Search instances on the first daemon
        result = await mcsm.instance.search(daemons[0].uuid)
        for inst in result.data:
            print("Instance:", inst.config.nickname)

asyncio.run(main())
```
