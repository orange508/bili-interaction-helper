# bili-interaction-helper

一个 Python 小脚本，可以跑在服务器上。


## 这个项目能干什么

获取 B站指定分区的最新视频。

纯学习用途，代码简单，适合新手看。


## 用之前需要装的东西

Python 3.8 以上，需要装两个库：

```bash
pip install requests python-dotenv
```

建议用虚拟环境（但不是必须）

```bash
python3 -m venv venv
source venv/bin/activate   # Windows 用 venv\Scripts\activate
pip install requests python-dotenv
```


## 配置文件

仓库里有 .env.example，复制一份改个名：

```bash
cp .env.example .env
```

然后编辑 .env，填上你自己的 Cookie：

```bash
nano .env   # 或者用记事本
```

## Cookie 获取方法

1. 浏览器登录 B站
2. 按 F12 → Application → Cookies
3. 找到下面三个，复制进去：
   · SESSDATA
   · bili_jct
   · buvid3

## 注意：不要把填好 Cookie 的 .env 文件传到 GitHub 上。


## 分区 ID

改了 TID 就能换分区：

TID 分区
188 科技区
1 动画区
24 MAD·AMV
129 宅舞区


## 运行

```bash
python main.py
```

如果要在后台跑，可以用 nohup 或 systemd，看你自己习惯。


## 联系方式

开发者电话： ```
           13476825301
           ```

