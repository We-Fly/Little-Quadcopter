### 第二次积分赛（简化）

#### 任务详情

电脑上运行OpenCV代码，让程序识别白纸上的三种形状`🔴``🟥``🔺`和三种不同颜色共9种组合

将识别结果通过`串口`传输给单片机，单片机执行相关处理执行一些反应（比如亮不同的灯

#### 需要了解的知识

[前置知识](https://gitee.com/codygua/little-quadcopter/wikis/Pre-knowledge)

[CV文档(没建好)]()

[如何搭建单片机编译环境(MDK)(没建好)]()

[关于Python、anaconda、pycharm、opencv的概念](https://cloud.lwqwq.com/s/vdoUQ/video?name=%E5%AD%A6%E9%95%BF%E8%AE%B2python%EF%BC%8Cpycharm%EF%BC%8Copencv%E6%A6%82%E5%BF%B5%E8%AE%B2%E8%A7%A3_x264.mp4&share_path=%2F%E8%A7%86%E9%A2%91%E8%B5%84%E6%BA%90%2F%E5%AD%A6%E9%95%BF%E8%AE%B2python%EF%BC%8Cpycharm%EF%BC%8Copencv%E6%A6%82%E5%BF%B5%E8%AE%B2%E8%A7%A3_x264.mp4)

[如何搭建Python-OpenCV环境](https://cloud.lwqwq.com/s/vdoUQ/video?name=opencv%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95_x264.mp4&share_path=%2F%E8%A7%86%E9%A2%91%E8%B5%84%E6%BA%90%2Fopencv%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95_x264.mp4)

#### 如何运行

0. 安装python，并正确配置环境变量
1. 克隆仓库，终端cd到当前位置
2. 需要安装`opencv-python`,运行`pip install opencv-python`

<details>
<summary>如果pip速度慢的话有以下解决方案</summary>

- 如果你有代理软件并使用`Powershell`,输入`$env:HTTP_PROXY="http://127.0.0.1:改成你的端口"`和`$env:HTTPS_PROXY="http://127.0.0.1:改成你的端口"`设置终端代理

- 如果你没有代理软件可以尝试[pip一行命令换源换源](https://www.cnblogs.com/137point5/p/15000954.html)

</details>

3. 确保你终端目录为`/pycv/challenge2`,终端输入`python main.py`

#### 代码

main.py是整个程序的入口，主要功能的实现都写在src下，我这边用了面向对象的写法以提高某些常用功能代码的复用