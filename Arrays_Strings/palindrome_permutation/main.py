from collections import Counter
from string import ascii_letters, ascii_lowercase


class Solution:
    # O(n)
    def is_palindrome_permutation_by_hash(self, text: str) -> bool:
        text_length = len(text)
        char_set = [0] * text_length
        
        for char in text:
            if char in ascii_letters:
                position = hash(ord(char.lower())) % text_length
                char_set[position] += 1
        
        singles = 0
        for count in char_set:
            singles += count % 2
        
        return True if singles <= 1 else False

    # O(n)
    def is_palindrome_permutationi_by_pythonic(self, text: str) -> bool:
        counter = Counter(text.lower().strip())
        singles = 0
        for char in text:
            if char in ascii_lowercase:
                singles += counter[char] % 2
        return True if singles <= 1 else False
