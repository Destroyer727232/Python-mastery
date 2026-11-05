class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def show(self):
        print(f"{self.title} by {self.author}")

class EBook(Book):
    def __init__(self,title,author,file_size_mb):
        super().__init__(title,author)
        self.file_size_mb = file_size_mb

    def show_size(self):
        print(f"File size: {self.file_size_mb} MB")

ebook1 = EBook("The Hobbit","J.R.Tolkien",20)
ebook1.show()
ebook1.show_size()
