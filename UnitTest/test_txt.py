# 导包 unittest、三角形、txt读取
import unittest
from sjx.Code.sjx import Sjx
from sjx.ReadData.read_txt import Read_Txt
# 实例化三角形
sjxClass=Sjx()
# 实例化txt
readTxtClass=Read_Txt()

class Test_Txt(unittest.TestCase):
    # 测试三角形程序
    def test001(self):
        for i in range(len(readTxtClass.readTxt())):
            # 调用三角形方法
            result=sjxClass.sjx(int(readTxtClass.readTxt()[i][0]),
                                int(readTxtClass.readTxt()[i][1]),
                                int(readTxtClass.readTxt()[i][2]))
            # 调用断言，判断三角形程序执行后的结果是否与预期结果相符
            self.assertEqual(result,readTxtClass.readTxt()[i][3])
            # 为了查看方便，我把执行成功后的数据打印一下
            print(readTxtClass.readTxt()[i][0],
                  readTxtClass.readTxt()[i][1],
                  readTxtClass.readTxt()[i][2],
                  readTxtClass.readTxt()[i][3],"-->通过！")

if __name__ == '__main__':
    unittest.main()