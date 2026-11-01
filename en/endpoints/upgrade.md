# Upgrade

## _class_ `Upgrade`

Get subclasses for upgrade operations.

```python
api = mcsm.upgrade
```

---

### _method_ `panel_info()`

Get available upgrade information for the panel.

#### Returns

- `UpgradeInfo`

#### Example

```python
info = await api.panel_info()
print("Latest version:", info)
```

### _method_ `panel()`

Perform a panel upgrade.

#### Returns

- `UpgradeResult`

#### Example

```python
result = await api.panel()
print(result)
```

### _method_ `daemon_info(uuid: str)`

Get available upgrade information for a daemon.

#### Parameters

- `uuid`: UUID of the daemon.

#### Returns

- `UpgradeInfo`

#### Example

```python
info = await api.daemon_info("daemon-uuid")
print(info)
```

### _method_ `daemon(uuid: str)`

Perform a daemon upgrade.

#### Parameters

- `uuid`: UUID of the daemon.

#### Returns

- `UpgradeResult`

#### Example

```python
result = await api.daemon("daemon-uuid")
print(result)
```