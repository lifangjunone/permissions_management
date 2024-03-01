# SkeletonExample ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

基于Flask Web框架的微服务骨架，后续的应用开发需要遵循此框架的示例规范

## 代码组织结构

```text
├── bin                      # 可执行的脚本程序
├── conf                     # 应用配置
│   ├── uwsgi.ini            # uWSGI 网关配置
│   └── config.py            # 通用配置
├── docs                     # 应用相关文档
│   └── api                  # API 文档
├── SkeletonExample               # 应用主目录
│   ├── api                  # API 接口
│   │   ├── v1      # v1　版本api
│   │   │   └──__init__.py   # API配置   
│   │   |   |──api.py      # API handler 
│   │   ├── v2      # v2　版本api
│   │   │   └──__init__.py  # API配置   
│   │   |   |──api.py      # API handler 
│   │   ├── common  # 公共 api
│   │   │   └──__init__.py   # API配置   
│   │   |   |──api.py      # API handler 
│   │   └──__init__.py      # 注册路由和蓝图
│   ├── models               # 数据库模型
│   ├── schemas              # schema 数据结构
│   ├── tasks                # 任务目录
│   └──__init__.py          # 初始化应用
├── common                   # 公共和辅助函数库
|   └── consul               # consul 类库
│   └── healthcheck.py       # 服务健康检测
│   └── helpers.py           # 帮助类
│   └── log_handler.py       # 日志自定义模块
│   └── mixins.py            # 上下文管理
│   └── utils.py             # 通用工具类
├── migrations               # 数据库迁移脚本
└── tests                    # 单元测试集合
```

## 快速开始
### 1. 安装依赖并启动项目：

```diff
- 注意，如果使用 conda 配置虚拟环境，请注释 `requirements.txt` 中的 `uwsgi==2.0.20` 依赖，
- 并使用 `conda install -c conda-forge uwsgi` 手动安装，避免出现本地编译时链接错误
```

```shell
  - pip install -r requirements.txt
  - 如果在目录　conf/default.py 中配置数据库的环境变量,则可以自动创建一个和项目同名的数据库,自动创建数据表和测试数据
  - 运行项目：　python manage.py runserver
  - 浏览器访问： http://127.0.0.1:8000/api/api_common/version
  - 返回值：
    
      {
        "api_version": "v1",
        "production": "SkeletonExample",
        "app_version": "v0.0.1",
        "application": "SkeletonExample",
        "platform": "Linux-5.10.18-amd64-desktop-x86_64-with-glibc2.28"
      }
  - 浏览器访问：　http://127.0.0.1:8000/api/api_v1/user[此接口需要在配置文件中配置数据库环境变量才行]
  - 返回值：　
      {
        "msg": "Successful",
        "code": 10000,
        "data": [
            {
                "id": 1,
                "age": 20,
                "updated_at": "2022-12-07T12:55:57",
                "username": "\u5f20\u4e09",
                "sex": "\u7537",
                "created_at": "2022-12-07T20:54:35"
            }
        ]
    　}
```
```diff
- 第一步默认会自动创建一个和项目同名的数据库，自动创建数据表和测试数据，
- 仅供学习和快速跑项目，正式开发时数据库创建请通过下面2[数据库配置]进行配置
```
### 2. 数据库配置

**创建数据库:**
- `create database if not exists 'db_name' default character set utf8 collate utf8_general_ci;`

**数据库迁移：**

1. 初始化并创建数据库表
2. 对数据库进行升级或回滚，保存不同数据库的版本
3. 修改数据库表，同时保留原始数据

- `$ python manage.py db init`    # 创建迁移仓库 migrations
- `$ python manage.py db migrate -m "initial migration"` # 创建迁移脚本
- `$ python manage.py db upgrade` # 更新数据库
- `$ python manage.py db history` # 获取 History ID
- `$ python manage.py db downgrade <history_id>` # 回滚到某个 history 版本


## 环境要求
* Linux
* Python 3.5.2 and up


## 使用说明
### 环境变量
本服务应用的大部分配置都是通过环境变量,本地调试启动需要自行设定如下环境变量：
- ENVIRONMENT # 指定服务当前运行的环境（production、development、testing）， 不指定时默认　开发环境　development


[//]: # (`$ make install`         # 安装依赖模块（运行必须优先执行）  )

[//]: # (`$ make test`            # 单元测试&#40;必须先启动服务&#41;  )

[//]: # (`$ make test-html`       # 生成单元测试报告  )

[//]: # (`$ make coverage-report` # 生成覆盖率报告  )

[//]: # (`$ make docker-doc`      # 文档镜像构建  )

## Docker方式运行
**主程序运行：**
```bash
$ docker build . -t skeleton_example:v1.0.0
$ docker run --rm -p 8000:8000  -e "ENVIRONMENT=testing"  skeleton_example:v1.0.0
```



**接口测试:**
```
$ http GET http://ip:port/api/common/version

```

## 中间件使用：
**redis：**
```bash
$ docker run --rm -p 6379:6379 --name my-redis redis
```


## 项目核心代码说明
**自动检测配置：**
```python
def create_app():
    ...
    # compare_type 设置为 True 会开启检测字段数据变化的功能，比如：字段长度的变更。注意：SQLite 还不支持 drop column 操作。
    migrate.init_app(app, db, compare_type=True)
    ...
```

**参考资料：**
- [自动生成迁移检测机制](http://alembic.zzzcomputing.com/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect)
- [sqlite-alter-table](http://www.sqlitetutorial.net/sqlite-alter-table/)

## 开发调试
```bash
$ virtualenv skeleton-venv
$ . skeleton-venv/bin/activate
$ make install
$ python manage.py runserver
```

# 单元测试
## pytest
**测试样例发现规则:**  
- 测试文件以 test_ 开头
- 测试类以 Test 开头，并且不能带有 `__init__` 方法
- 测试函数以 test_ 开头
- 断言使用基本的 assert 即可

### 常用命令
- `py.test -s -v` 显示运行的函数和内部的打印信息
- `py.test -s -v --html=./test_report.html` 生成 HTML 报告
- `py.test [file_or_dir] [file_or_dir] [...]` 指定一个或多个文件/目录测试

### setup和teardown
- 模块级（setup_module/teardown_module）开始于模块始末
- 类级（setup_class/teardown_class）开始于类的始末
- 类里面的（setup/teardown）（运行在调用函数的前后）
- 功能级（setup_function/teardown_function）开始于功能函数始末（不在类中）
- 方法级（setup_method/teardown_method）开始于方法始末（在类中）

### fixture scope
使用 @pytest.fixture(scope='module') 来定义框架，scope 的范围参数有以下几种

- function   每一个用例都执行
- class        每个类执行
- module     每个模块执行(函数形式的用例)
- session     每个 session 只运行一次，在自动化测试时，登录步骤可以使用该 session

### 框架介绍
+ 自动创建数据库，数据表，以及自动生成测试数据
+ 完善的 readme.md
+ api接口示例代码，models, schemas 示例代码
+ 常用中间件的集成，celery异步任务，redis数据库， sqlalchemy ORM插件， minio对象存储服务
+ 完善的部署脚本
+ 日志定制化插件，定制化的状态码，返回值格式
