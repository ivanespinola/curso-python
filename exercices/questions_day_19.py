# Please write a program to randomly print a integer number between 7 and 15 inclusive.
import random

random_number = random.randint(7,16)
print(random_number)

# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
import zlib

my_string = 'hello world!hello world!hello world!hello world!'
# compressed = zlib.compress(my_string)
# print(compressed)
# decompressed = zlib.decompress(compressed)
# print(decompressed)

# Please write a program to print the running time of execution of "1+1" for 100 times.
import datetime
before = datetime.datetime.now()
for _ in range(100):
    x = 1 + 1
after = datetime.datetime.now()
total_time = after - before
print(total_time.microseconds)

# Please write a program to shuffle and print the list [3,6,7,8].
my_list = [3,6,7,8]
shuffle_list = random.shuffle(my_list)
print(shuffle_list)

# Please write a program to generate all sentences where subject 
# is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey","Football"]

for sub in subjects:
    for ver in verbs:
        for obj in objects:
            print(f'{sub},{ver},{obj}')

