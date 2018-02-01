#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:48:14 2018

@author: beartrap
"""

s = 'azcbobobegghakl'
longsub = ''
i = 0
first = 0
last = len(s) - (len(s) - 1)
longsublist = []


while i < len(s):
    if last < len(s):
        tempx = s[first]
        tempy = s[last]
        if s[first] < s[last]:
            if len(longsub) >= 2:
                print('appending: ' + tempy)
                longsublist.append(tempy)
                pass
                
                
            else:
                longsub = longsub + tempx + tempy
                pass
                
        i += 1
        first += 1
        last +=1   
        longsublist.append(longsub)
        pass
        
    elif s[first] > s[last]:
        first += 2
        last += 2
        longsub = ''
        print ('substring ended')
        pass


    
longsublist.sort(key=len, reverse=True)
print (longsublist)
longestsub = longsublist[0]

print ('the longest substring is: ' + longestsub)