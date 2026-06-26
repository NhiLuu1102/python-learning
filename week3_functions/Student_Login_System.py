def check_username(username):
    return len(username) >= 5

def check_password(password):
    has_upper = False
    has_digit = False
    for ch in password:
        if(ch >= 'A' and ch <= 'Z'):
            has_upper = True
        if(ch >= '0' and ch <= '9'):
            has_digit = True
    return len(password) >=8 and has_upper and has_digit

def login(username, password):
    check_password(password)
    check_username(username)
    if check_username(username) and check_password(password):
        return "Login successful"
    else:
        return "Login failed"

#main 
username = input("Enter your username: ")
password = input("Enter your password: ")

login(username,password)
print(login(username,password))