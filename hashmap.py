class hash_map:
    def __init__(self, size=10, max_load_factor=0.75):
        self.size = size
        self.max_load_factor = max_load_factor
        self.num_items = 0
        self.num_buckets = 0
        self.buckets = [[] for i in range(self.size)]
        
    def clear(self):
        self.num_items = 0
        self.num_buckets = 0
        self.buckets = [[] for i in range(self.size)]
        
    def __setitem__(self, key, value):
        bucket_index = hash(key) % self.size
        bucket = self.buckets[bucket_index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.num_items += 1
        if len(bucket) == 1:
            self.num_buckets += 1
        load_factor = float(self.num_items) / float(self.size)
        if load_factor > self.max_load_factor:
            self.__rehash(2 * self.size + 1)
            
    def __getitem__(self, key):
        bucket_index = hash(key) % self.size
        bucket = self.buckets[bucket_index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        raise KeyError(key)
        
    def __delitem__(self, key):
        bucket_index = hash(key) % self.size
        bucket = self.buckets[bucket_index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                self.num_items -= 1
                if len(bucket) == 0:
                    self.num_buckets -= 1
                return
        raise KeyError(key)
        
    def __len__(self):
        return self.num_items
        
    def __get_load_factor(self):
        return float(self.num_items) / float(self.size)
        
    def __get_bucket_load_factor(self):
        return float(self.num_items) / float(self.num_buckets) if self.num_buckets > 0 else 0.0
        
    def __rehash(self, new_size):
        new_buckets = [[] for i in range(new_size)]
        for bucket in self.buckets:
            for key, value in bucket:
                new_bucket_index = hash(key) % new_size
                new_buckets[new_bucket_index].append((key, value))
        self.size = new_size
        self.buckets = new_buckets
        
    load_factor = property(__get_load_factor)
    bucket_load_factor = property(__get_bucket_load_factor)