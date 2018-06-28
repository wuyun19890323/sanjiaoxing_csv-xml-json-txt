# 导入模块
import unittest
from  whilt_test.lianxi.lianxi_whit.Cade.sjx import Sjx_pd
from whilt_test.lianxi.lianxi_whit.DateRead.sjx_txt import Sjx_txt

# 实例化三角函数
class_sjx = Sjx_pd()
class_txt = Sjx_txt()

class Test_txt(unittest.TestCase):
    def test_sjx(self):
        for i in range(len(class_txt.sjx_txt())):
            result = class_sjx.sjx_pd(int(class_txt.sjx_txt()[i][0]),
                                      int(class_txt.sjx_txt()[i][1]),
                                      int(class_txt.sjx_txt()[i][2]))

            self.assertEqual(result,class_txt.sjx_txt()[i][3])
            print(class_txt.sjx_txt()[i][0],
                  class_txt.sjx_txt()[i][1],
                  class_txt.sjx_txt()[i][2],
                  class_txt.sjx_txt()[i][3],'-------验证通过')
if __name__ == '__main__':
    unittest.main()