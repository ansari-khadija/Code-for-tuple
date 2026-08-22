name=input("Enter your name:")
age=int(input("Enter your age please:"))
city=input("Enter your city:")
course=input("Enter your course name:")

#putting all in tuple
student=(name,age,city,course)
          #or
#printing seperatly
print("Student Name:",name)
print("Student age:",age)
print("Student city:",city)
print("Student course:",course)

#using slicing 
print("Student Name:",student[0])
print("Student city and course:",student[2:4])

#showing tuples immutability,try changing age
student[1]=22

#print all
print(student)
