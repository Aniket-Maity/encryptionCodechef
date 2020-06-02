# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 07:20:02 2020

@author: Aniket Maity
"""

N = 9999
arr = []
T = input()
N = int(T)
while(N !=0):
    
    newStr = ''
    newStr = '%02d' %(int(T[0])*int(T[1])) + '%02d' %(int(T[1])*int(T[2]))
    
    sumLastPart ='%02d' %((int(T[0])*int(T[1])) + (int(T[1])*int(T[2])))
    
    sumLastPart = sumLastPart[::-1]
    newStr +=sumLastPart
    arr.append(newStr)
    T = input()
    N = int(T)


for item in arr:
    print(item)