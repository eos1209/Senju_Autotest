'''
@Created by jo
@Date : 2020/09/11
'''
import unittest
from data_config import showinpay_config
from base.showinpay_httpreuest import Showinpay_Http
from data_config.system_config import systemSetting
from base.HTMLTestReportCN import HTMLTestRunner



class User(unittest.TestCase):

    # def __init__(self, http):
    #     self.__http = http
    #     self.__connectionId = {}

    def setUp(self) -> None:
        self.__http = Showinpay_Http
        self.__connectionId = {}

    def test_login(self):
        path = 'https://dev-egate.oneclick-pay.com/user/Login/'
        data = {'username': showinpay_config.showinpay_Account,
                'password': showinpay_config.showinpay_Password}
        hedata = {'Content-Type': "application/json"}
        response_data = self.__http.post_login({}, path, data, hedata, {})

    # def info(self):
    #     # 取得資訊
    #     path = '/signalr/negotiate'
    #     data = {}
    #     response_data = self.__http.sendRequest('POST', path, data)
    #     self.__connectionId = response_data[1]['ConnectionId']
    #     return self.__connectionId

    def logout(self):
        path = '/Account/SignOut'
        data = {}
        self.__http.sendRequest('GET', path, data)

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())