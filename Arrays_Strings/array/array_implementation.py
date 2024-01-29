class Array:

    def __init__(self, size=-1):
        self.array = None
        self._index_end = -1
        if size > 0:
            self._create_array(size)


    def __repr__(self) -> str:
        if not self.array:
            return str([])
        
        # array = []
        # for x in self.array:
        #     if x:
        #         array.append(x[0])
        # return str(array)

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
        pass


if __name__ == '__main__':
    arr = Array()
    print(arr)
    arr.add_by_value(3)
    print(arr)
    arr.add_by_value(5)
    print(arr)
