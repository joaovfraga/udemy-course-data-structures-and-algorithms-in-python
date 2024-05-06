# Question 01 - Count Word Frequency

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']


def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


print(count_word_frequency(words))