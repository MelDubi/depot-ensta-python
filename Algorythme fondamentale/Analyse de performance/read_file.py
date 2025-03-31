#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

def decode(filename):
    sepwords = re.compile("[^a-zA-Z']+")
    words = []
    with open(filename) as f:
        for line in f:
            for word in sepwords.split(line.strip()):
                if len(word) > 0:
                    words.append(word)
    return words

if __name__ == '__main__':
    decode('text.txt')
