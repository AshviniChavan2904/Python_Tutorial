# Write a program to print numbers in Fibonacci series
# If user insert 4 it should print 4 numbers from fibonacci series, so the 4 numbers will be 0 1 1 2
# For e.g., 0 1 1 2 3 5 8 13
# What is fibonacci series?
# In fibonacci series two numbers are fixed 0 1
# The number after 1 is sum of first two and the same continues
user_num=int(input("Enter how many numbers of Fibonacci series to print: "))

def fibonacci_series(user_num):
    first_num=0
    sec_num=1
    if user_num <=0:
        exit
    elif user_num == 1:
        print(first_num)
    elif user_num == 2:
        print(first_num,sec_num,end=" ")    
    else: 
        print(first_num,sec_num,end=" ")
        for i in range(user_num-2):
            fib_num=first_num+sec_num
            first_num=sec_num
            sec_num=fib_num
            print(sec_num,end=" ")

fibonacci_series(user_num)