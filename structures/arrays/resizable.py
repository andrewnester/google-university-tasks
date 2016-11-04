class ResizableArray(object):
    """Class representing resizable array implementation"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def __getitem__(self, key):
        self._check_index_range(key)

        return self.arr[key]

    def __setitem__(self, key, value):
        self._check_index_range(key)

        self.arr[key] = value

    def __delitem__(self, key):
        self._check_index_range(key)
        self.arr[key:] = self.arr[key+1:]
        self.size -= 1

        if self.size <= self.capacity / 2:
            self._reduce_array_capacity()

    def __len__(self):
        return self.size

    def append(self, value):
        if self.size == self.capacity:
            self._double_array_capacity()

        self.arr[self.size] = value
        self.size += 1

    def _double_array_capacity(self):
        self.capacity *= 2

        new_arr = [None] * self.capacity
        for index, value in enumerate(self.arr):
            new_arr[index] = self.arr[index]

        self.arr = new_arr

    def _reduce_array_capacity(self):
        self.capacity = 1 if self.capacity == 1 else int(self.capacity / 2)

        new_arr = [None] * self.capacity
        if len(self.arr) != 0:
            for index, value in enumerate(new_arr):
                new_arr[index] = self.arr[index]

        self.arr = new_arr

    def _check_index_range(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index our of range')
