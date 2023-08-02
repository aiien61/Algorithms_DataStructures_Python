"""
Check Permutation: Given two strings, determine if the two strings are the 
permutation of each other. 

Assume that two strings are ASCII encoding and they are not the permutation of
each other if they are identical.
"""
from collections import Counter


class Solution:
    def is_permutation_by_pythonic(self, A: str, B: str, **kwargs) -> bool:
        
        if len(A.strip()) != len(B.strip()):
            return False
        
        if A.strip().lower() == B.strip().lower():
            return False
        
        counter = Counter()
        for char in A.strip().lower():
            if char != " ":
                counter[char] += 1

        for char in B.strip().lower():
            if char == " ":
                continue
            if counter[char] == 0:
                return False
            counter[char] -= 1
        return True


    def is_permutation_by_count(self, A: str, B: str, **kwargs) -> bool:

        if kwargs.get("skip_whitespace", True):
            A = A.strip()
            B = B.strip()

        if A == B:
            return False
        
        if len(A) != len(B):
            return False
        
        if not kwargs.get("case_sensitive", False):
            A = A.lower()
            B = B.lower()

        length = len(A)
        count_array = [0] * 128
        for char in A:
            position = ord(char)
            count_array[position] += 1

        for char in B:
            position = ord(char)
            count_array[position] -= 1
            if count_array[position] < 0:
                return False
        
        for count in count_array:
            if count != 0:
                return False
        return True


    def is_permutation_by_sort(self, A: str, B: str, **kwargs) -> bool:
        
        if kwargs.get("skip_whitespace", True):
            A = A.strip()
            B = B.strip()
        
        if A == B:
            return False
        
        if len(A) != len(B):
            return False

        if not kwargs.get("case_sensitive", False):
            A = A.lower()
            B = B.lower()

        return sorted(list(A)) == sorted(list(B))
