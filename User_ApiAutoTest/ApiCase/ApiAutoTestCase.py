#-*-coding:utf-8-*-
'''
----------------------------接口说明--------------------------
接口功能：查询城市天气
接口Url：https://www.apiopen.top/weatherApi
请求方式：get/post
请求参数：city  必填  string
'''
import unittest,requests,json
from ApiData.readXmlData import readXmlData

class ApiAutoTestCase(unittest.TestCase):
    def setUp(self):
        self.Url = "https://www.apiopen.top/weatherApi"
    def test_case(self):
        CityName = readXmlData().returnXmlFile("ApiTestData.xml","test_case","city")
        self.Value = {
            "city": CityName
        }
        requestMsg = requests.post(self.Url,self.Value)
        requestMsgText = json.loads(requestMsg.text)
        try:
            self.assertEqual(requestMsg.status_code,200)
            self.assertEqual(requestMsgText["code"],200)
            self.assertEqual(requestMsgText["msg"],"成功!")
            print ("执行成功：",requestMsgText["data"]["city"],requestMsgText["data"]["forecast"][0])
        except Exception as e:
            print ("执行失败：",requestMsgText)
    def tearDown(self):
        pass
