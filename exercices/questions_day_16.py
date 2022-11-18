# Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=0 

def f(n):
    if n <= 0:
        return 0
    else:
        return f(n-1) + 100
# n = int(input())

# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0 
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
# n = int(input())

# Please write a program using generator to print the even numbers 
# between 0 and n in comma separated form while n is input by console.
# input = 10 , output = 0,2,4,6,8,10

def even_generator(n):
    for x in range(0,n+1):
        if x % 2 == 0:
            yield x
        x+=1

values = []
n=int(input())
for i in even_generator(n):
    values.append(str(i))
print(",".join(values))


# Please write a program using generator to print the numbers which can be divisible 
# by 5 and 7 between 0 and n in comma separated form while n is input by console.

def number_generator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in number_generator(n):
    values.append(str(i))

print(",".join(values))

