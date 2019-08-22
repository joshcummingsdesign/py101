class Hashtable:

    def __init__(self, buckets = 10):
        self._table = []
        self._buckets = buckets
        self._initialize_table()

    def _initialize_table(self):
        for i in range(self._buckets):
            self._table.append([])

    def _hash_key(self, key):
        ordinal = 0
        for c in key:
            ordinal = ordinal + ord(c)
        return ordinal % self._buckets

    def _find(self, key):
        bucket = self._table[self._hash_key(key)]
        for entry in bucket:
            if entry[0] == key:
                return entry, bucket
        return False, bucket

    def add(self, key, value):
        entry, bucket = self._find(key)
        if entry:
            entry[1] = value
        else:
            bucket.append([key, value])

    def lookup(self, key):
        entry, bucket = self._find(key)
        if entry:
            return entry[1]
        return None


### Tests
ht = Hashtable(4)

ht.add('a', 'apple')
ht.add('b', 'banana')
ht.add('c', 'cherry')
ht.add('d', 'dongle')

print(ht.lookup('a')) # apple
print(ht.lookup('d')) # dongle
print(ht.lookup('e')) # None
print(ht._table) # [[['d', 'dongle']], [['a', 'apple']], [['b', 'banana']], [['c', 'cherry']]]
