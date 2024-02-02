import random

class InsertionSort:

    def sort_by_loop(self, *data, is_desc: bool) -> tuple:
        data = list(data)
        for round in range(1, len(data)):
            for i in range(round, 0, -1):
                if self._need_swap(data[i - 1], data[i], is_desc):
                    data[i - 1], data[i] = data[i], data[i - 1]
                else:
                    break
        return tuple(data)
    
    
    def sort_by_recursion(self, *data, is_desc: bool) -> tuple:
        round = 0
        data = self._outer_recursive(list(data), round, is_desc)
        return tuple(data)
    
    def _outer_recursive(self, data, round, is_desc) -> list:
        if round >= len(data):
            return data
        
        for i in range(round, 0, -1):
            if self._need_swap(data[i - 1], data[i], is_desc):
                data[i - 1], data[i] = data[i], data[i - 1]
            else:
                break
        
        return self._outer_recursive(data, round+1, is_desc)
    
    def _inner_recursive(self, data: list, i: int, is_desc: bool) -> list:
        if i < 0:
            return data
        
        if self._need_swap(data[i - 1], data[i], is_desc):
            data[i - 1], data[i] = data[i], data[i - 1]
            return self._inner_recursive(data, i-1, is_desc)
        else:
            return data

    def _need_swap(self, x, y, is_desc: bool) -> bool:
        if is_desc:
            return x < y
        else:
            return y < x


if __name__ == "__main__":
    random.seed(100)
    unsorted_nums = random.sample(range(10), 5)
    print(unsorted_nums)

    insertion = InsertionSort()
    sorted_nums = insertion.sort_by_loop(*unsorted_nums, is_desc=False)
    print(sorted_nums)

    sorted_nums = insertion.sort_by_recursion(*unsorted_nums, is_desc=False)
    print(sorted_nums)
