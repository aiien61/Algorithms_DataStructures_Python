from typing import Iterable


class BST:
    def __init__(self, sorted_array: Iterable[int]):
        self.tree = sorted_array
        self.length = len(sorted_array)

    def search(self, value: int) -> tuple:
        i_start = 0
        i_end = self.length - 1
        return self._search(value, i_start, i_end)
    
    def _search(self, value: int, i_start: int, i_end: int) -> tuple:
        if i_start > i_end:
            return tuple()
        
        i_root = (i_start + i_end) // 2
        if value == self.tree[i_root]:
            return (value, i_root)
        elif value < self.tree[i_root]:
            return self._search(value, i_start, i_root-1)
        elif value > self.tree[i_root]:
            return self._search(value, i_root+1, i_end)
        return tuple()

    def search_leftmost(self, value: int) -> tuple:
        i_start = 0
        i_end = self.length - 1
        return self._search_leftmost(value, i_start, i_end)
    
    def _search_leftmost(self, value: int, i_start: int, i_end: int) -> tuple:
        if i_start > i_end:
            return tuple()

        i_root = (i_start + i_end) // 2
        if value == self.tree[i_root]:
            result = (value, i_root)
            result_tmp = self._search_leftmost(value, i_start, i_root-1)
            if result_tmp:
                result = result_tmp
            return result

        elif value < self.tree[i_root]:
            return self._search_leftmost(value, i_start, i_root-1)

        elif value > self.tree[i_root]:
            return self._search_leftmost(value, i_root+1, i_end)

        return tuple()


    def search_rightmost(self, value: int) -> tuple:
        i_start = 0
        i_end = self.length - 1
        return self._search_rightmost(value, i_start, i_end)
    
    def _search_rightmost(self, value: int, i_start: int, i_end: int) -> tuple:
        if i_start > i_end:
            return tuple()

        i_root = (i_start + i_end) // 2
        if value == self.tree[i_root]:
            result = (value, i_root)
            result_tmp = self._search_rightmost(value, i_root+1, i_end)
            if result_tmp:
                result = result_tmp
            return result

        elif value < self.tree[i_root]:
            return self._search_rightmost(value, i_start, i_root-1)

        elif value > self.tree[i_root]:
            return self._search_rightmost(value, i_root+1, i_end)

        return tuple()


if __name__ == "__main__":
    bst = BST([1,2,3,4,5,8,8,8,9])
    result = bst.search(8) # (8, 6)
    print(result)

    result = bst.search_leftmost(8)  # (8, 5)
    print(result)

    result = bst.search_rightmost(8) # (8, 7)
    print(result)
