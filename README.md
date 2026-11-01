# MCSM API

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.x-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.10-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/molanp/mcsmapi)

English|[Chinese Simplified](README_zh-cn.md)

## Documentation

📄 Docs: [docs](https://mcsmapi.awkchan.top/en/)

💡 Example: [example](example)

## Introduction

mcsmapi is an async Python SDK for [MCSManager](https://github.com/MCSManager/MCSManager), built on httpx + pydantic.

- Fully async (sync/await)
- Typed models with IDE autocompletion
- Chainable operations on returned objects
- Supports sync with context manager

## Installation

`ash
pip install mcsmapi
`

For the latest build: [Actions](https://github.com/molanp/mcsmapi/actions/workflows/auto-build.yml)

## Supported Features

- [x] Dashboard data (Overview)
- [x] User management (User)
- [x] Instance management (Instance)
- [x] Daemon management (Daemon)
- [x] File management (File)
- [x] Image management (Image)
- [x] Schedule task management (Schedule)
- [x] Java runtime management (Java)
- [x] Mod management (Mod)
- [x] Panel & Daemon upgrade (Upgrade)

## Supported MCSM Versions

| MCSM Version | Support Status |
| :----------: | :------------: |
|     10.x     |       ✅       |

## Quick Example

`python
import asyncio
from mcsmapi import MCSMAPI


async def main():
    mcsm = MCSMAPI("http://localhost:23333")
    await mcsm.login("admin", "password")

    # Dashboard
    data = await mcsm.overview.overview()
    print(f"Panel version: {data.version}")

    # List daemons
    daemons = await mcsm.daemon.config()
    for d in daemons:
        print(f"  {d.remarks} ({d.ip}:{d.port})")

    # Search instances on a daemon
    instances = await daemons[0].search_instances()
    for inst in instances.data:
        print(f"  {inst.config.nickname} [{inst.status.name}]")

    # Partial config update (only sends provided fields)
    inst = instances.data[0]
    await inst.updateConfig({"nickname": "My Server"})

    # File operations via chaining
    files = await inst.files(target=".")
    for f in files.items[:5]:
        print(f"  {f.name}")

    await mcsm.close()


asyncio.run(main())
`

See [example/](example/) for more usage patterns.

## Contributing

Feel free to submit an [Issue](https://github.com/molanp/mcsmapi/issues) or [Pull Request](https://github.com/molanp/mcsmapi/pulls).

## License

[MIT License](https://opensource.org/licenses/MIT) — see [LICENSE](LICENSE).
