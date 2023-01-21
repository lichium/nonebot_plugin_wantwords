<p align="center">
  <a href="https://v2.nonebot.dev/store">
  <img src="https://user-images.githubusercontent.com/44545625/209862575-acdc9feb-3c76-471d-ad89-cc78927e5875.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
</p>
<div align="center">

# nonebot_plugin_wantwords

Use [WantWords](https://wantwords.net) as a plugin of [NoneBot](https://github.com/nonebot/nonebot2)

WantWords，但是Nonebot插件

</div>
<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license">
  </a>
  <a href="https://v2.nonebot.dev/">
    <img src="https://img.shields.io/static/v1?label=nonebot&message=v2rc1%2B&color=green" alt="nonebot2">
  </a>
  <img src="https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue" alt="python">
</p>

## 下载

#### 法一：[pip](https://pypi.org/project/nonebot_plugin_wantwords/)

``` bash
pip install nonebot_plugin_wantwords
```

``` python
# NoneBot项目中
nonebot.load_plugin('nonebot_plugin_wantwords')
```

#### 法二：nb-cli「推荐」
``` bash
nb plugin install nonebot_plugin_wantwords
```

## 配置

```bash
# .env或.env.*
wantwords_max_results=10 # 最大输出结果数，为[1,100]整数，默认为10。
```

## 更新日志
- v0.1.0 🎉

## TODO
- 增加筛选功能
- ~~对标官网用户体验~~

## 特别感谢

- [Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [nonebot / nonebot2](https://github.com/nonebot/nonebot2)
- [WantWords](https://wantwords.net)

**欢迎Contribution。因为大多数时间在校，所以各方面均迟缓，见谅。**

**侵权请联系删除**
