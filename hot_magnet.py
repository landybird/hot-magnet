# encoding : utf-8
# __author__ = 'jm'
import os
import csv
import codecs
import json
import argparse
import importlib

import yaml
from requests_html import HTMLSession
from requests.exceptions import RequestException


def _get_params():
    """
    获取命令行参数
    """
    parser = argparse.ArgumentParser(description='获取磁链的工具(默认为热度最高的TOP20)')

    parser.add_argument(
        'keyword',
        metavar="KEYWORD",
        type=str,
        nargs="*",
        help='磁链关键字, 必填项')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='导出至文件 output file path, supports csv and json format.')
    parser.add_argument(
        '-s',
        '--sort',
        type=int,
        default=0,
        help="0: hot, 1:new")
    parser.add_argument(
        '-c',
        '--count',
        type=int,
        default=20,
        help="指定返回的磁链数目")
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='version information.')
    return parser


def _check_web_site(cfg_dict):
    """
    测试网页是否可用
    """
    session = HTMLSession()
    for item in cfg_dict.get("WEB_SITE_LIST"):
        try:
            response = session.get(item[-1].get("BASE_URL"))
            if response.status_code != 200:
                continue
            else:
                return item[-1]
        except RequestException as __:
            continue


def _read_config():
    """
    获取配置
    """
    yaml_path = 'config.yaml'
    f = open(yaml_path, encoding='utf-8')
    cfg = f.read()
    cfg_dict = yaml.load(cfg)
    return cfg_dict


def _output_file(magnet_list, path):
    """
    导出文件
    """
    if path:
        __, extension = os.path.splitext(path)
        if extension == '.csv':
            with open(path, mode='w+', encoding='utf-8-sig', newline="") as fcsv:
                fieldnames = (
                    "magnet",
                    "magnet_name",
                    "magnet_size",
                    "magnet_date",
                    "magnet_rank"
                )
                file_csv = csv.DictWriter(
                    fcsv, fieldnames, extrasaction="ignore")
                file_csv.writeheader()
                file_csv.writerows(magnet_list)
                print("Save {} successfully!".format(path))

        elif extension == ".json":
            with codecs.open(path, mode="w+", encoding="utf-8") as f:
                json.dump(magnet_list, f, indent=2)
            print("Save {} successfully!".format(path))
        else:
            print("Failed to save the file!")


def _print_terminal(magnet_list):
    """
    输出到终端
    """
    if not magnet_list:
        return

    for magnet in magnet_list:
        print("磁链:", magnet["magnet"])
        print("名称:", magnet["magnet_name"])
        print("大小:", magnet["magnet_size"])
        print("日期:", magnet["magnet_date"])
        print("热度:", magnet["magnet_rank"], "\n")

    print("===================完成=====================")


def _sort_magnet_list(magnet_list, sort):

    sorted_magnet_list = sorted(
        magnet_list,
        key=lambda x: x['magnet_rank'],
        reverse=True) if sort == 0 else sorted(
        magnet_list,
        key=lambda x: x['magnet_date'],
        reverse=True)
    return sorted_magnet_list


def main():

    cfg_dict = _read_config()
    web_item = _check_web_site(cfg_dict)
    parser = _get_params()
    args = parser.parse_args()
    if args.version:
        print(cfg_dict["VERSION"])
        return

    if not web_item:
        print('配置中的磁链网站已不可用，请更换')
        return

    handler_name = web_item['HANDLER_NAME']
    base_url = web_item["BASE_URL"]
    module = importlib.import_module('handler.magnet_handler')
    if hasattr(module, handler_name):  # todo 完成测试后使用
        handler = getattr(module, handler_name)()
    else:
        print("没有对应的handler处理")
        return

    if not args.keyword:
        parser.print_help()

    else:
        temp_magnet_list = handler.run(
            base_url, args.keyword[0], args.count, args.sort)
        magnet_list = _sort_magnet_list(temp_magnet_list, args.sort)
        if args.output:
            _output_file(magnet_list, args.output)
        else:
            _print_terminal(magnet_list)


if __name__ == '__main__':
    main()
