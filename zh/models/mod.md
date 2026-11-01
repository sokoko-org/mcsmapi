# Mod 模型

## _class_ `ModSearchHit(BaseModel)`

Mod 搜索结果条目

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | str | 项目 ID |
| `slug` | str | 项目 slug |
| `title` | str | 项目标题 |
| `description` | str | 项目简介 |
| `icon_url` | str | 图标 URL |
| `author` | str | 作者 |
| `downloads` | int | 下载量 |
| `updated` | str | 最后更新时间 |
| `categories` | list[str] | 分类列表 |
| `version_number` | str | 最新版本号 |
| `game_versions` | list[str] | 支持的游戏版本 |
| `display_categories` | list[str] | 显示分类 |
| `source` | str | 资源来源 |
| `project_type` | str | 项目类型 |

## _class_ `ModSearchResult(BaseModel)`

Mod 搜索结果

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `hits` | list[ModSearchHit] | 搜索结果列表 |
| `total_hits` | int | 总匹配数 |

## _class_ `ModVersionFile(BaseModel)`

Mod 版本文件

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `url` | str | 下载地址 |
| `filename` | str | 文件名 |
| `primary` | bool | 是否为主文件 |

## _class_ `ModVersion(BaseModel)`

Mod 版本信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | str | 版本 ID |
| `name` | str \| None | 版本名称 |
| `version_number` | str | 版本号 |
| `game_versions` | list[str] | 支持的游戏版本 |
| `loaders` | list[str] | 支持的加载器 |
| `project_type` | str | 项目类型 |
| `files` | list[ModVersionFile] | 版本文件列表 |

## _class_ `ModInfoDetail(BaseModel)`

Mod 详细信息（通过哈希查询）

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `version` | Any | Modrinth 版本数据 |
| `project` | Any | Modrinth 项目数据 |

## _class_ `ModFileItem(BaseModel)`

实例 Mod 文件条目

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `fileName` | str | 文件名 |
| `size` | int | 文件大小（字节） |
| `enable` | bool | 是否启用 |
| `hash` | str | 文件哈希（sha1） |

## _class_ `ModListResult(BaseModel)`

实例 Mod 列表

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `items` | list[ModFileItem] | Mod 文件列表 |
| `page` | int | 当前页 |
| `pageSize` | int | 每页大小 |
| `total` | int | 总数 |
