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
    

    def book_report(self):
        word_count = self.word_count()
        letter_count = self.letter_count()
        sorted_letter_count = dict(sorted(letter_count.items()))
        print(f"--- Begin the report of {self.book_name} ---")
        print(word_count)
        for letter, count in sorted_letter_count.items():
            time = "times"
            if count != 1:
                time = "times"
            else:
                time = "time"
            print(f"The {letter} character was found {count} {time}")
        print(f"--- end of report on {self.book_name} ---")


frankenstien = Book("/home/mcfuddy/workspace/github.com/McFuddy2/bookbot/books/frankenstein.txt", "Frankenstien")

frankenstien.book_report()