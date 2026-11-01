# 升级管理

## _class_ `Upgrade`

获取操作升级功能的子类

```python
api = mcsm.upgrade
```

---

### _method_ `panel_info()`

获取面板升级信息

#### 返回

- `UpgradeInfo`: 面板升级信息模型

#### 例子

```python
info = await api.panel_info()
print("最新版本:", info.latestVersion)
```

### _method_ `panel()`

执行面板升级

#### 返回

- `UpgradeResult`: 升级结果模型

#### 例子

```python
result = await api.panel()
```

### _method_ `daemon_info(uuid: str)`

获取指定节点的升级信息

#### 参数

- `uuid`: 节点的 UUID

#### 返回

- `UpgradeInfo`: 节点升级信息模型

#### 例子

```python
info = await api.daemon_info("daemon-uuid")
```

### _method_ `daemon(uuid: str)`

执行指定节点的升级

#### 参数

- `uuid`: 节点的 UUID

#### 返回

- `UpgradeResult`: 升级结果模型

#### 例子

```python
result = await api.daemon("daemon-uuid")
```