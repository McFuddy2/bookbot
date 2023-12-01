class Book:
    def __init__(self, book_path, book_name):
        self.book_path = book_path
        self.book_name = book_name
        self.text = []
        
        
    def __get_text(self):
        with open(self.book_path) as f:
            self.text = f.read()
            return self.text

    def word_count(self):
        self.__get_text()
        words = self.text.split()
        word_count = len(words)
        return (f"{word_count} words found in {self.book_name}")
    

    def letter_count(self):
        self.__get_text()
        words = self.text.split()
        for i in range(len(words)):
            words[i] = words[i].lower()
        letters = {}
        for word in words:
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
        return letters


frankenstien = Book("/home/mcfuddy/workspace/github.com/McFuddy2/bookbot/books/frankenstein.txt", "Frankenstien")

print(frankenstien.word_count())