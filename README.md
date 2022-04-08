# Little-Quadcopter

#### 介绍

一个四旋翼无人机的仓库，包含了图像识别和无人机飞控等。

#### TODO

[「第二次积分赛」看板预览链接](https://web.banlikanban.com/kanban/62443f876605f437794b0829/欢迎查看板栗看板「第二次积分赛」)

- [x] 决定各项硬件参数
- [x] 购物
- [ ] 硬件组装
- [ ] 搞定飞控
- [ ] 搭建测试场地
- [ ] 让无人机飞起来
- [ ] 达成第二次积分赛的要求


#### 软件架构

| 项目 | 实现方式 | 链接 |
| --- | --- | --- |
| 图像识别 | OpenCV(C++) | [CV部分的文档](/cv/README.md) |
| 飞控方案 | ACFLY A9 | [[Github]ACFLY仓库](https://github.com/superstarzhu/ACFly-Prophet) |
| 地面站 | 待定 |  |


#### 硬件规格

| 硬件 | 具体型号/规格 | 备选 | 链接 | 能否开票 |
| --- | --- | --- | --- | --- |
| 飞控 | ACFLY A9 |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=591615647197&_u=72nf4lkkfb36) | 能，加6个点 |
| 电调 | 好盈XRotor乐天 40A |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=41195768497&_u=72nf4lkk8064) | 可以，补5个点 |
| 电机 | 朗宇 Angel系列 A2212 KV1400 II |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=37277354171&_u=72nf4lkk652d) | 可以，补4个点 |
| 机架 | f330 |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=560813937533&_u=72nf4lkk3529) |
| 电池 | 5000mAh 3S 40c |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=45510144405&_u=72nf4lkkf655) | 可以，补3个点 |
| 起落架 | 随便整一个 |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=560813937533&_u=72nf4lkk3529) |
| 螺旋桨 | 8038 |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=14478811742&_u=72nf4lkk47ac) |
| 图传 | 待定 |  |  |
| 遥控器 | 富斯i6x |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=559784577776&_u=72nf4lkk7c6f) | 可以 |
| 接收机 | IA10B |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=559784577776&_u=72nf4lkk7c6f) | 可以 |
| 深度相机 | 乐视体感摄像头 |  |  |
| 板载电脑 | 树莓派3b mini | OpenML |  |
| 充电器 | 可调电源？ |  |  |
| XT60插接件 | XT60公母头 |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=607100521066&_u=72nf4lkkfc0e) |
| 红色激光头 | 随便买 |  | [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.239b2e8dFKIICV&id=568607919381&_u=72nf4lkk37be) |


#### 参考资料

- [[CSDN]四旋翼无人机飞行器基本知识（四旋翼无人机结构和原理+四轴飞行diy全套入门教程）](https://blog.csdn.net/weixin_43394322/article/details/92832164)

- [[CSDN]多旋翼无人机构成及其原理详解](https://blog.csdn.net/Reign_Man/article/details/107138364)

- [[CSDN]快速搭建一个APMT265树莓派无人机](https://blog.csdn.net/sinat_16643223/article/details/108354556)

- [[CSDN]无人机从零到一（组装、校准到起飞）](https://blog.csdn.net/weixin_41869763/article/details/104991303)

- [[CSDN]小白带你入坑四旋翼无人机——物料篇](https://blog.csdn.net/weixin_43689161/article/details/109231863)

- [[CSDN]好盈电调，乐天和天行者](https://blog.csdn.net/sinat_16643223/article/details/107234723)

- [[CSDN]四旋翼无人机硬件，飞控，基站，NX](https://blog.csdn.net/weixin_54614931/article/details/120029310)

- [[CSDN]PX4系统学习](https://blog.csdn.net/qq_43096525/article/details/109283976)

- [[CSDN][ACFLY全新开源飞控--先知系列] ACFly Prophet](https://blog.csdn.net/weixin_40767422/article/details/102639677)

- [[Github]ACFLY仓库](https://github.com/superstarzhu/ACFly-Prophet)

- [[CSDN]ACfly调参记录（包括ACfly-F330和ACfly-T265）](https://www.csdn.net/tags/NtjaYg0sMzg4OTktYmxvZwO0O0OO0O0O.html)