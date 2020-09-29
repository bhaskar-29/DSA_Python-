class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, val):
        h = 0
        for char in val:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, item):
        h = self.get_hash(item)
        for k in self.arr[h]:
            if k[0] == item:
                return k[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
            if not found:
                self.arr[h].append((key, value))

    def __delattr__(self, item):
        h = self.get_hash(item)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == item:
                del self.arr[h][idx]




