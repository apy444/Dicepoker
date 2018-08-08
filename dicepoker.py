# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:34:04 2018

@author: AndiGabi
"""

import time
import random

dice ={1:["     ","  o  ","     "], 2:["o    ","     ","    o"],
       3:["o    ","  o  ","    o"], 4:["o   o","     ","o   o"],
       5:["o   o","  o  ","o   o"], 6:["o   o","o   o","o   o"]}


#This code will throw dicec, result stored in dict, where keys are a-e, values 1-6
#The argument is also a dict, in case, there is a previous result, 
#and this code chancd Docdge dices entered by the player
def throw(throw = {}):
    if throw == {}: #This is the initial throw, where dict is empty
        throw = {i:random.randrange(1,7) for i in 'abcde'}
    else: #This happen when there is a previous result of throw()
        change = input("\nMelyiket szeretnéd újra dobni?")
        for i in throw:
            if i in change:
                throw[i]=random.randrange(1,7)
    draw(throw) #The code draw the dices by calling draw() function
    return throw

#This function prints out the dices. The shape of dices stored in dice argumentum
def draw(throw):
    nums = [throw[i] for i in "abcde"]
    time.sleep(2)
    print("")
    for y in range(0,3):
        for x in nums:
            print("",dice[x][y],"      ", end="")
        print("")
    print("")
    print("   a            b            c            d            e")


first_throw = throw()
sec_throw = throw(first_throw)
third_throw = throw(sec_throw)
