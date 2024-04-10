from collections import Counter

def count_occurences(word, words):
    words_dict = Counter(words.lower().split())
    return words_dict[word.lower()]

word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))