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







@allure.feature("coinUpInterfaceTestForAndroid测试")
class TestInterface():

    #初始化请求头 TOKEN ,URL
    headers=headers,
    token=token,
    base_url=base_url
    #去除某个警告用的 删除也没事
    urllib3.disable_warnings()

    #获取市场行情
    #传入币对参数，获取对应价格
    @allure.title("行情列表")
    @pytest.mark.parametrize("contractId,symbol", yaml.safe_load(open("datas/marketPriceList.yaml")))
    def test_public_market_info(self,contractId,symbol):

        url = self.base_url + "/common/public_market_info"
        data = {"contractId":contractId,"sign":"8b6410c75c4d2cc549cad7fc5583a7b0","symbol":symbol,"time":"1652170832887"}
        data = json.dumps(data)

        r = requests.post(url=url, headers=headers, data=data, verify=False)
        print(r.request.body)

        indexPrice = json.dumps(r.json()["data"]["indexPrice"])
        msg = r.json()['msg']

        print(json.loads(r.content))
        print(r.status_code)
        print("指数价格:"+ indexPrice)
        assert msg== '成功'

        return indexPrice

    #U本位下单
    @allure.title("U本位下单")
    @pytest.mark.parametrize("contractId,leverageLevel,OPEN,positionType,price,side,volume", yaml.safe_load(open(
        "datas/openOrder.yaml")))
    def test_order_create(self,contractId,leverageLevel,OPEN,positionType,price,side,volume):
        # print(contractId)

        url = self.base_url + "/order/order_create"
        data = {"contractId":contractId,"expireTime":14,"isConditionOrder":"false","isOto":"false", "leverageLevel":leverageLevel,"open":OPEN,"positionType":positionType,"price":price,"side":side,"sign":"05f4f1ee5804114bad987d56166d2175","stopLossPrice":"0","stopLossTrigger":"", "stopLossType":"2","takerProfitPrice":"0","takerProfitTrigger":"","takerProfitType":"2",  "time":"1652349756240","triggerPrice":"","type":1,"volume":volume}
        data = json.dumps(data)

        r = requests.post(url=url, headers=headers, data=data, verify=False)
        #捕获异常， 如正常则 发送电报 信息：一切正常 ；
        try:
            assert r.json()['msg'] == '成功'
            url1 = "http://54.150.228.170/api/telegrambot/v1/sendMessage?username=BOT&text= 一切正常"
            re = requests.get(url1)
        except Exception as e:
            #  有异常则打印
            url1 = "http://54.150.228.170/api/telegrambot/v1/sendMessage?username=BOT&text= 这个接口有问题："+r.url
            re = requests.get(url1)



        print("订单号:{}".format(json.loads(r.content)))









        #
        # ids = json.dumps(r.json()["data"]["ids"])
        # ids = r.json()["data"]["ids"]
        # print(ids)
        # msg = r.json()['msg']
        # print(ids)
        # print(json.loads(r.content))
        # print(r.status_code)







