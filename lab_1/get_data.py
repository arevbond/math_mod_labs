class TXT:
    def __init__(self, file):
        self.file = file

    def graphs_from_file(self):
        ''' ВЕРСИЯ С ВЫВОДОМ ИЗ ФАЙЛА ( сколько угодно графиков )'''
        file_name, file_end = self.file.split('.')
        if file_end  == self.__class__.__name__.lower():
            with open(self.file) as f:
                data = f.read()
            data = data.split('\n')
            new_data = []
            for j in range(len(data)):
                data_list = []
                for i in data[j].split(','):
                    l = []
                    for sym in i.split():
                        s = float(sym)
                        l.append(s)
                    data_list.append(tuple(l))
                new_data.append(tuple(data_list))
            data = tuple(new_data)
            return data

# t = TXT('data.txt')
# res = t.graphs_from_file()
# print(res)