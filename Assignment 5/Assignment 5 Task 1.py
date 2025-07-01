std_name = {"Alice":85}
x = input("Enter the student's name: ")
if x in std_name:
    print(f"{x} marks are: {std_name[x]}")
else:
    print("Student not found")

