# -- coding: utf-8 --
import json
import requests
import pytest
import os
import yaml
import logging
import urllib3
from tools import headers,token,base_url
class TestInterface():
    #初始化请求头 TOKEN ,URL
    headers=headers,
    token=token,
    base_url=base_url
    #去除某个警告用的 删除也没事
    urllib3.disable_warnings()



            #获取资产合约账户USDT  资金流水列
    # def test_get_transaction_list(self):
    #     url = self.base_url + "/record/get_transaction_list"
    #     data ={"limit":"20","page":"1","sign":"b2fe823d437c3a1c9f4d7f117c625749","symbol":"USDT","time":"1652163118641"}
    #     data=json.dumps(data)
    #     r = requests.post(url=url,headers=self.headers,data=data,verify=False)
    #     msg = r.json()['msg']
    #     logging.info(type(r))
    #     print(json.loads(r.content))
    #     print(r.status_code)
    #     assert msg== '成功'
    #
    # # 获取用户资产
    # def test_get_assets_list(self):
    #     url = self.base_url + "/position/get_assets_list"
    #     data = {"onlyAccount":"1","sign":"fce1439be853d2e0b6ae02186268f5f2","time":"1652170454889"}
    #     data = json.dumps(data)
    #     r = requests.post(url=url, headers=self.headers, data=data, verify=False)
    #     msg = r.json()['msg']
    #     logging.info(type(r))
    #     print(json.loads(r.content))
    #     print(r.status_code)
    #     assert msg == '成功'
    #
    #
    #
    # #获取用户配置
    # def test_get_user_config(self):
    #     url = self.base_url + "/user/get_user_config"
    #     data = {"contractId":"1","sign":"721566e6d01863eb6925911ab0da30ce","time":"1652170659655"}
    #     data = json.dumps(data)
    #     r = requests.post(url=url, headers=self.headers, data=data, verify=False)
    #     msg = r.json()['msg']
    #     print(msg)
    #     logging.info(type(r))
    #     print(json.loads(r.content))
    #     print(r.status_code)
    #
    #     assert msg == '成功'



    #获取市场行情
    # 传入币对参数，获取对应价格
    @pytest.mark.parametrize("contractId,symbol",yaml.safe_load(open("datas/orderCreate.yaml")))
    def test_public_market_info(self,contractId,symbol):
        url = self.base_url + "/common/public_market_info"
        data = {"contractId":contractId,"sign":"f780cbb68ab2d6c8a5d8a57b0d40583a","symbol":symbol,"time":"1652170832887"}
        data = json.dumps(data)
        r = requests.post(url=url, headers=headers, data=data, verify=False)
        indexPrice = json.dumps(r.json()["data"]["indexPrice"])
        msg = r.json()['msg']

        print(json.loads(r.content))
        print(r.status_code)
        print("指数价格:"+ indexPrice)
        assert msg== '成功'

        return indexPrice


    # U本位下单
    # def test_order_create(self):
    #     url = self.base_url + "/order/order_create"
    #     data = {"contractId":2,"expireTime":14,"isConditionOrder":"false","isOto":"false","leverageLevel":32,"open":"OPEN","positionType":"2","price":TestInterface.test_public_market_info(self),"side":"BUY","sign":"73e9f678d37b6189e7d2402184d2c3d7","stopLossPrice":"0","stopLossTrigger":"","stopLossType":"2","takerProfitPrice":"0","takerProfitTrigger":"","takerProfitType":"2","time":"1652171857422","triggerPrice":"","type":1,"volume":"2"}
    #     data = json.dumps(data)
    #     r = requests.post(url=url, headers=headers, data=data, verify=False)
    #     #
    #     # ids = json.dumps(r.json()["data"]["ids"])
    #     # ids = r.json()["data"]["ids"]
    #     # print(ids)
    #     msg = r.json()['msg']
    #     # print(ids)
    #     print(json.loads(r.content))
    #     print(r.status_code)
    #     assert msg== '成功'

# test_order_create()


