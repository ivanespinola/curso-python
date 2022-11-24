# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

for x in range(2000,3201):
    if x%7 == 0 and x%5 != 0:
        print(x, end=',')
print()

# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= number:
    factorial = factorial * i
    i += 1
print(f"Refult: {factorial}")

# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that 
# is an integral number between 1 and n (both included)  and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8

number = int(input())
my_dict = {}
for i in range (1, number+1):
    my_dict[i] = i * i
print(my_dict)
