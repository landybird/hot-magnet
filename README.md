# 获取磁链热度TOP20

[![PyPI version](https://badge.fury.io/py/torrent-cli.svg)](https://badge.fury.io/py/torrent-cli) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


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
  -v, --version         查看当前版本 version information.```


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
$ torrent-cli 战狼2 -p -s 1
Crawling data for you.....
magnet:?xt=urn:btih:CC3854CACBB5434E03EFF39C693B20223E0AA39D 56.8 GB 2018-05-14
magnet:?xt=urn:btih:D6A5598C03C3123038DB6CAA04AE36D90BB569C6 35.0 GB 2018-02-22
magnet:?xt=urn:btih:5B411E880CB585B5B596DBB25BB7F0927FD44F54 13.2 GB 2018-01-01
magnet:?xt=urn:btih:B8E5C85B5B368060AB245AC5E434981B0D5543CA 12.4 GB 2018-02-23
magnet:?xt=urn:btih:4640565A71BB840D6A082B7F8D387A5FF604941A 9.2 GB 2017-12-12
magnet:?xt=urn:btih:B6401277BA77620727F7D6FE1345501555F7CA28 7.8 GB 2017-11-16
magnet:?xt=urn:btih:2154B29E07DF4D21B67488C55667B1AB22CD63F4 7.8 GB 2017-12-17
magnet:?xt=urn:btih:C1F01F089892ECF2AF168C190754B2921902D9E1 7.5 GB 2017-11-16
magnet:?xt=urn:btih:DE42BC281CF39F0F489B64F06C2440466D545C83 5.4 GB 2017-12-13
```

**3 保存json或者csv文件
```
$ torrent-cli 战狼2 -o movie.csv
```


### License

MIT [©landybird](https://github.com/landybird)
