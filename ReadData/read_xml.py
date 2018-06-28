# 1. 导入XML包
from xml.dom import minidom
class Read_Xml():
    def read_xml(self, x, y, z):
        # 2. 加载解析 获取文档位置
        dom=minidom.parse('../DatePool/sjx.xml')
        # 3. 获取对象 获取book
        root=dom.documentElement
        # 4. 获取子元素 获取第几个位置bian，根据下标
        aas=root.getElementsByTagName(x)[y]
        # 5. 获取子元素值 获取bian内的下标元素
        return aas.getElementsByTagName(z)[0].firstChild.data

    def get_len(self,x):
        # 2. 加载解析 获取文档位置
        dom=minidom.parse('../DatePool/sjx.xml')
        # 3. 获取对象 获取book
        root=dom.documentElement
        return len(root.getElementsByTagName(x))

if __name__ == '__main__':
   print(Read_Xml().read_xml('bian', 5, 'b4'))
   print(Read_Xml().get_len('bian'))