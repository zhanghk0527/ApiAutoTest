#-*-coding:utf-8-*-
import unittest
from ApiCase import ApiAutoTestCase
from ApiLog.Api_AutoTestLog import createReport
class ApiAutoTest(unittest.TestSuite):
    AutoSuite = unittest.TestSuite()
    AutoSuite.addTests(unittest.makeSuite(ApiAutoTestCase.ApiAutoTestCase))
    fileName = 'ApiAutoTestLoge'
    RevT = 'Test - 天气接口'
    revDes = 'Test - 天气接口'
    createReport().HTMLReporter(fileName, RevT, revDes, AutoSuite)

if __name__ == '__main__':
    unittest.main()