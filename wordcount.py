# put your code here.

import sys

word_count = {}


def count_words(file):
    file_name = open(file)
    for line in file_name:
        line = line.rstrip()
        words = line.split(" ")
        for word in words:
            word = word.strip(':.,"!();_\'?').lower()
            word_count[word] = word_count.get(word, 0) + 1

def print_dictionary(dictionary):
    for key, value in dictionary.iteritems():
        print key, value

text_file = sys.argv[1]

print sys.argv



# count_words(text_file)
# print_dictionary(word_count)

