def count_words(book):
    return len(book.split())

def count_characters(book):
    normalized = book.lower()
    occurrences = {}
    for c in set(normalized):
        occurrences.update({c: normalized.count(c)})
    return occurrences

def report_analysis(book, book_name):
    print('--- BEGIN BOOK ANALYSIS REPORT ---')

    print('Book:', book_name)

    print('Word analysis:', count_words(book), 'words.')

    print('Character analysis:')
    occurrences = count_characters(book)
    for c in sorted(occurrences, key=occurrences.get, reverse=True):
        print(f"{repr(c)} occurred {occurrences.get(c)} times.")

    print('--- END OF REPORT ---')

with open('./books/frankenstein.txt') as f:
    book = f.read()
    print(book)

    report_analysis(book, 'Frankenstein')
