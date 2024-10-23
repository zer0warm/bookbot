def count_words(book):
    return len(book.split())

with open('./books/frankenstein.txt') as f:
    book = f.read()
    print(book)
    print('The book contains', count_words(book), 'words.')
