class Read_Txt():
    def readTxt(self):
        # 打开txt文件流
        with open('../DatePool/sjx.txt', 'r',encoding="utf-8") as f:
            # 通过文件流调用读取的方法读取数据--->所有行
            datas=f.readlines()
            # 新建列表 --》添加分割后的单行列表数据
            lines=[]
            for data in datas:
                # 把分割后的单行列表数据添加到整体的列中，并返回
                lines.append(data.strip().split(","))
            # 返回数据  [1:] 返回从下标1开始返回数据、）P“
            return lines[1:]
if __name__ == '__main__':
    print(Read_Txt().readTxt())