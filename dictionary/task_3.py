# Словарь с вложенными данными

books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}
for book_key, book_info in books.values():
    title = book_info["title"]
    author = book_info["author"]
    year = book_info["year"]
    print(f"Book: {title}, Author: {author}, Year: {year}")