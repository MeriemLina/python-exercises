age1 = int(input("Please type in the age of the first person: "))
name1 = input('what is the name of the first person?')
age2 = int(input("Please type in the age of the second person: "))
name2 = input('what is the name of the second person?')

if age1 > age2:
    print(f"{name1} is the oldest!")
elif age2 > age1:
    print(f"{name2} is the oldest!")
else:
    print("Both people are the same age!")