import random

class SelectionSort:

    def sort_by_loop(self, *data, is_desc: bool) -> tuple:
        data = list(data)
        for round in range(len(data)):
            i_max = round
            for i in range(round, len(data)):
                i_max = self._swap(data, i_max, i, is_desc)
            data[round], data[i_max] = data[i_max], data[round]
        return tuple(data)
    
    
    def sort_by_recursion(self, *data, is_desc:bool) -> tuple:
        data = list(data)
        round = 0
        data = self._outer_recursive(data, round, is_desc)
        return tuple(data)
    

    def _outer_recursive(self, data, round, is_desc) -> tuple:
        if round >= len(data):
            return data
        
        i_max = round
        i = round
        i_max = self._inner_recursive(data, round, i_max, i, is_desc)
        data[round], data[i_max] = data[i_max], data[round]
        
        return self._outer_recursive(data, round+1, is_desc)
    

    def _inner_recursive(self, data, round, i_max, i, is_desc):
        if i >= len(data):
            return i_max
        
        i_max = self._swap(data, i_max, i, is_desc)

        return self._inner_recursive(data, round, i_max, i+1, is_desc)


    def _swap(self, data: list, i_max: int, i: int, is_desc: bool) -> int:
        if is_desc:
            return i if data[i_max] < data[i] else i_max
        else:
            return i if data[i_max] > data[i] else i_max


if __name__ == "__main__":
    random.seed(100)
    unsorted_nums = random.sample(range(10), 5)
    print(unsorted_nums)

    is_desc = False

    selection = SelectionSort()
    sorted_nums = selection.sort_by_loop(*unsorted_nums, is_desc=is_desc)
    print(sorted_nums)

    sorted_nums = selection.sort_by_recursion(*unsorted_nums, is_desc=is_desc)
    print(sorted_nums)
