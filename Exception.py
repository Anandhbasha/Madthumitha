# import math
# import random

# print(math.sqrt(4))

# num = random.randint(1,7)
# print(num)

# names = ["xyz","abc","def"]
# pick = random.choice(names)
# print(pick)

# arr = [1,2,3,4,5]
# random.shuffle(arr)
# print(arr)

# import os

# print(os.getcwd())

# import datetime

# print(datetime.datetime.now())

# import sys
# print(sys.path)

# try:
#     num1 = int(input("Enter the Number"))
#     print(2/num1)
# except ZeroDivisionError:
#     print("You can't Devide this")
# except ValueError:
#     print("Invalid Value from User")


try:
    num1 = int(input("Enter the Number"))
    print(2/num1)
except (ZeroDivisionError,ValueError) as e:
    print("Error",e)

