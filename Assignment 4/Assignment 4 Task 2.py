user_input = input("Enter text to write to the file: ")
with open('output.txt','w') as file1:
    file1.write(user_input + "\n")
add_input = input("Enter additional text to append: ")
with open('output.txt','a') as file1:
    file1.write(add_input + "\n")
print("\nFinal Content of 'output.txt: ")
with open('output.txt','r') as file1:
    for line in file1:
        print(line.strip())