# 导包 unittest 、三角形函数程序、读取json类
import unittest
from sjx.Code.sjx import Sjx
from sjx.ReadData.read_json import Read_Json


class Test_Json(unittest.TestCase):
    # 测试三角形
    def test001(self):
        for i in range(len(Read_Json().readJson())):
            # 调用三角形函数
            result=Sjx().sjx(int(Read_Json().readJson()[i]["b1"]),
                                int(Read_Json().readJson()[i]["b2"]),
                                int(Read_Json().readJson()[i]["b3"]))
            # 断言 三角形返回的结果是否与预期结果相符
            self.assertEqual(result,Read_Json().readJson()[i]["expect"])
            # 打印运行参数及结果
            print(Read_Json().readJson()[i]["b1"],
                  Read_Json().readJson()[i]["b2"],
                  Read_Json().readJson()[i]["b3"],
                  Read_Json().readJson()[i]["expect"],"--->通过！")

if __name__ == '__main__':
    unittest.main()