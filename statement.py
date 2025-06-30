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