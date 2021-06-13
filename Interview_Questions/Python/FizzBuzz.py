'''Problem Statement
Write a program that, given a number n from STDIN, prints out all numbers from 1 to n (inclusive) to STDOUT, each on their own line. But there's a catch:

For numbers divisible by 3, instead of n, print Fizz
For numbers divisible by 5, instead of n, print Buzz
For numbers divisible by 3 and 5, just print FizzBuzz
For example, given the input 1, your program should output:

1
Another example, given the input 15, your program should output:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
'''

n = int(input().strip())

for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)
