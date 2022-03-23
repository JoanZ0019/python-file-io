#!/usr/bin/env python

##REGEX
import re
import sys

def word_search(re_pat_obj, inf):
    line_iterator = 1
    for line in inf:
        if re_pat_obj.findall(line):
            line = line.strip()
           # print(line)
            word_list = re.split('\.|,|\-| |;', line)
            word_list.sort()
            for word in word_list:
                if re_pat_obj.findall(word):  
                    print(str(line_iterator) + '\t' + word)
        line_iterator = line_iterator + 1

if __name__ == '__main__':
    re_pattern_string = r'[a-zA-Z]+herit[a-zA-Z]+'
    re_pattern_obj = re.compile(re_pattern_string, re.IGNORECASE)
    with open("origin.txt", "r") as infile:
        word_search(re_pattern_obj, infile)
