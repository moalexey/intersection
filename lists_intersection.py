# -*- coding: UTF-8 -*-
import re

'''Intersection of words in files
'''

my_text_1_filename = 'my_text_1.txt'
my_text_2_filename = 'my_text_2.txt'
my_result_filename  = 'unique_words.txt'

text_1_file = open(my_text_1_filename).read().decode('utf8').lower()
text_2_file = open(my_text_2_filename).read().decode('utf8').lower()

# Remove all non-alphanumeric
wordlist_1 = re.compile(r'\W+', re.UNICODE).split(text_1_file)
wordlist_2 = re.compile(r'\W+', re.UNICODE).split(text_2_file)

# Intersection
unique_words = set.intersection(*map(set, [filter(None, wordlist_1), filter(None, wordlist_2)]))

# Write result in file
with open(my_result_filename, 'w') as result:
    for word in unique_words:
        result.write('{w}\n'.format(w=word.encode('utf8')))
