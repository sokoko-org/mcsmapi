# 升级模型

## _class_ `UpgradeInfo(BaseModel)`

面板/节点更新信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `configured` | bool | 是否配置了更新源 |
| `currentVersion` | str | 当前版本 |
| `onlineVersion` | str \| None | 在线最新版本 |
| `onlineNotes` | str \| dict[str, str] \| None | 更新日志 |
| `updateAvailable` | bool | 是否有可用更新 |
| `updateSourceUrl` | str | 使用的更新源地址 |
| `error` | str \| None | 获取更新信息时的错误 |

## _class_ `UpgradeResult(BaseModel)`

更新执行结果

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `started` | bool | 是否已开始更新 |
| `onlineVersion` | str \| None | 更新的目标版本 |
| `message` | str \| None | 结果消息 |
