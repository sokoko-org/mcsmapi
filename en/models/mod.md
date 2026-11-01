# Mod Models

## _class_ `ModSearchHit(BaseModel)`

Mod search hit

| Field | Type | Description |
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

Mod search result

| Field | Type | Description |
| --- | --- | --- |
| `hits` | list[ModSearchHit] | 搜索结果列表 |
| `total_hits` | int | 总匹配数 |

## _class_ `ModVersionFile(BaseModel)`

Mod version file

| Field | Type | Description |
| --- | --- | --- |
| `url` | str | 下载地址 |
| `filename` | str | 文件名 |
| `primary` | bool | 是否为主文件 |

## _class_ `ModVersion(BaseModel)`

Mod version info

| Field | Type | Description |
| --- | --- | --- |
| `id` | str | 版本 ID |
| `name` | str \| None | 版本名称 |
| `version_number` | str | 版本号 |
| `game_versions` | list[str] | 支持的游戏版本 |
| `loaders` | list[str] | 支持的加载器 |
| `project_type` | str | 项目类型 |
| `files` | list[ModVersionFile] | 版本File list |

## _class_ `ModInfoDetail(BaseModel)`

Mod detail (by hash)

| Field | Type | Description |
| --- | --- | --- |
| `version` | Any | Modrinth 版本数据 |
| `project` | Any | Modrinth 项目数据 |

## _class_ `ModFileItem(BaseModel)`

Instance mod file item

| Field | Type | Description |
| --- | --- | --- |
| `fileName` | str | 文件名 |
| `size` | int | 文件大小（字节） |
| `enable` | bool | 是否启用 |
| `hash` | str | 文件哈希（sha1） |

## _class_ `ModListResult(BaseModel)`

Instance mod list

| Field | Type | Description |
| --- | --- | --- |
| `items` | list[ModFileItem] | Mod File list |
| `page` | int | 当前页 |
| `pageSize` | int | 每页大小 |
| `total` | int | 总数 |
