# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

def calculate_upper_and_lower(word):
    upper = 0
    lower = 0
    for letter in word:
        if letter.isupper():
            upper += 1
        if letter.islower():
            lower +=1
    print(f'Upper case = {upper}, Lower case = {lower}')

calculate_upper_and_lower('Hello Word!')

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input()
total,tmp = 0,str()        

for i in range(4):
    tmp+=a               
    total+=int(tmp)      

print(total)


