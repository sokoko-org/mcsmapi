# User

## _class_ `User`

Get subclasses for user operations.

```python
api = mcsm.user
```

---

### _method_ `info(advanced: bool = False)`

Get the current authenticated user's information.

#### Parameters

- `advanced`: Whether to return advanced details, defaults to `False`.

#### Returns

- `UserInfo`

#### Example

```python
user = await api.info()
print(user.userName, user.permission)
```

### _method_ `search(username: str = "", page: int = 1, page_size: int = 20, role: Literal[-1, 1, 10, ""] = "")`

Search for users by username and role.

#### Parameters

- `username`: Username filter, defaults to empty string (no filtering).
- `page`: Page number, defaults to 1.
- `page_size`: Number of items per page, defaults to 20.
- `role`: Role filter, defaults to empty string (no filtering).

#### Returns

- `SearchUserModel`

#### Example

```python
result = await api.search(username="admin")
for user in result.data:
    print(user.userName)
```

### _method_ `overview()`

Get an overview of all users.

#### Returns

- `list[UserOverviewItem]`

#### Example

```python
items = await api.overview()
for item in items:
    print(item)
```

### _method_ `create(username: str, password: str, permission: int = 1)`

Create a new user.

#### Parameters

- `username`: Username.
- `password`: Password.
- `permission`: Permission level, defaults to 1.

#### Returns

- `UserCreateResult`

#### Example

```python
result = await api.create("newuser", "securepassword", permission=1)
print("Created user UUID:", result.uuid)
```

### _method_ `update(uuid: str, config: dict[str, Any])`

Update user information.

::: warning
This method is not recommended for direct use. It is suggested to call `search` first and then use the user object's `update` method to update as needed.
:::

#### Parameters

- `uuid`: User's UUID.
- `config`: New user information, provided as a dictionary. Missing values are filled with default values from the `UserModel` model.

#### Returns

- `bool`: Returns `True` if the operation is successful.

#### Example

```python
await api.update("user-uuid", {"permission": 10})
```

### _method_ `update_password(password: str)`

Update the current user's password.

#### Parameters

- `password`: New password.

#### Returns

- `bool`: Returns `True` if the operation is successful.

#### Example

```python
await api.update_password("new-secure-password")
```

### _method_ `toggle_apikey(enable: bool)`

Enable or disable the API key for the current user.

#### Parameters

- `enable`: `True` to enable, `False` to disable.

#### Returns

- `str`: The API key string (when enabling).

#### Example

```python
apikey = await api.toggle_apikey(True)
print("API Key:", apikey)
```

### _method_ `delete(uuids: list[str])`

Delete users.

#### Parameters

- `uuids`: List of UUIDs of users to delete.

#### Returns

- `bool`: Returns `True` if the deletion is successful.

#### Example

```python
await api.delete(["uuid1", "uuid2"])
```

### _method_ `login_info()`

Get login page information.

#### Returns

- `LoginInfo`

#### Example

```python
info = await api.login_info()
print(info)
```

### _method_ `status()`

Get the panel status (public, no auth required).

#### Returns

- `PanelStatus`

#### Example

```python
status = await api.status()
print(status)
```

### _method_ `token()`

Get a new token for the current session.

#### Returns

- `str`: New token string.

#### Example

```python
token = await api.token()
```

### _method_ `bind2fa()`

Start binding two-factor authentication. Returns the secret/QR data needed for setup.

#### Returns

- `Any`

#### Example

```python
secret = await api.bind2fa()
print(secret)
```

### _method_ `confirm2fa(enable: bool, totp_code: str)`

Confirm or disable two-factor authentication.

#### Parameters

- `enable`: `True` to enable 2FA, `False` to disable.
- `totp_code`: The TOTP verification code.

#### Returns

- `bool`: Returns `True` if the operation is successful.

#### Example

```python
await api.confirm2fa(True, "123456")
```