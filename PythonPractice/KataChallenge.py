#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:12:49 2018

@author: beartrap
"""




def spin_words(sentence):
    listsent = []
    finalsent = []
    listsent = sentence.split()
    i = 0
    for word in listsent:
        if len(word[i]) >= 5:
            length = len(word[i]) + 1
            for char in word:
                char = char[length]
                length -= 1
                i += 1
            finalsent.append(word)
        
        else:
            finalsent.append(word)
       
        
    return finalsent

spin_words('Welcome home')

print finalsent