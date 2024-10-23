def count_words(book):
    return len(book.split())

def count_characters(book):
    normalized = book.lower()
    occurrences = {}
    for c in set(normalized):
        occurrences.update({c: normalized.count(c)})
    return occurrences

with open('./books/frankenstein.txt') as f:
    book = f.read()
    print(book)

    print('The book contains', count_words(book), 'words.')

    occurrences = count_characters(book)
    print(occurrences)
