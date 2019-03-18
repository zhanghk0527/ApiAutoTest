#-*-coding:utf-8-*-
'''
----------------------------接口说明--------------------------
接口功能：查询城市天气
接口Url：https://www.apiopen.top/weatherApi
请求方式：get/post
请求参数：city  必填  string
'''
import unittest
import requests
import json
from ApiData.readXmlData import readXmlData

class ApiAutoTestCase(unittest.TestCase):
    def setUp(self):
        # 请求的Url
        self.Url = "https://www.apiopen.top/weatherApi"
    def test_case(self):
        # 定位数据，并把值赋给CityName
        CityName = readXmlData().returnXmlFile("ApiTestData.xml","test_case","city")
        self.Value = {
            "city": CityName  # 调用CityName的数据
        }
        requestMsg = requests.post(self.Url,self.Value)   # 使用requests扩展库中的post请求方法（url = ,header = ,Data = ）
        requestMsgText = json.loads(requestMsg.text)     # json.loads，解析成Python可识别的数据
        try:
            self.assertEqual(requestMsg.status_code,200)
            self.assertEqual(requestMsgText["code"],200)
            self.assertEqual(requestMsgText["msg"],"成功!")
            print ("执行成功：",requestMsgText["data"]["city"],requestMsgText["data"]["forecast"][0])
        except Exception as e:
            print ("执行失败：",requestMsgText,"|","异常信息：",e)
    def tearDown(self):
        pass
