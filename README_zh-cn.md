# MCSM API

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.x-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.10-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/molanp/mcsmapi)

简体中文|[English](README.md)

## 简介

mcsmapi 是 [MCSManager](https://github.com/MCSManager/MCSManager) 的异步 Python SDK，基于 httpx + pydantic 构建。

- 全异步 (sync/await)
- 类型化模型，IDE 自动补全
- 返回对象支持链式操作
- 支持 sync with 上下文管理器

## 文档

📄 文档: [docs](https://mcsmapi.awkchan.top/)

💡 示例: [example](example)

## 安装

`ash
pip install mcsmapi
`

最新构建: [Actions](https://github.com/molanp/mcsmapi/actions/workflows/auto-build.yml)

## 支持的功能

- [x] 仪表盘数据 (Overview)
- [x] 用户管理 (User)
- [x] 实例管理 (Instance)
- [x] 节点管理 (Daemon)
- [x] 文件管理 (File)
- [x] 镜像管理 (Image)
- [x] 计划任务管理 (Schedule)
- [x] Java 运行环境管理 (Java)
- [x] Mod 管理 (Mod)
- [x] 面板与节点升级 (Upgrade)

## 支持的 MCSM 版本

| MCSM 版本 | 支持状态 |
| :-------: | :------: |
|   10.x    |    ✅    |

## 快速示例

`python
import asyncio
from mcsmapi import MCSMAPI


async def main():
    async with MCSMAPI("http://localhost:23333") as mcsm:
        await mcsm.login("admin", "password")

        # 仪表盘
        data = await mcsm.overview.overview()
        print(f"面板版本: {data.version}")

        # 节点列表
        daemons = await mcsm.daemon.config()
        for d in daemons:
            print(f"  {d.remarks} ({d.ip}:{d.port})")

        # 搜索实例
        instances = await daemons[0].search_instances()
        for inst in instances.data:
            print(f"  {inst.config.nickname} [{inst.status.name}]")

        # 部分更新配置（只发送传入的字段，不会重置其他字段）
        inst = instances.data[0]
        await inst.updateConfig({"nickname": "我的服务器"})

        # 链式文件操作
        files = await inst.files(target="")
        for f in files.items[:5]:
            print(f"  {f.name}")


asyncio.run(main())
`

更多用法见 [example/](example/)。

## 贡献

欢迎提交 [Issue](https://github.com/molanp/mcsmapi/issues) 或 [Pull Request](https://github.com/molanp/mcsmapi/pulls)。

## 许可

[MIT License](https://opensource.org/licenses/MIT) — 详见 [LICENSE](LICENSE)。
