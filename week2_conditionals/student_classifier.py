#ask students name and age

name = input("Enter your name: ")
age =  int(input("Enter your age:"))

#checking students' age
while age < 0 or age >120:
    print("Invalid age! Please try again!")
    age =  int(input("Enter your age:"))

#students GPA
gpa = float(input("Enter your GPA: "))
while gpa < 0.0 or gpa > 4.0:
        print("Invalid. Please re-enter your GPA!")
        gpa = float(input("Enter your GPA: "))

if gpa >= 3.6:
    classification = "Excellent"
elif gpa >= 3.2:
    classification = "Good"
elif gpa >= 2.5:
    classification = "Average"
else:    
    classification = "Need improvement"


#number of courses
course = int(input("Enter number of courses you're taking: "))
while course <= 0 or course > 10:
        print("Invalid number of courses. Range: 1-10. Please re-enter!")
        course = int(input("Enter number of courses you're taking: "))

#display report: 
print("----Student Report----")
print(f"Name: {name}")
print(f"Age: {age}")

print(f"GPA: {gpa}")
print(f"Classificattion: {classification}")

print(f"Courses: {course}")
if gpa >=3.6 and course >=4:
    print("Eligible for scholarship")