class Solution:
    def is_one_away_edit(self, str1: str, str2: str) -> bool:
        """Return True if the edit distance between str1 and str2 is one edit 
        unit away (insertion, deletion, or replacement) or below.
        """
        str1_len, str2_len = len(str1), len(str2)
        if abs(str1_len - str2_len) > 1:
            return False

        if str1_len < str2_len:
            return self.is_one_edit_insertion(str1, str2)
        elif str2_len < str1_len:
            return self.is_one_edit_insertion(str2, str1)
        else:
            return self.is_one_edit_replacement(str1, str2)


    def is_one_edit_insertion(self, short_str: str, long_str: str) -> bool:
        short_len, long_len = len(short_str), len(long_str)
        i, j = 0, 0
        has_editted = False
        while i < short_len and j < long_len:
            if short_str[i] != long_str[j]:
                if has_editted:
                    return False
                has_editted = True
                j += 1
            else:
                i += 1
                j += 1
        return True


    def is_one_edit_replacement(self, str1: str, str2: str) -> bool:
        has_editted = False
        for a, b in zip(str1, str2):
            if a != b:
                if has_editted:
                    return False
                has_editted = True
        return True
