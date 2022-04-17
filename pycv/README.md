#### 关于此文件夹

经过团队投票决定，以Python语言作为我们目前些OpenCV的主要语言

##### 如何运行

0. 安装python，并正确配置环境变量
1. 克隆仓库，终端cd到当前位置
2. 需要安装`opencv-python`,运行`pip install opencv-python`

<details>
<summary>如果pip速度慢的话有以下解决方案</summary>

- 如果你有代理软件并使用`Powershell`,输入`$env:HTTP_PROXY="http://127.0.0.1:改成你的端口"`和`$env:HTTPS_PROXY="http://127.0.0.1:改成你的端口"`设置终端代理

- 如果你没有代理软件可以尝试[pip一行命令换源换源](https://www.cnblogs.com/137point5/p/15000954.html)

</details>

3. 确保你终端目录为`/pycv/challenge2`,终端输入`python main.py`

##### 代码

main.py是整个程序的入口，主要功能的实现都写在src下，我这边用了面向对象的写法以提高某些常用功能代码的复用