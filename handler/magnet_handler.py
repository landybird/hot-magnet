# encoding : utf-8
# __author__ = 'jm'

from urllib.parse import urlencode, urljoin
from concurrent.futures import ThreadPoolExecutor
import math
import json

from fake_useragent import UserAgent
from requests_html import HTMLSession


class BaseSearchMagnetHandler(object):
    def __init__(self):
        self.HEADERS = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': UserAgent().random
        }
        self.session = HTMLSession()
        self.magnet_list = []


class cilimaoHandler(BaseSearchMagnetHandler):

    def __init__(self):
        super(cilimaoHandler, self).__init__()
        self.page = 10

    def _get_param(self, sort):

        return {
            'resourceType': 1,  # 电影资源
            'sortProperties': 'download_count' if sort == 0 else 'created_time',
        }

    def run(self, url, keyword, count, sort):
        print("=========collecting Data=============")
        request_dict = self._get_param(sort)
        request_dict['word'] = keyword

        page_range = math.ceil(count / self.page)

        for page in range(page_range):
            request_dict['page'] = page + 1
            search_url = "{}?{}".format(
                urljoin(url, 'search'), urlencode(request_dict))
            r = self.session.get(search_url, headers=self.HEADERS)
            magnet_info_list = r.html.xpath(
                '//a[@class="Search__result_title___24kb_"]/@href')
            magnet_info_detail_url_list = [
                urljoin(url, info) for info in magnet_info_list]

            with ThreadPoolExecutor(10) as executor:
                for info_url in magnet_info_detail_url_list:
                    executor.submit(
                        self._get_info,
                        info_url).add_done_callback(
                        self._pack_data)

        magnet_list = self.magnet_list
        return magnet_list

    def _get_info(self, url):
        r = self.session.get(url, headers=self.HEADERS)
        magnet = dict()
        magnet['magnet'] = r.html.xpath(
            "//a[@class='Information__magnet___vubvz']/@href")[0]
        magnet['magnet_name'] = r.html.xpath(
            "//p[@id='Information__title___3V6H-']/text()")[0]
        magnet['magnet_size'] = r.html.xpath(
            "//div[@class='Information__detail_information___1Mmca Information__content_information___1e4H7']/b[3]/text()")[0]
        magnet['magnet_date'] = r.html.xpath(
            "//div[@class='Information__detail_information___1Mmca Information__content_information___1e4H7']/b[4]/text()")[0]
        magnet['magnet_rank'] = r.html.xpath(
            "//div[@class='Information__detail_information___1Mmca Information__content_information___1e4H7']/b[5]/text()")[0]
        return magnet

    def _pack_data(self, magnet):
        ret = magnet.result()
        self.magnet_list.append(ret)


class btantHandler(BaseSearchMagnetHandler):
    def run(self, url, keyword, count, sort):
        print("=========collecting Data=============")
        pass


# ... 添加
