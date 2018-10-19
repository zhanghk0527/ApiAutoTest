#coding:utf-8
# 导入生成测试报告模块
import HTMLTestRunner,time
class createReport(object):
    # 定义方法，并接受调用模块传递的参数
    def HTMLReporter(self,fileName,RevT,revDes,revTest):
        # 获取当前时间，并供日志名称使用
        now = time.strftime("%Y-%m-%d %H_%M",time.localtime())
        # 找到存储的测试报告报告名称+当前时间，公用模块不能写死
        fileHtmlName="../ApiLog/"+fileName+now+".html"
        # 打开测试报告，以二进制形式写入，并存储在内存空间中
        with open(fileHtmlName,'wb') as htmlSteam:
            # 使用HTMLTestRunner生存具体内容
            HTMLTestRunner.HTMLTestRunner(

                # 文本流（文本流向内存空间）
                stream=htmlSteam,
                # 报告详细级别，共10个级别（1——10），默认1
                # 无论多少条用例只会有一个结果，2有多少条就会有多少条结果，若失败会有错误信息，成功显示pass
                verbosity=3,
                # 报告标题，公用不能写死，用变量，谁使用谁传参
                title=RevT,
                # 具体描述信息，对应详细每条用例描述，不能写死，谁用谁传递参数
                description=revDes
            ).run(revTest)#需要运行用例才会有报告，所以最后运行，谁用谁传参数，但那个模块使用不能使用之前运行方法，需调用封装的方法，且传递参数
