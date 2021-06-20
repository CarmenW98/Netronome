#!/usr/bin/env python
# coding: utf-8


#import numpy libary for matematical operations
import numpy as np;

#recieve user input 
num = int(input("Please enter a number:  \n"));

while num<0:
    print("Factorial of a negative number does not exist");
    num = int(input("Please enter a positive number: \n"));
    
num=np.math.factorial(num);	#find factorial
num=[*map(int,str(num))]; 	#place digits of factorial into an array of numbers
print(np.sum(num));		#print result





