#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:06:01 2019

@author: peterle
"""
#7 Write one line of python that takes this list a and makes a new list that has
#only the even elements of this line in it

#a = [1,4,9,16,25,36,49,64,81,100]
#b = [number for number in a if number % 2 == 0]
#
#print (b)
#


#a = [1,4,9,16,25,36,49,64,81,100]
#b = []
#for i in a:
#    if ((i % 2) ==0):
#        b.append(i)
#print(b)

#8. rock paper sissors

#list = ['rock', 'paper', 'csissor']
#user = str(input("choose rock , paper or csissor "))
#bot = random.choice(list)
#if((user == 'rock') and (bot == 'rock') ):
#    print("tie")
#elif( user == 'rock' and bot == 'paper' ):
#    print("you lose")
#elif ( user == 'csissor' and bot == 'rock' ):
#    print("you lose")
#elif (user == 'paper' and bot == 'csissor'):
#    print("you lose")
#else: 
#    print("you win ")
#print("the computer chose   ",bot )

#9 Guessing Game One

#Generate a random number between 1 and 9 
#(including 1 and 9). Ask the user to guess
# the number, then tell them whether they guessed
# too low, too high, or exactly right.

#def function():
#   
#    list = [1,2,3,4,5,6,7,8,9]
#    num = random.choice(list)  
#    guess = int(input("Pick 1 number "))
#    print("the given number is ", num)
#    if (guess == num):
#        print("you are exactly right ")
#    elif (guess > (num + 2)):
#        print("your guess is too high ")
#    else :
#        print("your guess is too low")
#    return 0    
#    
#def condition ():
#    answer = str(input("do you want guess? yes/exit: "))
#    while (answer == 'yes'):
#        function()
#        return condition()
#    else: 
#        return 0
#    
#condition()


#10 
#

#11
# ask the user for a number and determine whether the number is prime or not
#a prime number is a number that has no divisors . should use the answer to exercuse 4

#def prime():
#    user_num = int(input("enter your number here: "))
#    if (user_num == 1):
#        print(user_num, " is a prime")
#    elif (user_num == 2):
#        print(user_num, " is a prime")
#    elif (user_num ==0):
#        print(user_num, " is not a prime")
#    else:
#    
#    
#        for i in range (2, user_num - 1):
#            if ((user_num % i ) != 0):
#                print(user_num , " is a prime "  )
#                return 0
#            else: 
#                print(user_num , " is not a prime")
#                return 0 
#            
#def program ():
#    ask = str(input("Do you want to check which number is prime? yes /no "))
#    if (ask == 'yes'):
#        prime()
#        return program()
#    else: 
#        return 0 
#program()


#12 
#write a program that takes a list of numbers ( for ex:
#a = [5,10,15,20,25]) and makes a new list of the first and last element of the given
#list 

#def new_list():
#    user_arr = []
#    
#    arr_len = int(input("choose the length of the array "))
#    while arr_len >0:
#        number = int(input("your number"))
#        user_arr.append(number)
#        arr_len -= 1
#    print(user_arr)
#    
#    len_user_arr = len(user_arr)
#    new_arr = [user_arr[0], user_arr[len_user_arr - 1]]
#    print (new_arr)
#    
#def program ():
#    ask = str(input("do you want to run the program again? yes/no "))
#    if (ask == 'yes'):
#        new_list()
#        return program()
#    else:
#        return 0
#    
#    
#program()
    


#13 Write a program that asks the user how many Fibonnaci numbers
# to generate and then generates them.
#
#def function():
#    num = int(input("how many fibonanci number do you want "))
#    fibo =[]
#    
#    if num ==1:
#        fibo =[0]
#    elif num == 2:
#        fibo = [0,1]
#    elif num ==3:
#        fibo = [0,1,1]
#    elif num > 3:
#        
#        
#        
#        
#        
#        
#        
#    print(fibo)
#function()



#15 Reverse Word Order
#write a program using functions that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.
# for example: My name is Peter -> Peter is name my

#def revWordOrder():
#    given_str = str(input("enter your string here, our system will reverse it "))
#    
#    new_str = given_str.split()     #split all the words in string
#    
#    rev_new_str =new_str[::-1]  # reverse the order of words in string
#    
#    rev_result = " ".join(rev_new_str)  #combine those words by " space " to a new string
#    print(rev_result)
#revWordOrder()


#16

# Write a password generator in Python. Be creative with how you generate passwords 
#- strong passwords have a mix of lowercase letters, uppercase letters,
# numbers, and symbols. The passwords should be random, generating a
# new password every time the user asks for a new password.
# Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list
#



#import random
#def generateHard_pwd():
#    
#    string = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()'
#    
#    passlen = 8
#    p = "".join(random.sample(string,passlen))
#    
#    print (p) 
#generate_pwd()
#
#def generateEasy_pwd():
#    string_ez = 'qwertyuiopasdfghjklzxcvbnm'
#    passle = 8
#    pwd ="".join(random.sample(string_ez,passle))
#    
#    print(pwd)
#
#generateEasy_pwd()
#def choice():
#    u_choice = str(input("Do you want a complicated pwd that no one can guess? y/n  \n "))
#    
#    if u_choice == 'y':
#    generate_pwd()
#    
#    return choice()
#
#    elif u_choice == 'n': 
#    generateEasy_pwd()
#    return choice()
#    
#        
#        
#choice ()































