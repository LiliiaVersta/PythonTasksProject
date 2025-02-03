# Фильтрация слов по первой букве (filter и lambda)

words = ["apple", "banana", "cherry", "apricot", "blueberry"]
target_letter = "a"  # Буква, по которой фильтруем

# list(filter(...)) - filter() возвращает итерируемый объект, поэтому мы оборачиваем его в list(), чтобы получить список
filtered_words = list(filter(lambda word: word.startswith(target_letter), words))

print(filtered_words)