<p align="center">
    <a href="https://github.com/HL56/auto_test.git" target="_blank">
        <img src="https://raw.githubusercontent.com/docker-library/docs/01c12653951b2fe592c1f93a13b4e289ada0e3a1/python/logo.png" height="100px">
    </a>
    <h2 align="center">自动化测试</h2>
    <br>
</p>

### 快速使用

```sh
# 拉取代码
$ git clone https://github.com/HL56/auto_test.git
```

```sh
# 安装依赖
$ pip install -r requirements.txt
```

```sh
# 执行测试
$ python main.py
```

### 使用docker

```sh
# 安装
$ docker-compose up -d

# 执行测试
$ docker exec test python main.py
```

### 目录结构

```txt
reports                  测试报告
src                      测试用例书写
    utils
        tool.py          工具
settings.py              环境变量
main.py                  入口文件
```
