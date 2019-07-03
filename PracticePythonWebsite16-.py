#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:26:48 2019

@author: peterle
"""

import random
def generateHard_pwd():
    
    string = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()'
    
    
    p = "".join(random.sample(string,9))
    
    print (p) 
generateHard_pwd()

def generateEasy_pwd():
    string_ez = 'qwertyuiopasdfghjklzxcvbnm'
    
    pwd ="".join(random.sample(string_ez,6))
    
    print(pwd)

generateEasy_pwd()
def choice():
    u_choice = str(input("Do you want a complicated pwd that no one can guess? y/n  \n "))
    
    if u_choice == 'y':
        generateHard_pwd()
    
        return choice()

    elif u_choice == 'n': 
        generateEasy_pwd()
        return choice()
    
        
        
choice ()







