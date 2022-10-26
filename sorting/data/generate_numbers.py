import os
import random

file = open("numbers.txt", "a")

numbers_count = 0
# while os.path.getsize("numbers.txt") < 1073741824:
while os.path.getsize("numbers.txt") < 10734:
    # for k in range(100000):
    for k in range(1000):
        n = random.randint(0, 2147483647)
        file.write(str(n) + " ")
    # numbers_count += 100000
    numbers_count += 1000
    print("Total numbers count: " + str(numbers_count), end = "\r")

file.close()

print("Total numbers count: " + str(numbers_count))
print("Process completed...")
print("File size: " + str(os.path.getsize("numbers.txt")))
