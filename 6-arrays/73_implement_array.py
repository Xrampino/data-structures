class MyArray:
    def __init__(self):
        self.data = {}
        self.length = 0

    def __repr__(self):
        output = '['
        output += ', '.join(str(value) for value in self.data.values())
        output += ']'
        return output

    def push(self, i):
        self.data.update({self.length: i})
        self.length += 1

    def pop(self):
        deleted_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return deleted_item

    def get(self, i):
        return self.data.get(i)
    
    def insert_first(self, value):
        new_array = {}
        new_array.update({0: value})
        for key, value in self.data.items():
            new_array.update({key+1: value})
        self.data = new_array
        self.length += 1
    
a = MyArray()
a.push('toto')
a.push('tata')
a.push('tutu')
print(a)
a.pop()
print(a)
print(a.get(1))
a.insert_first('coco')
print(a)
print(a.length)