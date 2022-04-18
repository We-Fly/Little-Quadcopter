## 第二次积分赛（简化）

### 任务详情

电脑上运行OpenCV代码，让程序识别白纸上的三种形状`🔴``🟥``🔺`和三种不同颜色共9种组合

将识别结果通过`串口`传输给单片机，单片机执行相关处理执行一些反应（比如亮不同的灯

### 需要了解的知识

[前置知识](https://gitee.com/codygua/little-quadcopter/wikis/Pre-knowledge)

[CV文档(没建好)]()

[如何搭建单片机编译环境(MDK)(没建好)]()

[关于Python、anaconda、pycharm、opencv的概念](https://cloud.lwqwq.com/s/vdoUQ/video?name=%E5%AD%A6%E9%95%BF%E8%AE%B2python%EF%BC%8Cpycharm%EF%BC%8Copencv%E6%A6%82%E5%BF%B5%E8%AE%B2%E8%A7%A3_x264.mp4&share_path=%2F%E8%A7%86%E9%A2%91%E8%B5%84%E6%BA%90%2F%E5%AD%A6%E9%95%BF%E8%AE%B2python%EF%BC%8Cpycharm%EF%BC%8Copencv%E6%A6%82%E5%BF%B5%E8%AE%B2%E8%A7%A3_x264.mp4)

[如何搭建Python-OpenCV环境](https://cloud.lwqwq.com/s/vdoUQ/video?name=opencv%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95_x264.mp4&share_path=%2F%E8%A7%86%E9%A2%91%E8%B5%84%E6%BA%90%2Fopencv%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95_x264.mp4)

### Windows下的配置

#### 0. 安装python，并正确配置和安装环境

<details>
<summary>conda配置方法</summary>

---

##### 1. 安装和配置conda

1. 首先安装Python和Anaconda，参照上面的视频[如何搭建Python-OpenCV环境](https://cloud.lwqwq.com/s/vdoUQ/video?name=opencv%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95_x264.mp4&share_path=%2F%E8%A7%86%E9%A2%91%E8%B5%84%E6%BA%90%2Fopencv%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95_x264.mp4)

2. 配置conda环境变量，按照你conda安装的位置来，比如你安装在`D:\anaconda3\`则需要添加的path有下面四条

```commandline
D:\anaconda3\
D:\anaconda3\Scripts
D:\anaconda3\Library\bin
D:\anaconda3\Library\mingw-w64
```

3. 然后需要开启Powershell运行PS脚本的限制

**右键**`开始按钮`，点击`Windows PowerShell(管理员)(A)`,然后输入
```commandline
set-executionpolicy remotesigned
```
会出现下面的信息
```commandline
执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”):
```
然后输入大写的`Y`，敲击回车

继续输入
```commandline
Get-ExecutionPolicy
```

如果显示的是 `RemoteSigned`说明设置成功了

4. 接下来需要初始化conda环境，在powershell中继续输入
```commandline
conda init powershell
```

然后关闭powershell

到这边你已经完成了conda环境的配置

##### 2. 配置conda环境

首先创建一个conda环境,`<你的conda环境名称>`可以自定义，我这边是`opencv`,后面的python版本我选择的是3.10,conda会自动搜索3.10最新版本，所有代码都在3.10.4的环境下测试通过
```commandline
conda create -n <你的conda环境名称> python=3.10
```

安装环境的时候可能会提示是否安装，按照提示输入y就可以了

接下来进入`opencv`环境

```commandline
conda activate <你的conda环境名称>
```

这个时候你的终端最左侧应该会从`(base)`变成`(opencv)`或者`<你的conda环境名称>`

接下来需要安装一些包，在安装之前你可能需要配置一下pip，不然速度会很慢

> - 如果你有代理软件并使用`Powershell`,输入`$env:HTTP_PROXY="http://127.0.0.1:改成你的端口"`和`$env:HTTPS_PROXY="http://127.0.0.1:改成你的端口"`设置终端代理

> - 如果你没有代理软件可以尝试[pip一行命令换源](https://www.cnblogs.com/137point5/p/15000954.html)

我们需要安装下面这些包

```commandline
pip install opencv-python
pip install imutils
pip install opencv-contrib-python
pip install argparse
```

---

</details>

#### 1. 克隆仓库，终端cd到当前位置或者配置你的IDE

哦，你或许需要先配置一下git，自己去b站搜教程吧，我就不多讲了

<details>
<summary>Pycharm 配置</summary>

---

首先，我们安装的是社区版的Pycharm，当然你有专业版也没问题

然后看这个教程设置中文[[知乎]如何安装pycharm并设置为中文。](https://zhuanlan.zhihu.com/p/454935826)

然后点击左上方`文件-打开`，定位到`little-quadcopter`文件夹，点击**确定**

这个时候你已经打开了整个项目，python的项目代码在`/pycv/challenge2`下，main.py是整个程序的入口

点击下方的**终端**按钮，会打开一个熟悉的powershell窗口，输入 `conda activate <你的conda环境名称>` 来进入前面配置好的conda环境

接下来通过cd命令来定位到`/pycv/challenge2`文件夹下

```commandline
cd .\pycv\challenge2\
```

这就准备完了，输入`python .\main.py -h` 查看帮助

---

</details>

<details>
<summary>VS Code 配置方法</summary>

---

首先打开项目文件夹，然后右下角会提示安装推荐插件，就全部安装就行，插件的配置前面视频里有讲

然后按`ctrl`+`shift`+`p`调出命令窗口，输入`python`,选择python解释器一项，选择你自己配置的环境

然后点击上方终端，新建终端，会自动帮你激活你的conda环境

接下来通过cd命令来定位到`/pycv/challenge2`文件夹下

```commandline
cd .\pycv\challenge2\
```

这就准备完了，输入`python .\main.py -h` 查看帮助


---

</details>

### 代码

`main.py`是整个程序的入口，主要功能的实现都写在`src/shapedetect`下

<details>
<summary>实现</summary>

| 方法                                                                    | 定义             |
|-----------------------------------------------------------------------|----------------|
| [Picture.\_\_init__()](pycv/challenge2/src/shapedetect/Picture.py#L8) | Picture实例初始化函数 |
|                                                                       |                |
|                                                                       |                |
|                                                                       |                |





</details>