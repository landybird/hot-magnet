# 获取磁链热度TOP20

[![PyPI version](https://badge.fury.io/py/hot-magnet.svg)](https://pypi.org/project/hot-magnet/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


> 兼容环境

`Windows`/`Linux`/`MacOs`


### 1 安装

> pip 安装
```
$ pip install hot-magnet
```

> 源码安装
```
 $ git clone https://github.com/landybird/hot-magnet.git
 $ cd hot-magnet
 $ pip install -r requirements.txt
 $ python setup.py install
 ```


### 2 使用
```
usage: hot-magnet [-h] [-o OUTPUT] [-s SORT] [-c COUNT] [-v]
                  [KEYWORD [KEYWORD ...]]

获取磁链的工具(默认为热度最高的TOP20)

positional arguments:
  KEYWORD               磁链关键字, 必填项

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        导出至文件 支持csv 和 json格式  output file path, supports csv and json format.
  -s SORT, --sort SORT  0: hot, 1:new   0 按热度（默认） 1 按时间
  -c COUNT, --count COUNT
                        指定返回的磁链数目 默认20条
  -v, --version         查看当前版本 version information.
  
  ```


> 示例


**1 根据关键字搜索**

```
(hot-magnet) λ hot-magnet 无名之辈

=========collecting Data=============

磁链: magnet:?xt=urn:btih:AB8E72974F4374E218770B1DC9EAA8287A81E6CA
名称: 无名之辈HD国语中字.mp4
大小: 1.07GB
日期: 2018-12-3
热度: 一般

磁链: magnet:?xt=urn:btih:FBAE30FB853DDDF6944CA7380E064F96B9C46825
名称: 无名之辈 HC 720P高清国语中字
大小: 1.65GB
日期: 2018-12-14
热度: 一般

...

磁链: magnet:?xt=urn:btih:AE2B6E55B8D00430FA8117E768DA4F0938331C8E
名称: 无名之辈HDTC高清版本.mp4
大小: 2.92GB
日期: 2018-12-4
热度: 一般

磁链: magnet:?xt=urn:btih:248DF944C119A841C2B2544E547AE096417A0DFA
名称: 无名之辈BD国语中字.mp4
大小: 1.14GB
日期: 2018-12-7
热度: 一般

磁链: magnet:?xt=urn:btih:ED423A662E458179B4864CBDBBF0D71CDDACFC6E
名称: [zilu1.com]无名之辈HC1080P高清国语中字
大小: 3.47GB
日期: 2018-12-7
热度: 一般

磁链: magnet:?xt=urn:btih:D3E5DA7DECD75250FD8A7CEBD0A96DDA3FE453E7
名称: 无名之辈.2018.TC720P.国语中字.mp4
大小: 1.04GB
日期: 2018-11-28
热度: 一般

===================完成============================
```


**2 排序（0 热度 1 时间）**

```
$  hot-magnet 无名之辈 -s 1 -c 10   # 按时间排序, 10条记录


磁链: magnet:?xt=urn:btih:AE2B6E55B8D00430FA8117E768DA4F0938331C8E
名称: 无名之辈HDTC高清版本.mp4
大小: 2.92GB
日期: 2018-12-4
热度: 一般

....

磁链: magnet:?xt=urn:btih:FBAE30FB853DDDF6944CA7380E064F96B9C46825
名称: 无名之辈 HC 720P高清国语中字
大小: 1.65GB
日期: 2018-12-14
热度: 一般

```

**3 保存json或者csv文件**

```
(hot-magnet) λ hot-magnet 无名之辈 -s 1 -c 10  -o a.json

=========collecting Data=============

Save a.json successfully!


[
  {
    "magnet": "magnet:?xt=urn:btih:ED423A662E458179B4864CBDBBF0D71CDDACFC6E",
    "magnet_name": "[zilu1.com]\u65e0\u540d\u4e4b\u8f88HC1080P\u9ad8\u6e05\u56fd\u8bed\u4e2d\u5b57",
    "magnet_size": "3.47GB",
    "magnet_date": "2018-12-7",
    "magnet_rank": "\u4e00\u822c"
  },
  ...,
  {
    "magnet": "magnet:?xt=urn:btih:248DF944C119A841C2B2544E547AE096417A0DFA",
    "magnet_name": "\u65e0\u540d\u4e4b\u8f88BD\u56fd\u8bed\u4e2d\u5b57.mp4",
    "magnet_size": "1.14GB",
    "magnet_date": "2018-12-7",
    "magnet_rank": "\u4e00\u822c"}
]

```


### License

MIT [©landybird](https://github.com/landybird)
