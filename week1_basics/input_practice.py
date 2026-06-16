name = input("Enter your name: ")
#input by default is string
# if: age = input(" ") so when print(type(age)) output will be string
# => must cast string to int: 
age = int(input("Enter your age: "))

print (f"Hello {name}")
print (f"You are {age} years old!")