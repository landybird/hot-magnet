# encoding : utf-8
# __author__ = 'jm'
# encoding : utf-8
# __author__ = 'jm'

from fake_useragent import UserAgent



class BaseSearchMagnetHandler(object):
    HEADERS = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': UserAgent().random
    }



class cilimaoHandler(BaseSearchMagnetHandler):
    def run(self, keyword, count, sort):
        print("=========collecting Data=============")
        pass

class btantHandler(BaseSearchMagnetHandler):
    def run(self, keyword, count, sort):
        print("=========collecting Data=============")
        pass


# ... 添加
