from collections import Counter


class Solution:
    def is_string_rotation_by_brute_force(self, s1: str, s2: str) -> bool:
        """Return True if s1 is a rotation of s2."""
        s1 = s1.strip().lower()
        s2 = s2.strip().lower()

        if Counter(s1) != Counter(s2):
            return False
        
        head_index = []
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                head_index.append(i)
            
        for new_head in head_index:
            rotated_s1 = s1[new_head:] + s1[:new_head]
            if rotated_s1 == s2:
                return True
        
        return False
    
    def is_string_rotation_by_pythonic(self, s1: str, s2: str) -> bool:
        """Return True if s1 is a rotation of s2."""
        s1 = s1.strip().lower()
        s2 = s2.strip().lower()

        if len(s1) != len(s2):
            return False
        return self.is_substring_by_pythonic(s1, s2 + s2)


    def is_substring_by_array(self, s1: str, s2: str) -> bool:
        """Return True if s1 is a substring of s2."""
        s1_head_in_s2 = []
        for i in range(len(s2)):
            if s2[i] == s1[0]:
                s1_head_in_s2.append(i)

        n = len(s1)
        for i in s1_head_in_s2:
            try:
                if s2[i:n+1] == s1:
                    return True
            except IndexError:
                continue
        return False


    def is_substring_by_pythonic(self, s1: str, s2: str) -> bool:
        """Return True if s1 is a substring of s2."""
        return True if s1 in s2 else False
