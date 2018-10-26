#-*-coding:utf-8-*-
import unittest
import sys
import os
from ApiCase import ApiAutoTestCase
from ApiLog.Api_AutoTestLog import createReport
#当前目录上层目录的所有文件
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class ApiAutoTest(unittest.TestSuite):
    AutoSuite = unittest.TestSuite()
    AutoSuite.addTests(unittest.makeSuite(ApiAutoTestCase.ApiAutoTestCase))
    fileName = 'ApiAutoTestLoge'
    RevT = 'Test - 天气接口'
    revDes = 'Test - 天气接口'
    createReport().HTMLReporter(fileName, RevT, revDes, AutoSuite)

if __name__ == '__main__':
    unittest.main()
