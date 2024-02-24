from typing import Iterable


class BST:
    tree = None

    @classmethod
    def search_range(cls, sorted_array: Iterable[int], target: int) -> tuple:
        i_low = 0
        i_high = len(sorted_array) - 1
        cls.tree = sorted_array
        return cls._search_range(target, i_low, i_high)
    
    @classmethod
    def _search_range(cls, target: int, i_low: int, i_high: int) -> tuple:
        if i_high < i_low:
            return [-1, -1]

        i_mid = (i_low + i_high) // 2

        if target == cls.tree[i_mid]:
            result = [i_mid, i_mid]
            result_tmp_left = cls._search_range(target, i_low, i_mid-1)
            if result_tmp_left[0] != -1:
                result[0] = result_tmp_left[0]

            result_tmp_right = cls._search_range(target, i_mid+1, i_high)
            if result_tmp_right[1] != -1:
                result[1] = result_tmp_right[1]
            return result

        elif target < cls.tree[i_mid]:
            return cls._search_range(target, i_low, i_mid-1)
        elif target > cls.tree[i_mid]:
            return cls._search_range(target, i_mid+1, i_high)
        
        return [-1, -1]

if __name__ == "__main__":
    nums = [5,7,7,8,8,8,8,8,10]
    result = BST.search_range(nums, target=8) # [3, 7]
    print(result)
