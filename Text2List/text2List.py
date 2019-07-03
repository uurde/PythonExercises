#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

path = 'D:/Solutions/Python/uur.txt'

wordList = []

wordsFile = open(path, 'r')

wordList = wordsFile.read().split(' ')

for word in wordList: 
    print(word)

for i in range(len(wordList)):
    print("{} {}".format(i + 1, wordList[i]))