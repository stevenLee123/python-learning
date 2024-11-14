# python-learning
# python 的特点
* 动态类型，不需要指定变量的类型
* 高级抽象和简洁性，通过缩进表示代码块
* 面向对象，支持类、继承、多态
* 广泛的标准库，涵盖从文本到网络编程等多种库
* 解释型语言，代码在运行时逐行执行，不需要编译
* 跨平台性 
* 函数式编程
* 元编程

## 基础语法

* 变量定义 `c = 1`，不需要指定变量类型
* 基本数据类型 整型、浮点型、字符串、布尔值
* 注释，单行注释 `#`，多行注释 """"""
* 基本输入输出 `input()`从键盘读取输入, `print()`输出到console
* 条件语句if、循环语句for、while
* 复合类型 列表与元组 list、 tuple
* 字典（json）允许直接对json进行修改，`person["job"]="enginner"`
* 函数定义与调用 `def method() method()`
* 类与对象（与java类似的写法，定义类，创建对象，调用对象api） class Person 


## python的web框架

* Flask 轻量灵活
* Django 高级web框架，高度模块化，内具如用户认证，界面管理，数据库迁移等功能，适合开发大型复杂应用
* FastAPI 快速高性能web框架
* Starlette用于构建中小型web应用，基于ASGI规范
* Tornado 异步web框架，设计用于处理大量并发连接，异步处理能力强，内置长轮询和WebSocket，Honcho 和 Uvicorn 可以用来部署 Tornado 应用。
* Bottle 简单且轻量的web框架，适合快速开发简单的web应用


## numpy库
强大的科学计算库，广泛应用于数据处理、数据分析、数值计算等领域
### 安装
```shell
pip install numpy
```

### 基础概念

#### 基本数据类型
* 整数int： 表示整数值，3242
* 浮点数float： 带有小数部分的数字，1.5
* 布尔值bool：表示True或False
* 字符串str：表示一串字符，可以使用单引号、双引号或三引号来定义，如'hello',"world",'''hello world''' 
* 列表list：
一个可以放置任意数据类型的有序集合，列表中的元素可变，列表用`[]` 包括元素，元素之间用逗号分隔
```python
[False,True,1,1.5555,'abc']
```
* 元组tuple： 类似于列表，一个可以放置任意数据类型的有序集合，元组中的元素不可变，元组用`()`包括元素，元素之间用逗号隔开
(False,1,'hello')
* 集合set：表示一组无序且不重复的数据，集合用花括号`{}`或`set()`函数来定义
```python
{1,2,3}
set([1,2,3])
```
* 字典dict：表示一组键值对，类似于java的map，用花括号`{}`或`dict()`函数来定义
```python
{'name':'steven',age=18}
dict(name='steven',age=18)
```


* 数组
* 索引与切片
