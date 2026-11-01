---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "MCSMAPI"
  text: "一个帮助开发者更好的使用MCSM的py-SDK"
  tagline: 异步 · 类型安全 · 链式操作
  actions:
    - theme: brand
      text: 快速上手
      link: quick-started
    - theme: alt
      text: 项目地址
      target: _blank
      link: https://github.com/sokoko-org/mcsmapi

features:
  - title: 全异步
    details: 基于 httpx，所有 API 均为 async/await
  - title: 类型安全
    details: Pydantic v2 模型，IDE 自动补全开箱即用
  - title: 链式操作
    details: 返回的模型对象可直接调用操作方法
---

