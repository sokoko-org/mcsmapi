# Quick Start

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.x-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.10-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/sokoko-org/mcsmapi)

## Introduction

`mcsmapi` is a fully async Python SDK for [MCSManager](https://github.com/MCSManager/MCSManager), built on **httpx** and **pydantic v2**.

- All APIs are `async`/`await`
- Typed return models with IDE autocompletion
- Instance-based `Request` (multi-instance safe)
- Returned model objects support direct chain operations

## Installation

```bash
pip install mcsmapi
```

If you need the latest build files, please visit
[Actions](https://github.com/sokoko-org/mcsmapi/actions/workflows/auto-build.yml)

## Supported MCSM Versions

| MCSM Version | Support Status |
| :----------: | :------------: |
|     10.x     |       ✅       |

## Contributing

If you find any issues or have suggestions for improvements, feel free to submit an [Issue](https://github.com/sokoko-org/mcsmapi/issues) or create a [Pull Request](https://github.com/sokoko-org/mcsmapi/pulls).

## License

`mcsmapi` is licensed under the [MIT License](https://opensource.org/licenses/MIT).
