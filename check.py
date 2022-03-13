name = input("What is your name? ")
age = input("What is your age? ")

# this allows for a number to be added
age = int(age)

print("Hi {} , your age is ""{}" .format(name, age))

print("\n" + "which means," + "")

if age == 21:
 print("You've just entered into adulthood, have a free one on us")
elif age >= 21:
 print("You can buy an alcoholic beverage")
else:
 print("You cannot buy an alcoholic beverage")

