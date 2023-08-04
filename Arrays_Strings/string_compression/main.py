class Solution:
    # O(n)
    def compress_string_by_brute_force(self, string: str) -> str:
        str_length = len(string)
        char_set = [None] * str_length
        counter = [0] * str_length
        i = 0
        j = i
        while i < str_length and j < str_length:
            if not counter[i]:
                char_set[i] = string[j]
                counter[i] += 1
                j += 1
                continue

            if string[j] == char_set[i]:
                counter[i] += 1
                j += 1
                continue

            i = j
        
        compressed = ''
        for i in range(len(counter)):
            if times := counter[i]:
                compressed += f"{char_set[i]}{times}"
        return compressed if len(compressed) < str_length else string
    

    # O(n)
    def compress_string(self, string: str) -> str:
        compressed = ""
        counter = 0

        for i in range(len(string)):
            if i != 0 and string[i] != string[i-1]:
                compressed += f"{string[i-1]}{counter}"
                counter = 0
            counter += 1

        compressed += f"{string[-1]}{counter}"

        return compressed if len(compressed) < len(string) else string
