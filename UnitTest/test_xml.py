import unittest
from sjx.Code.sjx import Sjx
from sjx.ReadData.read_xml import Read_Xml
class Test_Xml(unittest.TestCase):
    def test_xml(self):
        for i in range(Read_Xml().get_len('bian')):
            result = Sjx().sjx(int(Read_Xml().read_xml('bian', i, 'b1')),
                               int(Read_Xml().read_xml('bian', i, 'b2')),
                               int(Read_Xml().read_xml('bian', i, 'b3')))

            self.assertEqual(result, Read_Xml().read_xml('bian',i,'b4'))
            print(Read_Xml().read_xml('bian', i, 'b1'),
                  Read_Xml().read_xml('bian', i, 'b2'),
                  Read_Xml().read_xml('bian', i, 'b3'),
                  Read_Xml().read_xml('bian', i, 'b4'), '--------验证成功')

if __name__ == '__main__':
    unittest.main()