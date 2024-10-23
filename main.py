def count_words(book):
    # str.split() without argument split on any whitespace character, like
    # space, newline or tab
    return len(book.split())

# 1. Lowercase everything possible -> normalized content
# 2. Use a dictionary to store the distinct characters (by using set()) and
#    their respective counts
# 3. The result is an arbitrarily ordered dictionary
def count_characters_occurrences(book):
    normalized = book.lower()
    occurrences = {}
    for c in set(normalized):
        occurrences.update({c: normalized.count(c)})
    return occurrences

def report_analysis(book, book_name):
    # report header
    print('--- BEGIN BOOK ANALYSIS REPORT ---')

    print('Book:', book_name)

    print('Word analysis:', count_words(book), 'words.')

    print('Character analysis:')
    occurrences = count_characters_occurrences(book)
    # sort the characters (the dictionary keys) order based on their count (the
    # dictionary values), and because sorted() always use ascending order,
    # reverse it to get the largest count first
    for c in sorted(occurrences, key=occurrences.get, reverse=True):
        # repr() gets the representation of the string:
        # - Newline -> '\n'
        # - Single quote is double quoted ("'")
        # - Double quote is single quoted ('"')
        print(f"{repr(c)} occurred {occurrences.get(c)} times.")

    # report footer
    print('--- END OF REPORT ---')

with open('./books/frankenstein.txt') as f:
    book = f.read()
    print(book)

    report_analysis(book, 'Frankenstein')
