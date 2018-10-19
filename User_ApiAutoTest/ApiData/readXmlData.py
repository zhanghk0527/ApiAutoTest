#-*-conding:utf-8-*-

# 导入minidom类库
from xml.dom import minidom

class readXmlData(object):
    # 自定义方法读取XML数据
    def returnXmlFile(self,fileName,first,second):
        # 用parse定位文件并打开，相对路径，两个点回到项目
        xmlFile=minidom.parse('../ApiData/'+fileName)
        # 获取一级标签名（一级标签名可相同，但为了方便，不取相同名字）
        oneNode=xmlFile.getElementsByTagName(first)[0]
        #基于一级标签获取二级标签的节点值
        twoNode=oneNode.getElementsByTagName(second)[0].childNodes[0].nodeValue
        # 返回节点值
        return twoNode
