# # print("Hello python is working")
# a=10
# print("Hello Python is working", end=" ")
# # /n - new like
# print(a)
# print("apple","banana","cherry",sep="/")
# # apple|banana|cheery
# print("apple","banana","cherry" ,sep='-',end='$\n')
# print(10,20,30,40 ,sep=' ', end='\tDone!\n')
# print("1","2","3","4",'5', sep='*', end='#\n')

# # 10 20 30 40 Done!
# #1*2*3*4*5#
# # variable declartion
# # a - a is the variable name
# # = assignent Opeartor
# # 10,20 are values of a

# # value is not more one is called as premitive(Simple)Data types
# #  int,float,string,Boolean

# # 
# a=10
# # a[0] = 10
# a=20
# # a[0] = 20
# b=60
# a=b
# # a=60
# b=a
# print(a)
# print(b)
# # string
# name = "xyz"
# l='x'
# # boolean
# # true false
# isAlive = True
# print(type(isAlive))
# userInput= input("Enter the value")
# print(type(userInput))
# 
a= 10.5
# complex Datatypes
# list
# duplicate value
e=[10,20,50.5,True,10] 
# e[0]=10
# e[1] = 20
print(e)
print(e[3])

# tuple
d=(20,50,60,20)
print(d[0])
f=("xyz","abc")

# dictionary
person = {"name":"xyz",
          "age":22,
          "City":"CBE"
          }
print(person)
print(person.keys)
print(person["name"])
print(person.get('age'))
# set
sets = {10,20,30}
print(sets)