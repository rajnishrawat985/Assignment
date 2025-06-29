try:
    with open('sample.txt','r') as file1:
        for line in file1:
            print(line.strip())
except FileNotFoundError:
    print("Error: The File 'sample txt' was not found")

try:
    with open('sample1.txt', 'r') as file1:
        for line in file1:
            print(line.strip())
except FileNotFoundError:
    print("Error: The File 'sample txt' was not found")


