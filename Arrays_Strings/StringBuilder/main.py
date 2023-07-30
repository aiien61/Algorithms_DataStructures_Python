import numpy as np


def join_words(words: list) -> str:
    sentence = ""
    for word in words:
        sentence += word
    return sentence


def join_words_by_array_stringbuilder(words: list) -> str:
    class StringBuilder:
        def __init__(self):
            self.string = np.full(1, None)
            self.current = 0

        def append(self, word: str):
            try:
                if not self.string[-1]:
                    self.string[self.current] = word
                else:
                    new_string = np.full(len(self.string) * 2, None)
                    for i, char in enumerate(self.string):
                        new_string[i] = char
                    self.string = new_string
                    self.string[self.current] = word
            finally:
                self.current += 1

        def to_string(self):
            sentence = ''
            for word in self.string:
                if word:
                    sentence += word
            return sentence

    sentence = StringBuilder()
    for word in words:
        sentence.append(word)
    return sentence.to_string()


def join_words_by_linkedlist_stringbuilder(words: list) -> str:
    class Char:
        def __init__(self, data: str):
            self.data = data
            self.next = None
            self.prev = None


    class StringBuilder:
        def __init__(self):
            self.head = None
            self.last = None

        def append(self, word) -> None:
            char = Char(data=word)
            if not self.head:
                self.head = char
                self.last = char
            else:
                self.last.next = char
                char.prev = self.last
                self.last = char
            return None

        def to_string(self) -> str:
            sentence = ''
            char = self.head
            while char:
                sentence += char.data
                char = char.next
            return sentence
    
    sentence = StringBuilder()
    for word in words:
        sentence.append(word)
    return sentence.to_string()



def main():
    fruits = ['apple', 'pineapple', "banana", "orange", "grape", "pear"]
    print(join_words(fruits))
    print(join_words_by_array_stringbuilder(fruits))
    print(join_words_by_linkedlist_stringbuilder(fruits))


if __name__ == "__main__":
    main()
