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




    #获取市场行情
    #传入币对参数，获取对应价格
    # @allure.title("行情列表")
    # @pytest.mark.parametrize("contractId,symbol", yaml.safe_load(open("../datas/orderCreate.yaml")))
    # def test_public_market_info(self,contractId,symbol):
    #
    #     url = self.base_url + "/common/public_market_info"
    #     data = {"contractId":contractId,"sign":"8b6410c75c4d2cc549cad7fc5583a7b0","symbol":symbol,"time":"1652170832887"}
    #     data = json.dumps(data)
    #
    #     r = requests.post(url=url, headers=headers, data=data, verify=False)
    #     print(r.request.body)
    #
    #     indexPrice = json.dumps(r.json()["data"]["indexPrice"])
    #     msg = r.json()['msg']
    #
    #     print(json.loads(r.content))
    #     print(r.status_code)
    #     print("指数价格:"+ indexPrice)
    #     assert msg== '成功'
    #
    #     return indexPrice
    #
    # #U本位下单
    # @allure.title("U本位下单")
    # @pytest.mark.parametrize("contractId,leverageLevel,OPEN,positionType,price,side,volume", yaml.safe_load(open(
    #     "../datas/openOrder.yaml")))
    # def test_order_create(self,contractId,leverageLevel,OPEN,positionType,price,side,volume):
    #     # print(contractId)
    #     url = self.base_url + "/order/order_create"
    #     data = {"contractId":contractId,"expireTime":14,"isConditionOrder":"false","isOto":"false", "leverageLevel":leverageLevel,"open":OPEN,"positionType":positionType,"price":price,"side":side,"sign":"05f4f1ee5804114bad987d56166d2175","stopLossPrice":"0","stopLossTrigger":"", "stopLossType":"2","takerProfitPrice":"0","takerProfitTrigger":"","takerProfitType":"2",  "time":"1652349756240","triggerPrice":"","type":1,"volume":volume}
    #     data = json.dumps(data)
    #
    #     r = requests.post(url=url, headers=headers, data=data, verify=False)
    #
    #     msg =r.json()["msg"]
    #     print("订单号:{}".format(json.loads(r.content)))
    #     #
    #     # ids = json.dumps(r.json()["data"]["ids"])
    #     # ids = r.json()["data"]["ids"]
    #     # print(ids)
    #     # msg = r.json()['msg']
    #     # print(ids)
    #     # print(json.loads(r.content))
    #     # print(r.status_code)
    #     assert msg== '成功'




