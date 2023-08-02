import string

class Solution:
    # O(n)
    def urlify_by_pythonic(self, chars: str, true_length: int):
        return chars[: true_length].replace(" ", "%20")

    # O(n)
    def urlify_by_array(self, chars: str, true_length: int) -> str:
        space_count = 0
        for i in range(true_length):
            if chars[i] == ' ':
                space_count += 1

        index = true_length + space_count * 2
        chars_list = [None] * index
        for i in range(true_length - 1, -1, -1):
            if chars[i] == " ":
                chars_list[index - 1] = "0"
                chars_list[index - 2] = "2"
                chars_list[index - 3] = "%"
                index -= 3
            else:
                chars_list[index - 1] = chars[i]
                index -= 1

        new_chars = ""
        for char in chars_list:
            new_chars += char
        return new_chars



if __name__ == "__main__":
    sol = Solution()
    print(sol.urlify_by_array('Mr John Smith', 13))
    print(sol.urlify_by_pythonic('Mr John Smith', 13))
    print(sol.urlify_by_array("Mr John Smith        ", 13))