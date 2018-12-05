#-*-coding:utf-8-*-
import unittest
import sys
import os
from ApiCase import ApiAutoTestCase
from ApiLog.Api_AutoTestLog import createReport

# 返回当前文件所在的绝对路径
# __file__：获取当前文件的所在路径
curPath = os.path.abspath(os.path.dirname(__file__))

# 把文件路径分为：文件所在区域（dirname）和当前文件名(basename)，返回一个元组，取第一个元素（以0开始为第一个元素）
rootPath = os.path.split(curPath)[0]

# 把rootPath添加到环境变量，返回一个列表，执行时从该列表中搜索所需文件，如调用的ApiCase文件夹中的ApiAutoTestCase
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
