# 快速开始

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.x-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.10-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/sokoko-org/mcsmapi)

## 简介

`mcsmapi` 是一个基于 [MCSManager](https://github.com/MCSManager/MCSManager) 的异步 Python SDK，旨在简化与 MCSM API 的交互。

- 全异步设计，基于 `httpx` 异步 HTTP 客户端
- 使用 `pydantic` 进行数据验证，所有响应均为类型化模型
- 支持多实例安全调用，`Request` 为实例级别
- 支持链式操作，模型对象可直接调用关联方法

## 安装

```bash
pip install mcsmapi
```

如果你需要最新的构建文件，请访问
[Actions](https://github.com/sokoko-org/mcsmapi/actions/workflows/auto-build.yml)

## 支持的 MCSM 版本

| MCSM 版本 | 支持状态 |
| :-------: | :------: |
|   10.x    |    ✅    |

## 贡献

如果您发现任何问题或有改进建议，欢迎提交 [Issue](https://github.com/sokoko-org/mcsmapi/issues) 或者创建 [Pull Request](https://github.com/sokoko-org/mcsmapi/pulls)。

## 许可

`mcsmapi` 使用 [MIT 许可证](https://opensource.org/licenses/MIT)。