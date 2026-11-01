# 用户模型

## _class_ `UserPermission(IntEnum)`

用户权限级别

| 枚举项 | 枚举值 | 描述 |
| --- | --- | --- |
| `BANNED` | -1 | 封禁 |
| `USER` | 1 | 普通用户 |
| `ADMIN` | 10 | 管理员 |

## _class_ `UserInstances(BaseModel)`

用户实例信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `instanceUuid` | str | 实例 UUID |
| `daemonId` | str | 节点 ID |

## _class_ `UserCreateResult(BaseModel)`

用户创建结果

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | str | 用户 UUID |
| `userName` | str | 用户名 |
| `permission` | UserPermission | 用户权限级别 |

## _class_ `UserModel(BaseModel)`

用户信息模型

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | str | 用户 UUID |
| `userName` | str | 用户名 |
| `loginTime` | str | 最后登录时间 |
| `registerTime` | str | 注册时间 |
| `instances` | list[UserInstances] | 用户拥有的实例列表 |
| `permission` | UserPermission | 权限级别 |
| `passWord` | str | 密码 (搜索接口返回空字符串) |
| `passWordType` | int | 密码类型 |
| `salt` | str | 密码盐值 |
| `open2FA` | bool | 是否启用双因素认证 |
| `apiKey` | str | API 密钥 (掩码值) |
| `isInit` | bool | 是否为初始化用户 |
| `secret` | str | 2FA 密钥 (掩码值) |
| `ssoSub` | str | SSO 主题标识 |
| `ssoBound` | bool | 是否绑定 SSO |

### _method_ `delete()`

删除该用户

#### 返回

- `bool`

### _method_ `update(config)`

更新该用户的信息（部分更新）

#### 参数

- `config`: 要修改的字段 (dict)

#### 返回

- `bool`

## _class_ `SearchUserModel(BaseModel)`

用户搜索结果

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `total` | int | 匹配的用户总数 |
| `page` | int | 当前页码 |
| `pageSize` | int | 每页返回的用户数量 |
| `maxPage` | int | 最大可用页数 |
| `data` | list[UserModel] | 用户信息列表 |

## _class_ `UserInfo(BaseModel)`

当前登录用户信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | str | 用户 UUID |
| `userName` | str | 用户名 |
| `loginTime` | str | 最后登录时间 |
| `registerTime` | str | 注册时间 |
| `instances` | list[UserInstances] | 用户拥有的实例列表 |
| `permission` | UserPermission | 权限级别 |
| `apiKey` | str | API 密钥 (掩码值) |
| `isInit` | bool | 是否为初始化用户 |
| `open2FA` | bool | 是否启用双因素认证 |
| `token` | str | 当前会话 Token |

## _class_ `LoginInfo(BaseModel)`

登录页面信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `loginInfo` | str \| None | 登录页面自定义文本 |

## _class_ `PanelStatusSettings(BaseModel)`

面板状态设置

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `businessMode` | bool | 是否为商业模式 |
| `businessId` | str | 商业模式 ID |
| `canFileManager` | bool \| None | 是否允许文件管理 |
| `allowUsePreset` | bool \| None | 是否允许使用预设 |
| `allowChangeCmd` | bool \| None | 是否允许修改启动命令 |
| `panelId` | str \| None | 面板 ID |
| `ssoEnabled` | bool \| None | 是否启用 SSO |

## _class_ `PanelStatus(BaseModel)`

面板公开状态信息

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `isInstall` | bool | 面板是否已安装 |
| `language` | str \| None | 面板语言 |
| `settings` | PanelStatusSettings | 面板设置项 |

## _class_ `UserOverviewItem(BaseModel)`

用户概览条目

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | str | 用户 UUID |
| `userName` | str | 用户名 |
| `permission` | UserPermission | 权限级别 |
| `instances` | list[UserInstances] | 用户拥有的实例列表 |
| `loginTime` | str | 最后登录时间 |
| `registerTime` | str | 注册时间 |
