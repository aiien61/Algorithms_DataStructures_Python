class BubbleSort:
    def sort_by_loop(self, *data, is_desc: bool):
        data = list(data)
        for round in range(len(data)):
            length = len(data) - round
            for i in range(1, length):
                data[i - 1], data[i] = self._swap(data[i - 1], data[i], is_desc)
        return tuple(data)
    

    def sort_by_recursion(self, *data, is_desc: bool):
        round = 0
        data = list(data)
        data = self._outer_recursive(data, round, is_desc)
        return tuple(data)


    def _outer_recursive(self, data, round, is_desc) -> tuple:
        # end condition
        if len(data) - 1 < round:
            return data
        
        # main logic
        length = len(data) - round
        data = self._inner_recursive(data, length, 1, is_desc)
        
        # data flow
        round += 1
        return self._outer_recursive(data, round, is_desc)
    
    def _inner_recursive(self, data, length, i, is_desc):
        if i >= length:
            return data

        data[i - 1], data[i] = self._swap(data[i - 1], data[i], is_desc)

        return self._inner_recursive(data, length, i+1, is_desc)


    def _swap(self, x, y, is_desc: bool):
        if is_desc:
            return (y, x) if x < y else (x, y)
        else:
            return (y, x) if x > y else (x, y)
        



if __name__ == "__main__":
    bubble = BubbleSort()
    unsorted_list = [6, 2, 4, 10, 8]

    sorted_list = bubble.sort_by_loop(*unsorted_list, is_desc=False)
    print(sorted_list)

    sorted_list = bubble.sort_by_recursion(*unsorted_list, is_desc=False)
    print(sorted_list)
