class SecureList:
    result = []

    def __init__(self, base):
        self.base = list(base)

    def __getitem__(self, index):
        self.result = self.base[index]
        del self.base[index]
        return self.result

    
    def __str__(self):
        self.result = self.base.copy()
        self.base.clear()
        return str(self.result)
    

    def __repr__(self):
        self.result = self.base.copy()
        self.base.clear()
        return str(self.result)

    def __len__(self):
        i = 0
        for x in self.base:
            i = i + 1
        return i

base=[1,2,3,4]
a=SecureList(base)


print(a[0],base[0],"List returned wrong value.")
print(a[0],base[1],"List returned wrong value.")
print(len(a),2,"List hasn't deleted it's items once accessed")
print("current List: %s"%a)
print(len(a),0,"List Should be empty after printing")
a=SecureList(base)
print("current List: %r"%a)
print(len(a),0,"List Should be empty after printing a representation")