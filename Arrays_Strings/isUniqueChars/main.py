import string

def has_unique_chars_by_set(chars: str) -> bool:
    char_set = set()
    for char in chars:
        if char in char_set:
            return False
        char_set.add(char)
    return True


def has_unique_chars_by_array(chars: str) -> bool:
    # Assume all characters are ASCII encoding
    if len(chars) > 128:
        return False

    char_array = [False] * 128
    for char in chars:
        position = ord(char)
        if char_array[position]:
            return False
        char_array[position] = True
    return True


def has_unique_chars_by_hash(chars: str) -> bool:
    all_chars = len(string.ascii_letters) + len(string.digits) + len(string.punctuation)
    char_array = [False] * all_chars
    for char in chars:
        position = ord(char) % all_chars
        if char_array[position]:
            return False
        char_array[position] = True
    return True
