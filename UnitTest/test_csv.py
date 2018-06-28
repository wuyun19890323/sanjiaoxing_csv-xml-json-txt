import unittest
from sjx.Code.sjx import Sjx
from sjx.ReadData.read_csv import Read_Csv
class Test_Csv(unittest.TestCase):
    def test_Csv(self):
        for i in range(len(Read_Csv().read_Csv())):
            result = Sjx().sjx(int(Read_Csv().read_Csv()[i][0]),
                               int(Read_Csv().read_Csv()[i][1]),
                               int(Read_Csv().read_Csv()[i][2]))
            self.assertEqual(result, Read_Csv().read_Csv()[i][3])
            print(Read_Csv().read_Csv()[i][0],
                  Read_Csv().read_Csv()[i][1],
                  Read_Csv().read_Csv()[i][2],
                  Read_Csv().read_Csv()[i][3],'--------验证成功')
if __name__ == '__main__':
    unittest.main()