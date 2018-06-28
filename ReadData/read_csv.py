import csv
class Read_Csv():
    def read_Csv(self):
        with open('../DatePool/sjx.csv', 'r', encoding = 'utf-8')as f:
            reads = csv.reader(f)
            list = []
            for i in reads:
                list.append(i)
            return list

# if __name__ == '__main__':
#     Read_Csv().read_Csv()