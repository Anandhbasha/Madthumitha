# read
# file = open("UX.txt",'r')
# print(file.read())
# file.close()

# read line
# fileNew = open("UX.txt",'r')
# print(fileNew.readline())
# fileNew.close()
# read lines
# fileNew = open("UX.txt",'r')
# lines = (fileNew.readlines())
# print(lines)
# fileNew.close()
# Write
# right = open("UX.txt",'w')
# right.write("Hello this python write method")
# right.close()

# writeLine = open("UX.txt",'w')
# lines = ["Madhumitha \n",'She is Very new to Coding \n',"And She is Learning Basics of Py"]
# writeLine.writelines(lines)
# writeLine.close()

# with Key word

# with open("UX.txt",'r') as f:
#     data = f.read()
#     print(data)

# seek
# f = open("UX.txt",'r')
# f.seek(10)
# print(f.read())
# f.close()

# tell
# files= open("UX.txt",'r')
# print(files.tell())
# files.read(5)
# print(files.tell())
# files.close()

# import os

# if os.path.exists("UXe.txt"):
#     print("File Found")
# else:
#     print("File not Found")


# if os.path.exists("UX.txt"):
#     os.remove("UX.txt")

f = open("New.txt",'a')
f.write("She Cover almost 35% of Python")
f.close()

arr = [10,20,50,60]

# Numpy