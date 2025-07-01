# simple if
age = 18
if age >= 18:
    print("Eligle to vote")

# if-else
if age >= 18:
    print("Eligle to vote")
else:
    print("Not Eligible")

# if-elif-else
mark = 78
if mark >=90:
    print('Grade A')
elif mark>=60:
    print("Grade B")
else:
    print("Grade C")

# nested if
Natinality = "Indian"
State = "TN"
if age>=18:
    if Natinality=="Indian":
        if State=="TN":
            print("He is Eligible to Vote")
else:
    print("Not Eligible")

# Ternary = One is if
x=7
result = "Even" if x%2==0 else "odd"
print(result)

# if and or not
if age >=18 and State=="TN":
    print("Eligible")

if age >=18 or State=="TN":
    print("Eligible")

if not State=="TN":
    print("Not Eligible")

# membership 
fruits = ['apple','kiwi']
if 'kiwi' in fruits:
    print("Avalible")
# Indentity
x=None
if x is None:
    print('X is Empty')

cMarks = 65
mark12 = 60
mark10=55
if cMarks>=60:
    if mark12>=60:
        if mark10>=60:
           print("Eligilble")
        else:
            print("Not Elible because of 10th")
    else:
        print("Not Elible based on 12th")
else:
    print("Not Elible based on Colledge")

# loops
# i=1
# while i<=5:
#     print(i)
#     i=i+1
#     # i+=1

newList = [50,60,80,90,100]
for i in range(1,6):
    print(i)

for x in newList:
    print(x)
    # 1-x=50
    # 2-x=60
    # 3-x=80
    # 4-x=90
    # 5-x=100
# print(newList[0])
# print(newList[1])
# print(newList[3])

square = [x*x for x in range(1,6)]
print(square)

odd = [a for a in range(1,11) if a%2==0]
print(odd)

# swapping
a,b=10,20
# a=10
# b=20
a,b=b,a
# a=b
# b=a
print(a,b)
name = "madhumitha"
# m
# ma
# mad
# madh
# madhu
# madhumi
# madhumit
# madhumith
# madhumitha