import array

class Array:

    def __init__(self, data_type: str, value_list=None):
        self.array = None
        self._index_end = -1

        if self._validate_data_type(data_type):
            if data_type.lower().startswith('i'):
                self._required_data_type = int
            else:
                self._required_data_type = float

        if value_list:
            self._create_array(len(value_list))
            for value in value_list:
                self.add_by_value(value)


    def _validate_data_type(self, data_type: str) -> bool:
        if not isinstance(data_type, str):
            raise TypeError("Must use str to specify the data type.")
        
        acceptable_types = {"i", "int", "integer", "f", "float", "d", "double"}
        
        if data_type.lower() not in acceptable_types:
            raise TypeError("Data type must be integer or float.")
        
        return True
    
    def _validate_value_entry(self, value: (int, float)) -> (int, float):
        # value: int
        if isinstance(value, int):
            return self._required_data_type(value)
        
        # value: float
        if not isinstance(value, self._required_data_type):
            raise TypeError("floating value can't be inserted into int array.")
        else:
            return value
    

    def __repr__(self) -> str:
        if not self.array:
            value_list = str([])
        else:
            value_list = str([x[0] for x in self.array if x[0]])

        return f"array('{self._required_data_type}', {value_list})"


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


    def add_by_value(self, value: (int, float)) -> None:
        value = self._validate_value_entry(value)

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

    def add_by_index(self, index: int, value: (int, float)) -> None:
        if (index < 0) or (index > self._index_end + 1):
            return None
        
        value = self._validate_value_entry(value)

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


    def remove_by_value(self, value: (int, float)) -> None:
        i_found = None
        for i in range(self._index_end + 1):
            if self.array[i][0] == value:
                i_found = i
                break

        if not i_found:
            return None
        
        self.remove_by_index(i_found)
        return None


    def remove_by_index(self, index: (int, float)) -> int:
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
    arr = Array(data_type='Int')
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

    brr = array.array('i', [3, 5, 7, 5])
    print(brr)
