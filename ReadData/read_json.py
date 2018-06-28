# 导包 json
import json
# 打开文件流
class Read_Json():
    def readJson(self):
        with open('../DatePool/sjx.json', 'r', encoding="utf-8") as f:
            datas=json.load(f)
            # 返回字典data键名对应的值
            return datas["data"]

if __name__ == '__main__':
    print(Read_Json().readJson())