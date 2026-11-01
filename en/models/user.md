# User Models

## _class_ `UserPermission(IntEnum)`

User permission level

| Variant | Value | Description |
| --- | --- | --- |
| `BANNED` | -1 | 封禁 |
| `USER` | 1 | 普通用户 |
| `ADMIN` | 10 | 管理员 |

## _class_ `UserInstances(BaseModel)`

User instance info

| Field | Type | Description |
| --- | --- | --- |
| `instanceUuid` | str | 实例 UUID |
| `daemonId` | str | 节点 ID |

## _class_ `UserCreateResult(BaseModel)`

User creation result

| Field | Type | Description |
| --- | --- | --- |
| `uuid` | str | 用户 UUID |
| `userName` | str | 用户名 |
| `permission` | UserPermission | User permission level |

## _class_ `UserModel(BaseModel)`

User info model

| Field | Type | Description |
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

Delete this user

#### 返回

- `bool`

### _method_ `update(config)`

Update this user (partial)

#### 参数

- `config`: 要修改的字段 (dict)

#### 返回

- `bool`

## _class_ `SearchUserModel(BaseModel)`

User search result

| Field | Type | Description |
| --- | --- | --- |
| `total` | int | 匹配的用户总数 |
| `page` | int | 当前页码 |
| `pageSize` | int | 每页返回的用户数量 |
| `maxPage` | int | 最大可用页数 |
| `data` | list[UserModel] | 用户信息列表 |

## _class_ `UserInfo(BaseModel)`

Current user info

| Field | Type | Description |
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

Login page info

| Field | Type | Description |
| --- | --- | --- |
| `loginInfo` | str \| None | 登录页面自定义文本 |

## _class_ `PanelStatusSettings(BaseModel)`

Panel status settings

| Field | Type | Description |
| --- | --- | --- |
| `businessMode` | bool | 是否为商业模式 |
| `businessId` | str | 商业模式 ID |
| `canFileManager` | bool \| None | 是否允许文件管理 |
| `allowUsePreset` | bool \| None | 是否允许使用预设 |
| `allowChangeCmd` | bool \| None | 是否允许修改启动命令 |
| `panelId` | str \| None | 面板 ID |
| `ssoEnabled` | bool \| None | 是否启用 SSO |

## _class_ `PanelStatus(BaseModel)`

Panel public status

| Field | Type | Description |
| --- | --- | --- |
| `isInstall` | bool | 面板是否已安装 |
| `language` | str \| None | 面板语言 |
| `settings` | PanelStatusSettings | 面板设置项 |

## _class_ `UserOverviewItem(BaseModel)`

User overview item

| Field | Type | Description |
| --- | --- | --- |
| `uuid` | str | 用户 UUID |
| `userName` | str | 用户名 |
| `permission` | UserPermission | 权限级别 |
| `instances` | list[UserInstances] | 用户拥有的实例列表 |
| `loginTime` | str | 最后登录时间 |
| `registerTime` | str | 注册时间 |
