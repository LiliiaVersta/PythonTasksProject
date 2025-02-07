class Book:
    def __init__(self, title, author, year_published):
        self.title = title                  
        self.author = author                
        self.year_published = year_published  

    def __str__(self):
        # Переопределяем метод __str__ для красивого строкового представления объекта
        return f"{self.title} by {self.author} (Published: {self.year_published})"

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(my_book)