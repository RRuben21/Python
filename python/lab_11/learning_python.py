with open('what_I_learned_in_python.py')as file_object:
    contents=file_object.read()
print(contents*3)


filename='what_I_learned_in_python.py'

with open('what_I_learned_in_python.py')as file_object:
    contents=file_object.read()
print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
print('\n')      

with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())
