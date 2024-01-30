class Array:

    def __init__(self, size=-1):
        self.array = None
        self._index_end = -1
        if size > 0:
            self._create_array(size)


    def __repr__(self) -> str:
        if not self.array:
            return str([])

        return str([x[0] for x in self.array if x[0]])


    def _create_array(self, size: int) -> None:
        self.array = tuple([None] for _ in range(size))
        return None


    def _expand_array(self) -> None:
        new_size = len(self.array) * 2
        new_array = tuple([None] for _ in range(new_size))
        for i in range(len(self.array)):
            new_array[i][0] = self.array[i][0]
        self.array = new_array
        return None


    def add_by_value(self, value: int) -> None:
        if not self.array:
            self._create_array(size=1)
            self.array[0][0] = value
            self._index_end += 1
            return None
        
        if self.array[-1]:
            self._expand_array()

        self.array[self._index_end + 1][0] = value
        self._index_end += 1
        return None


    def add_by_index(self, index: int, value: int) -> None:
        if (index < 0) or (index > self._index_end + 1):
            return None
        
        for i in range(self._index_end, index-1, -1):
            self.array[i + 1][0] = self.array[i][0]
        
        self.array[index][0] = value
        self._index_end += 1

        if (self._index_end + 1) == len(self.array):
            self._expand_array()
        
        return None
    

    def search_by_value(self, value: int) -> int:
        for x in self.array:
            if x[0] == value:
                return x[0]
        return None


    def search_by_index(self, index: int) -> int:
        if (index < 0) or (index > self._index_end):
            return None
        
        return self.array[index][0]


    def remove_by_value(self, value: int) -> None:
        i_found = None
        for i in range(self._index_end + 1):
            if self.array[i][0] == value:
                i_found = i
                break

        if not i_found:
            return None
        
        self.remove_by_index(i_found)
        return None


    def remove_by_index(self, index: int) -> int:
        if (index < 0) or (index > self._index_end):
            return None
        
        if index == self._index_end:
            self.array[index][0] = None
        else:
            for i in range(index + 1, self._index_end + 1):
                self.array[i - 1][0] = self.array[i][0]
                self.array[i][0] = None
        
        self._index_end -= 1
        return None


if __name__ == '__main__':
    arr = Array()
    arr.add_by_value(3)
    arr.add_by_value(5)
    arr.add_by_value(7)
    arr.add_by_value(5)
    arr.add_by_index(index=1, value=9)
    print(arr)
    x = arr.search_by_value(19)
    print(x)
    arr.remove_by_value(5)
    print(arr)
