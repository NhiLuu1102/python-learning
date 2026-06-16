name = input("Enter your name: ")
#input mặc định là string
# nếu ghi age = input(" ") thì khi dùng print(type(age)) output sẽ là string
# phải ép string qua int: 
age = int(input("Enter your age: "))
print ("Hello ", name)
print ("You are ", age, " years old!")