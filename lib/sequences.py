#!/usr/bin/env python3

def print_fibonacci(length):
    fibo = []
    if length > 0:
            fibo.append(0) 
    if length >= 2:
           fibo.append(1)
           for i in range(2, length):
               fibo.append(fibo[-1] + fibo[-2])
    print(fibo)
             
                 

        

print_fibonacci(9)
    #pass
