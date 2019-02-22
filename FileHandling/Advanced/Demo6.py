class MyIterator:
    def  __iter__(self):
        self.no = 1
        return self

    def __next__(self):
            self.no = self.no*2
            return self.no

my = MyIterator()
i = my.__iter__()
for x in i:
    print(x)