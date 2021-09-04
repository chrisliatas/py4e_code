# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and
# numbers. You will extract all the numbers in the file and compute the sum of
# the numbers.

import re

fname = input("Enter file name: ")
if len(fname) < 1: fname = "regex_sum_37547.txt"
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

print(sum([int(i) for i in re.findall('[0-9]+', fh.read())]))
fh.close()
