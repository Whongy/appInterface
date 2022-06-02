# -- coding: utf-8 --
import json
import requests
import pytest
import os
import yaml
import logging
import urllib3
import allure
#调用上级目录的tools.py文件 出现报错 添加路径搜索
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from tools import headers,token,base_url
@allure.feature("coinUpInterfaceTestForAndroid-测试")
class TestUserConfig():

    #初始化请求头 TOKEN ,URL
    headers=headers,
    token=token,
    base_url=base_url
    #去除某个警告用的 删除也没事
    urllib3.disable_warnings()

    #获取资产合约账户USDT  资金流水列
    @allure.title("资金流水列表")
    def test_get_transaction_list(self):
        url = self.base_url + "/record/get_transaction_list"
        data ={"limit":"20","page":"1","sign":"06464ca6c708ea70cac6c2d59304982f","symbol":"USDT","time":"1652422764695"}
        data=json.dumps(data)
        r = requests.post(url=url,headers=headers,data=data,verify=False)
        msg = r.json()['msg']
        logging.info(type(r))
        print(json.loads(r.content))
        print(r.status_code)
        assert msg== '成功'

    # 获取用户资产
    @allure.title("用户资产")
    def test_get_assets_list(self):
        url = self.base_url + "/position/get_assets_list"
        data = {"onlyAccount":"1","sign":"7c1f8aacc36b3a33a45fecdf31791567","time":"1652422726349"}
        data = json.dumps(data)
        r = requests.post(url=url, headers=headers, data=data, verify=False)
        msg = r.json()['msg']
        logging.info(type(r))
        print(json.loads(r.content))
        print(r.status_code)
        assert msg == '成功'



    #获取用户配置
    @allure.title("用户配置")
    def test_get_user_config(self):
        url = self.base_url + "/user/get_user_config"
        data = {"contractId":"47","sign":"e58b289c4475befa7d7ed4af14368a53","time":"1652422830722"}
        data = json.dumps(data)
        r = requests.post(url=url, headers=headers, data=data, verify=False)
        msg = r.json()['msg']
        print(msg)
        logging.info(type(r))
        print(json.loads(r.content))
        print(r.status_code)

        assert msg == '成功'


    def test_history_position_list(self):
        url = self.base_url + "/position/history_position_list"
        data = {"contractId":"14","limit":"20","page":"1","sign":"49fa1de632ba74f41cdbdc4823367337","time":"1652239361601"}
        data = json.dumps(data)
        r = requests.post(url=url, headers=headers, data=data, verify=False)
        msg = r.json()['msg']
        print(msg)
        logging.info(type(r))
        print(json.loads(r.content))
        print(r.status_code)

        assert msg == '成功'


    @allure.title("用户总资产BTC核算")
    def test_get_total_balance(self):
        url = "https://appapi.coin-up.pro/finance/features/total_account_balance"
        data = {"sign":"a482b287ccd12003024287d11957ca67","time":"1654075569327"}
        data = json.dumps(data)

        r = requests.post(url=url, headers=headers, data=data, verify=False)

        msg = r.json()['msg']
        logging.info(type(r))

        print(json.loads(r.content))
        assert msg =='Succeed'


    @allure.title("获取快捷买卖价格")
    def test_get_quickly_buy_price(self):
        url = "https://appapi.coin-up.pro/quickly_buy_coins/get_symbol_price"
        data = {"getCoin": "AAVE", "payCoin": "AUD", "quantity": "12", "side": "buy",
                "sign": "fca8109cb54f1e3cfb809029e0339a19", "time": "1654157837523"}
        data = json.dumps(data)

        r = requests.post(url=url, headers=headers, data=data, verify=False)
        print(r.json())

        code = r.json()["code"]
        msg = r.json()['msg']

        print(code)
        logging.info(type(r))
        print(json.loads(r.content))
        assert code == '0'
        assert msg == 'Succeed'







