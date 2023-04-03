class hash_map:
    def __init__(self, size=10, load_factor=0.75):
        self.size = size
        self.load_factor = load_factor
        self.count = 0
        self.table = [[] for _ in range(size)]
    
    def clear(self):
        self.table = [[] for _ in range(self.size)]
        self.count = 0
    
    def __setitem__(self, key, value):
        index = hash(key) % self.size
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1
        if self.count > self.size * self.load_factor:
            self._resize(2 * self.size + 1)
    
    def __getitem__(self, key):
        index = hash(key) % self.size
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)
    
    def __delitem__(self, key):
        index = hash(key) % self.size
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return
        raise KeyError(key)
    
    def __len__(self):
        return self.count
    
    def load_factor(self):
        return self.count / self.size
    
    def current_load(self):
        return sum(len(lst) for lst in self.table) / len(self.table)
    
    def _resize(self, new_size):
        new_table = [[] for _ in range(new_size)]
        for lst in self.table:
            for k, v in lst:
                index = hash(k) % new_size
                new_table[index].append((k, v))
        self.size = new_size
        self.table = new_table
