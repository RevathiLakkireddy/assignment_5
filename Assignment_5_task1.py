#initialize a dictionary with student names and their marks
students = {'Alice': 85, 'Bob': 90, 'Reeta': 95}
#asking the user for the student name and storing it into a variable
x = input("Enter the student's name: ")
#checking if the student's name is in the dictionary and printing their marks if present
if x in students:
    print(students.get(x))# we can use student[x] also instead of get method
else:
    print("student not found")