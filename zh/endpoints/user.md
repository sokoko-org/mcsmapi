# 用户

## _class_ `User`

获取操作用户的子类

```python
api = mcsm.user
```

---

### _method_ `info(advanced: bool = False)`

获取当前登录用户的信息

#### 参数

- `advanced`: 是否获取高级信息

#### 返回

- `UserInfo`: 用户信息模型

#### 例子

```python
info = await api.info()
print(info.userName)
```

### _method_ `search(username: str = "", page: int = 1, page_size: int = 20, role: UserPermission | Literal[\"\"] = "")`

根据用户名和角色搜索用户信息

#### 参数

- `username`: 用户名，默认为空字符串，表示不进行用户名过滤
- `page`: 页码，用于指示返回数据的第几页
- `page_size`: 每页数据条数，默认为 20
- `role`: 过滤的用户权限，默认为空字符串，表示不进行权限过滤

#### 返回

- `SearchUserModel`: 搜索结果模型

#### 例子

```python
result = await api.search(username="admin", page=1)
for user in result.data:
    print(user.userName, user.permission)
```

### _method_ `overview()`

获取用户概览信息列表

#### 返回

- `list[UserOverviewItem]`: 用户概览列表

### _method_ `create(username: str, password: str, permission: int = 1)`

创建新用户

#### 参数

- `username`: 用户名
- `password`: 密码
- `permission`: 权限等级，默认为 1

#### 返回

- `UserCreateResult`: 包含创建结果的模型

#### 例子

```python
result = await api.create("newuser", "password123", permission=1)
print("新用户 UUID:", result.uuid)
```

### _method_ `update(uuid: str, config: dict[str, Any])`

更新用户信息

::: warning
此函数不建议直接使用，建议调用 `search` 后使用用户对象的 `update` 方法按需更新
:::

#### 参数

- `uuid`: 用户的 UUID
- `config`: 要修改的字段

#### 返回

- `bool`: 成功时返回 True

### _method_ `update_password(password: str)`

更新当前登录用户的密码

#### 参数

- `password`: 新密码

#### 返回

- `bool`: 成功时返回 True

### _method_ `toggle_apikey(enable: bool)`

开启或关闭当前用户的 API Key

#### 参数

- `enable`: `True` 开启，`False` 关闭

#### 返回

- `bool`: 成功时返回 True

### _method_ `delete(uuids: list[str])`

删除用户

#### 参数

- `uuids`: 要删除的用户 UUID 列表

#### 返回

- `bool`: 删除成功时返回 True

#### 例子

```python
await api.delete(["uuid1", "uuid2"])
```

### _method_ `login_info()`

获取当前登录信息

#### 返回

- `LoginInfo`: 登录信息模型

### _method_ `status()`

获取面板状态设置

#### 返回

- `PanelStatus`: 面板状态模型

### _method_ `token()`

获取当前用户的 token

#### 返回

- `str`: token 字符串

### _method_ `bind2fa()`

获取二步验证绑定信息

#### 返回

- `dict`: 包含二步验证绑定所需的密钥和二维码信息

### _method_ `confirm2fa(enable: bool, totp_code: str)`

确认绑定或关闭二步验证

#### 参数

- `enable`: `True` 开启，`False` 关闭
- `totp_code`: TOTP 验证码

#### 返回

- `bool`: 操作成功时返回 True