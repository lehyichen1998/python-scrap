## 自我介绍

> 姓名 ：计缘
> 英文名：Milk

## 课程模式

- 直播上课：如果有没有听懂的地方，随时可以和老师互动
- 高清录播：课下随时随地复习
- 课后答疑：有任何疑问可以随时联系老师

## 课程大纲

1. 开发环境配置

2. 爬虫基础

3. 基本库的使用

4. 解析库的使用

5. 项目作业修改与辅导 （foodpanda shopee)
6. 用requests做一个自用翻译软件
7. Ajax数据爬取
8. 阶段考核汇总与辅导
9. 用 selenium对动态网页进行爬取
10. 用selenium对网页做自动化
11. 图片验证码的破解
12. 滑动验证码的破解
13. App的爬取
14. scrapy框架的使用
15. 分布式爬虫
16. 结课考核点评



## 一.开发环境配置

工欲善其事，必先利其器！

编写和运行程序之前，我们必须先把开发环境配置好。只有配置好了环境且有了更方便的开发工具，我们才能更加高效地用程序实现相应的功能。然而很多情况下，我们可能在最开始就卡在环境配置上，如果这个过程花费了太多时间，学习的兴趣可能就下降了大半，所以这里专门对环境配置做一些说明。



### 1.1 Python3的安装

- 既然要用python3开发爬虫，那么第一步一定是安装Python3.
- 官方网站：http://python.org
- 下载地址：https://www.python.org/downloads
- 第三方库:https://pypi.python.org/pypi
- 官方文档:https://docs.pthon.org/3
- 中文教程:http://www.runoob.com/python3/python3-tutorial.html
- Awesome Python:https://github.com/vinta/awesome-python
- Awesome Python中文版:https://github.com/jobbole/awesome-python-cn

### 1.2 Windows下的安装

- 通过Anconda，它提供了Python的科学计算环境，里面自带了Python以及常用的库。如果选用了这种方式，后面的环境配置会更加简单。

- 直接下载安装包安装，即标准的安装方式

  #### 1.Anaconda安装

  下载链接https://www.anaconda.com/products/individual#Downloads,选择Python3版本的安装包下载如下图所示

  ![image-20210421140118737](C:\Users\javac\Desktop\class\image-20210421140118737.png)
  
  下载完成之后，直接双击安装包安装即可。安装完成之后,Python3的环境就配置好了。
  
  #### 2.安装包安装
  
  我们推荐直接下载安装包来安装，此时可以直接到官方网站下载Python3的安装包：https://www.python.org/downloads/
  
  > ​                                    **注意安装时要点击    add in path**

​    ![20180918205426465](C:\Users\javac\Desktop\class\20180918205426465.png)

**3.测试验证**

安装完成后，可以通过命令行测试一下安装是否成功。在“开始”菜单中搜索cmd，找到命令提示符。输入python，测试一下能否成功调用python，测试结果如下图所示

![image-20210421141800039](C:\Users\javac\Desktop\class\image-20210421141800039.png)

### 1.3 Linux下的安装

Linux下的安装方式有多种：命令安装，源码安装和Anaconda安装

> 推荐系统系带命令安装或Anaconda安装

- CentOS，Red Hat(以Python3.5为例)

```命令提示符
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm

sudo yum update

sudo yum install -y python35u python35u-libs python35u-devel python35u-pip
```

- Ubuntu，Debian和Deepin

```命令提示符
sudo apt-get install -y python3-dev build-essential libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev libcurl4-openssl-dev

sudo apt-get install -y python3

sudo apt-get install -y python3-pip
```

- Anaconda安装

下载链接https://www.anaconda.com/products/individual#Downloads,选择Python3版本的安装包下载如下图所示![image-20210421140118737](C:\Users\javac\Desktop\class\image-20210421140118737.png?lastModify=1618987941)

 **测试验证**

在命令行界面下测试Python3和pip3是否安装成功

```
$python3
python 3.5.2(default,Nov 17 2019, 17:05:23)
Type"help","copyright","credits"or"license" for more information
```

### 1.4 Mac下的安装

在Mac下同样有多种安装方式，如Homebrew，安装包安装，Anaconda安装等，这里推荐使用Homebrew安装

1.Homebrew安装

Homebrew是Mac平台下强大的包管理工具，其官方网站是https://brew.sh/

执行如下命令，即可安装Homebrew：

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2.安装包安装

可以到官网下载Python3安装包。 https://www.python.org/downloads/

3Anconda安装

下载链接https://www.anaconda.com/products/individual#Downloads,选择Python3版本的安装包下载如下图所示![image-20210421140118737](C:\Users\javac\Desktop\class\image-20210421140118737.png?lastModify=1618988497)

**测试验证**

打开终端，在命令行界面Python3和pip3是否成功安装

```
~python3
python 3.6.1 (default, Apr 4 2017, 09:40:21)
[Gcc 4.2.1 Compatible Apple LLVM 8.1.0(clang-802.0.38)] on darwin
Type "help" , "copyright" "credits" or "license" for more information.
```



## 二.爬虫基础

在写爬虫之前，我们还需要了解一些基础知识，如HTTP原理，网页的基础知识，爬虫的基本原理，Cookies的基本原理等。本章中，我们就对这些基础知识做一个简单的总结。

### 2.1 Http基本原理

在本节中，我们会详细了解HTTP的基本原理，了解在浏览器中敲入URL到获取网页内容之间发生了什么。了解这些内容，有助于我们进一步了解爬虫的基本原理。

#### 2.1.1URI和URL

 这里我们先了解一下URI和URL，URI的全称为Uniform Resource Identifier，即统一资源标志符，URL的全称为Universal Resurce Identifier，即统一资源定位符。

举例来说，https://github.com/favicon.ico是GitHub的网站图标链接，它是一个URL，也是一个URI。即有这样的一个图标资源，我们用URL/URL来唯一指定了它的访问方式，这其中包括了访问协议https，访问路径（/即根目录）和资源名称favicon.io通过这样一个链接，我们便可以从互联网上找到这个资源，这就是URL/URI.

URL是URI的子集，也就是说每个URL都是URI，但不是每个URI都是URL。那么，怎么样的URL不是URL呢？URI还包括一个子类叫作URN，他的全称为Universal　Resource　Name，即统一资源名称。URN只命名资源而不指定如何定位资源，比如urn:isbn:0451450523指定了一本书的ISBN，可以唯一标识这本书，但是没有指定到哪里去定位这本书，这就是URN。URL，URN和URI的关系可以用下图表示

![urluriurn](C:\Users\javac\Desktop\class\urluriurn.png)

但是在目前的互联网中，URN用的非常少，所以几乎所有的URI都是URL，一般的网页链接我们即可以称为URL，也可以称为URI，我个人习惯称为URL。

#### 2.1.2超文本

接下来，我们再了解一个概念——超文本，其英文名叫作hypertext，我们再浏览器里看到的网页就是超文本解析而成的，其网页源代码是一系列的HTML代码，里面包含了一系列标签，比如ｉｍｇ显示图片，ｐ指定显示段落等。浏览器解析这些标签后，便形成了我们平常看到的网页，而网页的源代码HTML就可以称作超文本．

　　　例如，我们在chrome浏览器里面打开任意一个页面，如ｓｈｏｐｅｅ首页，右击任一地方并选择“检查”项（或直接按快捷F１２），即可打开浏览器的开发者工具，这时在Elements选项卡即可看到当前网页的源代码，这些源代码都是超文本，如下图所示。![shopee](C:\Users\javac\Desktop\class\shopee.jpg)

#### 2.1.3HTTP和HTTPS

在虾皮网的首页https://shopee.com.my/中，URL的开头会有ｈｔｔｐ或ｈｔｔｐｓ，这就是访问资源需要的协议类型。有时，我们还会看到ｆｔｐ（POST协议，端口号２１，２０），ｓｆｔｐ（在ｆｔｐ基础上进行加密），ｓｍｂ（文件共享）开头的URL，它们都是协议类型。在爬虫中，我们抓取的页面通常就是ｈｔｔｐ或ｈｔｔｐｓ协议的，这里首先了解一下这两个协议的含义。

HTTP的全称是Hyper　Ｔｅｘｔ　Ｐｒｏｔｏｃｏｌ，中文名叫做超文本传输协议。HTTP协议是用于从网络传输超文本数据到本地浏览器的传送协议，它能保证高效而准确地传送超文本文档。HTTP由万维网协会（Ｗｏｒｌｄ　Ｗｉｄｅ　Ｗｅｂ　Ｃｏｎｓｏｒｔｉｕｍ）和Ｉｎｔｅｒｎｅｔ工作小组IETF（Ｉｎｔｅｒｎｅｔ，Engineering　Task　Force）共同合作定制的规范，目前广泛使用的是HTTP１.１版本。

HTTPS的全称是Hyper　Text　Transfer　Protocol　over　Secure　Socket　Layer，是以安全为目标的HTTP通道，简单讲是HTTP的安全版，即HTTP下加入SSL层，简称为HTTPS。

ＨＴＴＰＳ的安全基础是SSL，因此通过它传输的内容都是经过SSL加密的，它的主要作用可以分为两种。

建立一个信息安全通道来保证数据传输的安全

确认网站的真实性，凡是使用了HTTPS的网站，都可以通过点击浏览器地址栏的锁头标志来查看网站认证之后的真实信息，也可以通过CA机构颁发的安全签章来查询。现在越来越多的网站和Aｐｐ都已经向HTTPS方向发展，例如：

1.苹果公司强制所有IOS App在2017年1月1日前全部改为使用HTTPS加密，否则App就无法在应用商店上架；

2.谷歌从2017年1月推出的Chrome56开始，对未进行HTTPS加密的网址链接亮出风险提示，即在地址栏

的显著位置提醒用户“此网页不安全”；

3.腾讯微信小程序的官方需求文档要求后台使用HTTPS请求进行网络通信，不满足条件的域名和协议无法请求。

#### 2.1.4HTTP请求过程

我们在浏览器中输入一个URL，回车之后便会在浏览器中观察到页面内容，实际上，这个过程是浏览器向网站所在的服务器发送了一个请求，网站服务器收到这个请求后进行处理和解析，然后返回对应的相应，接着传回给浏览器。响应里包含了页面的源代码等内容，浏览器再对其进行解析，便将网页呈现里出来，模型如下图所示

<img src="C:\Users\javac\Desktop\class\a.jpg" alt="a" style="zoom:80%;" />

此处客户机即代表我们自己的PC或手机浏览器，服务器即要访问的网站所在的服务器。

为了更直观地说明这个过程，这里用Chrome浏览器的开发者模式下的Network监听组件来做下演示，它可以显示访问当前请求网页时所发生的所有网络请求和响应。

打开chrome浏览器，右击并选择“检查”选项，即可打开浏览器的开发者工具。这里访问https://shopee.com.my/，输入该URL后回车，观察这个过程中发生了怎样的网络请求。可以看到，再Network页面下方出现了一个个的条目，其中一个条目就代表一次发送请求和接收响应的过程，如下图所示

![shopee](C:\Users\javac\Desktop\class\shopeenet.png)

我们观察第一个网络请求，其中各列的含义如下

- 第一列Name：请求的名称，一般会将URL的最后一部分内容当作名称

- 第二列Status：响应的状态码，这里显示为200，代表响应是正常的。通过状态码，我们可以判断发送了请求之后是否得到了正常的响应。

- 第三列Type：请求的文档类型。这里为xhr，代表这次请求为一次ajax请求。若为document，代表请求的是一个HTML文档，内容就是一些HTML代码。

- 第四列Initator：请求源。用来标记请求是由哪个对象或进程发起的。

- 第五列Size：从服务器下载的文件和请求的资源大小。如果是从缓存中取得的资源，则该列会显示from cache

- 第六列Time：发起请求到获取响应所用的总时间。

- 第七列Waterfall：网络请求的可视化瀑布流。

  点击这个条目即可看到更详细的信息。如下图所示

![image-20210426144529892](C:\Users\javac\Desktop\class\image-20210426144529892.png)

首先是General部分，Request URL为请求的URL，Request Method为请求的方法，Status Code响应状态码，Remote Address 为远程服务器的地址和端口， Referrer Policy Referrer 判别策略。再继续往下，可以看到，有 Response Headers Request Headers ，这分别代表响应头和请求头请求头里带有许多请求信息，例如浏览器标识、 ookies Host 等信息，这是请求的一部分，服务器会根据请求头内的信息判断请求是否合法，进而作出对应的响应 图中看到的 Response Headers就是响应的一部分，例如其中包含了服务器的类型、文档类型、日期等信息，浏览器接受到响应后，会解析响应内容，进而呈现网页内容。

下面我们分别来介绍 下请求和响应都包含哪些内容

#### 2.1.5请求

请求，由客户端向服务端发出，可以分为 部分内容：请求方法（ Request Method 请求的网址

( Request URL ）、请求头（ Request Headers ），请求体（ Request Body ）。

- 请求方法

常见的请求方法有两种 GET POST。

在浏览器中直接输入 URL 并回车，这便发起了一个 GET 请求，请求的参数会直接包含到 URL里

> 例如，在百度中搜索 Python ，这就是一个 GET 请求，链接为 https://www.baidu.com/s?wd=python , 
>
> 其中 URL 中包含了请求的参数信息，这里参数 wd 表示要搜寻的关键字 POST 请求大多在表单提交
>
> 时发起。比如，对于一个登录表单，输入用户名和密码后，点击“登录”按钮，这通常会发起一个 POST请求，其数据通常以表单的形式传输，而不会体现在 URL中.

GET 和POST 请求方法有如下区别.

```
1.GET 请求中的参数包含在 URL 里面，数据可以在 URL 中看到，而 POST 请求的 URL 会包

含这些数据，数据都是通过表单形式传输的，会包含在请求体中。
```

```
2.GET 请求提交的数据最多只有 1024 字节，而 POST 方式没有限制.
```

一般来说，登录时，需要提交用户名和密码，其中包含了敏感信息，使用 GET 方式请求的话，

密码就会暴露在 URL 里面，造成密码泄露，所以这里最好以 POST 方式发送 上传文件时，由于文件

内容比较大，也会选用 POST 方式.

我们平常遇到的绝大部分请求都是 GET POST 请求，另外还有 些请求方法，如 GET,HEAD,

POST,PUT,DELETE,OPTIONS,CONNECT,TRACE ，我们简单将其总结为下图。

| 方法    | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| GET     | 请求页面，并返回页面内容                                     |
| HEAD    | 类似于 GET 请求， 只不过返回的响应中没有具体的内容，用于获取报头 |
| POST    | 大多用于提交表单或上传文件，数据包含在请求体中               |
| PUT     | 从客户端向服务器传送的数据取代指定文梢中的内容               |
| DELETE  | 请求服务器删除指定的页面                                     |
| CONNECT | 把服务器当作跳板，让服务器代替客户端防问其他网页             |
| OPTIONS | 允许客户端查看服务器的性能                                   |
| TRACE   | 囚显服务器收到的请求，主要用于测试或诊断                     |

- 请求的网址

  请求的网址，即统 资惊定位符 URL ，它可以唯一确定我们想请求的资源

- 请求头

  请求头，用来说明服务器要使用的附加信息，比较重要的信息有 Cookie Referer User-Agent等

  下面简要说明一些常用的头信息。

Accept ：请求报头域，用于指定客户端可接受哪些类型的信息

Accept-Language ：指定客户端可接受的语言类型

Accept-Encoding ：指定客户端可接受的内容编码

Host ：用于指定请求资源的主机 IP 和端口号，其内容为请求 URL 的原始服务器或网关的位置

从HTTP 1.1 版本开始，请求必须包含此内容

Cookie ：也常用复数形式 Cookies ，这是网站为了辨别用户进行会话跟踪而存储在用户本地

的数据，它的主要功能是维持当前访问会话，例如，我们输入用户名和密码成功登录某个网

站后，服务器会用会话保存登录状态信息，后面我们每次刷新或请求该站点的其他页面时，

会发现都是登录状态，这就是 Cookies 的功劳。Cookies 里有信息标识了我们所对应的服务器

的会话，每次浏览器在请求该站点的页面时，都会在请求头中加上 Cookies 并将其发送给服

务器，服务器通过 Cookies 识别出是我们自己，并且查出当前状态是登录状态，所以返回结

果就是登录之后才能看到的网页内容。

Referer ：此内容用来标识这个请求是从哪个页面发过来的，服务器可以拿到这一信息并做相

应的处理，如做来源统计、防盗链处理等。

User-Agent ：简称 UA ，它是一个特殊的字符串头，可以使服务器识别客户使用的操作系统

及版本 浏览器及版本等信息，在做爬虫时加上此信息，可以伪装为浏览器；如果不加，很

可能会被识别除为爬虫

Content-Type ：也叫互联网媒体类型（ Internet Media Type ）或者 MIME 类型，在 HTTP 协议

消息头中，它用来表示具体请求中的媒体类型信息 例如， text/html 代表 HTML 格式，

image/gif 代表 GIF 图片， application/json代表JSON 类型，更多对应关系可以查看此对照表

http://tool.oschina.net/commons.

- 4.请求体

  请求体一般承载的内容是 POST 请求中的表单数据，而对于 GET 请求，请求体则为空

  例如，这里我登录 GitHub 时捕获到的请求和响应如下图所示

![data](C:\Users\javac\Desktop\class\data.jpg)

登录之前，我们填写了用户名和密码信息，提交时这些内容就会以表单数据的形式提交给服务器，

此时需要注意 Request Headers 指定 Cont nt-Type application, x-www-form-urlencoded 只有设置

Content-Type application/x-www-form-urlencoded ，才会以表单数据的形式提 另外，我们也可以

将Content-Type 设置为 application/ison 来提交 JSON 数据，或者设置为 mu lti part/form-data 上传文件

下表列出了 content-Type POST 提交数据方式的关系.

| Content-Type                       | 提交数据的方式   |
| ---------------------------------- | ---------------- |
| application/x-www-forrn-urlencoded | 表单数据         |
| multi part/form-data               | 表单文件上传     |
| application/json                   | 序列化 JSON 数据 |
| 表单文件上传                       | XML 数据         |

在爬虫中，如果要构造 POST 请求，需要使用正确的 Content-Type ，并了解各种请求库的各个参

数设置时使用的是哪种 Content-Type 不然可能会导致 POST 提交后无法正常响应.

#### 2.1.6响应

响应，由服务端返回给客户端，可以分为三部分：响应状态码（ Response Status Code ）、响应头

( Response Headers ）和响应体（ Response Body ）。

1.响应状态码

响应状态码表示服务器的响应状态，如 200 代表服务器正常响应， 404 表页面未找到， 500代表服务器内部发生错误 在爬虫中，我们可以根据状态码来判断服务器响应状态，如状态码为 200 ，则证明成功返回数据 再进行进一步的处理，

| 状态码 | 说明           | 详情                                                         |
| ------ | -------------- | ------------------------------------------------------------ |
| 100    | 继续           | 请求者应当继续提出请求 服务器已收到请求的一部分，正在等待其余部分 |
| 101    | 切换协议       | 请求者已要求服务器切换协议，服务器已确认并准备切换           |
| 200    | 成功           | 服务然已成功处理了请求                                       |
| 201    | 已创建         | 请求成功并且服务器创建了新的资源                             |
| 202    | 已接受         | 服务然已接受请求，但尚未处理                                 |
| 203    | 非授权信息     | 服务器已成功处理了请求，但返回的信息可能来自另 个源          |
| 204    | 无内容         | 服务器成功处理了请求 但没有返回任何内容                      |
| 205    | 重置内容       | 服务器成功处理了请求，内容被重宜                             |
| 206    | 部分内容       | 服务器成功处理了部分请求                                     |
| 300    | 多种选择       | 针对请求，服务器可执行多种操作                               |
| 301    | 永久移动       | 请求的网页已永久移动到新位置，即永久重定向                   |
| 302    | 临时移动       | 请求的网页暂时跳转到其他页面，即暂时重定向                   |
| 303    | 查看其他位置   | 如果原来的请求是 POST 定向目标文档应该通过 GET 提取          |
| 304    | 未修改         | 此次请求返回的网页未修改 继续使用上次的资源                  |
| 305    | 使用代理       | 请求者应该使用代理访问该网页                                 |
| 307    | 临时重定向     | 请求的资源临时从其他位置 响应                                |
| 400    | 错误谙求       | 服务器无法解析该请求                                         |
| 401    | 米授权         | 请求没有进行身份验证或验证未通过                             |
| 403    | 禁止访问       | 服务将拒绝此请求                                             |
| 404    | 未找到         | 服务器找不到请求的网页                                       |
| 405    | 方法禁用       | 服务器禁用了请求中指定的方法                                 |
| 406    | 不接受         | 无法使用请求的内容响应请求的网页                             |
| 407    | 需要代理搜权   | 请求者需要使用代理授权                                       |
| 408    | 请求超时       | 服务器请求超时                                               |
| 409    | 冲突           | 服务器在完成请求时发生冲突                                   |
| 410    | 已删除         | 请求的资源已永久删除                                         |
| 411    | 需要有效长度   | 服务器不接受不含有效内容长度标头字段的请求                   |
| 412    | 未满足前提条件 | 服务器未满足请求者在请求中设置的其中 个前提条件              |
| 413    | 请求实体过大   | 请求实体过大，超出服务器的处理能力                           |
| 414    | 请求 URI 过长  | 请求网址过长，服务器无法处理                                 |
| 415    | 不支持类型     | 请求格式不被请求页面支持                                     |
| 416    | 请求范围不符   | 页而无法提供请求的范围                                       |
| 417    | 术满足期望值   | 服务器未满足期望请求标头 段的要求                            |
| 500    | 服务器内部错误 | 服务器遇到错误，无法完成请求                                 |
| 501    | 未实现         | 服务器不具备完成请求的功能                                   |
| 502    | 错误网关       | 服务器作为网关或代理 从上游服务器收到无效响应                |
| 503    | 服务器不可用   | 服务器目前无法使用                                           |
| 504    | 网关超时       | 服务器作为网关或代理，但是没有及时从上游服务~~收到请求       |
| 505    | HTTP版本不支持 | 服务器不支持请求中所用的 TP 协议版本                         |

2.响应头

响应头 含了 务器对请求的应答信息，如 Content-Type Server,Set- Cookie下面简要说明一些常用头信息.

- Date 标识响应产生的时间。

- Last-Modified 指定资源的最后修改时间。

- Content-Encoding 指定响应内容的编码。

- Server 包含服务器的信息 ，比如 名称、版本号等。

- Content-Type 文档类型 ，指定返回的数据类型是 ，如 text/html 代表返回 HTML 文档，application/x-javascript返回 JavaScript文件， image/jpeg 代表返回图片

- Set-Cookie 设置 Cookie 应头中的 Set-Cook 告诉浏览器需要将此内容放在 Cookies中，下次请求携带 Cookies 请求

- Expires 指定响应过期时间，可以使代理务器或浏览器将加载的内容更新到缓存中。如果再次访问时，就可 直接从缓存中加载， 降低服务器负载，缩短加载时间。

  3.响应体

  最重要的当属响应体的内容了，响应的正文数据都在响应体中，比如请求网页时，它的响应体就是网页的HTML代码，请求一张图片时，他的响应体就是图片的二进制数据。做爬虫请求网页后，要解析的内容就是响应体。![image-20210428141609751](C:\Users\javac\Desktop\class\image-20210428141609751.png)

  在浏览器开发者工具中点击 Preview ，就可以找到网页的源代码也就是响应体的内容，它是解析的目标。

  在做爬虫时，我们主要通过响应体得到网页得源代码，JSON 数据等，然后从中做相应内容的提取。

  本节中 ，我们了解了 HTTP 的基本原理大概了解了访问网页时背后的请求和响应过程。本节涉及的知识点需要好好掌握，后面分析网页请求会经常用到。

  ### 2.2网页基础

  用浏览器访问网页时，页面各不相同，你有没有想过它为何会呈现这个样子呢？本节中，我们就来了解一下网页的基本组成、结构和节点等内容。

  #### 2.2.1网页的组成

  网页可以分为三大部分一一HTML  CSS  JavaScript。如果把网页比作一个人的话， HTML相当

  于骨架， JavaScript 相当于肌肉，css相当于皮肤，三者结合起来才能形成一个完善的网页。下面我们分别来介绍一下这三部分的功能。

  1.HTML

  HTML 是用来描述网页的一种语言，其全称叫作 Hyper Text Markup Language，即超文本标记语言,网页包括文字、按钮、图片和视频等各种复杂的元素，其基础架构就是 HTML。不同类型的文字通过不同类型的标签来表示，如图片用 img 标签表示，视频用 video 标签表示，段落用p标签表示，它们之间的布局又常通过布局标签 div 嵌套组合而成，各种标签通过不同的排列和嵌套才形成了网页的框架.

  在 Chrome 浏览器中打开百度，右击并选择"检查"项（或按 F12 键），打开开发者模式，这时在 Elements 选项卡中即可看到网页的源代码，如下图。![image-20210428143800138](C:\Users\javac\Desktop\class\image-20210428143800138.png)

  这就是 HTML，整个网页就是由各种标签嵌套组合而成的。这些标签定义的节点元素相互嵌套和组合形成了复杂的层次关系，就形成了网页的架构。

  2.CSS

  HTML定义了网页的结构，但是只有 HTML 页面的布局并不美观，可能只是简单的节点元素的排列，为了让网页看起来更好看一些，这里借助了 CSS。

  CSS，全称叫作 Cascading Style Sheets，即层叠样式表。"层叠"是指当在 HTML 中引用了数个样式文件，并且样式发生冲突时，浏览器能依据层叠顺序处理。"样式"指网页中文字大小、颜色、元素间距、排列等格式。

  CSS 是目前唯一的网页页面排版样式标准，有了它的帮助，页面才会变得更为美观。上图的右侧即为 CSS，例如∶

  ```
  #thead wrapper.s-ps-islite .S-p-top {
  
  position: absolute; 	
  
  bottom: 40px; 
  
  width: 100%;
  
   height: 181px;
  
  }
  ```

  就是一个 CSS 样式。大括号前面是一个 CSS 选择器。此选择器的意思是首先选中 id为 head_wrapper且class 为 s-ps-islite 的节点，然后再选中其内部的 class 为s-p-top 的节点。大括号内部写的就是一条条样式规则，例如 position指定了这个元素的布局方式为绝对布局，bottom指定元素的下边距为 40 像素，width 指定了宽度为 100%占满父元素，height 则指定了元素的高度。也就是说，我们将位置、宽度、高度等样式配置统一写成这样的形式，然后用大括号括起来，接着在开头再加上 CSS 选择器，这就代表这个样式对 CSS 选择器选中的元素生效，元素就会根据此样式来展示了。

  在网页中，一般会统一定义整个网页的样式规则，并写入 CSS 文件中（其后缀为 css）。在 HTML中，只需要用link 标签即可引入写好的 CSS 文件，这样整个页面就会变得美观、优雅。

  3.JavaScript

  JavaScript，简称 JS，是一种脚本语言。HTML 和 CSS 配合使用，提供给用户的只是一种静态信息，缺乏交互性。我们在网页里可能会看到一些交互和动画效果，如下载进度条、提示框、轮播图等，这通常就是 JavaScript 的功劳。它的出现使得用户与信息之间不只是一种浏览与显示的关系，而是实现了一种实时、动态、交互的页面功能。

  JavaScript 通常也是以单独的文件形式加载的，后缀为 js，在 HTML 中通过 script 标签即可引入，例如

  ```
  <script src="jquery-2.1.0.js"></script>
  ```

  综上所述，HTML 定义了网页的内容和结构，CSS 描述了网页的布局，JavaScript 定义了网页的行为。

  2.2.2 网页的结构

  我们首先用例子来感受一下 HTML 的基本结构。新建一个文本文件，名称可以自取，后缀为 html，内容如下∶

  <!DOCTYPE html>
  <html>
      <head> 
          <meta charset="UTF-8"><title>This is a Demo</title>
      </head>
      <body>
          <div id="container"><div class="wrapper">
              <h2 class="title">Hello World</h2>
              <p class="text">Hello,this is a paragraph.</p></div</div>
              </body>
              </html>

  这就是一个最简单的 HTML 实例。开头用 DOCTYPE 定义了文档类型，其次最外层是 html标签，最后还有对应的结束标签来表示闭合，其内部是 head标签和 body标签，分别代表网页头和网页体，它们也需要结束标签。head 标签内定义了一些页面的配置和引用，如∶ <meta charset="UTF-8"> 它指定了网页的编码为 UTF-8。

  title 标签则定义了网页的标题，会显示在网页的选项卡中，不会显示在正文中。body 标签内则是在网页正文中显示的内容。div 标签定义了网页中的区块，它的 id是 container，这是一个非常常用的属性，且 id 的内容在网页中是唯一的，我们可以通过它来获取这个区块。然后在此区块内又有一个 div 标签，它的 class 为 wrapper，这也是一个非常常用的属性，经常与 CSS 配合使用来设定样式。然后此区块内部又有一个 h2 标签，这代表一个二级标题。另外，还有一个p标签，这代表一个段落。在这两者中直接写入相应的内容即可在网页中呈现出来，它们也有各自的 class 属性。

  将代码保存后，在浏览器中打开该文件，可以看到如图所示的内容。可以看到，在选项卡上显示了This is a Demo字样，这是我们在 head 中的 title 里定义的文字。而网页正文是 body 标签内部定义的各个元素生成的，可以看到这里显示了二级标题和段落。

  ![image-20210428145012799](C:\Users\javac\Desktop\class\image-20210428145012799.png)

  这个实例便是网页的一般结构。一个网页的标准形式是 html标签内嵌套 head和 body标签，head内定义网页的配置和引用，body 内定义网页的正文。

  2.2.3 节点树及节点间的关系

  在 HTML 中，所有标签定义的内容都是节点，它们构成了一个 HTML DOM树。

  我们先看下什么是DOM。DOM是W3C（万维网联盟）的标准，其英文全称 DocumentObject Model，即文档对象模型。它定义了访问 HTML 和 XML 文档的标准∶

  > W3C 文档对象模型（DOM）是中立于平台和语言的接口，它允许程序和脚本动态地访问和更新文档的内容、结构和样式。 

  W3C DOM标准被分为 3个不同的部分。

  > 口 核心 DOM∶ 针对任何结构化文档的标准模型。
  >
  > 口 XML DOM∶ 针对 XML 文档的标准模型。
  >
  > 口 HTML DOM∶ 针对 HTML 文档的标准模型。

  根据 W3C 的 HTML DOM标准，HTML 文档中的所有内容都是节点。

  > 口 整个文档是一个文档节点。
  >
  > 口 每个 HTML 元素是元素节点。
  >
  > 口 HTML 元素内的文本是文本节点。
  >
  > 口 每个 HTML 属性是属性节点。
  >
  > 口 注释是注释节点。

  HTML DOM将HTML 文档视作树结构，这种结构被称为节点树，如下图所示

![jiedianshu](C:\Users\javac\Desktop\class\jiedianshu.png)

通过 HTML DOM ，树中的所有节点均可通过 Java Script 访问，所有 HTML 节点元素均可被修改，也可以被创建或删除节点树中的节点彼此拥有层级关系 我们常用父（ parent ）、子（ child ）和兄弟（ sibling ）等术语描述这些关系 父节点拥有子节点，同级的子节点被称为兄弟节点在节点树中，顶端节点称为根（ roo 除了根节点之外，每个节点都有父节点，同时可拥有任意数量的子节点或兄弟节点下图展示了节点树以及节点之间的关系.![tree](C:\Users\javac\Desktop\class\tree.png)

 2.2.4 选择器

我们知道网页由一个个节点组成，CSS 选择器会根据不同的节点设置不同的样式规则，那么怎样来定位节点呢?

在 CSS中，我们使用CSS选择器来定位节点。例如，上例中 div 节点的id为 container，那么就可以表示为#container，其中#开头代表选择 id，其后紧跟 id 的名称。另外，如果我们想选择 class为 wrapper 的节点，便可以使用.wrapper，这里以点（.）开头代表选择 class，其后紧跟class 的名称。另外，还有一种选择方式，那就是根据标签名筛选，例如想选择二级标题，直接用 h2 即可。这是最常用的 3种表示，分别是根据 id、class、标签名筛选，请牢记它们的写法。

另外，CSS 选择器还支持嵌套选择，各个选择器之间加上空格分隔开便可以代表嵌套关系，如#container .wrapper    p则代表先选择 id为 container 的节点，然后选中其内部的 class 为 wrapper 的节点，然后再进一步选中其内部的p节点。另外，如果不加空格，则代表并列关系，如 div#container .wrapper p.text 代表先选择 id为 container的 div 节点，然后选中其内部的 class 为 wrapper 的节点，再进一步选中其内部的 class 为 text 的p节点。这就是 CSS 选择器，其筛选功能还是非常强大的。

另外，CSS 选择器还有一些其他语法规则,具体如下表所示

表**2-4 CSS**选择器的其他语法规则

| 选择器          | 例 子      | 例子描述                     |
| --------------- | ---------- | ---------------------------- |
| .class          | .intro     | 选择class="intro"的所有节点  |
| #id             | #firstname | 选择id="firstname"的所有节点 |
| *               | *          | 选择所有节点                 |
| element         | P          | 选择所有p节点                |
| element,element | div,p      | 选择所有div节点和所有p节点   |

| element element      | div p              | 选择div节点内部的所有p节点                |
| -------------------- | ------------------ | ----------------------------------------- |
| element>element      | div>p              | 选择父节点为div节点的所有p节点            |
| element+element      | div+p              | 选择紧接在div节点之后的所有p节点          |
| [attribute]          | [target]           | 选择带有target属性的所有节点              |
| [attribute=value]    | [target=blank]     | 选择target="blank"的所有节点              |
| [attribute~=value]   | [title~=flower]    | 选择title属性包含单词flower的所有节点     |
| :link                | a:link             | 选择所有未被访问的链接                    |
| :visited             | a:visited          | 选择所有已被访问的链接                    |
| :active              | a: active          | 选择活动链接                              |
| :hover               | a:hover            | 选择鼠标指针位于其上的链接                |
| :focus               | input:focus        | 选择获得焦点的i叩ut节点                   |
| :first-letter        | p:first-letter     | 选择每个p节点的首字母                     |
| :first-line          | p:first-line       | 选择每个p节点的首行                       |
| :first-child         | p:first-child      | 选择属于父节点的第一个子节点的所有p节点   |
| :before              | p:before           | 在每个p节点的内容之前插入内容             |
| :after               | p:after            | 在每个p节点的内容之后插入内容             |
| :lang(language)      | P：lang            | 选择带有以it开头的lang属性值的所有p节点   |
| elementl~element2    | p~ul               | 选择前面有p节点的所有ul节点               |
| [attributeA=value]   | a[srcA="https"]    | 选择其src属性值以https开头的所有a节点     |
| [attribute$=value]   | a[src$=".pdf"]     | 选择其src属性以,pdf结尾的所有a节点        |
| [attribute*=value]   | a[src*="abc"]      | 选择其src属性中包含abc子串的所有a节点     |
| :first-of-type       | p:first-of-type    | 选择属于其父节点的首个p节点的所有p节点    |
| :last-of-type        | p:last-of-type     | 选择属于其父节点的最后p节点的所有p节点    |
| :only-o仁type        | p:only-of-type     | 选择属于其父节点唯一的p节点的所有p节点    |
| :only-child          | p:only-child       | 选择属于其父节点的唯一子节点的所有p节点   |
| :nth-child(n)        | p:nth-child        | 选择属于其父节点的第二个子节点的所有p节点 |
| :nth-last-child(n)   | p:nth-last-child   | 同上，从最后一个子节点开始计数            |
| :nth-of-type(n)      | p:nth-of-type      | 选择属于其父节点第二个p节点的所有p节点    |
| :nth-last-of-type(n) | p:nth-last-of-type | 同上，但是从最后一个子节点开始计数        |
| :last-child          | p:last-child       | 选择属于其父节点最后一个子节点的所有p节点 |
| :root                | :root              | 选择文档的根节点                          |
| :empty               | p:empty            | 选择没有子节点的所有p节点（包括文本节点） |
| :target              | #news:target       | 选择当前活动的#news节点                   |
| :enabled             | input:enabled      | 选择每个启用的i叩ut节点                   |
| :disabled            | input:disabled     | 选择每个禁用的input节点                   |
| :checked             | input:checked      | 选择每个被选中的i叩ut节点                 |
| :not(selector)       | :not               | 选择非p节点的所有节点                     |
| ::selection          | ::selection        | 选择被用户选取的节点部分                  |

 另外，还有一种比较常用的选择器是XPath,这种选择方式后面会详细介绍。

本节介绍了网页的基本结构和节点间的关系，了解了这些内容，我们才有更加清晰的思路去解析 和提取网页内容。

### 2.3爬虫的基本原理

我们可以把互联网比作一张大网，而爬虫（即网络爬虫）便是在网上爬行的蜘蛛。把网的节点比 作一个个网页，爬虫爬到这就相当于访问了该页面，获取了其信息。可以把节点间的连线比作网页与 网页之间的链接关系，这样蜘蛛通过一个节点后，可以顺着节点连线继续爬行到达下一个节点，即通 过一个网页继续获取后续的网页，这样整个网的节点便可以被蜘蛛全部爬行到，网站的数据就可以被 抓取下来了。

#### 2.3.1爬虫概述

简单来说，爬虫就是获取网页并提取和保存信息的自动化程序，下面概要介绍一下。

1. 获取网页

爬虫首先要做的工作就是获取网页，这里就是获取网页的源代码。源代码里包含了网页的部分有 用信息，所以只要把源代码获取下来，就可以从中提取想要的信息了。

前面讲了请求和响应的概念，向网站的服务器发送一个请求，返回的响应体便是网页源代码。所 以，最关键的部分就是构造一个请求并发送给服务器，然后接收到响应并将其解析出来，那么这个流 程怎样实现呢？总不能手工去截取网页源码吧？

不用担心，Python提供了许多库来帮助我们实现这个操作，如urllib、requests等。我们可以用这 些库来帮助我们实现HTTP请求操作，请求和响应都可以用类库提供的数据结构来表示，得到响应之 后只需要解析数据结构中的Body部分即可，即得到网页的源代码，这样我们可以用程序来实现获取 网页的过程了。

2. 提取信息

获取网页源代码后，接下来就是分析网页源代码，从中提取我们想要的数据。首先，最通用的方 法便是釆用正则表达式提取，这是一个万能的方法，但是在构造正则表达式时比较复杂且容易出错。

另外，由于网页的结构有一定的规则，所以还有一些根据网页节点属性、CSS选择器或XPath来 提取网页信息的库，如Beautiful Soup, pyquery A Ixml等。使用这些库，我们可以高效快速地从中提 取网页信息，如节点的属性、文本值等。

提取信息是爬虫非常重要的部分，它可以使杂乱的数据变得条理清晰，以便我们后续处理和分析 数据。

3. 保存数据

提取信息后，我们一般会将提取到的数据保存到某处以便后续使用。这里保存形式有多种多样， 如可以简单保存为TXT文本或JSON文本，也可以保存到数据库，如MySQL和MongoDB等，也可保存至远程服务器，如借助SFTP进行操作等。

**4**.自动化程序

说到自动化程序，意思是说爬虫可以代替人来完成这些操作。首先，我们手工当然可以提取这些信息，

但是当量特别大或者想快速获取大量数据的话，肯定还是要借助程序。爬虫就是代替我们来完 成这份爬取工作的自动化程序，它可以在抓取过程中进行各种异常处理、错误重试等操作，确保爬取 持续高效地运行。

#### 2.3.2能抓怎样的数据

在网页中我们能看到各种各样的信息，最常见的便是常规网页，它们对应着HTML代码，而最常 抓取的便是HTML源代码。

另外，可能有些网页返回的不是HTML代码，而是一个JSON字符串（其中API接口大多采用这 样的式),这种格式的数据方便传输和解析，它们同样可以抓取，而且数据提取更加方便。

此外，我们还可以看到各种二进制数据，如图片、视频和音频等。利用爬虫，我们可以将这些二 进制数据抓取下来，然后保存成对应的文件名。

另外，还可以看到各种扩展名的文件，如CSS、JavaScript和配置文件等，这些其实也是最普通的文件，只要在浏览器里面可以访问到，就可以将其抓取下来。

上述内容其实都对应各自的URL,是基于HTTP或HTTPS协议的，只要是这种数据，爬虫都可以抓取。

#### 2.3.3 JavaScript 渲染页面

有时候，我们在用urllib或requests抓取网页时，得到的源代码实际和浏览器中看到的不一样。

这是一个非常常见的问题。现在网页越来越多地采用Ajax、前端模块化工具来构建，整个网页可 能都是由JavaScript渲染出来的，也就是说原始的HTML代码就是一个空壳，例如：

```
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>This is a Demo</title>

</head>

<body>

<div id="container">

</div>

</body>

<script src="app.js"x/script>

</html>
```

body节点里面只有一个id为container的节点，但是需要注意在body节点后引入了 app.js,它便 负责整个网站的渲染。

在浏览器中打开这个页面时，首先会加载这个HTML内容，接着浏览器会发现其中引入了一个 app.js文件，然后便会接着去请求这个文件，获取到该文件后，便会执行其中的JavaScript代码，而JavaScript则会改变HTML中的节点，向其添加内容，最后得到完整的页面。

但是在用urllib或requests等库请求当前页面时，我们得到的只是这个HTML代码，它不会帮助 我们去继续加载这个JavaScript文件，这样也就看不到浏览器中的内容了。这也解释了为什么有时我们得到的源代码和浏览器中看到的不一样。因此，使用基本HTTP请求库得到的源代码可能跟浏览器中的页面源代码不太一样。对于这样的情况，我们可以分析其后台Ajax接口，也可使用Selenium, Splash这样的库来实现模拟JavaScript渲染。后面，我们会详细介绍如何釆集JavaScript渲染的网页。

本节介绍了爬虫的一些基本原理，这可以帮助我们在后面编写爬虫时更加得心应手。

### 2.4 会话和 Cookies

在浏览网站的过程中，我们经常会遇到需要登录的情况，有些页面只有登录之后才可以访问，而 且登录之后可以连续访问很多次网站，但是有时候过一段时间就需要重新登录。还有一些网站，在打 开浏览器时就自动登录了，而且很长时间都不会失效，这种情况又是为什么？其实这里面涉及会话 (Session )和Cookies的相关知识，本节就来揭开它们的神秘面纱。

#### 2.4.1静态网页和动态网页

在开始之前，我们需要先了解一下静态网页和动态网页的概念。这里还是前面的示例代码，内容如下:

```
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>This is a Demo</title>

</head>

<body>

<div id="container">

<div class="wrapper">

<h2 class="title">Hello World</h2>

<p class="text">Hello, this is a paragraph.</p>

</div>

</div>

</body>

</html>
```

这是最基本的HTML代码，我们将其保存为一个.html文件，然后把它放在某台具有固定公网IP 的主机上主机上装上Apache或Nginx等服务器，这样这台主机就可以作为服务器了，其他人便可 以通过访问服务器看到这个页面，这就搭建了一个最简单的网站。

这种网页的内容是HTML代码编写的，文字、图片等内容均通过写好的HTML代码来指定，这 种页面叫作静态网页。它加载速度快，编写简单，但是存在很大的缺陷，如可维护性差，不能根据 URL灵活多变地显示内容等。例如，我们想要给这个网页的URL传入一个name参数，让其在网页中 显示出来，是无法做到的。

因此，动态网页应运而生，它可以动态解析URL中参数的变化，关联数据库并动态呈现不同的 页面内容，非常灵活多变。我们现在遇到的大多数网站都是动态网站，它们不再是一个简单的HTML, 而是可能由JSP、PHP、Python等语言编写的，其功能比静态网页强大和丰富太多了。

此外，动态网站还可以实现用户登录和注册的功能。再回到开头提到的问题，很多页面是需要登 录之后才可以查看的。按照一般的逻辑来说，输入用户名和密码登录之后，肯定是拿到了一种类似凭 证的东西，有了它，我们才能保持登录状态，才能访问登录之后才能看到的页面。

那么，这种神秘的凭证到底是什么呢？其实它就是会话和Cookies共同产生的结果，下面我们来 一探究竟。

#### 2.4.2无状态HTTP

在了解会话和Cookies之前，我们还需要了解HTTP的一个特点，叫作无状态。

HTTP的无状态是指HTTP协议对事务处理是没有记忆能力的，也就是说服务器不知道客户端是 什么状态。当我们向服务器发送请求后，服务器解析此请求，然后返回对应的响应，服务器负责完成 这个过程，而且这个过程是完全独立的，服务器不会记录前后状态的变化，也就是缺少状态记录。这 意味着如果后续需要处理前面的信息，则必须重传，这导致需要额外传递一些前面的重复请求，才能 获取后续响应，然而这种效果显然不是我们想要的。为了保持前后状态，我们肯定不能将前面的请求 全部重传一次，这太浪费资源了，对于这种需要用户登录的页面来说，更是棘手。

这时两个用于保持HTTP连接状态的技术就出现了，它们分别是会话和Cookieso会话在服务端, 也就是网站的服务器，用来保存用户的会话信息；Cookies在客户端，也可以理解为浏览器端，有了 Cookies,浏览器在下次访问网页时会自动附带上它发送给服务器，服务器通过识别Cookies并鉴定出 是哪个用户，然后再判断用户是否是登录状态，然后返回对应的响应。

我们可以理解为Cookies里面保存了登录的凭证，有了它，只需要在下次请求携带Cookies发送 请求而不必重新输入用户名、密码等信息重新登录了。

因此在爬虫中，有时候处理需要登录才能访问的页面时，我们一般会直接将登录成功后获取的 Cookies放在请求头里面直接请求，而不必重新模拟登录。

好了，了解会话和Cookies的概念之后，我们在来详细剖析它们的原理。

1. 会话

会话，其本来的含义是指有始有终的一系列动作/消息。比如，打电话时，从拿起电话拨号到挂断 电话这中间的一系列过程可以称为一个会话。

而在Web中，会话对象用来存储特定用户会话所需的属性及配置信息。这样，当用户在应用程序 的Web页之间跳转时，存储在会话对象中的变量将不会丢失，而是在整个用户会话中一直存在下去。 当用户请求来自应用程序的Web页时，如果该用户还没有会话，则Web服务器将自动创建一个会话 对象。当会话过期或被放弃后，服务器将终止该会话。

2. Cookies

Cookies指某些网站为了辨别用户身份、进行会话跟踪而存储在用户本地终端上的数据。

**・**会话维持

那么，我们怎样利用Cookies保持状态呢？当客户端第一次请求服务器时，服务器会返回一个请 求头中带有Set-Cookie字段的响应给客户端，用来标记是哪一个用户，客户端浏览器会把Cookies保 存起来。当浏览器下一次再请求该网站时，浏览器会把此Cookies放到请求头一起提交给服务器， Cookies携带了会话ID信息，服务器检查该Cookies即可找到对应的会话是什么，然后再判断会话来 以此来辨认用户状态。

在成功登录某个网站时，服务器会告诉客户端设置哪些Cookies信息，在后续访问页面时客户端 会把Cookies发送给服务器，服务器再找到对应的会话加以判断。如果会话中的某些设置登录状态的 变量是有效的，那就证明用户处于登录状态，此时返回登录之后才可以査看的网页内容，浏览器再进 行解析便可以看到了。

反之，如果传给服务器的Cookies是无效的，或者会话已经过期了，我们将不能继续访问页面， 此时可能会收到错误的响应或者跳转到登录页面重新登录。

所以，Cookies和会话需要配合，一个处于客户端，一个处于服务端，二者共同协作，就实现了 登录会话控制。

**・**属性结构

接下来，我们来看看Cookies都有哪些内容。这里以知乎为例，在浏览器开发者工具中打开 Application选项卡，然后在左侧会有一个Storage部分，最后一项即为Cookies,将其点开，如图2-13 所示，这些就是Cookieso

![image-20210428151018757](C:\Users\javac\Desktop\class\image-20210428151018757.png)

可以看到，这里有很多条目，其中每个条目可以称为Cookie。它有如下几个属性。

- Name：该Cookie的名称。一旦创建，该名称便不可更改。

- Value：该Cookie的值。如果值为Unicode字符，需要为字符编码。如果值为二进制数据，则 需要使用BASE64编码。

- Domain：可以访问该Cookie的域名。例如，如果设置为.zhihu.com,则所有以zhihu.com结尾 的域名都可以访问该Cookieo

- Max Age：该Cookie失效的时间，单位为秒，也常和Expires一起使用，通过它可以计算出其 有效时间。Max Age如果为正数，则该Cookie在Max Age秒之后失效。如果为负数，则关闭 浏览器时Cookie即失效，浏览器也不会以任何形式保存该Cookie0

- Path:该Cookie的使用路径。如果设置为/path/,则只有路径为/path/的页面可以访问该 Cookieo如果设置为/,则本域名下的所有页面都可以访问该Cookie0

-  Size字段：此Cookie的大小。

- HTTP字段：Cookie的httponly属性。若此属性为true,则只有在HTTP头中会带有此 Cookie的信息，而不能通过document.cookie来访问此Cookieo

- Secure：该Cookie是否仅被使用安全协议传输。安全协议有HTTPS和SSL等，在网络上传 输数据之前先将数据加密。默认为false。

  **会话Cookie和持久Cookie**

  从表面意思来说，会话Cookie就是把Cookie放在浏览器内存里，浏览器在关闭之后该Cookie即失效；持久Cookie则会保存到客户端的硬盘中，下次还可以继续使用，用于长久保持用户登录状态。

  其实严格来说，没有会话Cookie和持久Cookie之分，只是由Cookie的Max Age或Expires字段 决定了过期的时间。

  因此，一些持久化登录的网站其实就是把Cookie的有效时间和会话有效期设置得比较长，下次我 们再访问页面时仍然携带之前的Cookie,就可以直接保持登录状态。

  #### 2.4.3常见误区

  在谈论会话机制的时候，常常听到这样一种误解一一“只要关闭浏览器，会话就消失了”。可以 想象一下会员卡的例子，除非顾客主动对店家提出销卡，否则店家绝对不会轻易删除顾客的资料。对 会话来说，也是一样，除非程序通知服务器删除一个会话，否则服务器会一直保留。比如，程序一般 都是在我们做注销操作时才去删除会话。

  但是当我们关闭浏览器时，浏览器不会主动在关闭之前通知服务器它将要关闭，所以服务器根本 不会有机会知道浏览器已经关闭。之所以会有这种错觉，是因为大部分会话机制都使用会话Cookie 来保存会话ID信息，而关闭浏览器后Cookies就消失了，再次连接服务器时，也就无法找到原来的会 话了。如果服务器设置的Cookies保存到硬盘上，或者使用某种手段改写浏览器发出的HTTP请求头, 把原来的Cookies发送给服务器，则再次打开浏览器，仍然能够找到原来的会话ID,依旧还是可以保 持登录状态的。

  而且恰恰是由于关闭浏览器不会导致会话被删除，这就需要服务器为会话设置一个失效时间，当 距离客户端上一次使用会话的时间超过这个失效时间时，服务器就可以认为客户端已经停止了活动， 才会把会话删除以节省存储空间。

### 2.5代理的基本原理

我们在做爬虫的过程中经常会遇到这样的情况，最初爬虫正常运行，正常抓取数据，一切看起来 都是那么美好，然而一杯茶的功夫可能就会出现错误，比如403 Forbidden,这时候打开网页一看，可 能会看到“您的IP访问频率太高”这样的提示。出现这种现象的原因是网站釆取了一些反爬虫措施。 比如，服务器会检测某个IP在单位时间内的请求次数，如果超过了这个阈值，就会直接拒绝服务，返 回一些错误信息，这种情况可以称为封IP。

既然服务器检测的是某个IP单位时间的请求次数，那么借助某种方式来伪装我们的1P,让服务 器识别不出是由我们本机发起的请求，不就可以成功防止封IP 了吗？

一种有效的方式就是使用代理，后面会详细说明代理的用法。在这之前，需要先了解下代理的基 本原理，它是怎样实现IP伪装的呢？

#### 2.5.1基本原理

代理实际上指的就是代理服务器，英文叫作proxy server,它的功能是代理网络用户去取得网络信 息。形象地说，它是网络信息的中转站。在我们正常请求一个网站时，是发送了请求给Web服务器， Web服务器把响应传回给我们。如果设置了代理服务器，实际上就是在本机和服务器之间搭建了一个 桥，此时本机不是直接向Web服务器发起请求，而是向代理服务器发出请求，请求会发送给代理服务 器，然后由代理服务器再发送给Web服务器，接着由代理服务器再把Web服务器返回的响应转发给 本机。这样我们同样可以正常访问网页，但这个过程中Web服务器识别出的真实IP就不再是我们本 机的IP 了，就成功实现了 IP伪装，这就是代理的基本原理。

#### 2.5.2代理的作用

那么，代理有什么作用呢？我们可以简单列举如下。

突破自身ip访问限制，访问一些平时不能访问的站点。

访问一些单位或团体内部资源：比如使用教育网内地址段免费代理服务器，就可以用于对教 育网开放的各类FTP下载上传，以及各类资料查询共享等服务。

提高访问速度：通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同 时也将其保存到缓冲区中，当其他用户再访问相同的信息时，贝憤接由缓冲区中取出信息， 传给用户，以提高访问速度。

隐藏真实IP：上网者也可以通过这种方法隐藏自己的IP,免受攻击。对于爬虫来说，我们用 代理就是为了隐藏自身IP,防止自身的IP被封锁。

#### 2.5.3爬虫代理

对于爬虫来说，由于爬虫爬取速度过快，在爬取过程中可能遇到同一个ip访问过于频繁的问题， 此时网站就会让我们输入验证码登录或者直接封锁ip,这样会给爬取带来极大的不便。

使用代理隐藏真实的ip,让服务器误以为是代理服务器在请求自己。这样在爬取过程中通过不断 更换代理，就不会被封锁，可以达到很好的爬取效果。

#### 2.5.4代理分类

代理分类时，既可以根据协议区分，也可以根据其匿名程度区分。

1. 根据协议区分

根据代理的协议，代理可以分为如下类别。

a.FTP代理服务器：主要用于访问FTP服务器，一般有上传、下载以及缓存功能，端口一般为 21、2121 等。

b.HTTP代理服务器：主要用于访问网页，一般有内容过滤和缓存功能，端口一般为80、 8080、3128 等。

c.SSL/TLS代理：主要用于访问加密网站，一般有SSL或TLS加密功能（最高支持128位加密 强度），端口一般为443。

d.RTSP代理：主要用于访问Real流媒体服务器，一般有缓存功能，端口一般为554。

e.Telnet代理：主要用于telnet远程控制（黑客入侵计算机时常用于隐藏身份），端口一般为23

f. POP3/SMTPRS：主要用于POP3/SMTP方式收发邮件，一般有缓存功能,端口一般为110/25。

g.SOCKS代理：只是单纯传递数据包，不关心具体协议和用法，所以速度快很多，一般有缓存功能，端口一般为1080o SOCKS代理协议又分为SOCKS4和SOCKS5,前者只支持TCP, 而后者支持TCP和UDP,还支持各种身份验证机制、服务器端域名解析等。简单来说， SOCKS4能做到的SOCKS5都可以做到，但SOCKS5能做到的SOCKS4不一定能做到。

2. 根据匿名程度区分

根据代理的匿名程度，代理可以分为如下类别。

a.高度匿名代理：会将数据包原封不动地转发，在服务端看来就好像真的是一个普通客户端在 访问，而记录的IP是代理服务器的IPo

b.普通匿名代理：会在数据包上做一些改动，服务端上有可能发现这是个代理服务器，也有一定几 率追查到客户端的真实IPo代瑯艮务器通常会加入的HTTP头有HTTP_VIA和HTTP_X_FORWARDED_FOR。

c.透明代理：不但改动了数据包，还会告诉服务器客户端的真实IPo这种代理窿了能用缓存技 术提高浏览速度，能用内容过滤提高安全性之外，并无其他显著作用，最常见的例子是内网 中的硬件防火墙。

d.间谍代理：指组织或个人创建的用于记录用户传输的数据，然后进行研究、监控等目的的代 理服务器。

#### 2.5.5常见代理设置

- 使用网上的免费代理：最好使用高匿代理，另外可用的代理不多，需要在使用前筛选一下可 用代理，也可以进一步维护一个代理池。
- 使用付费代理服务：互联网上存在许多代理商，可以付费使用，质量比免费代理好很多。
-  ADSL拨号：拨一次号换一次IP,稳定性高，也是一种比较有效的解决方案。

在后文我们会详细介绍这几种代理的使用方式。

## 三.基本库的使用

### 概述:

  学习爬虫，最初的操作便是模拟浏览器向服务器发出请求，那么我们需要从哪个地方做起呢？请求需要我们自己来构造吗？需要关心请求这个数据结构的实现吗？需要了解HTTP、TCP、IP层的网 络传输通信吗？需要知道服务器的响应和应答原理吗？

可能你不知道无从下手，不过不用担心，Python的强大之处就是提供了功能齐全的类库来帮助我 们完成这些请求。最基础的HTTP库有urllib、httplib2、requests、treq等。

拿urllib这个库来说，有了它，我们只需要关心请求的链接是什么，需要传的参数是什么，以及 如何设置可选的请求头就好了，不用深入到底层去了解它到底是怎样传输和通信的。有了它，两行代 码就可以完成一个请求和响应的处理过程，得到网页内容，是不是感觉方便极了？

接下来，就让我们从最基础的部分开始了解这些库的使用方法吧。

### 3.1urllib库

   在Python 2中，有urllib和urllib2两个库来实现请求的发送。而在Python 3中，已经不存在urllib2 这个库了，统一为 urllib,其官方文档链接为：https://docs.python.Org/3/library/urllib.htmlo

首先，了解一下urllib库，它是Python内置的HTTP请求库，也就是说不需要额外安装即可使用, 它包含如下4个模块。

□ request：它是最基本的HTTP请求模块，可以用来模拟发送请求。就像在浏览器里输入网址 然后回车一样，只需要给库方法传入URL以及额外的参数，就可以模拟实现这个过程了。

□ error：异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操 作以保证程序不会意外终止。

□  parse： 一个工具模块，提供了许多URL处理方法，比如拆分、解析、合并等。

□ robotparser：主要是用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些网站不 可以爬，它其实用得比较少。

这里重点讲解一下前3个模块。

#### 3.1.1发送请求

使用urllib的request模块，我们可以方便地实现请求的发送并得到响应。本节就来看下它的具体用法。

##### 1.urlopen()

urllib.request模块提供了最基本的构造HTTP请求的方法，利用它可以模拟浏览器的一个请求 发起过程，同时它还带有处理授权验证(authenticaton )、重定向(redirection)、浏览器Cookies以及其 他内容。

下面我们来看一下它的强大之处。这里以Python官网为例，我们来把这个网页抓下来：

```
import urllib.request

response = urllib.request.urlopen('https://www.python.org')

 print(response.read().decode('utf-8'))
```

运行结果如下图所示![python](C:\Users\javac\Desktop\class\python.png)

这里我们只用了两行代码，便完成了 Python官网的抓取，输出了网页的源代码。得到源代码之后 呢？我们想要的链接、图片地址、文本信息不就都可以提取出来了吗？

接下来，看看它返回的到底是什么。利用type()方法输出响应的类型：

```python
import urllib.request

response = urllib.request.urlopen('https://www.python.org')

print(type(response))
```

输出结果如下：

```python
<class 'http.client.HTTPResponse'>
```

  可以发现，它是一个HTTPResposne类型的对象，主要包含read。、readinto。、getheader(name) getheaders() fileno()等方法,以及 msg、version, statuss reason, debuglevelclosed 等属性。

  得到这个对象之后，我们把它赋值为response变量，然后就可以调用这些方法和属性，得到返回 结果的一系列信息了。

  例如，调用read()方法可以得到返回的网页内容，调用status属性可以得到返回结果的状态码， 如200代表请求成功，404代表网页未找到等。

  下面再通过一个实例来看看：

```python
import urllib.request

response = urllib.request.urlopen('https://www.python.org')

print(response.status)

print(response.getheaders())

print(response.getheader('Server'))
```

运行结果如下：

200

[('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'), ('X-Frame-Options', 'SAMEORIGIN'),

('X-Clacks-Overhead', 'GNU Terry Pratchett'), ('Content-Length', '47397'), ('Accept-Ranges', 'bytes'), ('Date', 'Mon, 01 Aug 2016 09：57：31 GMT'), ('Via', '1.1 varnish'), ('Age', '2473'), ('Connection', 'close'), ('X-Served-By', 'cache-lcyll25-LCY'), ('X-Cache', 'HIT'), ('X-Cache-Hits', '23'), ('Vary', 'Cookie'), ('Strict-Transport-Security', 'max-age=63O72OOO; includeSubDomains')]

nginx

  可见，前两个输出分别输出了响应的状态码和响应的头信息，最后一个输出通过调用getheader() 方法并传递一个参数Server获取了响应头中的Server值，结果是nginx,意思是服务器是用Nginx 搭建的。

利用最基本的urlopen。方法，可以完成最基本的简单网页的GET请求抓取。

如果想给链接传递一些参数，该怎么实现呢？首先看一下urlopen。函数的API：

urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

可以发现，除了第一个参数可以传递URL之外，我们还可以传递其他内容，比如data (附加数 据)、timeout (超时时间)等。

下面我们详细说明下这几个参数的用法。

**1.data参数**

data参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即bytes类型， 则需要通过bytes()方法转化。另外，如果传递了这个参数，则它的请求方式就不再是GET方式，而 是POST方式。

下面用实例来看一下：

```python
import urllib.parse

import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8') 

response = urllib.request.urlopen('http://httpbin.org/post', data=data) 

print(response.read())
```

  这里我们传递了一个参数word,值是hello0它需要被转码成bytes (字节流)类型。其中转字 节流采用了 bytes。方法，该方法的第一个参数需要是str (字符串)类型，需要用urllib.parse模 块里的urlencode()方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为utf8。

  这里请求的站点是httpbin.org,它可以提供HTTP请求测试。本次我们请求的URL为http://httpbin. org/post,这个链接可以用来测试POST请求，它可以输出请求的一些信息，其中包含我们传递的data 参数。

运行结果如下：

```html
(

"args": {},

"data":

"files": {},

"form": {

"word": "hello"

},

"headers": {

"Accept-Encoding": "identity",

"Content-Length": "10",

"Content-Type": "application/x-www-form-urlencoded",

"Host": "httpbin.org", "User-Agent": "Python-urllib/3.5"

},

"json": null,

"origin": "123.124.23.253",

"url": "http://httpbin.org/post"

}
```

我们传递的参数出现在了 form字段中，这表明是模拟了表单提交的方式，以POST方式传输数据。

**timeout 参数**

timeout参数用于设置超时时间，单位为秒，意思就是如果请求超出了设置的这个时间，还没有得 到响应，就会抛出异常。如果不指定该参数，就会使用全局默认时间。它支持HTTP、HTTPS, FTP 请求。

下面用实例来看一下：

```python
import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)

print(response.read())
```

运行结果如下：

During handling of the above exception, another exception occurred:

Traceback (most recent call last): File "/var/py/python/urllibtest.py", line 4, in <module> response = urllib.request.urlopen('http://httpbin.org/get1, timeout=l)

urllib.error.URLError: <urlopen error timed out>

  这里我们设置超时时间是1秒。程序1秒过后，服务器依然没有响应，于是抛出了 URLError异常。 该异常属于urllib.error模块，错误原因是超时。

  因此，可以通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过它的抓取。这可以 利用try except语句来实现，相关代码如下：

```python
import socket

import urllib.request

import urllib.error

try:

	response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)

except urllib.error.URLError as e:

	if isinstance(e.reason, socket.timeout):

		print('TIME OUT')
```

这里我们请求了 http://httpbin.org/get测试链接，设置超时时间是0.1秒，然后捕获了 URLError异 常，接着判断异常是socket.timeout类型(意思就是超时异常)，从而得出它确实是因为超时而报错， 打印输出了 TIME OUTo

运行结果如下：

TIME OUT

按照常理来说，0.1秒内基本不可能得到服务器响应，因此输出了 TIME OUT的提示。

通过设置timeout这个参数来实现超时处理，有时还是很有用的。

**其他参数**

  除了 data参数和timeout参数外，还有context参数，它必须是ssl.SSLContext类型，用来指定 SSL设置。

此外，cafile和capath这两个参数分别指定CA证书和它的路径，这个在请求HTTPS链接时会 有用。

cadefault参数现在已经弃用了，其默认值为False。

  前面讲解了 urlopen()方法的用法，通过这个最基本的方法，我们可以完成简单的请求和网页抓取。若需更加详细的信息，可以参见官方文档：https://docs.python.Org/3/library/urllib.request.html.

##### 2.Request

  我们知道利用urloPen()方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建一 个完整的请求。如果请求中需要加入Headers等信息，就可以利用更强大的Request类来构建。

首先，我们用实例来感受一下Request的用法：

```python
import urllib.request

request = urllib.request.Request('https://python.org')

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
```

  可以发现，我们依然是用urlopen。方法来发送这个请求，只不过这次该方法的参数不再是URL, 而是一个Request类型的对象。通过构造这个数据结构，一方面我们可以将请求独立成一个对象，另 一方面可更加丰富和灵活地配置参数。

下面我们看一下Request可以通过怎样的参数来构造，它的构造方法如下：

class urllib.request.Request(url, data=None, headers"}, origin_req_host=None, unverifiable=False, method=None) 

1. 第一个参数url用于请求URL,这是必传参数，其他都是可选参数。
2. 第二个参数data如果要传，必须传bytes (字节流)类型的。如果它是字典，可以先用 urllib.parse 模块里的 urlencode()编码。
3. 第三个参数headers是一个字典，它就是请求头，我们可以在构造请求时通过headers参数直 接构造，也可以通过调用请求实例的add_header()方法添加。 添加请求头最常用的用法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是 Python-urllib,我们可以通过修改它来伪装浏览器。比如要伪装火狐浏览器，你可以把它设 置为：Mozilla/5.0 (Xll; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
4. 第四个参数origin_req_host指的是请求方的host名称或者IP地址。
5. 第五个参数unverifiable表示这个请求是否是无法验证的，默认是False,意思就是说用户没 有足够权限来选择接收这个请求的结果。例如，我们请求一个HTML文档中的图片，但是我 们没有自动抓取图像的权限，这时unverifiable的值就是True。
6. 第六个参数method是一个字符串，用来指示请求使用的方法，比如GET. POST和PUT等。

**下面我们传入多个参数构建请求来看一下:**

```python
from urllib import request, parse

url = 'http://httpbin.org/post'

headers = {

'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5； Windows NT)',

'Host': 'httpbin.org'

}

dict ={

'name': 'Germey'

}

data = bytes(parse.urlencode(dict), encoding='utf8')

req = request.Request(url=url, data=data, headers=headers, method='POST')

response = request.urlopen(req)

print(response.read().decode('utf-8'))
```

这里我们通过4个参数构造了一个请求，其中url即请求URL, headers中指定了 User-Agent和 Host,参数data用urlencode()和bytes。方法转成字节流。另外，指定了请求方式为POST。

运行结果如下：

"args": (},

"data":

"files": {},

"form": {

"name": "Germey"

},

"headers": (

"Accept-Encoding": "identity",

"Content-Length": "11",

"Content-Type": "application/x-www-form-urlencoded",

"Host": "httpbin.org",

"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5； Windows NT)"

},

"json": null,

"origin": "219.224.169.11",

"url": "http://httpbin.org/post"}

观察结果可以发现，我们成功设置了 data, headers和method。

另外,headers也可以用add_header()方法来添加：

req = request.Request(url=url, data=data, method='POST')

req.add_header('User-Agent1, 'Mozilla/4.0 (compatible; MSIE 5.5； Windows NT)')

如此一来，我们就可以更加方便地构造请求，实现请求的发送啦。

##### 3.高级用法

  在上面的过程中，我们虽然可以构造请求，但是对于一些更高级的操作(比如Cookies处理、代理设置等)，我们该怎么办呢？

  接下来，就需要更强大的工具Handler登场了.*简而言之，我们可以把它理解为各种处理器，有 专门处理登录验证的，有处理Cookies的，有处理代理设置的。利用它们，我们几乎可以做到HTTP 请求中所有的事情。

首先，介绍一下urllib.request模块里的BaseHandler类，它是所有其他Handler的父类，它提供了最基本的方法，例如 default_open()、protocol_request()等。

接下来，就有各种Handler子类继承这个BaseHandler类，举例如下。

□  HTTPDefaultErrorHandler：用于处理HTTP响应错误，错误都会抛出HTTPError类型的异常。

□  HTTPRedirectHandler:用于处理重定向。

□  HTTPCookieProcessor:用于处理 Cookieso

□  ProxyHandler:用于设置代理，默认代理为空。

□  HTTPPasswordMgr：用于管理密码，它维护了用户名和密码的表。

□ HTTPBasicAuthHandler：用于管理认证，如果一个链接打开时需要认证，那么可以用它来解 决认证问题。

另外，还有其他的Handler类，这里就不一一列举了，详情可以参考官方文档：https://docs.python. org/3/library/urllib.request.html#urllib.request.BaseHandlero

关于怎么使用它们，现在先不用着急，后面会有实例演示。

另一个比较重要的类就是OpenerDirector,我们可以称为Opener。我们之前用过urlopen()这个 方法，实际上它就是urllib为我们提供的一个Openero

那么，为什么要引入Opener呢？因为需要实现更高级的功能。之前使用的Request和urlopen。 相当于类库为你封装好了极其常用的请求方法，利用它们可以完成基本的请求，但是现在不一样了， 我们需要实现更高级的功能，所以需要深入一层进行配置，使用更底层的实例来完成操作，所以这里 就用到了 0penero

Opener可以使用open()方法，返回的类型和urlopen。如出一辙。那么，它和Handler有什么关 系呢？简而言之，就是利用Handler来构建Opener。

  下面用几个实例来看看它们的用法。

**验证**

有些网站在打开时就会弹出提示框，直接提示你输入用户名和密码，验证成功后才能查看页面, 如下图所示。

![yanzheng](C:\Users\javac\Desktop\class\yanzheng.jpg)

那么，如果要请求这样的页面，该怎么办呢？借助HTTPBasicAuthHandler就可以完成，相关代码 如下：

```python
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
username = 'username'
password = 'password'
url = 'http://localhost:5000/'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
try:
result = opener.open(url)
html = result.read().decode('utf-8')
print(html)
except URLError as e:
print(e.reason)
```

这里首先实例化 HTTPBasicAuthHandler 对象，其参数是 HTTPPasswordMgrWithDefaultRealm 对象,它利用add_password()添加进去用户名和密码，这样就建立了一个处理验证的Handler。

接下来，利用这个Handler并使用build_opener()方法构建一个Opener,这个Opener在发送请求时就相当于已经验证成功了。

接下来，利用Opener的open。方法打开链接，就可以完成验证了。这里获取到的结果就是验证后的页面源码内容。

・代理

在做爬虫的时候，免不了要使用代理，如果要添加代理，可以这样做：

```python
from urllib.error import URLError

from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler((

'http': 'http://127.0.0.1:9743',

'https': 'https://127.0.0.1:9743'

})

opener = build_opener(proxy_handler)

try:

response = opener.open('https://www.baidu.com')

print(response.read().decode('utf-8'))

except URLError as e: print(e.reason)
```

这里我们在本地搭建了一个代理，它运行在9743端口上。

这里使用了 ProxyHandler,其参数是一个字典，键名是协议类型(比如HTTP或者HTTPS等)， 键值是代理链接，可以添加多个代理。

然后，利用这个Handler及build_opener()方法构造一个Opener,之后发送请求即可。

• Cookies

Cookies的处理就需要相关的Handler 了。

我们先用实例来看看怎样将网站的Cookies获取下来，相关代码如下：

```python
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()

handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name+"="+item.value)
```

首先，我们必须声明一个CookieJar对象。接下来，就需要利用HTTPCookieProcessor来构建一个 Handler,最后利用build_opener()方法构建出Opener,执行open。函数即可。

运行结果如下：

> BAIDUID=E3CC40A4DD1E265EBFFFCB1AB365D799:FG=1
> BIDUPSID=E3CC40A4DD1E265E90C9D1520DE2CAD1
> H_PS_PSSID=33818_31254_33848_33676_33607_26350
> PSTM=1620629346
> BDSVRTM=0
> BD_HOME=1

可以看到，这里输出了每条Cookie的名称和值。

不过既然能输出，那可不可以输出成文件格式呢？我们知道Cookies实际上也是以文本形式保存 的。

答案当然是肯定的，这里通过下面的实例来看看:

```python
filename = 'cookies.txt'

cookie = http.cookiejar.MozillaCookieJar(filename) 

handler = urllib.request.HTTPCookieProcessor(cookie) 

opener = urllib.request.build_opener(handler) 
response = opener.open('http://www.baidu.com') 
cookie.save(ignore_discard=True, ignore_expires=True)
```

这时CookieJar就需要换成MozillaCookieJar,它在生成文件时会用到，是CookieJar的子类，可 以用来处理Cookies和文件相关的事件，比如读取和保存Cookies,可以将Cookies保存成Mozilla型 浏览器的Cookies格式。

运行之后，可以发现生成了一个cookies.txt文件，其内容如下:

![cookies](C:\Users\javac\Desktop\class\cookies.png)

另外，LWPCookielar同样可以读取和保存Cookies,但是保存的格式和MozillaCookieJar不一样, 它会保存成libwww-perl(LWP)格式的Cookies文件。

要保存成LWP格式的Cookies文件，可以在声明时就改为:

> ​	cookie = http.cookiejar.LWPCookieJar(filename)

此时生成的效果如下：![cookie](C:\Users\javac\Desktop\class\cookie.png)

由此看来，生成的格式还是有比较大差异的。

那么，生成了 Cookies文件后，怎样从文件中读取并利用呢?

下面我们以LWPCookieJar格式为例来看一下:

```python
cookie = http.cookiejar.LWPCookieJar()

cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)

handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')

print(response.read().decode('utf-8'))
```

可以看到，这里调用load()方法来读取本地的Cookies文件，获取到了 Cookies的内容。不过前 提是我们首先生成了 LWPCookieJar格式的Cookies,并保存成文件，然后读取Cookies之后使用同样 的方法构建Handler和Opener即可完成操作。

运行结果正常的话，会输出百度网页的源代码。

通过上面的方法，我们可以实现绝大多数请求功能的设置了。

这便是urllib库中request模块的基本用法，如果想实现更多的功能，可以参考官方文档的说明： [https://docs.python.org/3/library/urllib.request.html#basehandler-objectSo](https://docs.python.org/3/library/urllib.request.html%23basehandler-objectSo)

#### 3.1.2处理异常

前一节我们了解了请求的发送过程，但是在网络不好的情况下，如果出现了异常，该怎么办呢？ 这时如果不处理这些异常，程序很可能因报错而终止运行，所以异常处理还是十分有必要的。

urllib的error模块定义了由request模块产生的异常。如果出现了问题，request模块便会抛出 error模块中定义的异常。

##### 1.URLError

URLError类来自urllib库的error模块，它继承自OSError类，是error异常模块的基类，由request 模块生的异常都可以通过捕获这个类来处理。

它具有一个属性reason，即返回错误的原因。

下面用一个实例来看一下：

```python
from urllib import request, error

try:                                                .

    response = request.urlopen('https://aa.com/index.htm')

except error.URLError as e:
    print(e.reason)
```

我们打开一个不存在的页面，照理来说应该会报错，但是这时我们捕获了 URLError这个异常，运 行结果如下：

Not Found

程序没有直接报错，而是输出了如上内容，这样通过如上操作，我们就可以避免程序异常终止， 同时异常得到了有效处理。

##### 2.HTTPError

它是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等。它有如下3个属性。

□ code：返回HTTP状态码，比如404表示网页不存在，500表示服务器内部错误等。

□  reason：同父类一样，用于返回错误的原因。

□  headers:返回请求头。

下面我们用几个实例来看看：

```python
from urllib import request,error

try:

    response = request.urlopen('https://aa.com/index.htm')

except error.HTTPError as e:

    print(e.reason, e.code, e.headers, sep='\n')
```

运行结果如下：

![error](C:\Users\javac\Desktop\class\error.png)

依然是同样的网址，这里捕获了 HTTPError异常，输出了 reason、code和headers属性。

因为URLError是HTTPError的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误，所 以上述代码更好的写法如下：

```python
from urllib import request, error

try:

    response = request.urlopen('https//:aa.com/index.htm')

except error.HTTPError as e:

    print(e.reason, e.code, e.headers, sep='\n')

except error.URLError as e:

    print(e.reason)

else:

    print('Request Successfully')
```

  这样就可以做到先捕获HTTPError,获取它的错误状态码、原因、headers等信息。如果不是 HTTPError异常，就会捕获URLError异常，输出错误原因。最后，用else来处理正常的逻辑。这是一 个较好的异常处理写法。

有时候，reason属性返回的不一定是字符串，也可能是一个对象。再看下面的实例：

```python
import socket

import urllib.request

import urllib.error

try:

    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)

except urllib.error.URLError as e:

    print(type(e.reason))

if isinstance(e.reason, socket.timeout):

    print('TIME OUT')
```

这里我们直接设置超时时间来强制抛出timeout异常。

运行结果如下：

```
<class 'socket.timeout'>

TIME OUT
```

可以发现,reason属性的结果是socket, timeout类。所以，这里我们可以用isinstance。方法来 判断它的类型，作出更详细的异常判断。

本节中，我们讲述了 error模块的相关用法，通过合理地捕获异常可以做出更准确的异常判断， 使程序更加稳健。

#### 3.1.3解析链接

前面说过，urllib库里还提供了 parse模块，它定义了处理URL的标准接口，例如实现URL各部 分的抽取、合并以及链接转换。它支持如下协议的URL处理：file. ftps gophers hdl、http、https. imap、 mailto、mms、news、nntp、prosper。、rsync、rtsp、rtspu、sftp、sip、sips、snews、svn、svn+ssh. telnet 和wais。本节中，我们介绍一下该模块中常用的方法来看一下它的便捷之处。

##### 1.urlparse()

该方法可以实现URL的识别和分段，这里先用一个实例来看一下：

```python
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')

print(type(result), result)
```



这里我们利用urlparse()方法进行了一个URL的解析。首先，输岀了解析结果的类型，然后将 结果也输出出来。

运行结果如下：

<class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')

可以看到，返回结果是一个ParseResult类型的对象，它包含6个部分，分另U是scheme、netloc、 path、 params、 query 和 fragment。

观察一下该实例的URL：

http://www.baidu.com/index.html;user?id=5#comment

可以发现，urlparse()方法将其拆分成了 6个部分。大体观察可以发现，解析时有特定的分隔符。 比如，：     //前面的就是scheme,代表协议；第一个/符号前面便是netloc,即域名，后面是path,即访 问路径；分号;前面是params,代表参数；问号?后面是査询条件query, 一般用作GET类型的URL； 井号#后面是锚点，用于直接定位页面内部的下拉位置。

一个标准的URL都会符合这个规则，利用urlParse()方法可以将它拆分开来。

除了这种最基本的解析方式外，urlparse。方法还有其他配置吗？接下来，看一下它的API用法：

```python
urllib.parse.urlparse(urlstring, scheme=' ',allow_fragments=True)
```

可以看到，它有3个参数。

□  **urlstring**：这是必填项，即待解析的URL。

□ **scheme**：它是默认的协议(比如http或https等)。假如这个链接没有带协议信息，会将这个作为默认的协议。我们用实例来看一下：

```python
from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https') 

print(result)
```

运行结果如下：

```
ParseResult(scheme='https', netloc=' ', path='[www.baidu.com/index.html'](http://www.baidu.com/index.html'), params='user', query='id=5', fragment='comment')
```

可以发现，我们提供的URL没有包含最前面的scheme信息，但是通过指定默认的scheme参 数，返回的结果是https

假设我们带上了 scheme：

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')

则结果如下：

ParseResult(scheme='http,, netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')

  可见，scheme参数只有在URL中不包含scheme信息时才生效。如果URL中有scheme信息， 就会返回解析出的scheme.

□ **allow_fragments**：即是否忽略fragment。如果它被设置为False, fragment部分就会被忽略， 它会被解析为path、parameters或者query的一部分，而fragment部分为空。

下面我们用实例来看一下：

```python
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False) 

print(result)
```

运行结果如下：

ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5#comment', fragment：')

假设URL中不包含params和query,我们再通过实例看一下：

```python
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html%23comment', allow_fragments=False)

print(result)
```

运行结果如下：

ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html%23comment', params='', query='', fragment='')

##### 2.unurlparse()

有了 urlparse(),相应地就有了它的对立方法urlunparse()o它接受的参数是一个可迭代对象， 但是它的长度必须是6,否则会抛岀参数数量不足或者过多的问题。先用一个实例看一下：

```python
from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']

print(urlunparse(data))
```

这里参数data用了列表类型。当然，你也可以用其他类型，比如元组或者特定的数据结构。

运行结果如下：

http://www.baidu.com/index.html;user?a=6#comment

这样我们就成功实现了 URL的构造。

##### 3.urlsplit()

这个方法和urlparse()方法非常相似，只不过它不再单独解析params这一部分,只返回5个结果。 上面例子中的params会合并到path中。示例如下：

```python
from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')

 print(result)
```

运行结果如下：

SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')

可以发现，返回结果是SplitResult,它其实也是一个元组类型，既可以用属性获取值，也可以用索引来获取。示例如下：

```python
from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')

 print(result.scheme, result[o])
```

运行结果如下：

http  http

##### 4.urlunspilt()

与urlunparse()类似，它也是将链接各个部分组合成完整链接的方法，传入的参数也是一个可迭代对象，例如列表、元组等，唯一的区别是长度必须为5。示例如下：

```python
from urllib.parse import urlunsplit

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']

 print(urlunsplit(data))
```

运行结果如下：

[http://www.baidu.com/index.html?a=6#comment](http://www.baidu.com/index.html?a=6%23comment)

##### 5.urljoin()

  有了 urlunparse()和urlunsplit()方法，我们可以完成链接的合并，不过前提必须要有特定长度 的对象，链接的每一部分都要清晰分开。

  此外，生成链接还有另一个方法，那就是urljoin()方法。我们可以提供一个base_url (基础链接)作为第一个参数，将新的链接作为第二个参数，该方法会分析base_url的scheme、netloc和path 这3个内容并对新链接缺失的部分进行补充，最后返回结果。

```python
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))

print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))

print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))
```

运行结果如下：

http://www.baidu.com/FAQ.html
https://cuiqingcai.com/FAQ.html
https://cuiqingcai.com/FAQ.html
https://cuiqingcai.com/FAQ.html?question=2
https://cuiqingcai.com/index.php
http://www.baidu.com?category=2#comment
www.baidu.com?category=2#comment
www.baidu.com?category=2

##### 6.urlencode()

这里我们再介绍一个常用的方法——urlencode(),它在构造GET请求参数的时候非常有用，示例如下：

```python
from urllib.parse import urlencode

params = (

'name': 'germey',

'age': 22

}

base_url = 'http://www.baidu.com?'

url = base_url + urlencode(params)

print(url)
```

这里首先声明了一个字典来将参数表示出来，然后调用urlencode（）方法将其序列化为GET请求参数。

运行结果如下：

http://www.baidu.com?name=germey&age=22

可以看到，参数就成功地由字典类型转化为GET请求参数了。

这个方法非常常用。有时为了更加方便地构造参数，我们会事先用字典来表示。要转化为URL 的参数时，只需要调用该方法即可。

##### 7.parse_qs

有了序列化，必然就有反序列化。如果我们有一串GET请求参数，利用parse_qs()方法，就可 以将它转回字典，示例如下：

```python
from urllib.parse import parse_qs

query = 'name=germey&age=22'

print(parse_qs(query))
```

运行结果如下：

('name': ['germey'], 'age': ['22']})

可以看到，这样就成功转回为字典类型了。

##### 8.parse_qsl()

另外，还有一个parse_qsl()方法，它用于将参数转化为元组组成的列表，示例如下：

```python
from urllib.parse import parse_qsl

query = 'name=germey&age=22'

print(parse_qsl(query))
```

运行结果如下：

[('name', 'germey'), ('age', '22')]

  可以看到，运行结果是一个列表，而列表中的每一个元素都是一个元组，元组的第一个内容是参 数名，第二个内容是参数值。

##### 9.quote()

  该方法可以将内容转化为URL编码的格式。URL中带有中文参数时，有时可能会导致乱码的问 题，此时用这个方法可以将中文字符转化为URL编码，示例如下：

```python
from urllib.parse import quote

keyword ='壁纸'

url = 'https://www.baidu.com/s?wd=' + quote(keyword)

print(url)
```

这里我们声明了一个中文的搜索文字，然后用quote()方法对其进行URL编码，最后得到的结果 如下：

https: / /www. baidu. com/s?wd=%E 5%A3%81%E7%BA%B8

##### 10.unquote()

有了 quote()方法，当然还有unquote()方法，它可以进行URL解码，示例如下: 

```python
from urllib.parse import unquote

url = 'https://www.baidu.com/s2wd=%E5%A3%81%E7%BA%B8'

print(unquote(url))
```

这是上面得到的URL编码后的结果，这里利用unquote()方法还原，结果如下：

https://www.baidu. com/s?wd=壁纸

可以看到，利用unquote()方法可以方便地实现解码。

本节中，我们介绍了 parse模块的一些常用URL处理方法。有了这些方法，我们可以方便地实现 URL的解析和构造，建议熟练掌握。

#### 3.1.4分析Robots协议

  利用urllib的robotparser模块，我们可以实现网站Robots协议的分析。本节中，我们来简单了解一下该模块的用法。

##### 1.Robots协议

  Robots协议也称作爬虫协议、机器人协议，它的全名叫作网络爬虫排除标准(Robots Exclusion Protocol),用来告诉爬虫和搜索引擎哪些页面可以抓取，哪些不可以抓取。它通常是一个叫作robots.txt 的文本文件，一般放在网站的根目录下。

当搜索爬虫访问一个站点时，它首先会检查这个站点根目录下是否存在robots.txt文件，如果存在， 搜索爬虫会根据其中定义的爬取范围来爬取。如果没有找到这个文件，搜索爬虫便会访问所有可直接 访问的页面。

下面我们看一个robots.txt的样例：

User-agent: *

Disallow: /

Allow: /public/

  这实现了对所有搜索爬虫只允许爬取public目录的功能，将上述内容保存成robots.txt文件，放在 网站的根目录下，和网站的入口文件（比如index.php、index.html和index.jsp等）放在一起。 上面的User-agent描述了搜索爬虫的名称，这里将其设置为*则代表该协议对任何爬取爬虫有效。

比如，我们可以设置：

User-agent: Baiduspider

  这就代表我们设置的规则对百度爬虫是有效的。如果有多条User-agent记录，则就会有多个爬虫 会受到爬取限制，但至少需要指定一条。

  Disallow指定了不允许抓取的目录，比如上例子中设置为/则代表不允许抓取所有页面。

  Allow —般和Disallow 一起使用，一般不会单独使用，用来排除某些限制。现在我们设置为

  /public/,则表示所有页面不允许抓取，但可以抓取public目录。

下面我们再来看几个例子。禁止所有爬虫访问任何目录的代码如下：

User-agent: *

Disallow: /

允许所有爬虫访问任何目录的代码如下：

User-agent: *

Disallow:

另外，直接把robots.txt文件留空也是可以的。

禁止所有爬虫访问网站某些目录的代码如下：

User-agent: *

Disallow: /private/

Disallow: /tmp/

只允许某一个爬虫访问的代码如下：

User-agent: Webcrawler

Disallow:

User-agent: *

Disallow: /

这些是robots.txt的一些常见写法。

##### 2.爬虫名称

  大家可能会疑惑，爬虫名是哪儿来的？为什么就叫这个名？其实它是有固定名字的了，比如百度的就叫作BaiduSpidero下表列出了一些常见的搜索爬虫的名称及对应的网站。

| 爬虫名称    | 名  称    | 网  站                                        |
| ----------- | --------- | --------------------------------------------- |
| BaiduSpider | 百度      | [www.baidu.com](http://www.baidu.com)         |
| Googlebot   | 谷歌      | [www.google.com](http://www.google.com)       |
| 360Spider   | 360搜索   | [www.so.com](http://www.so.com)               |
| YodaoBot    | 有道      | www.youdao.com                                |
| iaarchiver  | Alexa     | [www.alexa.cn](http://www.alexa.cn)           |
| Scooter     | altavista | [www.altavista.com](http://www.altavista.com) |

##### 3.robotparser

  了解Robots协议之后，我们就可以使用robotparser模块来解析robots.txt To该模块提供了一个类RobotFileParser,它可以根据某网站的robots.txt文件来判断一个爬取爬虫是否有权限来爬取这个 网页。

该类用起来非常简单，只需要在构造方法里传入robots.txt的链接即可。首先看一下它的声明：

urllib.robotparser.RobotFileParser(url=' ')

当然，也可以在声明时不传入，默认为空，最后再使用set_url()方法设置一下也可。

下面列出了这个类常用的几个方法。

□  set_url():用来设置robots.txt文件的链接。如果在创建RobotFileParser对象时传入了链 接，那么就不需要再使用这个方法设置了。

□  read()：读取robots.txt文件并进行分析。注意，这个方法执行一个读取和分析操作，如果不 调用这个方法，接下来的判断都会为False,所以一定记得调用这个方法。这个方法不会返 回任何内容，但是执行了读取操作。

□  parse()：用来解析robots.txt文件，传入的参数是robots.txt某些行的内容，它会按照robots.txt 的语法规则来分析这些内容。

□  can_fetch()：该方法传入两个参数，第一个是User-agent,第二个是要抓取的URL。返回的 内容是该搜索引擎是否可以抓取这个URL,返回结果是True或False。

□  mtime()：返回的是上次抓取和分析robots.txt的时间，这对于长时间分析和抓取的搜索爬虫是 很有必要的，你可能需要定期检查来抓取最新的robots.txto

□  modified()：它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取 和分析robots.txt的时间。

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()

rp.set_url('http://www.jianshu.com/robots.txt')

rp.read()

print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))

print(rp.can_fetch(, "http://www.jianshu.com/search?q=python&page=l&type=collections"))

这里以简书为例，首先创建RobotFileParser对象，然后通过set_url()方法设置了 robots.txt的链 接。当然，不用这个方法的话，可以在声明时直接用如下方法设置：

rp = RobotFileParser('http://www.jianshu.com/robots.txt')

接着利用can_fetch()方法判断了网页是否可以被抓取。

运行结果如下：

False

False

本节介绍了 robotparser模块的基本用法和实例，利用它，我们可以方便地判断哪些页面可以抓取，哪些页面不可以抓取。

### 3.2requests库

上一节中，我们了解了 urllib的基本用法，但是其中确实有不方便的地方，比如处理网页验证和 Cookies时，需要写Opener和Handler来处理。为了更加方便地实现这些操作，就有了更为强大的库 requests,有了它，Cookies、登录验证、代理设置等操作都不是事儿。接下来，让我们领略一下它的强大之处吧。

#### 3.2.1使用requests

##### 1.准备工作

在开始之前请确保安装了requests库，如果没有安装，请打开cmd输入

```python
pip install requests
```

##### 2.实例引入

  urllib库中的urlopen()方法实际上是以GET方式请求网页，而requests中相应的方法就是get() 方法，是不是感觉表达更明确一些？下面通过实例来看一下：

```python
import requests

r = requests.get('https://www.baidu.com/')

print(type(r))

print(r.status_code)

print(type(r.text))

print(r.text)

print(r.cookies)
```

运行结果如下：![baidu](C:\Users\javac\Desktop\class\baidu.png)

这里我们调用get()方法实现与urlopen()相同的操作，得到一个Response对象，然后分别输出 了 Response的类型、状态码、响应体的类型、内容以及Cookies.

通过运行结果可以发现，它的返回类型是requests.models.Response,响应体的类型是字符串str, Cookies 的类型是 RequestsCookieJar0

使用get。方法成功实现一个GET请求，这倒不算什么，更方便之处在于其他的请求类型依然可以用一句话来完成，示例如下：

r = requests.post('http://httpbin.org/post')

r = requests.put('http://httpbin.org/put')

r = requests.delete('http://httpbin.org/delete')

r = requests.head('http://httpbin.org/get')

r = requests.options('http://httpbin.org/get')

这里分别用post。、put()、deleteO等方法实现了 POST、PUT, DELETE等请求。是不是比urllib 简单太多了？

其实这只是冰山一角，更多的还在后面。

##### 3.get请求

HTTP中最常见的请求之一就是GET请求，下面首先来详细了解一下利用requests构建GET请求的方法。

```python
import requests

r = requests.get('http://httpbin.org/get')

print(r.text)
```

运行结果如下：

{

"args"： {),

"headers": {

"Acc叩t": "*/*",

"Accept-Encoding": "gzip, deflate",

"Host": "httpbin.org",

"User-Agent": "python-requests/2.10.0"

},

"origin": "122.4.215.33",

"url": "http://httpbin.org/get"

}

可以发现，我们成功发起了 GET请求，返回结果中包含请求头、URL、IP等信息。

{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.25.1", 
    "X-Amzn-Trace-Id": "Root=1-609a6834-1811955770aa6dac0d63cb2c"
  }, 
  "origin": "113.247.22.65", 
  "url": "http://httpbin.org/get"

那么，对于GET请求，如果要附加额外的信息，一般怎样添加呢？比如现在想添加两个参数， 其中name是germey, age是22。要构造这个请求链接，是不是要直接写成：

r = requests.get('http://httpbin.org/get ?name=germey&age=22')

这样也可以，但是是不是有点不人性化呢？ 一般情况下，这种信息数据会用字典来存储。那么，怎样来构造这个链接呢？

这同样很简单，利用params这个参数就好了，示例如下：

```python
import requests

data = {

'name': 'germey',

'age': 22

}

r = requests.get("http://httpbin.org/get", params=data)

print(r.text)
```

运行结果如下：

{
  "args": {
    "age": "22", 
    "name": "germey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.25.1", 
    "X-Amzn-Trace-Id": "Root=1-609a6890-3f4ff3f83f3b0d225baef496"
  }, 
  "origin": "113.247.22.65", 
  "url": "http://httpbin.org/get?name=germey&age=22"
}

通过运行结果可以判断,请求的链接自动被构造成了：http://httpbin.org/get?age=22&name=germey: 另外，网页的返回类型实际上是str类型，但是它很特殊，是JSON格式的。所以，如果想直接 解析返回结果，得到一个字典格式的话，可以直接调用json()方法。示例如下：

```python
import requests

r = requests.get("http://httpbin.org/get")

print(type(r.text))

print(r.json())

print(type(r.json()))
```

运行结果如下：

<class 'str'>
{'args': {}, 'headers': {'Accept-Encoding': 'gzip, deflate', 'X-Amzn-Trace-Id': 'Root=1-609b73b3-7781037d69af1a6228739bd1', 'Accept': '*/*', 'User-Agent': 'python-requests/2.25.1', 'Host': 'httpbin.org'}, 'url': 'http://httpbin.org/get', 'origin': '113.246.94.40'}
<class 'dict'>

可以发现，调用json()方法，就可以将返回结果是JSON格式的字符串转化为字典。

但需要注意的书，如果返回结果不是JSON格式，便会出现解析错误，抛出json.decoder.JSONDecodeError 异常。

**抓取网页**

上面的请求链接返回的是JSON形式的字符串，那么如果请求普通的网页，则肯定能获得相应的

内容了。下面以shopee页面为例来看一下:

```python
import requests
import re #解析库
import csv
keyword=input('请输入想要爬取的内容')
url='https://shopee.com.my/api/v4/search/search_items?by=relevancy&keyword={}&limit=50&newest=0&order=desc&page_type=search&version=2'
url=url.format(keyword)
all_date={}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'cookie': '_gcl_au=1.1.1445177354.1619177862; _med=refer; SPC_IA=-1; SPC_EC=-; SPC_U=-; REC_T_ID=63f95a3e-a428-11eb-b6b1-b4969197e5a8; REC_T_ID=63fe25d9-a428-11eb-9621-2cea7f4af375; SPC_F=CeY9areYf6SttUDDHwqJMBCVIVHGyw81; language=en; SPC_SI=bfftocsg4.Z2DXFV9ZZBMjC19nvxNLOqtbukUkIrQH; csrftoken=eUij6QSsGbAe7XzXMpMWAS9cLOn5f42p; welcomePkgShown=true; SPC_R_T_ID="X3JLrZbfDKJQ2yfsulSPlXANkpzuJHAbh4Dql5Vrh0a2MM2zfIb5lN1pXlQNrZWBkVqYDZyZ79hUJH5+XNRhKbzYuXx1cEs2k68OVvTaSdQ="; SPC_T_IV="xWDCS1wh6/UJoFj3CvP7QA=="; SPC_R_T_IV="xWDCS1wh6/UJoFj3CvP7QA=="; SPC_T_ID="X3JLrZbfDKJQ2yfsulSPlXANkpzuJHAbh4Dql5Vrh0a2MM2zfIb5lN1pXlQNrZWBkVqYDZyZ79hUJH5+XNRhKbzYuXx1cEs2k68OVvTaSdQ="'
}
names=[]
response=requests.get(url,headers=headers).text
results=re.findall('{\"item_basic\":{(.*?),\"image',response,re.S)
prices=re.findall('normal\",\"price\":(.*?),',response,re.S)


for result in results:
    name=re.findall('\"name\":\"(.*?)\",',result,re.S)
    names.append(name[0])
with open('data.csv','w',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['name','price'])
    for i in range(50):
        writer.writerow([names[i],int(prices[i])/100000])

```

这里我们加入了 headers信息，其中包含了 User-Agent字段信息，也就是浏览器标识信息。如果 不加这个，抓取的数据会错误。

接下来我们用到了最基础的正则表达式来匹配出所有的问题内容。关于正则表达式的相关内容， 我们会在3.3节中详细介绍，这里作为实例来配合讲解。

运行结果如下：

name,price

Hush Puppies Men's Backpack HPG50038BK,107.7

Case Valker Outdoor Nylon Backpack Hiking Bag (40L),36.0

PUMA Base College Women's Bag Basics Backpack,89.0



**抓取二进制数据**

在上面的例子中，我们抓取的是shopee的一个页面，实际上它返回的是一个HTML文档。如果想抓去图片、音频、视频等文件，应该怎么办呢？

图片、音频、视频这些文件本质上都是由二进制码组成的，由于有特定的保存格式和对应的解析方式，我们才可以看到这些形形色色的多媒体。所以，想要抓取它们，就要拿到它们的二进制码。

下面以GitHub的站点图标为例来看一下：

```python
import requests

r = requests.get("https://github.com/favicon.ico")

print(r.text)

print(r.content)
```

这里抓取的内容是站点图标，也就是在浏览器每一个标签上显示的小图标，如图所示

![](C:\Users\javac\Desktop\class\github.png)

这里打印了 Response对象的两个属性，一个是text,另一个是content。

运行结果如图3-4所示，其中前两行是r.text的结果，最后一行是r.content的结果。

8 ♦♦❷ ♦♦♦♦♦♦♦♦♦♦

b*\x00\x00\x01\x00\x02\x00\xl0\xl0\x00\x00\x01\x00 Xx00C\x05\x00\x00&\x00\x00\x00 \x00\x00\x01\x00 \x0

可以注意到，前者出现了乱码，后者结果前带有一个b,这代表是bytes类型的数据。由于图片是二进制数据，所以前者在打印时转化为str类型，也就是图片直接转化为字符串，这理所当然会出现乱码。

接着，我们将刚才提取到的图片保存下来：

```python
import requests

r = requests.get("https://github.com/favicon.ico")

with open('favicon.ico', 'wb') as f:

f.write(r.content)
```

这里用了 open。方法，它的第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可 以向文件里写入二进制数据。

运行结束之后，可以发现在文件夹中出现了名为favicon.ico的图标，如图所示。

![](C:\Users\javac\Desktop\class\github.png)

同样地，音频和视频文件也可以用这种方法获取.

**添加 headers**

与urllib.request 一样，我们也可以通过headers参数来传递头信息。

比如，在上面“shopee”的例子中，如果不传递headers,就不能正常请求,当然，我们可以在headers这个参数中任意添加其他的字段信息。

##### 4.post请求

前面我们了解了最基本的GET请求，另外一种比较常见的请求方式是POSTo使用requests实 现POST请求同样非常简单，示例如下：

```python
import requests

data = ('name': 'germey', 'age': '22'}

r = requests.post("http://httpbin.org/post", data=data)

printer.text)
```

这里还是请求http://httpbin.org/post,该网站可以判断如果请求是POST方式，就把相关请求信息 返回。•

运行结果如下：

{

"args": {},

"data":

"files": {),

"form": (

"age": "22”,

"name": "germey"

},

"headers": (

"Accept": "*/*",

"Accept-Encoding": "gzip, deflate",

"Content-Length": "18",

"Content-Type": "application/x-www-form-urlencoded",

"Host": "httpbin.org",

"User-Agent": "python-requests/2.10.0"

},

"json": null,

"origin": "182.33.248.131",

"url": "http://httpbin.org/post"

}

可以发现，我们成功获得了返回结果，其中form部分就是提交的数据，这就证明POST请求成功发送了。

##### 5.响应

发送请求后，得到的自然就是响应。在上面的实例中，我们使用text和content获取了响应的内 容。此外，还有很多属性和方法可以用来获取其他信息，比如状态码、响应头、Cookies等。示例如下：

```python
import requests
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'

}
r = requests.get('http://www.jianshu.com',headers=headers)

print(type(r.status_code), r.status_code)

print(type(r.headers), r.headers)

print(type(r.cookies), r.cookies)

print(type(r.url), r.url)

print(type(r.history), r.history)
```

这里分别打印输出status_code属性得到状态码，输出headers属性得到响应头，输出cookies 属性得到Cookies,输出url属性得到URL,输出history属性得到请求历史。

运行结果如下：

<class 'int'> 200
<class 'requests.structures.CaseInsensitiveDict'> {'X-XSS-Protection': '1; mode=block', 'Server': 'Tengine', 'Connection': 'keep-alive', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Encoding': 'gzip', 'Cache-Control': 'max-age=0, private, must-revalidate', 'Date': 'Wed, 12 May 2021 06:42:57 GMT', 'ETag': 'W/"4e73152cbd5c57292103f03d9bd67900"', 'Set-Cookie': 'locale=zh-CN; path=/', 'X-Request-Id': '4958bce2-056b-4f77-9f82-167eec7a7b5c', 'Vary': 'Accept-Encoding', 'Content-Type': 'text/html; charset=utf-8', 'X-Content-Type-Options': 'nosniff', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload', 'X-Runtime': '0.005863', 'Transfer-Encoding': 'chunked'}
<class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[<Cookie locale=zh-CN for www.jianshu.com/>]>
<class 'str'> https://www.jianshu.com/
<class 'list'> [<Response [301]>]

#### 3.2.2高级用法

在前一节中，我们了解了 requests的基本用法，如基本的GET、POST请求以及Response对象。 本节中，我们再来了解下requests的一些高级用法，如文件上传、Cookies设置、代理设置等。

##### 1.文件上传

import requests

files ={ ('file': open('favicon.ico', 'rb')}

r = requests.post("http://httpbin.org/post", files=files)

print(r.text)

在前一节中我们保存了一个文件favicon.ico,这次用它来模拟文件上传的过程。需要注意的是， favicon.ico需要和当前脚本在同一目录下。如果有其他文件，当然也可以使用其他文件来上传，更改 下代码即可。

运行结果如下：

(

"args": {},

"data":

"files": (

"file": "data:application/octet-stream;base64,AAAAAA.

},

"form": {),

"headers": (

"Accept": "*/*",

"Accept-Encoding": "gzip, deflate",

"Content-Length": "6665",

"Content-Type": "multipart/form-data; boundary=809f80bla2974132bl33adela8e8e058",

"Host": "httpbin.org",

"User-Agent": "python-requests/2.10.0"

},

"json": null,

"origin": "60.207.237.16",                                                '

"url": "http://httpbin.org/post"

)

以上省略部分内容，这个网站会返回响应，里面包含files这个字段，而form字段是空的，这证 明文件上传部分会单独有一个files字段来标识。

##### 2.cookies

前面我们使用urllib处理过Cookies,写法比较复杂，而有了 requests,获取和设置Cookies只需 一步即可完成。

我们先用一个实例看一下获取Cookies的过程：

```python
import requests

r=requests.get('https://www.baidu.com')

print(r.cookies)

for key,value in r.cookies.item():

	print(key+'='+value)
```

运行结果：

<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
BDORZ=27315

##### 3.会话维持

在requests中，如果直接利用get()或post。等方法的确可以做到模拟网页的请求，但是这实际 上是相当于不同的会话，也就是说相当于你用了两个浏览器打开了不同的页面。

设想这样一个场景，第一个请求利用post()方法登录了某个网站，第二次想获取成功登录后的自己的个人信息，你又用了一次get()方法去请求个人信息页面。实际上，这相当于打开了两个浏览器, 是两个完全不相关的会话，能成功获取个人信息吗？那当然不能。

有小伙伴可能说了，我在两次请求时设置一样的cookies不就行了？可以，但这样做起来显得很 烦琐，我们有更简单的解决方法。

其实解决这个问题的主要方法就是维持同一个会话，也就是相当于打开一个新的浏览器选项卡而不是新开一个浏览器。但是我又不想每次设置cookies,那该怎么办呢？这时候就有了新的 利器  Session对象。

利用它，我们可以方便地维护一个会话，而且不用担心cookies的问题，它会帮我们自动处理好。 示例如下：

import requests

requests.get('http://httpbin.org/cookies/set/number/123456789') 

r = requests.get('http://httpbin.org/cookies')

print(r.text)

这里我们请求了一个测试网址http://httpbin.org/cookies/set/number/123456789请求这个网址时， 可以设置一个 cookie,名称叫作 number,内容是 123456789,随后又请求了 http://httpbin.org/cookies, 此网址可以获取当前的Cookies0

这样能成功获取到设置的Cookies吗？试试看。

运行结果如下：

{

"cookies": ()

)

这并不行。我们再用Session试试看:

import requests

s = requests.Session()

s.get('http://httpbin.org/cookies/set/number/123456789')

r = s.get('http://httpbin.org/cookies )

 print(r.text)

再看下运行结果：

{

"cookiesM: (

"number": "123456789"

}

)

成功获取！这下能体会到同一个会话和不同会话的区别了吧!

所以，利用Session,可以做到模拟同一个会话而不用担心Cookies的问题。它通常用于模拟登录 成功之后再进行下一步的操作。

Session在平常用得非常广泛，可以用于模拟在一个浏览器中打开同一站点的不同页面，后面会 有专门的章节来讲解这部分内容。

##### 4.SSL证书验证

此外，requests还提供了证书验证的功能。当发送HTTP请求的时候，它会检査SSL证书，我们 可以使用verify参数控制是否检查此证书。其实如果不加verify参数的话，默认是True,会自动验 证。

前面我们提到过，12306的证书没有被官方CA机构信任，会出现证书验证错误的结果。我们现 在访问它，都可以看到一个证书问题的页面。这时在get参数中加一个verify=False。

##### 5.代理设置

对于某些网站，在测试的时候请求几次，能正常获取内容。但是一旦开始大规模爬取，对于大规 模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，更甚者可能会直接封禁客户端 的IP,导致一定时间段内无法访问。

那么，为了防止这种情况发生，我们需要设置代理来解决这个问题，这就需要用到proxies参数。 可以用这样的方式设置：

```
import requests

proxies = {

"http": "http://10.10.1.10:3128",

"https": "http://10.10.1.10:1080"}

requests.get('https://www.taobao.com',proxies=proxies)
```

当然，直接运行这个实例可能不行，因为这个代理可能是无效的，请换成自己的有效代理试验 一下。

##### 6 .超时设置

在本机网络状况不好或者服务器网络响应太慢甚至无响应时，我们可能会等待特别久的时间才可 能收到响应，甚至到最后收不到响应而报错。为了防止服务器不能及时响应，应该设置一个超时时间， 即超过了这个时间还没有得到响应，那就报错。这需要用到timeout参数。这个时间的计算是发出请 求到服务器返回响应的时间。示例如下：

import requests

r = requests.get("https://www.taobao.com", timeout = 1)

print(r.status_code)

通过这样的方式，我们可以将超时时间设置为1秒，如果1秒内没有响应，那就抛出异常。

> 本节讲解了 requests的一些高级用法，这些用法在后面实战部分会经常用到，需要熟练掌握。更 多的用法可以参考 requests 的官方文档：http://docs.python-requests.org/

### 3.3正则表达式

本节中，我们看一下正则表达式的相关用法。正则表达式是处理字符串的强大工具，库为re，它有自己特定的语法结构，有了它，实现字符串的检索、替换、匹配验证都不在话下。

当然，对于爬虫来说，有了它，从HTML里提取想要的信息就非常方便了。

下图是正则表达式的匹配规则

| 模式   | 描  述                                                       |
| ------ | ------------------------------------------------------------ |
| \w     | 匹配字母，数字及下划线                                       |
| \W     | 匹配不是字母，数字及下划线的字符                             |
| \s     | 匹配任意空白字符，等价于［\t\n\r\f］                         |
| \S     | 匹配任意非空字符                                             |
| \d     | 匹配任意数字，等价于［0-9］                                  |
| \D     | 匹配任意非数字的字符                                         |
| \A     | 匹配字符串开头                                               |
| \Z     | 匹配字符串结尾，如果存在换行，只匹配到换行前的结束字符串     |
| \z     | 匹配字符串结尾，如果存在换行，同时还会匹配换行符             |
| \G     | 匹配最后匹配完成的位置                                       |
| \t     | 匹配一个制表符                                               |
| \n     | 匹配一个换行符                                               |
| ^      | 匹配一行字符串的开头                                         |
| $      | 匹配一行字符串的结尾                                         |
| .      | **匹配任意字符，除了换行符,当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符** |
| [...]  | 用来表示一组字符，单独列出，比如［amk］匹配a、m或k           |
| [^...] | 不在［］中的字符，比如［Aabc］匹配除了 a、b、c之外的字符     |
| *      | **匹配0个或多个表达式**                                      |
| +      | **匹配1个或多个表达式**                                      |
| ?      | **匹配0个或1个前面的正则表达式定义的片段，非贪婪方式**       |
| {n}    | 精确匹配n个前面的表达式                                      |
| {n,m}  | 匹配n到m次由前面正则表达式定义的片段，贪婪方式               |
| a\|b   | 匹配a或b                                                     |
| ()     | **匹配括号内的表达式，也表示一个组**                         |

看完了之后，可能有点晕晕的吧，不过不用担心，后面我们会详细讲解一些常见规则的用法。

其实正则表达式不是Python独有的，它也可以用在其他编程语言中。但是Python的re库提供了 整个正则表达式的实现，利用这个库，可以在Python中使用正则表达式。在Python中写正则表达式 几乎都用这个库，下面就来了解它的一些常用方法。

##### 3.3.1match()

这里首先介绍第一个常用的匹配方法一match(),向它传入要匹配的字符串以及正则表达式，就可以检测这个正则表达式是否匹配字符串。

match()方法会尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果；如果不匹配，就返回None。示例如下：

```python
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())
```

运行结果如下：

41
<_sre.SRE_Match object; span=(0, 25), match='Hello 123 4567 World_This'>
Hello 123 4567 World_This
(0, 25)

这里首先声明了一个字符串，其中包含英文字母、空白字符、数字等。接下来，我们写一个正则表达式：

^Hello\s\d\d\d\s\d{4}\s\w{10}

用它来匹配这个长字符串。开头的^是匹配字符串的开头，也就是以Hello开头；然后\s匹配空 白字符，用来匹配目标字符串的空格；\d匹配数字，3个\d匹配123;然后再写1个\s匹配空格；后 面还有4567,我们其实可以依然用4个\d来匹配，但是这么写比较烦琐，所以后面可以跟{4}以代表 匹配前面的规则4次，也就是匹配4个数字；然后后面再紧接1个空白字符，最后\w{10}匹配10个字母及下划线。我们注意到，这里其实并没有把目标字符串匹配完，不过这样依然可以进行匹配，只不 过匹配结果短一点而已。

而在match()方法中，第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串。

打印输出结果，可以看到结果是SRE_Match对象，这证明成功匹配。该对象有两个方法：group() 方法可以输出匹配到的内容，结果是Hello 123 4567 World_This,这恰好是正则表达式规则所匹配的内容；span()方法可以输岀匹配的范围，结果是(0, 25),这就是匹配到的结果字符串在原字符串中的位置范围。

通过上面的例子，我们基本了解了如何在Python中使用正则表达式来匹配一段文字

**匹配目标**

刚才我们用match()方法可以得到匹配到的字符串内容，但是如果想从字符串中提取一部分内容， 该怎么办呢？就像最前面的实例一样，从一段文本中提取出邮件或电话号码等内容。

这里可以使用()括号将想提取的子字符串括起来。()实际上标记了一个子表达式的开始和结束位 置，被标记的每个子表达式会依次对应每一个分组，调用group()方法传入分组的索引即可获取提取的结果。示例如下：

```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'

result = re.match('^Hello\s(\d+)\sWorld', content)

print(result)

print(result.group())

print(result.group(1))

print(result.span())
```

运行结果如下

<_sre.SRE_Match object; span=(0, 19), match='Hello 1234567 World'>
Hello 1234567 World
1234567
(0, 19)

可以看到，我们成功得到了 1234567。这里用的是group(l),它与group()有所不同，后者会输出完整的匹配结果，而前者会输出第一个被()包围的匹配结果。假如正则表达式后面还有()包括的内容, 那么可以依次用group(2)、group(3)等来获取。

##### 通用匹配

刚才我们写的正则表达式其实比较复杂，出现空白字符我们就写\s匹配，出现数字我们就用\d 匹配，这样的工作量非常大。其实完全没必要这么做，因为还有一个万能匹配可以用，那就是.*(点 星)。其中.(点)可以匹配任意字符(除换行符)， (星)代表匹配前面的字符无限次，所以它们组 合在一起就可以匹配任意字符了。有了它，我们就不用挨个字符地匹配了。

接着上面的例子，我们可以改写一下正则表达式：

```python
import re

content = 'Hello 123 4567 World_This is a Regex Demo'

result = re.match('^Hello.*Demo$', content)

print(result)

print(result.group())

print(result.span())
```

这里我们将中间部分直接省略，全部用.*来代替，最后加一个结尾字符串就好了。运行结果如下:

<_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
Hello 123 4567 World_This is a Regex Demo
(0, 41)

可以看到,group()方法输出了匹配的全部字符串，也就是说我们写的正则表达式匹配到了目标字 符串的全部内容；span。方法输出(0, 41),这是整个字符串的长度。

因此，我们可以使用.*简化正则表达式的书写。

##### 贪婪和非贪婪

使用上面的通用匹配.*时，可能有时候匹配到的并不是我们想要的结果。看下面的例子: 

```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'

result = re.match('^He.*(\d+).*Demo$', content)

print(result)

print(result.group(l))
```

这里我们依然想获取中间的数字，所以中间依然写的是(\d+).而数字两侧由于内容比较杂乱， 所以想省略来写，都写成. * 。最后，组成We.* (\d+).*Demo$,看样子并没有什么问题。我们看下运行结果

<_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
7

奇怪的事情发生了，我们只得到了 7这个数字，这是怎么回事呢？

这里就涉及一个贪婪匹配与非贪婪匹配的问题了。在贪婪匹配下，.* 会匹配尽可能多的字符。正则表达式中. * 后面是\d+,也就是至少一个数字，并没有指定具体多少个数字，因此，.*就尽可能匹配 多的字符，这里就把123456匹配了，给\d+留下一个可满足条件的数字7,最后得到的内容就只有数字7 了。

但这很明显会给我们带来很大的不便。有时候，匹配结果会莫名其妙少了一部分内容。其实，这 里只需要使用非贪婪匹配就好了。非贪婪匹配的写法是.*?,多了一个？，那么它可以达到怎样的效果？ 我们再用实例看一下：

```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'

result = re.match('^He.*?(\d+).*Demo$',content)

print(result)

print(result.group(1))
```

结果如下

<_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
1234567

此时就可以成功获取1234567 了。原因可想而知，贪婪匹配是尽可能匹配多的字符，非贪婪匹配 就是尽可能匹配少的字符。当.* ?匹配到Hello后面的空白字符时，再往后的字符就是数字了，而\d+ 恰好可以匹配，那么这里.* ?就不再进行匹配，交给\d+去匹配后面的数字。所以这样.*?匹配了尽可能 少的字符，\d+的结果就是1234567 了。

所以说，在做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用.* ?来代替.*,以免出现 匹配结果缺失的情况

但这里需要注意，如果匹配的结果在字符串结尾， .*?就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符。例如：

```
import re

content = 'http://weibo.com/comment/kEraCN'

result1 = re.match('http.*?comment/(.*?)', content)

result2 = re.match('http.*?comment/(.*)', content)

print('resultl', result1.group(1))

print('result2', result2.group(1))
```

运行结果如下：

result1

result2 kEraCN

可以观察到，.* ?没有匹配到任何结果，而.*则尽量匹配多的内容，成功得到了匹配结果。

**修饰符**

正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。 我们用实例来看一下：

```python
import re

content = '''Hello 1234567 World_This

is a Regex Demo'''

result = re.match('^He.*?(\d+).*?Demo$', content)

print(result.group(1))
```

运行结果如下

Traceback (most recent call last):
  File "C:/Users/javac/Desktop/学生作业/class 2/测试.py", line 9, in <module>
    print(result.group(1))
AttributeError: 'NoneType' object has no attribute 'group'

运行直接报错，也就是说正则表达式没有匹配到这个字符串，返回结果为None,而我们又调用了 group()方法导致 AttributeError。

那么，为什么加了一个换行符，就匹配不到了呢？这是因为.匹配的是除换行符之外的任意字符, 当遇到换行符时，.*?就不能匹配了，所以导致匹配失败。这里只需加一个修饰符re.S,即可修正这 个错误：

result = re.match('AHe.* ?(\d+).*?Demo$', content, re.S)

这个修饰符的作用是使.匹配包括换行符在内的所有字符。此时运行结果如下：

1234567

这个re.S在网页匹配中经常用到。因为HTML节点经常会有换行，加上它，就可以匹配节点与 节点之间的换行了。

另外，还有一些修饰符，在必要的情况下也可以使用，如下表所示。

| 修饰符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| re.I   | 使匹配对大小写不敏感                                         |
| re.L   | 做本地化识别(locale-aware )匹配                              |
| re.M   | 多行匹配，影响"和$                                           |
| re.S   | 使.匹配包括换行在内的所有字符                                |
| re.U   | 根据Unicode字符集解析字符。这个标志影响\w、\W, \b和\B        |
| re.X   | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解 |

在网页匹配中，较为常用的有re.S和re.I.

**转义匹配**

我们知道正则表达式定义了许多匹配模式，如.匹配除换行符以外的任意字符，但是如果目标字符串里面就包含.，那该怎么办呢？

这里就需要用到转义匹配了，示例如下：

```python
import re

content ='(百度)www.baidu.com'

result = re.match('\(百度\)www\.baidu\.com', content)

print(result)
```

当遇到用于正则匹配模式的特殊字符时，在前面加反斜线转义一下即可。例如.就可以用\.来匹 配，运行结果如下：

<_sre.SRE_Match object; span=(0, 17), match='(百度)www.baidu.com'>

可以看到，这里成功匹配到了原字符串。

这些是写正则表达式常用的几个知识点，熟练掌握它们对后面写正则表达式匹配非常有帮助。

##### 3.3.2search()

前面提到过，match()方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败 了。我们看下面的例子：

```python
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'

result = re.match('Hello.*?(\d+).*?Demo', content)

print(result)
```

这里的字符串以Extra开头，但是正则表达式以Hello开头，整个正则表达式是字符串的一部分, 但是这样匹配是失败的。运行结果如下：

None

因为match()方法在使用时需要考虑到开头的内容，这在做匹配时并不方便。它更适合用来检测

某个字符串是否符合某个正则表达式的规则。

这里就有另外一个方法search(),它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。也就是说，正则表达式可以是字符串的一部分，在匹配时，search()方法会依次扫描字符串，直到找到第一个符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就返回None。

  我们把上面代码中的match。方法修改成search(),再看下运行结果：

<_sre.SRE_Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>

这时就得到了匹配结果。

因此，为了匹配方便，我们可以尽量使用search。方法。

下面再用几个实例来看看search()方法的用法。

首先，这里有一段待匹配的HTML文本，接下来写几个正则表达式实例来实现相应信息的提取：

```html
html = '''<div id="songs-list">

<h2 class="title">经典老歌</h2>

<p class="introduction">

经典老歌列表

</p>

<ul id="list" class="list-group">

<li data-view="2">—路上有你</li>

<li data-view="7">

<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>

</li>

<li data-view="4" class="active">

<a href="/3.mp3" singer="齐秦">往事随风</a>

</li>

    <li data-view="6">
    <a href="/4.mp3"singer="beyond">光辉岁月</a></li>

     <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
```

可以观察到，ul节点里有许多li节点，其中li节点中有的包含a节点，有的不包含a节点，a 节点还有一些相应的属性——超链接和歌手名。

首先，我们尝试提取class为active的li节点内部的超链接包含的歌手名和歌名，此时需要提 取第三个li节点下a节点的singer属性和文本。

此时正则表达式可以以li开头，然后寻找一个标志符active,中间的部分可以用.* ?来匹配。接 下来，要提取singer这个属性值，所以还需要写入singer="(•* ?)",这里需要提取的部分用小括号括 起来，以便用group()方法提取出来，它的两侧边界是双引号。然后还需要匹配a节点的文本，其中它 的左边界是〉，右边界是</a>。然后目标内容依然用(.*?)来匹配，所以最后的正则表达式就变成了：

```python
<li.*?active.*?singer="(.*?)">(.*?)</a>
```

然后再调用search。方法，它会搜索整个HTML文本，找到符合正则表达式的第一个内容返回。 另外，由于代码有换行，所以这里第三个参数需要传入re.S。整个匹配代码如下：

```python
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)

if result:
    print(result.group(1),result.group(2))
```

运行结果如下：

齐秦往事随风

可以看到，这正是class为active的li节点内部的超链接包含的歌手名和歌名。

如果正则表达式不加active (也就是匹配不带class为active的节点内容),那会怎样呢？我们 将正则表达式中的active去掉，代码改写如下：

```python
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)

if result:

	print(result.group(1), result.group(2))
```

由于search()方法会返回第一个符合条件的匹配目标，这里结果就变了：

任贤齐沧海一声笑

把active标签去掉后，从字符串开头开始搜索，此时符合条件的节点就变成了第二个li节点， 后面的就不再匹配，所以运行结果就变成第二个li节点中的内容。
注意，在上面的两次匹配中，search()方法的第三个参数都加了 re.S,这使得.*?可以匹配换行, 所以含有换行的li节点被匹配到了。如果我们将其去掉，结果会是什么？代码如下：

```python
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)

if result:

    print(result.group(1), result.group(2))
```

结果如下：

beyond 光辉岁月 

可以看到，结果变成了第四个li节点的内容。这是因为第二个和第三个li节点都包含了换行符, 去掉re.S之后，.*?已经不能匹配换行符，所以正则表达式不会匹配到第二个和第三个li节点，而第 四个li节点中不包含换行符，所以成功匹配。

由于绝大部分的HTML文本都包含了换行符，所以尽量都需要加上re.S修饰符，以免出现匹配不到的问题。

##### 3.3.3findall()

前面我们介绍了 search()方法的用法，它可以返回匹配正则表达式的第一个内容，但是如果想要 \获取匹配正则表达式的所有内容，那该怎么办呢？这时就要借助findall())方法了。该方法会搜索整个字符串，然后返回匹配正则表达式的所有内容。

还是上面的HTML文本，如果想获取所有a节点的超链接、歌手和歌名，就可以将search()方法 换成findall()方法。如果有返回结果的话，就是列表类型，所以需要遍历一下来依次获取每组内容。 代码如下：

```python
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html,re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0],result[1],result[2])
```

运行结果如下：

[('/2.mp3', '任贤齐', '沧海一声笑'), ('/3.mp3', '齐秦', '往事随风'), ('/4.mp3', 'beyond', '光辉岁月'), ('/5.mp3', '陈慧琳', '记事本'), ('/6.mp3', '邓丽君', '但愿人长久')]
<class 'list'>
('/2.mp3', '任贤齐', '沧海一声笑')
/2.mp3 任贤齐 沧海一声笑
('/3.mp3', '齐秦', '往事随风')
/3.mp3 齐秦 往事随风
('/4.mp3', 'beyond', '光辉岁月')
/4.mp3 beyond 光辉岁月
('/5.mp3', '陈慧琳', '记事本')
/5.mp3 陈慧琳 记事本
('/6.mp3', '邓丽君', '但愿人长久')
/6.mp3 邓丽君 但愿人长久

可以看到，返回的列表中的每个元素都是元组类型，我们用对应的索引依次取出即可。如果只是获取第一个内容，可以用search()方法。当需要提取多个内容时，可以用findall()方法。

##### 3.3.4sub()

除了使用正则表达式提取信息外，有时候还需要借助它来修改文本。比如，想要把一串文本中的 所有数字都去掉，如果只用字符串的replace()方法，那就太烦琐了，这时可以借助sub()方法。示例 如下：

```python
import re
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)
print(content)
```

运行结果如下

aKyroiRixLg

这里只需要给第一个参数传入\d+来匹配所有的数字，第二个参数为替换成的字符串(如果去掉该参数的话，可以赋值为空)，第三个参数是原字符串。

在上面的HTML文本中，如果想获取所有li节点的歌名,直接用正则表达式来提取可能比较烦 琐。比如，可以写成这样子：

```python
results=re.findall('li.*?\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
for result in results:
	print(result[1])
```

运行结果如下

> 路上有你
> 沧海一声笑
> 往事随风
> 光辉岁月
> 记事本
> 但愿人长久

此时借助sub()方法就比较简单了。可以先用sub。方法将a节点去掉，只留下文本，然后再利用 findall()提取就好了：

```python
html = re.sub('<a.*?>|</a>', '', html)

print(html)

results = re.findall('<li.*?>(.*?)</li>', html, re.S)

for result in results:

	print(result.strip())
```

运行结果如下：

```


<div id="songs-list">


<h2 class="title">经典老歌</h2>

<p class="introduction">


经典老歌列表

</p>

<ul id="list" class="list-group">


<li data-view="2">—路上有你</li>

<li data-view="7">

沧海一声笑

</li>

<li data-view="4" class="active">

往事随风

</li>

    <li data-view="6">
    光辉岁月</li>
    
     <li data-view="5">记事本</li>

<li data-view="5">
但愿人长久
</li>
</ul>
</div>
—路上有你
沧海一声笑
往事随风
光辉岁月
记事本
但愿人长久

Process finished with exit code 0
```

可以看到，a节点经过sub()方法处理后就没有了，然后再通过findall()方法直接提取即可。可 以看到，在适当的时候，借助sub()方法可以起到事半功倍的效果。

##### 3.3.5compile()

前面所讲的方法都是用来处理字符串的方法，最后再介绍一下compile()方法，这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用。示例代码如下：

```python
import re
content1= '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13：21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)

```

例如，这里有3个日期，我们想分别将3个日期中的时间去掉，这时可以借助sub()方法。该方 法的第一个参数是正则表达式，但是这里没有必要重复写3个同样的正则表达式，此时可以借助 compile()方法将正则表达式编译成一个正则表达式对象，以便复用。

运行结果如下：

2016-12-15 2016-12-17 2016-12-22

另外，compile()还可以传入修饰符,例如re.S等修饰符，这样在search。、findall()等方法中 就不需要额外传了。所以，compile。方法可以说是给正则表达式做了一层封装，以便我们更好地复用。

到此为止，正则表达式的基本用法就介绍完了，后面会通过具体的实例来讲解正则表达式的用法

## 四.解析库的使用

上一章中，我们实现了一个最基本的爬虫，但提取页面信息时使用的是正则表达式，这还是比较 烦琐，而且万一有地方写错了，可能导致匹配失败，所以使用正则表达式提取页面信息多多少少还是 有些不方便。

对于网页的节点来说，它可以定义id、class或其他属性。而且节点之间还有层次关系，在网页 中可以通过XPath或CSS选择器来定位一个或多个节点。那么，在页面解析时，利用XPath或CSS 选择器来提取某个节点，然后再调用相应方法获取它的正文内容或者属性，不就可以提取我们想要的 任意信息了吗？

在Python中，怎样实现这个操作呢？不用担心，这种解析库已经非常多,其中比较强大的库有Ixml. Beautiful Soup、pyquery等，本章就来介绍这3个解析库的用法。有了它们，我们就不用再为正则表 达式发愁，而且解析效率也会大大提高。

### 4.1 使用 XPath

XPath,全称XML Path Language,即XML路径语言，它是一门在XML文档中查找信息的语言。 它最初是用来搜寻XML文档的，但是它同样适用于HTML文档的搜索。

所以在做爬虫时，我们完全可以使用XPath来做相应的信息抽取。本节中，我们就来介绍XPath 的基本用法。

1. XPath 概览

XPath的选择功能十分强大，它提供了非常简洁明了的路径选择表达式。另外，它还提供了超过 100个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理等。几乎所有我们想要定位 的节点，都可以用XPath来选择。

XPath于1999年11月16日成为W3C标准，它被设计为供XSLT、XPointer以及其他XML解析 软件使用，更多的文档可以访问其官方网站：https://www.w3.org/TR/xpath/。

2. XPath常用规则

下表列举了 XPath的几个常用规则。

| 表达式   | 描 述                    |
| -------- | ------------------------ |
| nodename | 选取此节点的所有子节点   |
| /        | 从当前节点选取直接子节点 |
| //       | 从当前节点选取子孙节点   |
| .        | 选取当前节点             |
| ..       | 选取当前节点的父节点     |
| @        | 选取属性                 |

 

这里列出了 XPath的常用匹配规则，示例如下：

//title[@lang='eng']

这就是一个XPath规则，它代表选择所有名称为title,同时属性lang的值为eng的节点。 后面会通过Python的Ixrnl库，利用XPath进行HTML的解析。

3. 准备工作

使用之前，首先要确保安装好Ixml库，若没有安装，可以参考第1章的安装过程。

4. 实例引入

现在通过实例来感受一下使用XPath来对网页进行解析的过程，相关代码如下:

```html
from Ixml import etree

text =

<div>

<ul>

<li class="item-O"xa href="linkl.htinl">first item</ax/li>

<li class="item-l"xa href ="link2.html">second item</ax/li>

<li class="item-inactive"><a href="link3.html">third item</ax/li>

<li class="item-l"xa href="link4.html">fourth item</ax/li>

<li class="item-O"xa href="links.ifth item</a>

</ul>

</div>

html = etree.HTML(text)

result = etree.tostring(html)

print(result.decode('utf-8'))
```

这里首先导入Ixml库的etree模块，然后声明了一段HTML文本，调用HTML类进行初始化，这 样就成功构造了一个XPath解析对象。这里需要注意的是，HTML文本中的最后一个li节点是没有 闭合的，但是etree模块可以自动修正HTML文本。

这里我们调用tostring()方法即可输出修正后的HTML代码，但是结果是bytes类型。这里利用 decode()方法将其转成str类型，结果如下：

```
<htmlxbodyxdiv>

<ul>

<li class="item-o"xa href =" 1 inkl.html">first item</ax/li>

<li class="item-l"xa href =" 1 ink2.htmln>second item</ax/li>

<li class="item-inactive"><a href="link3.html">third item</ax/li>
<li class="item-i"xa href ="Iink4.html">fourth item</ax/li>
<li class="item-o"xa href="link5.html">fifth item</a>
</lix/ul>
</div>
</bodyx/html>

```

可以看到，经过处理之后，li节点标签被补全，并且还自动添加了 body、html节点。

另外，也可以直接读取文本文件进行解析，示例如下：

```
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser())

result = etree.tostring(html)

print(result.decode('utf-8'))
```

其中test.html的内容就是上面例子中的HTML代码，内容如下：

<div>

```html
<ul>

<li class="item-o"xa href=Mlinkl.html">first item</ax/li>

<li class="item-l"xa href ="link2.html">second item</ax/li>

<li class="item-inactive"><a href=Hlink3.html">thircl item</ax/li>

<li class="item-l"xa href =Mlink4.html">fourth item</ax/li>

<li class="item-O"xa href="links.html">fifth item</a>

</ul>

</div>
```

这次的输出结果略有不同，多了一个DOCTYPE的声明，不过对解析无任何影响，结果如下：

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html4O/loose.dtd"> <htmlxbodyxdiv>

<ul>

<li class="item-o"xa href ="linkl.html">first item</ax/li>

<li class="item-l"xa href="link2.html">second item</ax/li>

<li class="item-inactive"><a href="link3.html">third item</ax/li>

<li class="item-l"xa href="link4.html">fourth item</ax/li>

<li class="item-0"xa href ="link5.html">fifth item</a>

</lix/ul>

</divx/bodyx/html>
```

5. 所有节点

我们一般会用〃开头的XPath规则来选取所有符合要求的节点。这里以前面的HTML文本为例， 如果要选取所有节点，可以这样实现：

```
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath(//*')

print(result)
```

运行结果如下：

```
[<Element html at OxlO51Od9c8>, <Element body at OxlO51OdaO8>, <Element div at OxlO51Oda48>, <Element ul at OxlO51Oda88>, <Element li at OxlO51Odac8>, <Element a at OxlO51Odb48>, <Element li at OxlO51Odb88>, <Element a at OxlO51Odbc8>, <Element li at OxlO51OdcO8>, <Element a at OxlO51OdbO8>, <Element li at OxlO51Odc48>, <Element a at OxlO51Odc88>, <Element li at OxlO51Odcc8>, <Element a at 0xl0510dd08>]
```

这里使用*代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取。可以看到，返 回形式是一个列表，每个元素是Element类型，其后跟了节点的名称，如html、body、div、ul、li、a等，所有节点都包含在列表中了。

当然，此处匹配也可以指定节点名称。如果想获取所有li节点，示例如下：

```python
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser())

result = html-xpathC/Zli')

print(result)

print(result[o])
```

这里要选取所有li节点，可以使用//,然后直接加上节点名称即可，调用时直接使用xpath()方 法即可。

[<Element li at 0x105849208〉, <Element li at 0x105849248〉, <Element li at 0x105849288〉, <Element li at OxlO58492c8>, <Element li at OxlO58493O8>]

<Element li at 0x105849208〉

这里可以看到提取结果是一个列表形式，其中每个元素都是一个Element对象。如果要取出其中 一个对象，可以直接用中括号加索引，如[0]。

6. 子节点

我们通过/或//即可查找元素的子节点或子孙节点。假如现在想选择li节点的所有直接a子节点， 可以这样实现：

```python
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//li/a')

print(result)
```

这里通过追加/a即选择了所有li节点的所有直接a子节点。因为〃li用于选中所有li节点，/a 用于选中li节点的所有直接子节点a,二者组合在一起即获取所有li节点的所有直接a子节点。

运行结果如下：

[<Element a at OxlO6ee8688>, <Element a at 0xl06ee86c8>, <Element a at OxlO6ee87O8>, <Element a at OxlO6ee8748>, <Element a at OxlO6ee8788>]

此处的/用于选取直接子节点，如果要获取所有子孙节点，就可以使用//。例如，要获取U1节点 下的所有子孙a节点，可以这样实现：

```python
from Ixml import etree

html = etree.parse(*./test.html', etree.HTMLParser())

result = html.xpath('//ul//a')

print(result)
```

运行结果是相同的。

但是如果这里用〃ul/a,就无法获取任何结果了。因为/用于获取直接子节点，而在ul节点下没 有直接的a子节点，只有li节点，所以无法获取任何匹配结果，代码如下：

```python
from Ixml import etree

html = etree.parse(*./test.html', etree.HTMLParser())

result = html.xpath('//ul/a')

print(result)
```

运行结果如下：

[]

因此，这里我们要注意/和//的区别，其中/用于获取直接子节点，//用于获取子孙节点。

7. 父节点

我们知道通过连续的/或//可以查找子节点或子孙节点，那么假如我们知道了子节点，怎样来査 找父节点呢？这可以用..来实现。

比如，现在首先选中href属性为link4.html的a节点，然后再获取其父节点,然后再获取其class 属性，相关代码如下：

```python
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser()) 

result = html.xpath('//a[@href="link4.html"]/../@class') 

print(result)
```

运行结果如下：

['item-1']

检査一下结果发现，这正是我们获取的目标li节点的classo

同时，我们也可以通过parent::来获取父节点，代码如下：

```python
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser()) 

result = html.xpath('//a[@href="iink4.html"]/parent::*/@class') 

print(result)
```

8. 属性匹配

在选取的时候，我们还可以用@符号进行属性过滤。比如，这里如果要选取class为item-1的li 节点，可以这样实现：

```python
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//li[@class="item-0"]') 

print(result)
```

这里我们通过加入[@class="item-0"],限制了节点的class属性为item-0,而HTML文本中符合 条件的li节点有两个，所以结果应该返回两个匹配到的元素。结果如下：

[<Element li at OxlOa399288>, <Element li at OxlOa3992c8>]

可见，匹配结果正是两个，至于是不是那正确的两个，后面再验证。

9. 文本获取

我们用XPath中的text()方法获取节点中的文本，接下来尝试获取前面li节点中的文本，相关 代码如下：

```python
from Ixml import etree

html = etree.parse(1./test.html', etree.HTMLParser()) 

result = html.xpath('//li[@class="item-O"]/text()') 

print(result)
```

运行结果如下：

['\n   ']

奇怪的是，我们并没有获取到任何文本，只获取到了一个换行符，这是为什么呢？因为XPath中 text()前面是/,而此处/的含义是选取直接子节点，很明显li的直接子节点都是a节点，文本都是在 a节点内部的，所以这里匹配到的结果就是被修正的li节点内部的换行符，因为自动修正的li节点 的尾标签换行了。

即选中的是这两个节点：

```
<li class="item-0"xa href ="linkl.html">first item</ax/li>

<li class="item-0"xa href="link5.html">fifth item</a>

</li>
```

其中一个节点因为自动修正，li节点的尾标签添加的时候换行了，所以提取文本得到的唯一结果 就是li节点的尾标签和a节点的尾标签之间的换行符。

因此，如果想获取li节点内部的文本，就有两种方式，一种是先选取a节点再获取文本，另一 种就是使用//。接下来，我们来看下二者的区别。

首先，选取到a节点再获取文本，代码如下：

```python
from Ixml import etree

html = etree.parse(1./test.html', etree.HTMLParser())

result = html.xpath('//li[@class="item-0"]/a/text()') 

print(result)
```

运行结果如下：

['first item', 'fifth item']

可以看到，这里的返回值是两个，内容都是属性为item-0的li节点的文本，这也印证了前面属 性匹配的结果是正确的。

这里我们是逐层选取的，先选取了 li节点，又利用/选取了其直接子节点a,然后再选取其文本, 得到的结果恰好是符合我们预期的两个结果。

再来看下用另一种方式(即使用// )选取的结果，代码如下：

```python
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser()) 

result = html.xpath('//li[@class="item-O"]//text()') 

print(result)
```

运行结果如下：

['first item', 'fifth item*, '\n    ']

不岀所料，这里的返回结果是3个。可想而知，这里是选取所有子孙节点的文本，其中前两个就 是li的子节点a节点内部的文本，另外一个就是最后一个li节点内部的文本，即换行符。

所以说，如果要想获取子孙节点内部的所有文本，可以直接用〃加text。的方式，这样可以保证 获取到最全面的文本信息，但是可能会夹杂一些换行符等特殊字符。如果想获取某些特定子孙节点下 的所有文本，可以先选取到特定的子孙节点，然后再调用text()方法获取其内部文本，这样可以保证 获取的结果是整洁的。

10. 属性获取

我们知道用text()可以获取节点内部文本，那么节点属性该怎样获取呢？其实还是用@符号就可 以。例如，我们想获取所有li节点下所有a节点的href属性，代码如下：

```python
from Ixml import etree

html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//li/a/@href')

print(result)
```

这里我们通过@href即可获取节点的href属性。注意，此处和属性匹配的方法不同，属性匹配是 中括号加属性名和值来限定某个属性，如[@href="linkl.html"],而此处的飾珪卡指的是获取节点的某 个属性，二者需要做好区分。

运行结果如下：

['linkl.html', 'link2.html', 'link3.html', *link4.html', 'link5.html']

可以看到，我们成功获取了所有li节点下a节点的href属性，它们以列表形式返回。

11. 属性多值匹配

有时候，某些节点的某个属性可能有多个值，例如：

from Ixml import etree

text ='''

<li class="li li-first"xa href ="link.html">flist item</ax/li>

html = etree.HTML(text)                                                -

result = html.xpath('//li[@class="li"]/a/text()*)

print(result)

这里HTML文本中li节点的class属性有两个值li和li-first,此时如果还想用之前的属性匹 配获取，就无法匹配了，此时的运行结果如下：

[]

这时就需要用contains()函数了，代码可以改写如下：

from Ixml import etree

text ='''

<li class="li li-first"xa href ="link.html">first item</ax/li>

html = etree.HTML(text)

result = html.xpath('//li[contains(@class, "li")]/a/text()')

print(result)

这样通过contains()方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含 所传入的属性值，就可以完成匹配了。

此时运行结果如下：

['first item']

此种方式在某个节点的某个属性有多个值时经常用到，如某个节点的class属性通常有多个。

12. 多属性匹配

另外，我们可能还遇到一种情况，那就是根据多个属性确定一个节点，这时就需要同时匹配多个 属性。此时可以使用运算符and来连接，示例如下：

from Ixml import etree

text ='''

<li class="li li-first" name="item"xa href ="link.html">first item</ax/li>

html = etree.HTML(text)

result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')

print(result)

这里的li节点又增加了一个属性name。要确定这个节点，需要同时根据class和name属性来选 择，一个条件是class属性里面包含li字符串，另一个条件是name属性为item字符串，二者需要同 时满足，需要用and操作符相连，相连之后置于中括号内进行条件筛选。运行结果如下：

['first item']

这里的and其实是XPath中的运算符。另外，还有很多运算符，如or、mod等，在此总结为表4-20

表4-2运算符及其介绍

| 运算符 | 描 述          | 实                | 例                                             | 返回值                                          |
| ------ | -------------- | ----------------- | ---------------------------------------------- | ----------------------------------------------- |
| 01     | 或             | age=19 or         | age=20                                         | 如果age是19,则返回trueo如果age是21,则返回false  |
| and    | 与             | age>19 and age<21 | 如果age是20,则返回true0如果age是18,则返回false |                                                 |
| mod    | 计算除法的余数 | 5 mod 2           |                                                | 1                                               |
| 1      | 计算两个节点集 | //book \|         | //cd                                           | 返回所有拥有book和cd元素的节点集                |
| +      | 加法           | 6 + 4             |                                                | 10                                              |
| -      | 减法           | 6-4               |                                                | 2                                               |
| *      | 乘法           | 6*4               |                                                | 24                                              |
| div    | 除法           | 8 div 4           |                                                | 2                                               |
| =      | 等于           | age=19            |                                                | 如果age是19,则返回true。如果age是20,则返回false |
| !=     | 不等于         | age!=19           |                                                | 如果age是18,则返回true。如果age是19,则返回false |
| <      | 小于           | age<19            |                                                | 如果age是18,则返回true。如果age是19,则返回false |
| <=     | 小于或等于     | age<=19           |                                                | 如果age是19,则返回trueo如果age是20,则返回false  |
| >      | 大于           | age>19            |                                                | 如果age是20,则返回trueo如果age是19,则返回false  |
| >=     | 大于或等于     | age>=19           |                                                | 如果age是19,则返回true0如果age是18,则返回false  |

此表参考来源：http://www.w3school.com.cn/xpath/xpath_operators.aspo

13. 按序选择

有时候，我们在选择的时候某些属性可能同时匹配了多个节点，但是只想要其中的某个节点，如 第二个节点或者最后一个节点，这时该怎么办呢？

这时可以利用中括号传入索引的方法获取特定次序的节点，示例如下：

```python
from Ixml import etree

text ='''

<div>

<ul>

<li class="item-o"xa href ="linkl.html">first item</ax/li>

<li class="item-i"xa href =" 1 ink2.html">second item</ax/li>

<li class="item-inactive"><a href="link3.html">third item</ax/li>

<li class="item-l"xa href ="link4.html">fourth item</ax/li>

<li class="item-O"xa href="links.html">fifth item</a>

</ul>

</div>

html = etree.HTML(text)

result = html.xpath('//li[l]/a/text()')

print(result)

result = html.xpath('//li[last()]/a/text()')

print(result)

result = html.xpath('//li[pos ition()<3]/a/text()')

print(result)

result = html.xpath('//li[last()-2]/a/text()')

print(result)
```

第一次选择时，我们选取了第一个li节点，中括号中传入数字1即可。注意，这里和代码中不 同，序号是以1开头的，不是以0开头。

第二次选择时，我们选取了最后一个li节点，中括号中传入last。即可，返回的便是最后一个 li节点。

第三次选择时，我们选取了位置小于3的li节点，也就是位置序号为1和2的节点，得到的结果 就是前两个li节点。

第四次选择时，我们选取了倒数第三个li节点，中括号中传入last()-2即可。因为last。是最 后一个，所以last()-2就是倒数第三个。

运行结果如下：

['first item']

['fifth item']

['first item', 'second item']

['third item']

这里我们使用了 last。、position()等函数。在XPath中，提供了 100多个函数，包括存取、数 值、字符串、逻辑、节点、序列等处理功能，它们的具体作用可以参考：http://www.w3school.com. cn/xpath/xpathfiinctions.aspo

14. 节点轴选择

XPath提供了很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等，示例如下:

```python
from Ixml import etree

text =

<div>

<ul>

<li class="item-O"xa href="linkl.html"xspan>first item</spanx/ax/li>

<li class="item-l"xa href="link2.html">second item</ax/li>

<li class="item-inactive"><a href="link3.html">third item</ax/li>

<li class="item-l"xa href="link4.html">fourth item</ax/li>

<li class="item-0"xa href="link5.html">fifth item</a>

</ul>

</div>

html = etree.HTML(text)

result = html.xpath('//li[l]/ancestor::*')

print(result)

result = html.xpath('//li[l]/ancestor::div')

print(result)

result = html.xpath('//li[l]/attribute::*')

print(result)

result = html.xpath('//li[1]/child::a[@href="linkl.html"]')

print(result)

result = html.xpath('//li[1]/descendant::span')

print(result)

result = html.xpath('//li[l]/following::*[2]')

print(result)

result = htmi.xpath('//li[l]/following-sibling::*')

print(result)
```

运行结果如下：

```
[<Element html at 0x107941808〉, <Element body at OxlO79418c8>, <Element div at 0x107941908〉，

<Element ul at 0x107941948〉]

[<Element div at OxlO79419O8>]

['item-0']

[<Element a at OxlO79418c8>]

[<Element span at OxlO7941948>]

[<Element a at OxlO79418c8>]

[<Element li at 0x107941948〉， <Element li at 0x107941988〉， <Element li at OxlO79419c8>, <Element li at OxlO7941aO8>]
```

第一次选择时，我们调用了 ancestor轴，可以获取所有祖先节点。其后需要跟两个冒号，然后是 节点的选择器，这里我们直接使用*,表示匹配所有节点，因此返回结果是第一个li节点的所有祖先 节点，包括 html、body、div 和 ul。

第二次选择时，我们又加了限定条件，这次在冒号后面加了 div,这样得到的结果就只有div这 个祖先节点了。

第三次选择时，我们调用了 attribute轴，可以获取所有属性值，其后跟的选择器还是*,这代表 获取节点的所有属性，返回值就是li节点的所有属性值。

第四次选择时，我们调用了 child轴，可以获取所有直接子节点。这里我们又加了限定条件，选 取href属性为linkl.html的a节点。

第五次选择时，我们调用了 descendant轴，可以获取所有子孙节点。这里我们又加了限定条件获 取span节点，所以返回的结果只包含span节点而不包含a节点。

第六次选择时，我们调用了 following轴，可以获取当前节点之后的所有节点。这里我们虽然使 用的是*匹配，但又加了索引选择，所以只获取了第二个后续节点。

第七次选择时，我们调用了 following-sibling轴，可以获取当前节点之后的所有同级节点。这 里我们使用*匹配，所以获取了所有后续同级节点。

以上是XPath轴的简单用法，更多轴的用法可以参考：http://www.w3school.com.cn/xpath/xpath/axes.aspo

15. 结语

到现在为止，我们基本上把可能用到的XPath选择器介绍完了。XPath功能非常强大，内置函数 非常多，熟练使用之后，可以大大提升HTML信息的提取效率。

如果想查询更多 XPath 的用法，可以查看：http://www.w3school.com.cn/xpath/index.aspo

如果想查询更多Python Ixml库的用法，可以查看http://lxml.de/。



## 五.数据存储

用解析器解析出数据之后，接下来就是存储数据了。保存的形式可以多种多样，最简单的形式是 直接保存为文本文件，如TXT、JSON、CSV等。另外，还可以保存到数据库中，如关系型数据库 MySQL,非关系型数据库MongoDB、Redis等。

### 5.1文件存储

文件存储形式多种多样，比如可以保存成TXT纯文本形式，也可以保存为JSON格式、CSV格 式等，本节就来了解一下文本文件的存储方式。

#### 5.1.1  TXT文本存储

将数据保存到TXT文本的操作非常简单，而且TXT文本几乎兼容任何平台，但是这有个缺点， 那就是不利于检索。所以如果对检索和数据结构要求不高，追求方便第一的话，可以采用TXT文本 存储。本节中，我们就来看下如何利用Python保存TXT文本文件。

1. 本节目标

本节中，我们要保存知乎上“发现”页面的“热门话题”部分，将其问题和答案统一保存成文本 形式。

2. 基本实例

首先，可以用requests将网页源代码获取下来，然后使用lxml解析库解析，接下来将提取的 标题、演员，评分保存到文本，代码如下：

```python
from lxml import etree
import requests
import csv
url='https://maoyan.com/board'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
,'Host':'maoyan.com',
'Referer':'https://maoyan.com/',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cookie':'__mta=19360135.1621229699619.1621232605407.1621233615312.18; uuid_n_v=v1; uuid=9D5AB640B6D111EB92E297064163C32DAB9FB285B447472289C8C36C4594B6C7; _lxsdk_cuid=17978d1fb8689-032c049c2944-5771133-e1000-17978d1fb87c8; _lxsdk=9D5AB640B6D111EB92E297064163C32DAB9FB285B447472289C8C36C4594B6C7; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; recentCis=883%3D165%3D332%3D150%3D1; _csrf=b5882b07f344eb59866902f27ea243d9c163d190850eefba777b055f6ef40a20; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1621229698,1621231348,1621233637; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1621234490; __mta=19360135.1621229699619.1621233615312.1621234490166.19; _lxsdk_s=17978d1fb87-d71-c77-f99%7C%7C71'
}
response=requests.get(url,headers=headers)
print(response.status_code)
html=etree.HTML(response.text)
result=etree.tostring(html,encoding='utf-8')
titles=html.xpath('//p[@class="name"]/a/text()')
actors=html.xpath('//p[@class="star"]/text()')
scores1=html.xpath('//p[@class="score"]/i[@class="integer"]/text()')
scores2=html.xpath('//p[@class="score"]/i[@class="fraction"]/text()')
file = open('explore.txt','a',encoding='utf-8')
file.write('\n'.join([titles[0],actors[0]]))
file.close()
# print(result.decode('utf8'))
```



这里主要是为了演示文件保存的方式，因此requests异常处理部分在此省去。首先，用requests 提取猫眼的页面，然后利用Python 提供的open()方法打开一个文本文件，获取一个文件操作对象，这里赋值为file,接着利用file对 象的write()方法将提取的内容写入文件，最后调用close()方法将其关闭，这样抓取的内容即可成功 写入文本中了。

运行程序，可以发现在本地生成了一个explore.txt文件

这样页面的内容就被保存成文本形式了。

这里open()方法的第一个参数即要保存的目标文件名称，第二个参数为a,代表以追加方式写入 到文本。另外，我们还指定了文件的编码为utf-8。最后，写入完成后，还需要调用close()方法来关 闭文件对象。

3. 打开方式

在刚才的实例中，open()方法的第二个参数设置成了 a,这样在每次写入文本时不会清空源文件, 而是在文件末尾写入新的内容，这是一种文件打开方式。关于文件的打开方式，其实还有其他几种， 这里简要介绍一下。

□  **r**：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。

□  **rb***：以二进制只读方式打开一个文件。文件指针将会放在文件的开头。

□  **r+***：以读写方式打开一个文件。文件指针将会放在文件的开头。

□  **rb+***：以二进制读写方式打开一个文件"文件指针将会放在文件的开头。

□  **w***：以写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创 建新文件。

□  **Wb***：以二进制写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存 在，则创建新文件。

□  **W+***：以读写方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创 建新文件。

□  **Wb+***：以二进制读写格式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存 在，则创建新文件。

□  **a***：以追加方式打开一个文件。如果该文件已存在，文件指针将会放在文件结尾。也就是 说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件来写入。

□  **ab***：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。 也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件来写入。

□  **a+***：以读写方式打开一个文件。如果该文件已存在，文件指针将会放在文件的结尾。文件打 开时会是追加模式。如果该文件不存在，则创建新文件来读写。

□  **ab+***：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。 如果该文件不存在，则创建新文件用于读写。

**4**. 简化写法

另外，文件写入还有一种简写方法，那就是使用with as语法。在with控制块结束时，文件会自 动关闭，所以就不需要再调用close()方法了。这种保存方式可以简写如下：

with open('explore.txt', 'a', encoding='utf-8') as file:

#### 5.1.2 JSON文件存储

JSON,全称为JavaScript Object Notation,也就是JavaScript对象标记，它通过对象和数组的组合 来表示数据，构造简洁但是结构化程度非常高，是一种轻量级的数据交换格式。本节中，我们就来了 解如何利用Python保存数据到JSON文件。

**1.**对象和数组

在JavaScript语言中，一切都是对象。因此，任何支持的类型都可以通过JSON来表示，例如字 符串、数字、对象、数组等，但是对象和数组是比较特殊且常用的两种类型，下面简要介绍一下 它们。

**对象**：它在JavaScript中是使用花括号{}包裹起来的内容，数据结构为{keyl： valuel, key2： value2, ...}的键值对结构。在面向对象的语言中，key为对象的属性，value为对应的值。 键名可以使用整数和字符串来表示。值的类型可以是任意类型。

**数组**：数组在JavaScript中是方括号[]包裹起来的内容，数据结构为["java", "javascript", "vb", ...]的索引结构。在JavaScript中，数组是一种比较特殊的数据类型，它也可以像对象 那样使用键值对，但还是索引用得多。同样，值的类型可以是任意类型。

所以，一个JSON对象可以写为如下形式：

[(

"name": "Bob",

"gender": "male",

"birthday": "1992-10-18"

}, {

"name": "Selina",

"gender": "female",

"birthday": "1995-10-18"

}]

由中括号包围的就相当于列表类型，列表中的每个元素可以是任意类型，这个示例中它是字典类 型，由大括号包围。

JSON可以由以上两种形式自由组合而成，可以无限次嵌套，结构清晰，是数据交换的极佳方式。

**2**.读取JSON

Python为我们提供了简单易用的JSON库来实现JSON文件的读写操作，我们可以调用JSON库 的loads()方法将JSON文本字符串转为JSON对象，可以通过dumps()方法将JSON对象转为文本字 符串。

例如，这里有一段JSON形式的字符串，它是str类型，我们用Python将其转换为可操作的数据 结构，如列表或字典：

```python
import json

str =

[{ '

"name": "Bob",

"gender": "male",

"birthday": "1992-10-18"

}, {

"name": "Selina",

"gender": "female",

"birthday": "1995-10-18"

}],

print(type(str))

data = json.loads(str)

print(data)

print(type(data))
```

运行结果如下：

<class 'str'>

[{'name': 'Bob', 'gender': 'male', 'birthday': '1992-10-18'('name': 'Selina', 'gender': 'female', 'birthday': '1995-10-18'}]

<class 'list'〉

这里使用loads。方法将字符串转为JSON对象。由于最外层是中括号，所以最终的类型是列表 类型。

这样一来，我们就可以用索引来获取对应的内容了。例如，如果想取第一个元素里的name属性， 就可以使用如下方式：

data[0]'name']

data[0].get('name')

得到的结果都是：

Bob

通过中括号加0索引，可以得到第一个字典元素，然后再调用其键名即可得到相应的键值。获取 键值时有两种方式，一种是中括号加键名，另一种是通过get()方法传入键名。这里推荐使用get() 方法，这样如果键名不存在，则不会报错，会返回None。另外，get()方法还可以传入第二个参数(即 默认值)，示例如下：

data[0].get('age')

data[o].get('age', 25)

运行结果如下：

None

25

这里我们尝试获取年龄age,其实在原字典中该键名不存在，此时默认会返回None。如果传入第 二个参数(即默认值),那么在不存在的情况下返回该默认值。

值得注意的是，JSON的数据需要用双引号来包围，不能使用单引号。例如，若使用如下形式表 示，则会出现错误：

import json

str =

[(

'name': 'Bob',

'gender': 'male', 'birthday': '1992-10-18 }](

data = json.loads(str)

运行结果如下：

json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 3 column 5 (char 8) 这里会出现JSON解析错误的提示。这是因为这里数据用单引号来包围，请千万注意JSON字符 串的表示需要用双引号，否则loads()方法会解析失败。

如果从JSON文本中读取内容，例如这里有一个data.json文本文件，其内容是刚才定义的JSON 字符串，我们可以先将文本文件内容读出，然后再利用loads()方法转化：

```python
import json

with open('data.json', 'r') as file:

str = file.read()

data = json.loads(str)

print(data)
```

运行结果如下：

[('name': 'Bob', 'gender': 'male', 'birthday': '1992-10-18'}, {'name': 'Selina', 'gender': 'female1, 'birthday': '1995-10-18')]



**3**.输出JSON

另外，我们还可以调用dumps。方法将JSON对象转化为字符串。例如，将上例中的列表重新写 入文本：

```python
import json

data = [(

'name': 'Bob',

'gender': 'male',

'birthday': '1992-10-18'

}]

with open('data.json', 'w') as file:

	file.write(json.dumps(data))
```

利用dumps()方法，我们可以将JSON对象转为字符串，然后再调用文件的write()方法写入文本. 

另外，如果想保存JSON的格式，可以再加一个参数indent，代表缩进字符个数。示例如下:

```python
 with open('data.json', 'w') as file:

	file.write(json.dumps(data, indent=2))
```

这样得到的内容会自动带缩进，格式会更加清晰。

另外，如果JSON中包含中文字符，会怎么样呢？例如，我们将之前的JSON的部分值改为中文, 再用之前的方法写入到文本：

```python
import json

data = [(

'name':，王伟

'gender':

'birthday': '1992-10-18'

)]

with open('data.json ', 'w') as file:

file.write(json.dumps(data, indent=2))
```

写入结果如图所示。

![xierujieguo](C:\Users\javac\Desktop\class\xierujieguo.jpg)

可以看到，中文字符都变成了 Unicode字符，这并不是我们想要的结果。

为了输出中文，还需要指定参数ensure_ascii= False,另外还要规定文件输出的编码:

```python
 with open('data.json ', 'w', encoding='utf-8') as file:

	file.write(json.dumps(data, indent=2, ensure_ascii=False))
```

写入结果如图所示。

![xierujieguo1](C:\Users\javac\Desktop\class\xierujieguo1.jpg)

#### 5.1.3 CSV文件存储

CSV,全称为Comma-Separated Values,中文可以叫作逗号分隔值或字符分隔值，其文件以纯文 本形式存储表格数据。该文件是一个字符序列，可以由任意数目的记录组成，记录间以某种换行符分 隔。每条记录由字段组成，字段间的分隔符是其他字符或字符串，最常见的是逗号或制表符。不过所 有记录都有完全相同的字段序列，相当于一个结构化表的纯文本形式。它比Excel文件更加简介，XLS 文本是电子表格，它包含了文本、数值、公式和格式等内容，而CSV中不包含这些内容，就是特定
 字符分隔的纯文本，结构简单清晰。所以，有时候用csv来保存数据是比较方便的。本节中，我们 来讲解Python读取和写入CSV文件的过程。

**1.**写入

这里先看一个最简单的例子：

import csv

with open('data.csv', 'w') as csvfile:

writer = csv.writer(csvfile)

writer.writerow(['id', 'name', 'age'])

writer.writerow(['10001', 'Mike', 20])

writer.writerow(['10002', 1 Bob', 22])

writer.writerow(['100031, 'Jordan', 21])

首先，打开data.csv文件，然后指定打开的模式*为*即写入)，获得文件句柄，随后调用csv库 的writer()方法初始化写入对象，传入该句柄，然后调用writerow()方法传入每行的数据即可完成 写入。

运行结束后，会生成一个名为data.csv的文件，此时数据就成功写入了。直接以文本形式打开的 话，其内容如下：

id,name,age

10001,Mike,20

10002,Bob,22

10003,Jordan,21

如果想修改列与列之间的分隔符，可以传入delimiter参数，其代码如下:

import csv

with open('data.csv', 'w') as csvfile: 

writer = csv.writer(csvfile, delimiter='') 

writer.writerow(['id', 'name', 'age'])

writer.writerow(['10001', 'Mike', 20])

writer.writerow(['10002', 'Bob', 22])

writer.writerow(['10003', 'Jordan', 21])

这里在初始化写入对象时传入delimiter 空格，此时输出结果的每一列就是以空格分隔了，内 容如下：

id name age

10001  Mike 20

10002  Bob 22

10003  Jordan 21

另外，我们也可以调用writerows()方法同时写入多行，此时参数就需要为二维列表，例如：

```
import csv

    with open('data.csv', 'w') as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(['id', 'name', 'age'])

    writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
```

输出效果是相同的，内容如下：

id,name,age                                                                    .

10001,Mike,20

10002,Bob,22

10003,Jordan,21

但是一般情况下，爬虫爬取的都是结构化数据，我们一般会用字典来表示。在CSV库中也提供了 字典的写入方式，示例如下：

```
import csv

with open('data.csv', 'w') as csvfile: 

    fieldnames = ['id', 'name', 'age'] 

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 

    writer.writeheader()

    writer.writerow(('id': '10001', 'name': 'Mike', 'age': 20)) 

    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22))

     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21))
```

这里先定义3个字段，用fieldnames表示，然后将其传给DictWriter来初始化一个字典写入对 象接着可以调用writeheader。方法先写入头信息，然后再调用writerow()方法传入相应字典即可。 最终写入的结果是完全相同的，内容如下：

id,name,age

loooi,Mike,20

10002,Bob,22

10003,Jordan,21

这样就可以完成字典到csv文件的写入了。

另外，如果想追加写入的话，可以修改文件的打开模式，即将open()函数的第二个参数改成a, 代码如下：

import csv

with open('data.csv', 'a') as csvfile: fieldnames = ['id', Fame', 'age']

writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 

writer.writerow({'id': '10004'» ' name': 'Durant', 'age': 22})

这样在上面的基础上再执行这段代码，文件内容便会变成：

id,name,age

10001,Mike,20

10002,Bob,22

10003,Jordan,21

10004,Durant,22

可见，数据被追加写入到文件中。

如果要写入中文内容的话，可能会遇到字符编码的问题，此时需要给open()参数指定编码格式。 比如，这里再写入一行包含中文的数据，代码需要改写如下：

import csv

with open('data.csv', 'a', encoding='utf-8') as csvfile: 

fieldnames = ['id', 'name', 'age']

writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 writer.writerow(('id,: '10005', 'name':'王伟,age': 22))

这里需要给open。函数指定编码，否则可能发生编码错误。

另外，如果接触过pandas等库的话，可以调用DataFrame对象的to_csv()方法来将数据写入CSV 文件中。

**2.**读取

我们同样可以使用csv库来读取CSV文件。例如，将刚才写入的文件内容读取出来，相关代码 如下：

```python
import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:

     reader = csv.reader(csvfile) for row in reader:

    print(row)
```

运行结果如下：

['id', 'name', 'age']

['10001', 'Mike', '20']

['10002', 'Bob', '22']

['10003', 'Jordan', '21']

['10004', 'Durant', '22']

['10005','王伟'，'22']

这里我们构造的是Reader对象，通过遍历输出了每行的内容，每一行都是一个列表形式。注意, 如果CSV文件中包含中文的话，还需要指定文件编码。

另外，如果接触过pandas的话，可以利用read_csv()方法将数据从CSV中读取出来，例如： 

import pandas as pd

df = pd.read_csv('data.csv')

print(df)



运行结果如下：

id name age

0 10001 Mike 20

1   10002 Bob 22

2   10003 Jordan 21

3   10004 Durant 22

4   10005 王伟 22

在做数据分析的时候，此种方法用得比较多，也是一种比较方便地读取CSV文件的方法。

本节中，我们了解了 CSV文件的写入和读取方式。这也是一种常用的数据存储方式，需要熟练掌握。

### 5.2数据库存储

#### 5.2.1关系型数据库存储

​       关系型数据库是基于关系模型的数据库，而关系模型是通过二维表来保存的，所以它的存储方式 就是行列组成的表，每一列是一个字段，每一行是一条记录。表可以看作某个实体的集合，而实体之 间存在联系，这就需要表与表之间的关联关系来体现，如主键外键的关联关系。多个表组成一个数据库，也就是关系型数据库。

关系型数据库有多种，如 SQLite、MySQL、Oracle、SQL Server, DB2 等。

**Mysql的存储**

1.准备工作下载mysql

相关链接

□官方网站：https://www.mysql.com/cn

□下载地址：https://www.mysql.com/cn/downloads

□中文教程：http://www.runoob.com/mysql/mysql-tutorial.html

2.连接数据库

里，首先尝试连接一下数据库。假设当前的MySQL运行在本地，用户名为root,密码为123456, 运行端口为3306,这里利用PyMySQL先连接MySQL,然后创建一个新的数据库，名字叫作spiders, 代码如下：

```
import pymysql

db = pymysql.connect(host='localhost',user='root', password:'123456', port=3306)

cursor = db.cursor()

cursor.execute('SELECT VERSION()')

data = cursor.fetchone()

print('Database version:', data)

cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")

db.close()

运行结果如下：

Database version: ('5.6.22',)
```

  这里通过PyMySQL的connect()方法声明一个MySQL连接对象db,此时需要传入MySQL运行 的host (即IP)。由于MySQL在本地运行，所以传入的是localhost。如果MySQL在远程运行，则 传入其公网IP地址。后续的参数user即用户名，password即密码，port即端口(默认为3306 )。

连接成功后，需要再调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句。这 里我们执行了两句SQL,直接用execute。方法执行即可。第一句SQL用于获得MySQL的当前版本， 然后调用fetchone。方法获得第一条数据，也就得到了版本号。第二句SQL执行创建数据库的操作， 数据库名叫作spiders,默认编码为UTF-8。由于该语句不是查询语句，所以直接执行后就成功创建了 数据库spiders.接着，再利用这个数据库进行后续的操作。

3.创建表

一般来说，创建数据库的操作只需要执行一次就好了。当然，我们也可以手动创建数据库。以后， 我们的操作都在spiders数据库上执行。

创建数据库后，在连接时需要额外指定一个参数db。

接下来，新创建一个数据表students,此时执行创建表的SQL语句即可。这里指定3个字段，结构如表5-1所示。

| 字段名 | 含 义 | 类  型  |
| ------ | ----- | ------- |
| id     | 学号  | varchar |
| name   | 姓名  | varchar |
| age    | 年龄  | int     |

创建该表的示例代码如下：

```python
import pymysql

db = pymysql.connect(host='localhost', user='root', password'123456', port=3306, db='spiders') 
cursor = db.cursor()

sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'

cursor.execute(sql)
db.close()
```

运行之后，我们便创建了一个名为students的数据表。

当然，为了演示，这里只指定了最简单的几个字段。实际上，在爬虫过程中，我们会根据爬取结果设计特定的字段。

4.插入数据

下一步就是向数据库中插入数据了。例如，这里爬取了一个学生信息，学号为20120001,名字为 Bob,年龄为20,那么如何将该条数据插入数据库呢？示例代码如下：

```python
import pymysql

id = '20120001'

user = 'Bob'

age = 20

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders') cursor = db.cursor()

sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'

try:

cursor.execute(sql, (id, user, age))

db.commit()

except:

db.rollback()

db.close()
```

这里首先构造了一个SQL语句，其Value值没有用字符串拼接的方式来构造，如：

sql = 'INSERT INTO students(id, name, age) values(' + id + ',' + name + ','+age+')'

这样的写法烦琐而且不直观，所以我们选择直接用格式化符％s来实现。有几个Value写几个％s, 我们只需要在execute。方法的第一个参数传入该SQL语句，Value值用统一的元组传过来就好了。 这样的写法既可以避免字符串拼接的麻烦，又可以避免引号冲突的问题。

之后值得注意的是，需要执行db对象的commit ()方法才可实现数据插入，这个方法才是真正将 语句提交到数据库执行的方法。对于数据插入、更新、删除操作，都需要调用该方法才能生效。

接下来，我们加了一层异常处理。如果执行失败，则调用rollback()执行数据回滚，相当于什么 都没有发生过。

这里涉及事务的问题。事务机制可以确保数据的一致性，也就是这件事要么发生了，要么没有发 生。比如插入一条数据，不会存在插入一半的情况，要么全部插入，要么都不插入，这就是事务的原 子性。另外，事务还有3个属性——一致性、隔离性和持久性。这4个属性通常称为ACID特性，具 体如下表所示。

| 原子性 | 事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做 |
| ------ | ------------------------------------------------------------ |
| 一致性 | 事务必须使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的 |
| 隔离性 | 事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事 务是隔离的，并发执行的各个事务之间不能互相干扰 |
| 持久性 | 持续性也称永久性(permanence ),指一个事务一旦提交，它对数据库中数据的改变就应该 是永久性的。接下来的其他操作或故障不应该对其有任何影响 |

插入、更新和删除操作都是对数据库进行更改的操作，而更改操作都必须为一个事务，所以这些 操作的标准写法就是：

```python
try:

	cursor.execute(sql) db.commit()

except:
	
	db.rollback()
```

这样便可以保证数据的一致性。这里的commit()和rollback()方法就为事务的实现提供了支持

上面数据插入的操作是通过构造SQL语句实现的，但是很明显，这有一个极其不方便的地方，比 如突然增加了性别字段gender,此时SQL语句就需要改成：

INSERT INTO students(id, name, age, gender) values(%s, %s, %s, %s)

相应的元组参数则需要改成：

(id, name, age, gender)

这显然不是我们想要的。在很多情况下，我们要达到的效果是插入方法无需改动，做成一个通用 方法，只需要传入一个动态变化的字典就好了。比如，构造这样一个字典：

{

'id'： 120120001',

'name': 'Bob',

'age': 20

}

然后SQL语句会根据字典动态构造，元组也动态构造，这样才能实现通用的插入方法。所以，这 里我们需要改写一下插入方法：

data = (

'id'： '20120001',

'name': 'Bob',

'age': 20

}

table = 'students'

keys = ', '.join(data.keys())

values =     .join(['%s'] * len(data))

sql = 'INSERT INTO {table)((keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

try:

​	if cursor.execute(sql, tuple(data.values())):

​	print('Successful')

​	db.commit()

except:

​	print('Failed')

​	db.rollback()

​	db.close()

这里我们传入的数据是字典，并将其定义为data变量。表名也定义成变量tableo接下来，就需 要构造一个动态的SQL语句了。

首先，需要构造插入的字段id、name和age。这里只需要将data的键名拿过来，然后用逗号分隔即可。所以’，'.join(data.keys())的结果就是id, name, age,然后需要构造多个%s当作占位符, 有几个字段构造几个即可。比如，这里有三个字段，就需要构造％s, %s, %s0这里首先定义了长度为 1的数组['%s'],然后用乘法将其扩充为['%s', '%s', '%s'],再调用join()方法,最终变成%s, %s, %s。 最后，我们再利用字符串的format()方法将表名、字段名和占位符构造出来。最终的SQL语句就被 动态构造成了：

INSERT INTO students(id, name, age) VALUES (%s, %s, %s)

最后，为execute()方法的第一个参数传入sql变量，第二个参数传入data的键值构造的元组,就可以成功插入数据了。

如此以来，我们便实现了传入一个字典来插入数据的方法，不需要再去修改SQL语句和插入操作了。

5.更新数据

数据更新操作实际上也是执行SQL语句，最简单的方式就是构造一个SQL语句，然后执行:

sql = ' UPDATE students SET age = %s WHERE name = %s 

try:

​	cursor.execute(sql, (25, 'Bob'))

​	db.commit()

except:

​	db.rollback()

​	db.close()

里同样用占位符的方式构造SQL,然后执行execute()方法，传入元组形式的参数，同样执行 commit()方法执行操作。如果要做简单的数据更新的话，完全可以使用此方法。

但是在实际的数据抓取过程中，大部分情况下需要插入数据，但是我们关心的是会不会出现重复 数据，如果出现了，我们希望更新数据而不是重复保存一次。另外，就像前面所说的动态构造SQL 的问题，所以这里可以再实现一种去重的方法，如果数据存在，则更新数据；如果数据不存在，则插 入数据。另外，这种做法支持灵活的字典传值。示例如下：

data = {

'id': '20120001', 'name': 'Bob', 'age': 21

}

table = 'students'

keys = ', '.join(data.keys())

values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO (table)((keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)

update = ','.join([" (key} = %s".format(key=key) for key in data])

sql += update

try:

​	if cursor.execute(sql, tuple(data.values())*2):

​	print('Successful')

​	db.commit()

except:

​	print('Failed')

​	db.rollback()

​	db.close()

这里构造的SQL语句其实是插入语句，但是我们在后面加了 ON DUPLICATE KEY UPDATE这行代 码的意思是如果主键已经存在，就执行更新操作。比如，我们传入的数据id仍然为20120001,但是 年龄有所变化，由20变成了 21,此时这条数据不会被插入，而是直接更新id为20120001的数据。 完整的SQL构造出来是这样的：

INSERT INTO students(id, name, age) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s 这里就变成了 6个％$。所以在后面的execute()方法的第二个参数元组就需要乘以2变成原来的 2倍。

如此一来，我们就可以实现主键不存在便插入数据，存在则更新数据的功能了。

6.删除数据

删除操作相对简单，直接使用DELETE语句即可，只是需要指定要删除的目标表名和删除条件，而 且仍然需要使用db的commit。方法才能生效。示例如下：

table = 'students'

condition = 'age > 20'

sql = 'DELETE FROM {table} WHERE (condition)'.format(table=table, condition=condition)

try:

​	cursor.execute(sql)

​	db.commit()

except:

​	db.rollback()

​	db.close()

因为删除条件有多种多样，运算符有大于、小于、等于、LIKE等，条件连接符有AND、OR等，所 以不再继续构造复杂的判断条件。这里直接将条件当作字符串来传递，以实现删除操作。

7.查询数据

说完插入、修改和删除等操作，还剩下非常重要的一个操作，那就是查询。查询会用到SELECT 语句，示例如下：

sql = 'SELECT * FROM students WHERE age >= 20'

try:

​	cursor.execute(sql)

​	print('Count:', cursor.rowcount)

​	one = cursor.fetchone()

​	print('One:', one)

​	results = cursor.fetchall()

​	print('Results:', results)

​	print('Results Type:', type(results))

​	for row in results:

​		print(row)

except:

​	print('Error')

运行结果如下：

Count: 4

One: ('20120001', 'Bob', 25)

Results: (('20120011', 'Mary', 21), ('20120012', 'Mike', 20), ('20120013', 'James', 22))

Results Type: <class 'tuple'>

('20120011', 'Mary', 21)

('20120012', 'Mike', 20)

('20120013', 'James', 22)

这里我们构造了一条SQL语句，将年龄20岁及以上的学生查询出来，然后将其传给execute() 方法。注意，这里不再需要db的commit ()方法。接着，调用cursor的rowcount属性获取查询结果的 条数，当前示例中是4条。

然后我们调用了 fetchone。方法，这个方法可以获取结果的第一条数据，返回结果是元组形式， 元组的元素顺序跟字段一一对应，即第一个元素就是第一个字段id,第二个元素就是第二个字段name, 以此类推。随后，我们又调用了 fetchall()方法，它可以得到结果的所有数据。然后将其结果和类型 打印出来，它是二重元组，每个元素都是一条记录，我们将其遍历输出出来。

但是这里需要注意一个问题，这里显示的是3条数据而不是4条，fetchall。方法不是获取所有 数据吗？这是因为它的内部实现有一个偏移指针用来指向查询结果，最开始偏移指针指向第一条数 据，取一次之后，指针偏移到下一条数据，这样再取的话，就会取到下一条数据了。我们最初调用了 一次fetchone。方法，这样结果的偏移指针就指向下一条数据，fetchall。方法返回的是偏移指针指 向的数据一直到结束的所有数据，所以该方法获取的结果就只剩3个了。

此夕卜，我们还可以用while循环加fetchone()方法来获取所有数据，而不是用fetchallO全部一 起获取出来。fetchall()会将结果以元组形式全部返回，如果数据量很大，那么占用的开销会非常高。 因此，推荐使用如下方法来逐条取数据：

sql = 'SELECT * FROM students WHERE age >= 20'

try:

​	cursor.execute(sql)

​	print('Count:', cursor.rowcount)

​	row = cursor.fetchone()

while row:

​	print('Row:1, row)

​	row = cursor.fetchone()

except:

​	print('Error')

这样每循环一次，指针就会偏移一条数据，随用随取，简单高效。

本节中，我们介绍了如何使用PyMySQL操作MySQL数据库以及一些SQL语句的构造方法，后面会在实战案例中应用这些操作来存储数据。

#### 5.2.2非关系型数据库存储

NoSQL,全称Not Only SQL,意为不仅仅是SQL,泛指非关系型数据库。NoSQL是基于键值对 的，而且不需要经过SQL层的解析，数据之间没有耦合性，性能非常高。

非关系型数据库又可细分如下。

□键值存储数据库：代表有Redis, Voldemort和Oracle BDB等。

□列存储数据库：代表有Cassandra, HBase和Riak等。

□文档型数据库：代表有CouchDB和MongoDB等。

□图形数据库：代表有Neo4J、InfoGrid和Infinite Graph等。

对于爬虫的数据存储来说，一条数据可能存在某些字段提取失败而缺失的情况，而且数据可能随时调整。另外，数据之间还存在嵌套关系。如果使用关系型数据库存储，一是需要提前建表，二是如果存在数据嵌套关系的话，需要进行序列化操作才可以存储，这非常不方便。如果用了非关系型数据库，就可以避免一些麻烦，更简单高效。

本节中，我们主要介绍MongoDB的数据存储操作。

MongoDB 存储

MongoDB是由C++语言编写的非关系型数据库，是一个基于分布式文件存储的开源数据库系统， 其内容存储形式类似JSON对象，它的字段值可以包含其他文档、数组及文档数组，非常灵活。在这 —•节中，我们就来看看Python 3下MongoDB的存储操作。

1.准备工作

在开始之前，请确保已经安装好了 MongoDB并启动了其服务，并且安装好了 Python的PyMongo 库。

 相关链接

□官方网站：https://www.mongodb.com

□官方文档：https://docs.mongodb.com

□ GitHub: https://github.com/mongodb

□中文教程：http://www.runoob.com/mongodb/mongodb-tutorial.html

2.连接MongoDB

​    连接MongoDB时，我们需要使用PyMongo库里面的MongoClient。一般来说，传入MongoDB 的IP及端口即可，其中第一个参数为地址host,第二个参数为端口 port (如果不给它传递参数，默 认是 27017)：

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

这样就可以创建MongoDB的连接对象了。

另外，MongoClient的第一个参数host还可以直接传入MongoDB的连接字符串，它以mongodb 开头，例如：

client = MongoClient('mongodb://localhost:27017/')

这也可以达到同样的连接效果。

3.指定数据库

MongoDB中可以建立多个数据库，接下来我们需要指定操作哪个数据库。这里我们以test数据库 为例来说明，下一步需要在程序中指定要使用的数据库：

db = client.test

这里调用client的test属性即可返回test数据库。当然，我们也可以这样指定：

db = client['test']

这两种方式是等价的.

4.指定集合

MongoDB的每个数据库又包含许多集合(collection),它们类似于关系型数据库中的表。

下一步需要指定要操作的集合，这里指定一个集合名称为studentSo与指定数据库类似，指定集 合也有两种方式：

collection = db.students

collection = db['students']

这样我们便声明了一个Collection对象。

5.插入数据

接下来，便可以插入数据了。对于students这个集合，新建一条学生数据，这条数据以字典形式 表不:

student = {

'id': '20170101',

'name1: 'Jordan',

'age': 20,

'gender': 'male'

}

这里指定了学生的学号、姓名、年龄和性别。接下来，直接调用collection的insert。方法即可 插入数据，代码如下：

result= collection.insert(student)

print(result)

在MongoDB中，每条数据其实都有一个一id属性来唯一标识。如果没有显式指明该属性,MongoDB 会自动产生一个Objectld类型的id属性。insert。方法会在执行后返回id值。

运行结果如下：

5932a68615c26O6814c91f3d

当然，我们也可以同时插入多条数据，只需要以列表形式传递即可，示例如下：

student1 = {

'id': '20170101',

'name': 'Jordan',

'age': 20,

'gender': 'male'

}

student2 = {'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}

result = collection.insert([student1, student2])

print(result)



返回结果是对应的_id的集合：

[ObjectldC5932a8O115c26O6a59e8aO48'), Objectld('5932a8O115c26O6a59e8aO49')]

实际上，在PyMongo3.x版本中，官方已经不推荐使用insert。方法了。当然，继续使用也没有 什么问题。官方推荐使用insert_one()和insert_many()方法来分别插入单条记录和多条记录，示例 如下：

student = {

'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}

result = collection.insert_one(student)

print(result)

print(result.inserted_id)

运行结果如下：

<pymongo.results.InsertOneResult object at OxlOd68b558>

5932abOfl5c26O6fOclcf6c5

与insert()方法不同，这次返回的是InsertOneResult对象，我们可以调用其inserted_id属性获取_id

对于insert_many()方法，我们可以将数据以列表形式传递，示例如下：

student1 = {

'id': '20170101',

'name': 'Jordan',

'age': 20,

'gender': 'male'

}

student2 = {

'id': '20170202',

'name': 'Mike',

'age': 21,

'gender': 'male'

}

result = collection.insert_many([student1, student2])

print(result)

print(result.inserted_ids)

运行结果如下：

<pymongo.results.InsertManyResult object at OxlOldea558>

[ObjectldC5932abf415c26O7O83d3b2ac'), Objectld('5932abf415c26O7O83d3b2ad')]

该方法返回的类型是InsertManyResult,调用inserted_ids属性可以获取插入数据的_id列表。

5.删除

删除操作比较简单，直接调用remove()方法指定删除的条件即可，此时符合条件的所有数据均会 被删除。示例如下：

result = collection.remove({'name': 'Kevin'})

print(result)

运行结果如下：

('ok': 1, 'n': 1}

另外，这里依然存在两个新的推荐方法----- delete_one()和delete_many()示例如下：

result = collection.delete_one({'name': 'Kevin'})

print(result)

print(result.deleted_count)

result = collection.delete_many(('age': ('$lt': 25}})

print(result.deleted_count)

运行结果如下：

<pymongo.results.DeleteResult object at 0xl0e6ba4c8>

delete_one()即删除第一条符合条件的数据，deletejnany。即删除所有符合条件的数据。它们的 返回结果都是DeleteResult类型，可以调用deleted_count属性获取删除的数据条数。

## 六.selenium的使用

  Selenium是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击、下拉等操作, 同时还可以获取浏览器当前呈现的页面的源代码，做到可见即可爬。对于一些JavaScript动态渲染的 页面来说，此种抓取方式非常有效。本节中，就让我们来感受一下它的强大之处吧。

### 6.1selenium的使用

#### 1.准备工作

本节以Chrome为例来讲解Selenium的用法。在开始之前，请确保已经正确安装好了 Chrome浏览器并配置好了 ChromeDriver。另外，还需要正确安装好Python的Selenium库，Chrome下载网址http://npm.taobao.org/mirrors/chromedriver/。下载对应版本即可。

配置Chrome Driver的方法：确定你的chrome版本，并下载对应版本的chromedriver

问题1：如何查看自己chrome的版本？如下图所示：

点击帮助------关于Google Chrome

![](C:\Users\javac\Desktop\class\checkbanben.PNG)

版本如图所示

![banben](C:\Users\javac\Desktop\class\banben.png)

#### 2.基本使用

准备工作做好之后，首先来大体看一下Selenium有一些怎样的功能。示例如下：

```python
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
browser = webdriver.Chrome()
try:
browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('Python')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
finally:
browser.close()

```

运行代码后发现，会自动弹出一个Chrome浏览器。浏览器首先会跳转到百度，然后在搜索框中 输入Python,接着跳转到搜索结果页。

搜索结果加载出来后，控制台分别会输出当前的URL、当前的Cookies和网页源代码：

> https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=8c2f680000001fed&rsv_t=983cpiEcErX0%2BN%2Frs%2FYfZsn03bLmmllVHu9vLXOVF1SHr%2F2Ufmmg%2BiyACyA&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug2=0&rsv_btype=i&inputT=191&rsv_sug4=190
> [{'domain': 'www.baidu.com', 'path': '/', 'value': '0_0_0_0_0_1_0_0_0_1_1_0_0_0_0_0_0_0_1621837950%7C1%230_0_1621837950%7C1', 'expiry': 1653373950, 'secure': False, 'name': 'COOKIE_SESSION', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': 'ao8ka1al2h0k8l44cs1gami3u0r', 'expiry': 1621841550, 'secure': False, 'name': 'BA_HECTOR', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': '6', 'secure': False, 'name': 'PSINO', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': '1621837948', 'expiry': 3769321595, 'secure': False, 'name': 'PSTM', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': 'FDD970FE7DAA3CF126C3241DCBF6FF6C', 'expiry': 3769321595, 'secure': False, 'name': 'BIDUPSID', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': 'FDD970FE7DAA3CF1DA2D60AF86DEFA13:FG=1', 'expiry': 1653373948, 'secure': False, 'name': 'BAIDUID', 'httpOnly': False}, {'domain': 'www.baidu.com', 'path': '/', 'value': '1', 'secure': False, 'name': 'BD_CK_SAM', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': '', 'secure': False, 'name': 'H_PS_PSSID', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': 'B490B5EBF6F3CD402E515D22BCDA1598', 'expiry': 1621924350, 'secure': False, 'name': 'BDORZ', 'httpOnly': False}, {'domain': '.baidu.com', 'path': '/', 'value': '0', 'secure': False, 'name': 'delPer', 'httpOnly': False}, {'domain': 'www.baidu.com', 'path': '/', 'value': '1c47XopZWpAdXN6D143LQpL3OYbNXCpOQuwrnOZB%2B1vcuUpO3u6ghcJ07JE', 'expiry': 1621840542, 'secure': False, 'name': 'H_PS_645EC', 'httpOnly': False}, {'domain': 'www.baidu.com', 'path': '/', 'value': '12314753', 'expiry': 1622701948, 'secure': False, 'name': 'BD_UPN', 'httpOnly': False}, {'domain': 'www.baidu.com', 'path': '/', 'value': '1', 'secure': False, 'name': 'BD_HOME', 'httpOnly': False}]

源代码过长，在此省略。可以看到，我们得到的当前URL、Cookies和源代码都是浏览器中的真 实内容。

所以说，如果用Selenium来驱动浏览器加载网页的话，就可以直接拿到JavaScript渲染的结果了， 不用担心使用的是什么加密系统。

下面来详细了解一下Selenium的用法。

#### 3.声明浏览器对象

Selenium支持非常多的浏览器，如Chrome、Firefbx、Edge等，还有Android, BlackBerry等手机 端的浏览器。另外，也支持无界面浏览器PhantomJSo

此外，我们可以用如下方式初始化：

```python
from selenium import webdriver

browser = webdriver.Chrome()

browser = webdriver.Firefox()

browser = webdriver.Edge()

browser = webdriver.PhantomJS()

browser = webdriver.Safari()
```

这样就完成了浏览器对象的初始化并将其赋值为browser对象。接下来，我们要做的就是调用 browser对象，让其执行各个动作以模拟浏览器操作。

#### 4.访问页面

我们可以用get()方法来请求网页，参数传入链接URL即可。比如，这里用get()方法访问淘宝, 然后打印出源代码，代码如下：

```python
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.taobao.com')

print(browser.page_source)

browser.close()
```

运行后发现，弹出了 Chrome浏览器并且自动访问了淘宝，然后控制台输出了淘宝页面的源代码， 随后浏览器关闭。

通过这几行简单的代码，我们可以实现浏览器的驱动并获取网页源码，非常便捷。

#### 5.查找节点

  Selenium可以驱动浏览器完成各种操作，比如填充表单、模拟点击等。比如，我们想要完成向某 个输入框输入文字的操作，总需要知道这个输入框在哪里吧？而Selenium提供了一系列查找节点的方 法，我们可以用这些方法来获取想要的节点，以便下一步执行一些动作或者提取信息。

•单个节点

比如，想要从淘宝页面中提取捜索框这个节点，首先要观察它的源代码，如下图所示。

![taobao](C:\Users\javac\Desktop\class\taobao.png)

可以发现，它的id是q, name也是q。此外，还有许多其他属性，此时我们就可以用多种方式获取它了。比如，find_element_by_name()是根据name值获取，find_element_by_id()是根据 id 获取。 另外，还有根据XPath、CSS选择器等获取的方式。

我们用代码实现一下：

```python
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
```

这里我们使用3种方式获取输入框，分别是根据ID、CSS选择器和XPath获取，它们返回的结果 完全一致。运行结果如下：

<selenium.webdriver.remote.webelement.WebElement (session="dd34b9bca15d6a21117e5e23d64d7bf2", element="fb4da1db-4c61-4fb1-9b5a-d7576d31301e")>

 <selenium.webdriver.remote.webelement.WebElement (session="dd34b9bca15d6a21117e5e23d64d7bf2", element="fb4da1db-4c61-4fb1-9b5a-d7576d31301e")> 

<selenium.webdriver.remote.webelement.WebElement (session="dd34b9bca15d6a21117e5e23d64d7bf2", element="fb4da1db-4c61-4fb1-9b5a-d7576d31301e")>

可以看到，这3个节点都是WebElement类型，是完全一致的。

这里列出所有获取单个节点的方法:

- find_element_by_id 
- find_element_by_name
-  find_element_by_xpath
-  find_element_by_link_text
-  find_element_by_partial_link_text
-  find_element_by_tag_name
-  find_element_by_class_name 
- find_element_by_css_selector

另外，Selenium还提供了通用方法find_element(),它需要传入两个参数：查找方式By和值。实 际上，它就是find_element_by_id()这种方法的通用函数版本，比如find_element_by_id(id)就等价 于find_element(By.ID, id),二者得到的结果完全一致。我们用代码实现一下：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()
```

实际上，这种查找方式的功能和上面列举的查找函数完全一致，不过参数更加灵活。

•多个节点

如果查找的目标在网页中只有一个，那么完全可以用find_element()方法。但如果有多个节点， 再用find_element()方法查找，就只能得到第一个节点了。如果要查找所有满足条件的节点，需要用 find_elements()这样的方法。注意，在这个方法的名称中，element多了一个s,注意区分。

比如，要查找淘宝左侧导航条的所有条目，如下图所示

![taobaoelements](C:\Users\javac\Desktop\class\taobaoelements.png)

就可以这样来实现：

```python
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")

browser.get('https://www.taobao.com')

lis = browser.find_elements_by_css_selector('.service-bd li')

print(lis)

browser.close()
```

运行结果如下：

[<selenium.webdriver.remote.webelement.WebElement (session="db0e317d5f7f7f7c37ffa3cb3ed08a3f", element="cd1cfff1-7c78-4544-8582-f92499f54766")>, <selenium.webdriver.remote.webelement.WebElement (session="db0e317d5f7f7f7c37ffa3cb3ed08a3f", element="b580fe50-113e-4f28-bfde-d995305f99e8")>, <selenium.webdriver.remote.webelement.WebElement (session="db0e317d5f7f7f7c37ffa3cb3ed08a3f", element="bbe4013d-8016-420a-8960-44be8a664bbb")>, <selenium.webdriver.remote.webelement.WebElement (session="db0e317d5f7f7f7c37ffa3cb3ed08a3f", element="d125e716-07b4-45e4-8efc-49baff1c03aa")>, <selenium.webdriver.remote.webelement.WebElement (session="db0e317d5f7f7f7c37ffa3cb3ed08a3f", element="c5e221fe-53d1-47cd-95d6-94112c44f6dc")>, <selenium.webdriver.remote.webelement.WebElement (session="db0e317d5f7f7f7c37ffa3cb3ed08a3f", element="5bc65a44-9c11-4a04-af89-d29bd5335bf5")>, <selenium.webdriver.remote.webelement.WebElement (session="db0e317d5f7f7f7c37ffa3cb3ed08a3f", element="9d650777-b19d-45f5-a9d6-dfcfe5920d63")>]

这里简化了输出结果，中间部分省略

可以看到，得到的内容变成了列表类型，列表中的每个节点都是WebElement类型。

也就是说，如果我们用find_element()方法，只能获取匹配的第一个节点，结果是WebElement类 型。如果用find_elements()方法，则结果是列表类型，列表中的每个节点是WebElement类型。

这里列出所有获取多个节点的方法：

- find_elements_by_id 
- find_elements_by_name
-  find_elements_by_xpath
-  find_elements_by_link_text
-  find_elements_by_partial_link_text
-  find_elements_by_tag_name
-  find_elements_by_class_name 
- find_elements_by_css_selector

#### **6**.节点交互

Selenium可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些动作。比较常见 的用法有：输入文字时用send_keys()方法，清空文字时用clear()方法，点击按钮时用click()方法。 示例如下：

```python
from selenium import webdriver

import time

browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")

browser.get('https://www.taobao.com') 

input = browser.find_element_by_id('q') 

input.send_keys('iPhone') 

time.sleep(1) 

input.clear()

input.send_keys('iPad')

button = browser.find_element_by_class_name('btn-search') 

button.click()
```

这里首先驱动浏览器打开淘宝，然后用find_element_by_id()方法获取输入框，然后用send_keys() 方法输入iPhone文字，等待一秒后用clear()方法清空输入框，再次调用send_keys()方法输入iPad 文字，之后再用find_element_by_class_name()方法获取搜索按钮，最后调用click。方法完成搜索动作。

通过上面的方法，我们就完成了一些常见节点的动作操作，更多的操作可以参见官方文档的交互 动作介绍:[http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement](http://selenium-python.readthedocs.io/api.html%23module-selenium.webdriver.remote.webelement。)

#### **7.**动作链

在上面的实例中，一些交互动作都是针对某个节点执行的。比如，对于输入框，我们就调用它的输入文字和清空文字方法；对于按钮，就调用它的点击方法。其实，还有另外一些操作，它们没有特 定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。

比如，现在实现一个节点的拖曳操作，将某个节点从一处拖曳到另外一处，可以这样实现：

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
```

首先，打开网页中的一个拖曳实例，然后依次选中要拖曳的节点和拖曳到的目标节点，接着声明 Actionchains对象并将其赋值为actions变量，然后通过调用actions变量的drag_and_drop()方法， 再调用perform。方法执行动作，此时就完成了拖曳操作.

更多的动作链操作可以参考官方文档：

[http://selenium-python.readthedocs.io/api.html#module- selenium.webdriver.common.actionchainso](http://selenium-python.readthedocs.io/api.html%23module-selenium.webdriver.common.actionchainso)

#### **8.**执行 JavaScript

对于某些操作，Selenium API并没有提供。比如，下拉进度条，它可以直接模拟运行JavaScript, 此时使用execute_script()方法即可实现，代码如下：

```python
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
```

这里就利用execute_script()方法将进度条下拉到最底部，然后弹出alert提示框。

所以说有了这个方法，基本上API没有提供的所有功能都可以用执行JavaScript的方式来实现了。

#### **9.**获取节点信息

前面说过，通过page_source属性可以获取网页的源代码，接着就可以使用解析库(如正则表达式、Beautiful Soup pyquery 等)来提取信息了。

不过，既然Selenium已经提供了选择节点的方法，返回的是WebElement类型，那么它也有相关 的方法和属性来直接提取节点信息，如属性、文本等。这样的话，我们就可以不用通过解析源代码来 提取信息了，非常方便。

接下来，就看看通过怎样的方式来获取节点信息吧。

**获取属性**

我们可以使用get_attribute()方法来获取节点的属性，但是其前提是先选中这个节点，示例如下：

```
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('Popover1-toggle')
print(logo)
print(logo.get_attribute('class'))
```

运行之后,程序便会驱动浏览器打开知乎页面，然后获取知乎的logo节点，最后打印出它的class。

控制台的输出结果如下：

<selenium.webdriver.remote.webelement.WebElement (session="680b81fc8a5c7c231c669465f1036471", element="2374457f-f5d0-4fcb-9957-0ab8a23710e4")>
Input

通过get_attribute()方法，然后传入想要获取的属性名，就可以得到它的值了。

**获取文本值**

每个WebElement节点都有text属性，直接调用这个属性就可以得到节点内部的文本信息，这相 当于 Beautiful Soup 的 get_text()方法、pyquery 的 text()方法，示例如下：

```python
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_xpath('//[@id="root"]/div/div[2]/header/div[1]/div[2]/div/div/button[1]')
print(logo)
print(logo.text)
```

这里依然先打开知乎页面，然后获取“提问”按钮这个节点，再将其文本值打印出来。

控制台的输出结果如下：

<selenium.webdriver.remote.webelement.WebElement (session="4b7676fc9df76da4d59f93177fc2b3ee", element="a5ce66fd-0209-47b2-b344-ee0c182cca0d")>
登录

**获取id、位置、标签名和大小**

另外，WebElement节点还有一些其他属性，比如id属性可以获取节点id, location属性可以获 取该节点在页面中的相对位置，tag_name属性可以获取标签名称，size属性可以获取节点的大小，也 就是宽高，这些属性有时候还是很有用的。示例如下：

```python
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('Input')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
```

结果如下

0d276728-f5c9-42ad-b784-ded632b7b9ea
{'x': 407, 'y': 14}
input
{'width': 354, 'height': 24}

这里首先获得“提问”按钮这个节点，然后调用其id，location，tag_name，size等属性来获取对应的属性值

#### 10.切换 Frame

我们知道网页中有一种节点叫作iframe,也就是子Frame,相当于页面的子页面，它的结构和外 部网页的结构完全一致。Selenium打开页面后，它默认是在父级Frame里面操作，而此时如果页面中 还有子Frame,它是不能获取到子Frame里面的节点的。这时就需要使用switch_to.frame。方法来切 换Frame。示例如下：

```python
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

```

这里还是以前面演示动作链操作的网页为实例，首先通过switch_to.frame()方法切换到子Frame 里面，然后尝试获取父级Frame里的logo节点(这是不能找到的)，如果找不到的话，就会抛出 NoSuchElementException异常，异常被捕捉之后，就会输出NO LOGO。接下来，重新切换回父级Frame, 然后再次重新获取节点，发现此时可以成功获取了。

所以，当页面中包含子Frame时，如果想获取子Frame中的节点，需要先调用switch_to.frame。 方法切换到对应的Frame,然后再进行操作。

#### **11**.延时等待

在Selenium中，get()方法会在网页框架加载结束后结束执行，此时如果获取page_source,可能 并不是浏览器完全加载完成的页面，如果某些页面有额外的Ajax请求，我们在网页源代码中也不一 定能成功获取到。所以，这里需要延时等待一定时间，确保节点已经加载出来。

这里等待的方式有两种：一种是隐式等待，一种是显式等待。

**•隐式等待**

当使用隐式等待执行测试的时候，如果Selenium没有在DOM中找到节点，将继续等待，超出设 定时间后，则抛出找不到节点的异常。换句话说，当查找节点而节点并没有立即出现的时候，隐式等 待将等待一段时间再查找D0M,默认的时间是0。示例如下：

```python
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('Input')
print(input)
```

这里我们用implicitly_wait()方法实现了隐式等待。

**・显式等待**

隐式等待的效果其实并没有那么好，因为我们只规定了一个固定时间，而页面的加载时间会受到 网络条件的影响。

这里还有一种更合适的显式等待方法，它指定要查找的节点，然后指定一个最长等待时间。如果 在规定时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点， 则抛出超时异常。示例如下：

```python
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")

browser.get('https://www.taobao.com/')

wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
```

这里首先引入WebDriverWait这个对象，指定最长等待时间，然后调用它的until。方法，传入要 等待条件expected_conditionso比如，这里传入了 presence_of_element_located这个条件，代表节 点出现的意思，其裘数是节点的定位元组，也就是ID为q的节点搜索框。

这样可以做到的效果就是，在10秒内如果ID为q的节点(即搜索框)成功加载出来，就返回该 节点；如果超过10秒还没有加载出来，就抛出异常。

对于按钮，可以更改一下等待条件，比如改为element_to_be_clickable,也就是可点击，所以查 找按钮时查找CSS选择器为.btn-search的按钮，如果10秒内它是可点击的，也就是成功加载出来了， 就返回这个按钮节点；如果超过10秒还不可点击，也就是没有加载出来，就抛出异常。

运行代码，在网速较佳的情况下是可以成功加载出来的。

控制台的输出如下：

<selenium.webdriver.remote.webelement.WebElement (session="0dfe4a1eb4bbde7e1a5f66fc0b1395a7", element="bab549cb-cf51-4755-8a0b-79360547a375")>

 <selenium.webdriver.remote.webelement.WebElement (session="0dfe4a1eb4bbde7e1a5f66fc0b1395a7", element="3eabfb30-4bb4-45db-a1cf-b85b2736f1ed")>

可以看到，控制台成功输出了两个节点，它们都是WebElement类型。

如果网络有问题，10秒内没有成功加载，那就抛出Timeout Except ion异常.

关于等待条件，其实还有很多，比如判断标题内容，判断某个节点内是否出现了某文字等。表7-1 列出了所有的等待条件。

| 等待条件                               | 含 义                                            |
| -------------------------------------- | ------------------------------------------------ |
| title_is                               | 标题是某内容                                     |
| title_contains                         | 标题包含某内容                                   |
| presence_of_element_located            | 节点加载出来，传入定位元组，如(By.ID, 'p')       |
| visibility_of_element_located          | 节点可见，传入定位元组                           |
| visibility_of                          | 可见，传入节点对象                               |
| presence_of_all_elements_located       | 所有节点加载出来                                 |
| text_to_be_present_in_element          | 某个节点文本包含某文字                           |
| text_to_be_present_in_element_value    | 某个节点值包含某文字                             |
| frame_to_be_available_and_switch_to_it | 加载并切换                                       |
| invisibility_of_element_located        | 节点不可见                                       |
| element_to_be_clickable                | 节点可点击                                       |
| staleness_of                           | 判断一个节点是否仍在D0M,可判断页面是否已经刷新   |
| element_to_be_selected                 | 节点可选择，传节点对象                           |
| element_located_to_be_selected         | 节点可选择，传入定位元组                         |
| element_selection_state_to_be          | 传入节点对象以及状态，相等返回True,否则返回False |
| element_located_selection_state_to_be  | 传人定位元组以及状态，相等返回True,否则返回False |
| alert_is_present                       | 是否出现警告                                     |

于更多等待条件的参数及用法，可以参考官方文档：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expectedconditionso

#### 12.前进和后退

平常使用浏览器时都有前进和后退功能，Selenium也可以完成这个操作，它使用back。方法后退, 使用forward()方法前进。示例如下：

```python
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
```

这里我们连续访问3个页面，然后调用back()方法回到第二个页面，接下来再调用forward()方 法又可以前进到第三个页面。

#### 13.Cookies

使用Selenium,还可以方便地对Cookies进行操作，例如获取、添加、删除Cookies等。示例如下:

```python
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihii.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
```

首先，我们访问了知乎。加载完成后，浏览器实际上已经生成Cookies 了。接着，调用get_cookies() 方法获取所有的Cookieso然后，我们添加一个Cookie,这里传入一个字典，有name、domain和value 等内容。接下来，再次获取所有的Cookieso可以发现，结果就多了这一项新加的Cookieo最后，调 用delete_all_cookies()方法删除所有的Cookies0再重新获取，发现结果就为空了。

控制台的输出如下：

[('secure': False, 'value':

'"NGMOZTM5NDAwMWEyNDQwNDk5ODlkZWV3OTkxY2lONDY=114916040911236e3429Oa6f4O7bfbb517888849ea5O9ac366dO"', 'domain': '.zhihu.com', 'path':        , 'httpOnly1: False, 'name': 'l_cap_id', 'expiry': 1494196091.403418}]

[('secure': False, 'value': 'germey', 'domain': '.www.zhihu.com', 'path':             , 'httpOnly': False, 'name':

Same'}, {'secure': False, 'value':

'"NGMOZTM5NDAwMWEyNDQwNDk5ODlkZWY3OTkxY2lONDY=114916040911236e3429Oa6f4O7bfbb517888849ea5O9ac366dO"', 'domain': ' .zhihu.com', 'path':       'httpOnly': False, 'name': 'l_cap_id', 'expiry': 1494196091.403418)]

[]

#### 14.选项卡管理

在访问网页的时候，会开启一个个选项卡。在Selenium中，我们也可以对选项卡进行操作。示例 如下：

```python
import time

from selenium import webdriver

browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")

browser.get('https://www.baidu.com')

browser.execute_script('window.open()')

print(browser.window_handles)

browser.switch_to_window(browser.window_handles[1])

browser.get('https://www.taobao.com')

time.sleep(1)

browser.switch_to_window(browser.window_handles[0])

browser.get('https://python.org')
```

控制台的输出如下：

['CDwindow-E6A46C2B2E2A81D776C6B744848D7EDA', 'CDwindow1FB2C830052948523FC844552566DAC3']

首先访问了百度，然后调用了 execute_script()方法，这里传入window.open()这个JavaScript语 句新开启一个选项卡。接下来，我们想切换到该选项卡。这里调用window_handles属性获取当前开启 的所有选项卡，返回的是选项卡的代号列表。要想切换选项卡，只需要调用switch_to_window()方法 即可，其中参数是选项卡的代号。这里我们将第二个选项卡代号传入，即跳转到第二个选项卡，接下 来在第二个选项卡下打开一个新页面，然后切换回第一个选项卡重新调用switch_to_window()方法， 再执行其他操作即可。

#### 15.异常处理

在使用Selenium的过程中，难免会遇到一些异常，例如超时、节点未找到等错误，一旦岀现此类错误，程序便不会继续运行了。这里我们可以使用try except 语句来捕获各种异常。

首先，演示一下节点未找到的异常，示例如下：

```python
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
browser.get('https://www.baidu.com')
browser.find_element_by_id('hello')
```

这里首先打开百度页面，然后尝试选择一个并不存在的节点，此时就会遇到异常。 运行之后控制台的输出如下：

selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="hello"]"}

可以看到，这里抛出了 NoSuchElementException异常，这通常是节点未找到的异常。为了防止程 序遇到异常而中断，我们需要捕获这些异常，示例如下：

```python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
browser = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
```

这里我们使用try except来捕获各类异常。比如，我们对find_element_by_id()查找节点的方法 捕获NoSuchElementException异常，这样一旦出现这样的错误，就进行异常处理，程序也不会中断了。

控制台的输出如下：

No Element

关于更多的异常类，可以参考官方文档：[http://selenium-python.readthedocs.io/api.html#module- selenium.common.exceptions。](http://selenium-python.readthedocs.io/api.html%23module-selenium.common.exceptions。)

现在，我们基本对Selenium的常规用法有了大体的了解。使用Selenium,处理JavaScript不再是难事。

### 七.验证码的识别

​       目前，许多网站采取各种各样的措施来反爬虫，其中一个措施便是使用验证码 随着技术的发展，验证码的花样越来越多 验证码最初是几个数字组合的简单的图形验证码，后来加入了英文字母和混淆曲线，有的网站还可能看到中文字符的验证码，这使得识别愈发困难后来 12306 验证码的归现使得行为验证码开始发展起来，用过 12306 的用户肯定多少为它的验证码头疼过 我们需要识别文字，点击与文字描述相符的图片验证码完全正确，验证才能通过 现在这种交互式验证码越来越多，如极验滑动验证码需要滑动拼合滑块才可以完成验证，点触验证码需要完全点击正确结果才可 完成验证，另外还有滑动宫格验证码、计算题验证码等验证码变得越来越复杂，爬虫的工作也变得愈发艰难 有时候我们必须通过验证码的验证才可以访问页面 本章就专门针对验证码的识别做统一讲解本章涉及的验证码有普通图形验证码、滑动验证码、点触验证码、这些验证码识别的方式和思路各有不同 了解这几个验证码的识别方式之后，我们可以举 ，用类似的方法识别其他类型验证码



#### 7.1图片验证码的识别

我们首先识别最简单的一种验证码，即图形验证码。这种验证码最早出现，现在也很常见，一般 由4位字母或者数字组成。例如，中国知网的注册页面有类似的验证码，链接为http://my.cnki.net/elibregister/commonRegister.aspx  页面如下图所示

![zhiwang](C:\Users\javac\Desktop\class\zhiwang.png)

表单的最后一项就是图形验证码，我们必须完全正确输入图中的字符才可以完成注册。

**1.**  本节目标

以知网的验证码为例，讲解利用OCR技术识别图形验证码的方法。

**2.**  准备工作

识别图形验证码需要库tesserocr。

 相关链接

□   tesserocr GitHub: https://github.com/sirfz/tesserocr                             1

□   tesserocr PyPI: https://pypi.python.org/pypi/tesserocr

□   tesseract 下载地址：http://digi.bib.uni-mannheim.de/tesseract

□   tesseract GitHub: https://github.com/tesseract-ocr/tesseract

□   tesseract 语言包：https://github.com/tesseract-ocr/tessdata

□   tesseract 文档:https://github.com/tesseract-ocr/tesseract/wiki/Documentation

在Windows下，首先需要下载tesseract,它为tesserocr提供了支持，进入下载页面，可以看到有各种.exe文件的下载列表，这里可以选择下载3.0版本，其中文件名中带有dev的为开发版本，不带dev的为稳定版本，可以选择下载不带dev的版本, 例如可以选择下载 tesseract-ocr-setup-3.05.01 .exe。

下载完成后打开，勾选Additional language data(download)选项来安装OCR识别支持的语言包，这样OCR 便可以识别多国语言。然后一路点击Next按钮即可。

最后pip3 install tesserocr pillow

**3.**    获取验证码

为了便于实验，我们先将验证码的图片保存到本地。

打开开发者工具，找到验证码元素。验证码元素是一张图片，它的src属性是CheckCode.aspx我们直接打开这个链接http://my.cnki.net/elibregister/CheckCode.aspx,就可以看到一个验证码，右键保 存即可，将其命名为code.jpg



**4.** 识别测试

接下来新建一个项目，将验证码图片放到项目根目录下，用tesserocr库识别该验证码，代码如下 所示：

import tesserocr from PIL import Image

image = Image.open('code.jpg')

result = tesserocr.image_to_text(image)

 print(result)

在这里我们新建了一个Image对象，调用了 tesserocr的image_to_text()方法。传入该Image对象 即可完成识别，实现过程非常简单，结果如下所示：

![JR42](C:\Users\javac\Desktop\class\JR42.JPG)

JR42

另外,tesserocr还有一个更加简单的方法，这个方法可直接将图片文件转为字符串，代码如下所示: import tesserocr

print(tesserocr.file_to_text(' image.png'))

不过，此种方法的识别效果不如上一种方法好。

**5.**验证码处理

接下来我们换一个验证码，将其命名为code2.jpg,如图所示。

![PFRT](C:\Users\javac\Desktop\class\PFRT.jpg)

重新用如下的代码来测试:

import tesserocr from PIL import Image

image = Image.open('code2.jpg') result = tesserocr.image_to_text(image) print(result)

可以看到如下输出结果：

FFKT

这次识别和实际结果有偏差，这是因为验证码内的多余线条干扰了图片的识别。

对于这种情况，我们还需要做一下额外的处理，如转灰度、二值化等操作。

我们可以利用Image对象的convert()方法参数传入L,即可将图片转化为灰度图像，代码如下 所示:

image = image.convert('L') image.show()

传入1即可将图片进行二值化处理，如下所示:

image = image.convert('1')

image.show()

我们还可以指定二值化的阈值。上面的方法釆用的是默认阈值127O不过我们不能直接转化原图. 要将原图先转为灰度图像，然后再指定二值化阈值，代码如下所示：

image = image.convert('L') 

threshold = 80

table =[]

for i in range(256):

​	if i < threshold: 

​		table.append(0) 

​	else:

​		table.append(l)

​		image = image.point(table, '1')

​		image.show()

在这里，变量threshold代表二值化阈值，阈值设置为80。之后我们看看结果，如下所示。

PFRT

我们发现原来验证码中的线条已经去除，整个验证码变得黑白分明。这时重新识别验证码，代码 如下所示:

import tesserocr

from PIL import Image

image = Image.open('code?.jpg')

image = image.convert('L')

threshold = 127

table =[]

for i in range(256):

​	if i < threshold:

​		table.append(O)

​	else:

​		table.append(l)

​		image = image.point(table, '1')

​		result = tesserocr.image_to_text(image)

​		print.( result)

即可发现运行结果变成如下所示:

PFRT

那么，针对一些有干扰的图片，我们做一些灰度和二值化处理，这会提高图片识别的正确率

### 7.2滑动验证码的识别

代码如下所示

```python
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import matplotlib.pylab as plt
from scipy import signal
import numpy as np
import time
import random
import os

#定义宏变量
#TEST_URL = 'https://www.geetest.com/type/'
TEST_URL = 'http://dun.163.com/trial/sense'
HD_TAG = "body > main > div.g-bd > div > div.g-mn2 > div.m-tcapt > ul > li:nth-child(2)"
TC_CLASS_SNAME = "yidun_intelli-tips"
PIC_CLASS_NAME = "yidun_bg-img"
HD_BTN = "yidun_slider"


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options,executable_path=r"C:\Downloads\driver\chromedriver.exe")
wait = WebDriverWait(driver,5)

driver.get(TEST_URL)
time.sleep(2)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,HD_TAG)))
button.click()
time.sleep(2)
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,TC_CLASS_SNAME)))
button.click()

#得到图片
time.sleep(2)
img = wait.until(EC.presence_of_element_located((By.CLASS_NAME,PIC_CLASS_NAME)))
location = img.location
size = img.size
driver.save_screenshot('snap.png')
#得到验证码的位置
left = location['x']
top = location['y']
right = left+size['width']
bottom = top+size['height']
img_obg = Image.open('snap.png')
crop_img = img_obg.crop((left,top,right,bottom))
crop_img.save('crop.png')
#卷积操作
im = np.array(crop_img.convert('L'))
#先进行平滑处理
# 生成高斯算子的函数
def func(x,y,sigma=1):
    return 100*(1/(2*np.pi*sigma))*np.exp(-((x-2)**2+(y-2)**2)/(2.0*sigma**2))
# 生成标准差为5的5*5高斯算子
g = np.fromfunction(func,(3,3),sigma=1)

grad = signal.convolve2d(im, g, mode="same")
plt.figure()
plt.imshow(grad)
plt.show()

f = np.array([[-1,0,1],
              [-2,0,2],
              [-1,0,1],
              ])

grad = signal.convolve2d(grad,f,boundary='symm',mode='same')
plt.figure()
plt.imshow(grad)
plt.show()

#得到距离
grad = np.sum(grad[:,:],axis=0)
# print(grad)
max_to_min = np.argsort(grad)

positive = []
i = 0
j = 0
while(j<6):
    if max_to_min[i]>55:
        positive.append(max_to_min[i])
        j = j+1
    i = i+1
# print(i,j,max_to_min[i])

x_left_index = 0
diffs = [x-positive[i] for i,x in enumerate(positive[1:])]
# print(diffs)
for i,d in enumerate(diffs):
    if d==1 or d==-1:
        x_left_index=i
        break
x_left = positive[x_left_index]
# x_left -= 0

# #模拟人为滑动
v0 = random.randint(0,2)
t = 0.1
tracks = []
cur = 0
mid = x_left*0.8
while cur < x_left:
    if cur<mid:
        a = random.randint(2,4)
    else:
        a = -random.randint(3,5)
    v = v0
    s = v*t+0.5*a*t**2
    cur += s
    v0 = v+a*t
    tracks.append(round(s))

tracks.append(x_left-sum(tracks))
n_stop = [0]*random.randint(10,30)
stop = random.randint(round(len(tracks)*0.85),round(len(tracks)*0.95))
tracks = tracks[:stop]+n_stop+tracks[stop:]
#开始滑动
button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,HD_BTN)))
ActionChains(driver).click_and_hold(button).perform()
for t in tracks:
    ActionChains(driver).move_by_offset(t,0).perform()

fore = random.randint(0,7)
# ActionChains(driver).move_by_offset(fore,0).perform()
# time.sleep(0.6)
# ActionChains(driver).move_by_offset(-fore,0).perform()
#
# time.sleep(0.5)
ActionChains(driver).release().perform()
time.sleep(3)
# driver.close()
```



### 7.3点触式验证码识别

代码如下所示

```python
from chaojiying_Python.chaojiying import Chaojiying_Client
import random
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

CHAOJIYING_NAME = '1219534922'  # 超级鹰账号
CHAOJIYING_PWD = 'w505377017'  # 超级鹰密码
CHAOJIYING_ID = 905045  # 软件ID
CHAOJIYING_KIND = 9004  # 验证码类型


class YYVerification(object):
    """
      此类用于YY的验证码识别，可以应用到类似的验证码识别上，这种验证码类型是
     点击类验证码.这里我们是对接超级鹰平台。
      """

    def __init__(self):
        self.url = 'https://aq.yy.com/p/reg/account.do?appid=&url=&fromadv=udbclsd_r'
        self.driver = webdriver.Chrome(r"C:\Downloads\driver\chromedriver.exe")
        self.chaojiying = Chaojiying_Client(CHAOJIYING_NAME, CHAOJIYING_PWD, CHAOJIYING_ID)

    # @property
    # def __del__(self):
    #     self.driver.close()

    def screen_shot(self):
        """
        网页截屏
         :return: bool值
        """
        # self.driver.maximize_window()
        time.sleep(2)

    # # 用于网页的向下滚动
    # js = 'var q=document.documentElement.scrollTop=300'
    # self.driver.execute_script(js)
    # time.sleep(1)
        self.driver.save_screenshot('yy.png')
        return True


    def i_url(self):
        """
        实现对iframe标签的url请求，并定位新网页
        :return: 定位对象
         """
        i = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/iframe')


        url_1 = i.get_attribute('src')
        print(url_1)
        self.driver.get(url_1)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mPickWords"]/div[1]')))
        return element


    def shear_location(self):
        """
        计算对截屏剪切的坐标，注意这里不同电脑可能会修改start_x到end_y
         后边添加的数是根据作者的电脑优化的
         :return: 返回坐标以及网页剪切定位的对象
        """
        time.sleep(random.random() + 1)
        print('正在获取div')


        div = self.i_url()
        start_x = div.location['x'] + 25
        start_y = div.location['y'] + 65
        end_x = div.location['x'] + 350 + 25
        end_y = div.location['y'] + 218 + 65
        result = (start_x, start_y, end_x, end_y)
        print(result)
        return result, div


    # @staticmethod
    def shear_image(axis):
        im = Image.open('yy.png')
        new_image = im.crop(axis)


        new_image.save('new_img.png')
        return new_image


    def upload_picture(self, img):
        """
        上传图片(Byte)，返回点击的坐标。这里对返回的坐标进行了处理，
       处理过程可以看成 shear_location 函数的坐标数据逆处理过程
         :param img: 上传的图片
        :return: 点击坐标
        """
        image = img
        byte_array = BytesIO()
        image.save(byte_array, format('PNG'))
        # 提交图片


        result = self.chaojiying.PostPic(byte_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        if '无可用题分' in result['err_str']:
            print('题分已经不足请充值')
            raise ValueError
        pic_str = result['pic_str']
        pic_list = [[i for i in x.split(',')] for x in pic_str.split('|')]
        for i in pic_list:
            i[0] = int(int(i[0]) * (282 / 354))
            i[1] = int(int(i[1]) * (219 / 274))
        print(pic_list)
        return pic_list


    def click_now(self, coordinates, axis, element):
        """
         这里如果验证失败会进行回调，实现验证码的自动验证。
         :param coordinates: 点击坐标
         :param axis: 剪切坐标
          :param element: 剪切位置的定位
          :return: 返回点击的成功信息
         """
        print('点击开始')


        print(coordinates)
        for location in coordinates:
            ActionChains(self.driver).move_to_element_with_offset(element, location[0], location[1]).click().perform()
        time.sleep(random.random() + 1.8)
        submission = self.driver.find_element_by_xpath('//*[@id="mPickWords"]/div[2]/span[4]')
        submission.click()
        time.sleep(1)
        if 'pw_submit_disabled' in submission.get_attribute('class'):
            return '点击成功'
        else:
            time.sleep(2)
        print('正在重新识别新的验证码')
        self.revalidation(axis, element)
        return '点击成功'


    def revalidation(self, axis, element):
        """
        网页跳转之后，执行验证的主程序
       :param axis: 剪切坐标
         :param element: 剪切位置的定位对象
        :return: 验证成果
        """
        self.screen_shot()


        if not self.screen_shot():
            return '截图失败'
        time.sleep(1)
        # 剪切图片
        new_image = self.shear_image(axis)
        new_image.show()
        # 上传图片并返回点击坐标
        click_coordinates = self.upload_picture(new_image)
        # 点击验证码
        print(self.click_now(click_coordinates, axis, element))
        return '点击验证结束'


    def main(self):
        self.driver.get(self.url)


        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/iframe')))
        axis, element = self.shear_location()
        self.revalidation(axis, element)

if __name__ == '__main__':
    yy = YYVerification()
    yy.main()
```

## 八.Scrapy的使用

​       Scrapy功能非常强大，爬取效率高，相关扩展组件多，可配置和可扩展程度非常高，它几乎可以 应对所有反爬网站，是目前Python中使用最广泛的爬虫框架。

### 8.1Scrapy框架介绍

​       Scrapy是一个基于Twisted的异步处理框架，是纯Python实现的爬虫框架，其架构清晰，模块之 间的耦合程度低，可扩展性极强，可以灵活完成各种需求。我们只需要定制开发几个模块就可以轻松实现一个爬虫。

**1**.架构介绍

首先我们看看Scrapy框架的架构，如图所示

![scrapy](C:\Users\javac\Desktop\class\scrapy.jpg)

它可以分为如下的几个部分。

□ Engine。引擎，处理整个系统的数据流处理、触发事务，是整个框架的核心。

□ Item。项目，它定义了爬取结果的数据结构，爬取的数据会被赋值成该Item对象。

□ Scheduler0调度器，接受引擎发过来的请求并将其加入队列中，在引擎再次请求的时候将 请求提供给引擎。

□ Downloader。下载器，下载网页内容，并将网页内容返回给蜘蛛。

□ Spiders.蜘蛛，其内定义了爬取的逻辑和网页的解析规则，它主要负责解析响应并生成提取 结果和新的请求。

□ Item Pipelineo项目管道，负责处理由蜘蛛从网页中抽取的项目，它的主要任务是清洗、验 证和存储数据。

□ Downloader Middlewares。下载器中间件，位于引擎和下载器之间的钩子框架，主要处理引 擎与下载器之间的请求及响应。

□ Spider Middlewareso蜘蛛中间件，位于引擎和蜘蛛之间的钩子框架，主要处理蜘蛛输入的 响应和输出的结果及新的请求。

**2**.数据流

Scrapy中的数据流由引擎控制，数据流的过程如下。

(1)   Engine首先打开一个网站，找到处理该网站的Spider,并向该Spider请求第一个要爬取的URL。

(2)   Engine从Spider中获取到第一个要爬取的URL,并通过Scheduler以Request的形式调度。

(3)   Engine向Scheduler请求下一*个要爬取的URL。

(4)   Scheduler 返回下一个要爬取的 URL 给 Engine, Engine 将 URL 通过 Downloader Middlewares 转 发给Downloader下载。

(5)   —旦页面下载完毕，Downloader生成该页面的Response,并将其通过Downloader Middlewares 发送给Engineo

(6)   Engine从下载器中接收到Response,并将其通过Spider Middlewares发送给Spider处理。

(7)   Spider处理Response,并返回爬取到的Item及新的Request给Engine。

(8)   Engine 将 Spider 返回的 Item 给 Item Pipeline,将新的 Request 给 Scheduler。

(9)   重复第(2)步到第(8)步，直到Scheduler中没有更多的Request, Engine关闭该网站，爬取结束。 通过多个组件的相互协作、不同组件完成工作的不同、组件对异步处理的支持，Scrapy最大限度

地利用了网络带宽，大大提高了数据爬取和处理的效率。

3. 项目结构

Scrapy框架和pyspider不同，它是通过命令行来创建项目的，代码的编写还是需要IDE。项目创 建之后，项目文件结构如下所示：

scrapy.cfg project/

_init__.py items.py pipelines.py



settings.py

middlewares.py

spiders/

_init _.py

spiderl.py

spider2.py

这里各个文件的功能描述如下。

□  scrapy.cfg：它是Scrapy项目的配置文件，其内定义了项目的配置文件路径、部署相关信息 等内容。

□   items.py：它定义Item数据结构，所有的Item的定义都可以放这里。

□   pipelines.py：它定义Item Pipeline的实现，所有的Item Pipeline的实现都可以放这里。

□   settings.py：它定义项目的全局配置。

□   middlewares.py:它定义 Spider Middlewares 和 Downloader Middlewares 的实现。

□   spiders：其内包含一个个Spider的实现，每个Spider都有一个文件。

4. 结语

本节介绍了 Scrapy框架的基本架构、数据流过程以及项目结构。后面我们会详细了解Scrapy的 用法，感受它的强大。

### 8.2Scrapy入门

接下来介绍一个简单的项目，完成一遍Scrapy抓取流程。通过这个过程，我们可以对Scrapy的 基本用法和原理有大体了解。

1. 本节目标

本节要完成的任务如下。

□创建一个Scrapy项目。

□创建一个Spider来抓取站点和处理数据。

□通过命令行将抓取的内容导出。

2. 准备工作

我们需要安装好Scrapy框架。如果尚未安装，请参照上一节的安装说明。

3. 创建项目

创建一个Scrapy项目，项目文件可以直接用scrapy命令生成，命令如下所示：

scrapy startproject tutorial

这个命令可以在任意文件夹运行。如果提示权限问题，可以加sudo运行该命令。这个命令将会创

建一个名为tutorial的文件夹，文件夹结构如下所示：

scrapy.cfg # Scrapy部署时的配置文件

tutorial #项目的模块，需要从这里引入

_init _.py

items.py #Items的定义定义爬取的数据结构

middlewares.py   #MiddleWares的定义 定义爬取中间件

piepelines.py #Piepelines的定义，定义数据管道

settings.py #配置文件

4. 创建 Spider

Spider是自己定义的类，Scrapy用它来从网页里抓取内容，并解析抓取的结果。不过这个类必须 继承Scrapy提供的Spider类scrapy.Spider,还要定义Spider的名称和起始请求，以及怎样处理爬取 后的结果的方法。

也可以使用命令行创建一个Spidero比如要生成Quotes这个Spider,可以执行如下命令：

cd tutorial

scrapy genspider quotes quotes.toscrape.com

进入刚才创建的tutorial文件夹,然后执行genspider命令。第一个参数是Spider的名称，第二 个参数是网站域名。执行完毕之后，spiders文件夹中多了一个quotes.py,它就是刚刚创建的Spider, 内容如下所示：

import scrapy

class QuotesSpider(scrapy.Spider):

​	name = "quotes" allowed_domains = ["quotes.toscrape.com"] 

​	start_urls = ['http://quotes.toscrape.com/'] 

​	def parse(self, response):

​			pass

这里有三个属性--- name、allowed_domains和start_urls,还有一个方法parse0

□   name,它是每个项目唯一的名字，用来区分不同的Spider。

□  allowedjomains,它是允许爬取的域名，如果初始或后续的请求链接不是这个域名下的，则 请求链诡会被过滤掉。

□   start_urls,它包含了 Spider在启动时爬取的url列表，初始请求是由它来定义的。

□  parse,它是Spider的一个方法。默认情况下，被调用时start_urls里面的链接构成的请求完 成下载执行后，返回的响应就会作为唯一的参数传递给这个函数。该方法负责解析返回的响 应、提取数据或者进一步生成要处理的请求。

5. 创建Item

Item是保存爬取数据的容器，它的使用方法和字典类似。不过，相比字典，Item多了额外的保护 机制，可以避免拼写错误或者定义字段错误。

创建Item需要继承scrapy.Item类，并且定义类型为scrapy.Field的字段。观察目标网站，我们 可以获取到到内容有text、author、tags。

定义Item,此时将items.py修改如下：

import scrapy

class Quoteltem(scrapy.Item):

​	text = scrapy.Field()

​	author = scrapy.Field()

​	tags = scrapy.Field()

这里定义了三个字段，接下来爬取时我们会使用到这个Item()

6. 解析 Response

前面我们看到，parse()方法的参数resposne是start_urls里面的链接爬取后的结果。所以在 parse()方法中，我们可以直接对response变量包含的内容进行解析，比如浏览请求结果的网页源代 码，或者进一步分析源代码内容，或者找出结果中的链接而得到下一个请求。

我们可以看到网页中既有我们想要的结果，又有下一页的链接，这两部分内容我们都要进行处理首先看看网页结构，如图所示。每一页都有多个class为quote的区块，每个区块内都包含 text、author、tags。那么我们先找出所有的quote,然后提取每一个quote中的内容。

![quotes](C:\Users\javac\Desktop\class\quotes.png)

提取的方式可以是CSS选择器或XPath选择器。在这里我们使用CSS选择器进行选择，parse() 方法的改写如下所示：

def parse(self, response):

​	quotes = response.css('.quote')

​	for quote in quotes:

​		text = quote.css(1.text::text').extract_first()

​		author = quote.css(1.author::text1).extract_first() 

​		tags = quote.css('.tags .tag::text').extract()

这里首先利用选择器选取所有的quote，并将其赋值为quotes变量,然后利用for循环对每个quote 遍历，解析每个quote的内容。对text来说，观察到它的class为text,所以可以用.text选择器来选取，这个结果实际上是整 个带有标签的节点，要获取它的正文内容，可以加::text来获取。这时的结果是长度为1的列表，所 以还需要用extract_first()方法来获取第一个元素。而对于tags来说，由于我们要获取所有的标签， 所以用extract。方法获取整个列表即可。

以第一个quote的结果为例，各个选择方法及结果的说明如下内容。

源码如下：

<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">

<span class="text" itemprop="text">rtThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.w</span>

<span>by <small class="author" itemprop="author">Albert Einstein</small>

<a href='7author/Albert-Einstein">(about)</a>

</span>

<div class="tags">

Tags:

<meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world">

<a class="tag" href="/tag/change/page/l/">change</a>

<a class="tag" href='7tag/deep-thoughts/page/l/">deep-thoughts</a>

<a class="tag" href="/tag/thinking/page/l/">thinking</a>

<a class="tag" href="/tag/world/page/l/">world</a>

</div>

</div>

不同选择器的返回结果如下。

•   quote.css('.text')

[<Selector xpath="descendant-or-self::*[@class and contains(concat('                            normalize-space(@class),''),

'text ')]" data='<span class="text" itemprop="text">rtThe '>]

•   quote.css('.text::text')

[<Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class),''), 'text ')]/text()" data=,aThe world as we have created it is a pr'>]

• quote.css('.text1).extract()

['<span class="text" itemprop="text">aThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.w</span>']

• quote.css('.text::text').extract()

['"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.11']

• quote.css('. text::text')・ extract.first()

"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking." 所以，对于text,获取结果的第一个元素即可，所以使用extract_first()方法，对于tags,要 获取所有结果组成的列表，所以使用extract()方法



7. 使用Item

上文定义了 Item,接下来就要使用它了。Item可以理解为一个字典，不过在声明的时候需要实例 化。然后依次用刚才解析的结果赋值Item的每一个字段，最后将Item返回即可。

QuotesSpider的改写如下所示：

import scrapy

from tutorial.items import Quoteltem

class QuotesSpider(scrapy.Spider):

​	name = "quotes"

​	allowed_domains = ["quotes.toscrape.com"] start_urls = ['http://quotes.toscrape.com/']

​	def parse(self, response):

​		quotes = response.css('.quote')

​		for quote in quotes:

​				item = Quoteltem()

​				item['text'] = quote.css('.text::text').extract_first()

​				item['author'] = quote.css('.author::text').extract_first()

​				item['tags'] = quote.css('.tags .tag::text').extract() yield item

如此一来，首页的所有内容被解析出来，并被赋值成了一个个Quoteitem。

8. 后续 Request

上面的操作实现了从初始页面抓取内容。那么，下一页的内容该如何抓取？这就需要我们从当前 页面中找到信息来生成下一个请求，然后在下一个请求的页面里找到信息再构造再下一个请求。这样 循环往复迭代，从而实现整站的爬取。

将刚才的页面拉到最底部，如图所示

![next](C:\Users\javac\Desktop\class\next.png)

这里有一个Next按钮。查看它的源代码，可以发现它的链接是/page/2/,全链接就是：http://quotes. toscrape.com/page/2,通过这个链接我们就可以构造下一个请求。

构造请求时需要用到scrapy.Requesto这里我们传递两个参数----- url和callback,这两个参数的

说明如下。

□   url：它是请求链接。

□  callback：它是回调函数。当指定了该回调函数的请求完成之后，获取到响应，引擎会将该 响应作为参数传递给这个回调函数。回调函数进行解析或生成下一个请求，回调函数如上文 的parse()所示。

由于parse()就是解析text, author, tags的方法，而下一页的结构和刚才已经解析的页面结构 是-样的，所以我们可以再次使用parse()方法来做页面解析。

接下来我们要做的就是利用选择器得到下一页链接并生成请求，在parse。方法后追加如下的代码:

next = response.css('.pager .next a::attr(href)1).extract_first()

url = response.urljoin(next)

yield scrapy.Request(url=url, callback=self.parse)

第一句代码首先通过CSS选择器获取下一个页面的链接，即要获取a超链接中的href属性。这 里用到了 ：：attr(href)操作。然后再调用extract_first()方法获取内容。

第二句代码调用了 urljoin。方法，urljoin。方法可以将相对URL构造成一个绝对的URL。例如， 茯取到的下一页地址是/page/2, urljoin。方法处理后得到的结果就是：http://quotes.toscrape.eom/page/2/o

第三句代码通过url和callback变量构造了一个新的请求，回调函数callback依然使用parse() 方法。这个请求完成后，响应会重新经过parse方法处理，得到第二页的解析结果，然后生成第二页 的下一页，也就是第三页的请求。这样爬虫就进入了一个循环，直到最后一页。

通过几行代码，我们就轻松实现了一个抓取循环，将每个页面的结果抓取下来了。

现在，改写之后的整个Spider类如下所示：

import scrapy

from tutorial.items import Quoteltem

class QuotesSpider(scrapy.Spider):

​	name = "quotes"

allowed_domains = ["quotes.toscrapy.com"] start_urls = ['http://quotes.toscrape.com/']

def parse(self, response):

​	quotes = response.css('.quote')

​	for quote in quotes:

​		item = Quoteltem()

​		item['text'] = quote.css('.text::text').extract_first() 

​		item['author'] = quote.css(*.author::text').extract_first() 

​		item['tags'] = quote.css('.tags .tag::text').extract() 

​		yield item

​		next = response.css('.pager .next a::attr("href")').extract_first() url = response.urljoin(next)

​	yield scrapy.Request(url=url, callback=self.parse)

9. 运行

接下来，进入目录，运行如下命令：

scrapy crawl quotes

就可以看到Scrapy的运行结果了

**10.**保存到文件

运行完Scrapy后，我们只在控制台看到了输出结果。如果想保存结果该怎么办呢？

要完成这个任务其实不需要任何额外的代码，Scrapy提供的Feed Exports可以轻松将抓取结果输 出。例如，我们想将上面的结果保存成CSV文件，可以执行如下命令：

scrapy crawl quotes -o quotes.CSV

命令运行后，项目内多了一个quotes.json文件，文件包含了刚才抓取的所有内容，内容是JSON 格式。

另外我们还可以每一个Item输出一行JSON,输出后缀为jl,为jsonline的缩写，命令如下所示： scrapy crawl quotes -o quotes.jl

或

scrapy crawl quotes -o quotes.jsonlines

输出格式还支持很多种，例如JSON、xml、pickle、marshal等，还支持ftp、s3等远程输出，另外 还可以通过自定义ItemExporter来实现其他的输出。



### 8.3Spider的用法

在Scrapy中，要抓取网站的链接配置、抓取逻辑、解析逻辑里其实都是在Spider中配置的。在 前一节实例中，我们发现抓取逻辑也是在Spider中完成的。本节我们就来专门了解一下Spider的基本 用法。

1. Spider运行流程

在实现Scrapy爬虫项目时，最核心的类便是Spider类了，它定义了如何爬取某个网站的流程和 解析方式。简单来讲，Spider要做的事就是如下两件：

□定义爬取网站的动作；

□分析爬取下来的网页。

对于Spider类来说，整个爬取循环过程如下所述。

□以初始的URL初始化Request,并设置回调函数。当该Request成功请求并返回时，Response 生成并作为参数传给该回调函数。

□在回调函数内分析返回的网页内容。返回结果有两种形式。一种是解析到的有效结果返回字 典或Item对象，它们可以经过处理后(或直接)保存。另一种是解析得到下一个(如下一页) 链接，可以利用此链接构造Request并设置新的回调函数，返回Request等待后续调度。

口如果返回的是字典或Item对象，我们可通过Feed Exports等组件将返回结果存入到文件。如 果设置了 Pipeline的话，我们可以使用Pipeline处理(如过滤、修正等)并保存。

□如果返回的是Reqeust,那么Request执行成功得到Response之后，Response会被传递给 Request中定义的回调函数，在回调函数中我们可以再次使用选择器来分析新得到的网页内 容，并根据分析的数据生成Item。

通过以上几步循环往复进行，我们完成了站点的爬取。

2. Spider类分析

在上一节的例子中，我们定义的 Spider 是继承自 scrapy.spiders.Spider- scrapy.spiders.Spider 这个类是最简单最基本的Spider类，其他Spider必须继承这个类。还有后面一些特殊Spider类也都 是继承自它。



scrapy. spiders. Spider这个类提供了 start_requests()方法的默认实现，读取并请求start_urls 属性，并根据返回的结果调用parse()方法解析结果。它还有如下一些基础属性。

□  name：爬虫名称，是定义Spider名字的字符串。Spider的名字定义了 Scrapy如何定位并初始 化Spider,它必须是唯一的。不过我们可以生成多个相同的Spider实例，数量没有限制。 name是Spider最重要的属性。如果Spider爬取单个网站，一个常见的做法是以该网站的域名 名称来命名Spider例如，Spider爬取mywebsite.com,该Spider通常会被命名为mywebsite。

□   allowed domains允许爬取的域名，是可选配置，不在此范围的链接不会被跟进爬取。

□  start_urls0它是起始URL列表，当我们没有实现start_requests()方法时，默认会从这个 列表开始抓取。

□  custom_settings0它是一个字典，是专属于本Spider的配置，此设置会覆盖项目全局的设 置。此设置必须在初始化前被更新，必须定义成类变量。

□  crawler。它是由from_crawler()方法设置的，代表的是本Spider类对应的Crawler对象。 Crawler对象包含了很多项目组件，利用它我们可以获取项目的一些配置信息，如最常见的获 取项目的设置信息，即Settings0

□   settings0它是一个Settings对象，利用它我们可以直接获取项目的全局设置变量。

除了基础属性，Spider还有一些常用的方法。

□  start_requests()0此方法用于生成初始请求，它必须返回一个可迭代对象。此方法会默认 使用start_urls里面的URL来构造Request,而且Request是GET请求方式。如果我们想在启 动时以POST方式访问某个站点，可以直接重写这个方法，发送POST请求时使用FormRequest 即可。

□  parse()o当Response没有指定回调函数时，该方法会默认被调用。它负责处理Response,处 理返回结果，并从中提取出想要的数据和下一步的请求，然后返回。该方法需要返回一个包 含Request或Item的可迭代对象。

□  closed()当Spider关闭时，该方法会被调用，在这里一般会定义释放资源的一些操作或其 他收尾操作。

**3**.结语

以上内容可能不太好理解。不过不用担心，后面会有很多使用这些属性和方法的实例。通过这些 实例，我们慢慢熟练掌握它们。

### 8.4Downloader Middleware 的用法

Downloader Middleware即下载中间件，它是处于Scrapy的Request和Response之间的处理模块。 我们首先来看看它的架构，如图13.1所示。

Scheduler从队列中拿出一个Request发送给Downloader执行下载，这个过程会经过Downloader Middleware的处理。另外，当Downloader将Request T载完成得到Response返回给Spider时会再次 经过 Downloader Middleware 处理

也就是说，Downloader Middleware在整个架构中起作用的位置是以下两个。

□在Scheduler调度出队列的Request发送给Doanloader下载之前，也就是我们可以在Request 执行下载之前对其进行修改。

□在下载后生成的Response发送给Spider之前，也就是我们可以在生成Resposne被Spider解析 之前对其进行修改。

Downloader Middleware的功能十分强大，修改User-Agentx处理重定向、设置代理、失败重试、 设置Cookies等功能都需要借助它来实现。下面我们来了解一下Downloader Middleware的详细用法。

1. 使用说明

需要说明的是，Scrapy其实已经提供了许多D ownloader Middleware，比如负责失败重试、自动重 定向等功能的Middleware,它们被DOWNLOADER_MIDDLEWARES_BASE变量所定义。

DOWNLOADER_MIDDLEWARES_BASE 变量的内容如下所示:

{

'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,

'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,

'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,

'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,

'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,

'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,

'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,

'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,

'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,

'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,

'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,

'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,

'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,

'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,

}

这是一个字典格式，字典的键名是Scrapy内置的Downloader Middleware的名称，键值代表了调 用的优先级，优先级是一个数字，数字越小代表越靠近Scrapy引擎，数字越大代表越靠近Downloader, 数字小的Downloader Middleware会被优先调用。

如果自己定义的Downloader Middleware要添加到项目里，DOWN LOAD E R_MI DD L E WAR E S_B AS E变量不 能直接修改。Scrapy提供了另外一个设置变量DOWNLOADER_MIDDLEWARES,我们直接修改这个变量就可 以添加自己定义的Downloader Middleware,以及禁用DOWNLOADER_MIDDLEWARES_BASE里面定义的 Downloader Middlewareo下面我们具体来看看Downloader Middleware的使用方法。

2. 核心方法

Scrapy内置的Downloader Middleware为Scrapy提供了基础的功能，但在项目实战中我们往往需 要单独定义Downloader Middlewareo不用担心，这个过程非常简单，我们只需要实现某几个方法即可。

每个Downloader Middleware都定义了一个或多个方法的类，核心的方法有如下三个。

□   process_request(request, spider)

□   process_response(request> response, spider)

process_exception(request, exception, spider)

我们只需要实现至少一个方法，就可以定义一个Downloader Middlewareo下面我们来看看这三个 方法的详细用法。

• process_request(request, spider)

Request被Scrapy引擎调度给Downloader之前，process_request()方法就会被调用，也就是在 Request从队列里调度出来到Downloader下载执行之前，我们都可以用process_request()方法对 Request进行处理。方法的返回值必须为None‘Response对象.Request对象之一，或者抛出IgnoreRequest 异常。

process_request()方法的参数有如下两个。

□ request,是 Request 对象，即被处理的 Request。

□ spider,是 Spdier 对象，即此 Request对应的 Spider。

返回类型不同，产生的效果也不同。下面归纳一下不同的返回情况。

□当返回是None时，Scrapy将继续处理该Request,接着执行其他Downloader Middleware的 process_request()方法，一直到Downloader把Request执行后得到Response才结束。这个过 程其实就是修改Request的过程，不同的Downloader Middleware按照设置的优先级顺序依次 对Request进行修改，最后送至Downloader执行。

□当返回为 Response 对象时，更低优先级的 Downloader Middleware 的 process_request()和 process_exception()方法就不会被继续调用，每个 Downloader Middleware 的 process_response() 方法转而被依次调用。调用完毕之后，直接将Response对象发送给Spider来处理。

□当返回为Request对象时，更低优先级的Downloader Middleware的process_request()方法会 停止执行。这个Request会重新放到调度队列里，其实它就是一个全新的Request,等待被调 度。如果被 Scheduler 调度了，那么所有的 Downloader Middleware 的 process_request()方法 会被重新按照顺序执行。

□如果 IgnoreRequest 异常抛出，则所有的 Downloader Middleware 的 process_exception()方法 会依次执行。如果没有一个方法处理这个异常，那么Request的errorback()方法就会回调。 如果该异常还没有被处理，那么它便会被忽略。

• process_response(request, response, spider)

Downloader执行Request下载之后，会得到对应的Responseo Scrapy引擎便会将Response发送给 Spider进行解析。在发送之前，我们都可以用process_response()方法来对Response进行处理。方法 的返回值必须为Request对象、Response对象之一，或者抛出IgnoreRequest异常。

process_response()方法的参数有如下三个。

□ request,是 Request 对象，即此 Response对应的 Request0

□ response,是 Response 对象，即此被处理的 Response□

□ spider,是 Spider 对象，即此 Response对应的 Spider。

下面归纳一下不同的返回情况。

当返回为Request对象时，更低优先级的Downloader Middleware的process_response()方法 不会继续调用。该Request对象会重新放到调度队列里等待被调度，它相当于一个全新的 Requesto 然后，该 Request 会被 process_request()方法顺次处理。

□当返回为Response对象时，更低优先级的Downloader Middleware的process_response()方法 会继续调用，继续对该Response对象进行处理。

□如果IgnoreRequest异常抛出，贝0 Request的errorback。方法会回调。如果该异常还没有被处 理，那么它便会被忽略。

• process_exception(request, exception, spider)

当Downloader或process_request()方法抛出异常时，例如抛出IgnoreRequest异常, process_exception()方法就会被调用。方法的返回值必须为None、Response对象、Request对象之一。

process_exception ()方法的参数有如下三个。

□   request,是Request对象，即产生异常的Requesto

□   exception,是Exception对象，即抛出的异常。

□   spdier,是 Spider 对象，BP Request对应的 Spidero

下面归纳一下不同的返回值。

□当返回为None时，更低优先级的Downloader Middleware的process_exception()会被继续顺 次调用，直到所有的方法都被调度完毕。

□当返回为 Response 对象时，更低优先级的 Downloader Middleware 的 process_exception()方 法不再被继续调用，每个Downloader Middleware的process_response()方法转而被依次调 用。

□当返回为Request对象时，更低优先级的Downloader Middleware的process_exception()也不 再被继续调用，该Request对象会重新放到调度队列里面等待被调度，它相当于一个全新的 Requesto然后，该Request又会被process_request()方法顺次处理。

以上内容便是这三个方法的详细使用逻辑。在使用它们之前，请先对这三个方法的返回值的处理 情况有一个清晰的认识。在自定义Downloader Middleware的时候，也一定要注意每个方法的返回类型「

下面我们用一个案例实战来加深一下对Downloader Middleware用法的理解。

**3**.项目实战

新建一个项目，命令如下所示：

scrapy startproject scrapydownloadertest

新建了一个Scrapy项目，名为scrapydownloadertest。进入项目，新建一个Spider,命令如下所示:

scrapy genspider httpbin httpbin.org

新建了一个Spider,名为httpbin,源代码如下所示：

import scrapy

class HttpbinSpider(scrapy.Spider):

​	name = 'httpbin'

allowed_domains = ['httpbin.org'] start_urls = ['http://httpbin.org/']

def parse(self, response): pass

接下来我们修改 start_urls 为：[[http://httpbin.org/]](http://httpbin.org/](http:/httpbin.org/)o) 随后将 parse() 方法添加一行日志输出，将response变量的text属性输出出来，这样我们便可以看到Scrapy发送的 Request 信息了。

修改Spider内容如下所示:

import scrapy

class HttpbinSpider(scrapy.Spider): najne = ' httpbin' allowed_domains = ['httpbin.org'] start_urls = ['http://httpbin.org/get']

def parse(self, response):

self.logger.debug(response.text)

接下来运行此Spider,执行如下命令:

scrapy crawl httpbin

Scrapy运行结果包含Scrapy发送的Request信息，内容如下所示:

"args": (),

"headers": (

"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*；q=0.8", "Accept-Encoding": "gzip,deflate,br",

"Accept-Language": "en",

"Connection": "close",

"Host": "httpbin.org",

 


"User-Agent": "Scrapy/1.4.0 (+http://scrapy.org)"



我们观察一下 Headers, Scrapy 发送的 Request 使用的 User-Agent 是 Scrapy /1.4.0(+http://scrapy.org),

这其实是由Scrapy内置的UserAgentMiddleware设置的，UserAgentMiddleware的源码如下所示:

from scrapy import signals

class UserAgentMiddleware(object): def       init    (self, user_agent='Scrapy'): self.user_agent = user_agent

@classmethod

def from_crawler(cls, crawler):

o = cis(crawler.settings['USER_AGENT'])

crawler.signals.connect(o.spider_opened, signal=signals.spider_opened) return o

def spider_opened(self, spider):

self.user_agent = getatti(spider, 'user_agent', self.user_agent)

def process_request(self, request, spider):

if self.user_agent: request.headers.setdefault(b'User-Agent', self.user_agent)

在from_crawler()方法中，首先尝试获取settings里面USER_AGENT,然后把USER_AGENT传递给 _init_()方法进行初始化，其参数就是user_agento如果没有传递USER_AGENT参数就默认设置为 Scrapy字符串。我们新建的项目没有设置USER_AGENT,所以这里的user_agent变量就是Scrapy接 下来，在process_request()方法中，将user-agent变量设置为headers变量的一个属性，这样就成功 设置了 User-Agento 因此，User-Agent 就是通过此 Downloader Middleware 的 process_request()方法设 置的。

修改请求时的User-Agent可以有两种方式：一是修改settings里面的USER_AGENT变量；二是通 过 Downloader Middleware 的 process_request()方法来修改。

第一种方法非常简单，我们只需要在setting.py里面加一行USER_AGENT的定义即可：

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 1O_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

一般推荐使用此方法来设置。但是如果想设置得更灵活，比如设置随机的User-Agent,那就需要 借助 Downloader Middleware 了。所以接下来我们用 Downloader Middleware 实现一个随机 User-Agent 的设置。

在 middlewares.py 里面添加一个 RandomUserAgentMiddleware 的类，如下所示：

import random

class RandomUserAgentMiddleware():

​	def     init     (self):

​		self.user_agents =[

​		'Mozilla/5.0 (Windows; U; MSIE 9.0； Windows NT 9.0； en-US)',

​		'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',

​		'Mozilla/5.0 (Xll; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1' ]

​	def process_request(self, request, spider):

​		request.headers['User-Agent'] = random.choice(self.user_agents)

我们首先在类的_ init_()方法中定义了三个不同的User-Agent,并用一个列表来表示。接下来 实现了 process_request()方法，它有一个参数request,我们直接修改request的属性即可。在这里 我们直接设置了 request变量的headers属性的User-Agent,设置内容是随机选择的User-Agent,这 样一个 Downloader Middleware 就写好了。

不过，要使之生效我们还需要再去调用这个Downloader Middlewareo在settings.py中，将 DOWNLOADER_MIDDLEWARES取消注释，并设置成如下内容：

DOWNLOADER_MIDDLEWARES = (

'scrapydownloadertest.middlewares.RandomUserAgentMiddleware': 543,

接下来我们重新运行Spider,就可以看到User-Agent被成功修改为列表中所定义的随机的一个 User-Agent 了 ：

{

"args": {),

"headers": (

"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8”,

"Accept-Encoding": "gzip,deflate,br",

"Accept-Language": "en",

"Connection": "close",

"Host": "httpbin.org",

"User-Agent": "Mozilla/5.0 (Windows; U; MSIE 9.0； Windows NT 9.0; en-US)"

},

"origin": "60.207.237.85",

"url": "http://httpbin.org/get"

}

我们就通过实现Downloader Middleware并利用process_Tequest()方法成功设置了随机的User-Agent。

另外，Downloader Middleware 还有 process_response()方法。Downloader 对 Request 执行下载之 后会得到Response,随后Scrapy引擎会将Response发送回Spider进行处理。但是在Response被发送 给Spider之前，我们同样可以使用process_response()方法对Response进行处理。比如这里修改一下 Response 的状态码，在 RandomUserAgentMiddleware 添加如下代码：

def process_response(self, request, response, spider):

response.status = 201

return response

我们将response变量的status属性修改为201,随后将response返回，这个被修改后的Response 就会被发送到Spidero

我们再在Spider里面输出修改后的状态码，在parse()方法中添加如下的输出语句：

self.logger.debug('Status Code: ' + str(response.status))

重新运行之后，控制台输出了如下内容：

[httpbin] DEBUG: Status Code: 201

可以发现，Response的状态码成功修改了。

因此要想对Response进行后处理，就可以借助于process_response()方法。

另外还有一个process_exception()方法，它是用来处理异常的方法。如果需要异常处理的话，我 们可以调用此方法。不过这个方法的使用频率相对低一些，在此不用实例演示。

4.本节代码

本节源代码为：https://github.com/Python3WebSpider/ScrapyDownloaderTesto

5.结语

本节讲解了 Downloader Middleware的基本用法。此组件非常重要，是做异常处理和反爬处理的 核心。后面我们会在实战中应用此组件来处理代理、Cookies等内容。



### 8.5 Spider Middleware 的用法

当 Downloader 生成 Response 之后，Response 会被发送给 Spider,在发送给 Spider之前，Response 会首先经过Spider Middleware处理,当Spider处理生成Item和Request之后，Item和Request还会经 过 Spider Middleware 的处理。

Spider Middleware有如下三个作用。

□我们可以在Downloader生成的Response发送给Spider之前，也就是在Response发送给Spider 之前对Response进行处理。

□我们可以在Spider生成的Request发送给Scheduler之前，也就是在Request发送给Scheduler 之前对Request进行处理。

□我们可以在Spider生成的Item发送给Item Pipeline之前，也就是在Item发送给Item Pipeline 之前对Item进行处理。’

1. 使用说明

需要说明的是，Scrapy其实已经提供了许多Spider Middleware,它们被SPIDER_MIDDLEWARES_BASE 这个变量所定义。

SPIDER_MIDDLEWARES_BASE 变量的内容如下：

(

'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,

'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,

'scrapy.spidermiddlewares.referer.RefererMiddleware': 700, 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800, 'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,

)

和 Downloader Middleware 一样，Spider Middleware 首先加入到 SPIDER_MIDDLEWARES 设置中,该设 置会和Scrapy中SPIDER_MIDDLEWARES_BASE定义的Spider Middleware合并。然后根据键值的数字优先级排 序，得到一个有序列表。第一个Middleware是最靠近引擎的，最后一个Middleware是最靠近Spider的〉

2. 核心方法

Scrapy内置的Spider Middleware    Scrapy提供了基础的功能。如果我们想要扩展其功能，只需要

实现某几个方法即可。

每个Spider Middleware都定义了以下一个或多个方法的类，核心方法有如下4个。

□   process_spider_input(response, spider)o

□   process_spider_output(response, result, spider)o

□   process_spider_exception(response, exception, spider)o

□   process_start_requests(start_requests, spider)。



只需要实现其中一个方法就可以定义一个Spider Middlewareo下面我们来看看这4个方法的详细 用法。

• process_spider_input(response, spider)

当 Response 被 Spider Middleware 处理时，process_spider_input ()方法被调用。

process_spider_input ()方法的参数有如下两个。

□   response,是 Response 对象，即被处理的 Responseo

□   spider,是 Spider 对象，即该 Response 对应的 Spidero

process_spider_input()应该返回None或者抛出一个异常。

口如果它返回None, Scrapy将会继续处理该Response,调用所有其他的Spider Middleware,直 到 Spider 处理该 Response 0

□如果它抛出一个异常，Scrapy将不会调用任何其他Spider Middleware的process_spider_input () 方法，而调用Request的errback()方法。errback的输出将会被重新输入到中间件中，使用 process_spider_output()方法来处理，当其抛出异常时则调用 process_spider_exception()来 处理。

•   process_spider_output(response, result, spider)

当Spider处理Response返回结果时，process_spider_output()方法被调用。 process_spider_output ()方法的参数有如下三个。

□   response,是Response对象，即生成该输出的Responseo

□   result,包含Request或Item对象的可迭代对象，即Spider返回的结果。

□   spider,是Spider对象，即其结果对应的Spider。

process_spider_output()必须返回包含Request或Item对象的可迭代对象。

•   process_spider_exception(response, exception, spider)

当 Spider 或 Spider Middleware 的 process_spider_input()方法抛出异常时，process_spider_exception() 方法被调用。

process_spider_exception()方法的参数有如下三个。

□   response,是Response对象，即异常被抛出时被处理的Responseo

□   exception,是Exception对象，即被抛出的异常。

□   spider,是Spider对象，即抛出该异常的Spidero

process_spider_exception()必须要么返回None,要么返回一个包含Response或Item对象的可迭 代对象。

□如果它返回None, Scrapy将继续处理该异常，调用其他Spider Middleware中的process_spider_ exception()方法，直到所有Spider Middleware都被调用。



□如果它返回一个可迭代对象，则其他Spider Middleware的process_spider_output()方法被调 用，其他的 process_spider_exception()不会被调用。

• process_start_requests(start_requests, spider)

process_start_requests()方法以Spider启动的Request为参数被调用，执行的过程类似于process_ spider_output(),只不过它没有相关联的Response,并且必须返回Requesto

process_start_requests ()方法的参数有如下两个。

□   start_requests,是包含 Request 的可迭代对象，即 Start Requestso

□   spider,是 Spider 对象，即 Start Requests 所属的 Spidero

process_start_requests()必须返回另一个包含Request对象的可迭代对象。

**3**.结语

本节介绍了 Spider Middleware 的基本原理和自定义 Spider Middleware 的方法。Spider Middleware 使用的频率不如Downloader Middleware的高，在必要的情况下它可以用来方便数据的处理。

### 8.6 Item Pipeline 的用法

Item Pipeline是项目管道。在前面我们已经了解了 Item Pipeline的基本用法，本节我们再作详细 了解它的用法。

首先我们看看Item Pipeline在Scrapy中的架构，如图13-1所示。

图中的最左侧即为Item Pipeline,它的调用发生在Spider产生Item之后。当Spider解析完Response 之后，Item就会传递到Item Pipeline,被定义的Item Pipeline组件会顺次调用，完成一连串的处理过 程，比如数据清洗、存储等。

Item Pipeline的主要功能有如下4点。

□清理HTML数据。

□验证爬取数据，检查爬取字段。

□査重并丢弃重复内容。

□将爬取结果保存到数据库。

1.核心方法

我们可以自定义Item Pipeline,只需要实现指定的方法，其中必须要实现的一个方法是： process_item(item, spider)o

另外还有如下几个比较实用的方法。

□   open_spider(spider)0

□   close_spider(spider)0

□   from_crawler(cls, crawler)o

下面我们详细介绍这几个方法的用法。



•   process_item(item, spider)

process_item()是必须要实现的方法，被定义的Item Pipeline会默认调用这个方法对Item进行处 理 比如，我们可以进行数据处理或者将数据写入到数据库等操作。它必须返回Item类型的值或者 抛出一个Dropitem异常。

process_item ()方法的参数有如下两个。

□   item,是Item对象，即被处理的Item。

□   spider,是 Spider 对象，即生成该 Item 的 Spidero

process_item ()方法的返回类型归纳如下。

□如果它返回的是Item对象，那么此Item会被低优先级的Item Pipeline的process_item()方法 处理，直到所有的方法被调用完毕。

□如果它抛出的是Dropitem异常，那么此Item会被丢弃，不再进行处理。

•   open_spider(self, spider)

open_spider()方法是在Spider开启的时候被自动调用的。在这里我们可以做一些初始化操作，如 开启数据库连接等。其中，参数spider就是被开启的Spider对象。

•   close_spider(spider)

close_spider()方法是在Spider关闭的时候自动调用的。在这里我们可以做一些收尾工作，如关 闭数据库连接等。其中，参数spider就是被关闭的Spider对象。

•   from_crawler(cls, crawler)

from_crawler()方法是一个类方法，用@classmethod标识，是一种依赖注入的方式。它的参数是 crawler,通过crawler对象，我们可以拿到Scrapy的所有核心组件，如全局配置的每个信息，然后创 建一个Pipeline实例。参数cis就是Class,最后返回一个Class实例。

### 8.7Scrapy 对接 Selenium

这里举简书的例子，创建框架请看上节，这里直接列举所有部分的代码

js.py

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spider.spider_demo.jianshu_spider.jianshu_spider.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//h1[@class="_1RuRku"]/text()').get()
        avatar = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/a/img/@src').get()
        author = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/div/div[1]/span/a/text()').get()
        pub_time=response.xpath('//div[@class="s-dsoj"]/time/text()').get()
        article_id = response.url.split('/')[-1]
        content = response.xpath("//article[@class='_2rhmJa']").get()
        word_count=response.xpath("//div[@class='s-dsoj']/span[2]/text()").get()
        read_count=response.xpath("//div[@class='s-dsoj']/span[3]/text()").get()
        like_count=response.xpath("//span[@class='_1LOh_5']").get()
        comment_count=",".join(response.xpath("//span[@class='_2R7vBo']/text()").getall())
        subjects=",".join(response.xpath("//div[@class='_2Nttfz']/a/span/text()").getall())


        item = ArticleItem(title=title,
                           content=content,
                           article_id=article_id,
                           pub_time=pub_time,
                           avatar=avatar,
                           author=author,
                           origin_url=response.url,
                           word_count=word_count,
                           read_count=read_count,
                           like_count=like_count,
                           comment_count=comment_count,
                           subjects=subjects
                           )
        yield item
```

item.py

```python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    article_id = scrapy.Field()
    origin_url = scrapy.Field()
    author = scrapy.Field()
    avatar = scrapy.Field()
    pub_time = scrapy.Field()
    read_count=scrapy.Field()
    like_count=scrapy.Field()
    word_count=scrapy.Field()
    subjects=scrapy.Field()
    comment_count=scrapy.Field()
```

middleware.py

```python
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse

class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='C:\Downloads\driver\chromedriver.exe')

    def process_request(self,request,spider):
        self.driver.get(request.url)
        time.sleep(1)
        try:
            while True:
                showMore=self.driver.find_element_by_class_name('load-more')
                showMore.click()
                time.sleep(0.3)
                if not showMore:
                    break
        except:
            pass
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')
        return response
```

piplines.py

```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import cmdline

    def process_item(self, item, spider):
        '''
        存入数据
        '''
        cmdline.execute("scrapy crawl js -o js.csv".split())
        return item


```

settings.py

```python
# -*- coding: utf-8 -*-

# Scrapy settings for jianshu_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jianshu_spider'

SPIDER_MODULES = ['jianshu_spider.spiders']
NEWSPIDER_MODULE = 'jianshu_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jianshu_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jianshu_spider.middlewares.JianshuSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'jianshu_spider.middlewares.SeleniumDownloadMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'jianshu_spider.pipelines.JianshuSpiderPipeline': 300,
   'jianshu_spider.pipelines.JianshuTwistePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```

## 九.结语

  在互联网软件开发工程师的分类中，爬虫工程师是非常重要的。爬虫工作往往是一个公司核 心业务开展的基础，数据抓取下来，才有后续的加工处理和最终展现。此时数据的抓取规模、稳定 性、实时性、准确性就显得非常重要。早期的互联网充分幵放互联，数据获取的难度很小。随着各大公司对数据资产日益看重，反爬水平也在不断提高，各种新技术不断给爬虫软件提出新的课题。 所以编程语言中掌握爬虫是很重要的。