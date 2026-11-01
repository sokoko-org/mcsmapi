# Common Models

## _class_ `CpuMemChart(BaseModel)`

Resource usage info

| Field | Type | Description |
| --- | --- | --- |
| `cpu` | float | CPU 使用率 |
| `mem` | float | 内存使用率 |

## _class_ `ProcessInfo(BaseModel)`

Process details

| Field | Type | Description |
| --- | --- | --- |
| `cpu` | int | CPU 使用率（百分比） |
| `memory` | int | 内存使用量（字节） |
| `cwd` | str | 工作路径 |

## _class_ `InstanceStat(BaseModel)`

Instance statistics

| Field | Type | Description |
| --- | --- | --- |
| `running` | int | 运行中实例数量 |
| `total` | int | 全部实例数量 |
