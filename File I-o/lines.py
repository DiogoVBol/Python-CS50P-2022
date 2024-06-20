import sys

if len(sys.argv) != 2:
    if len(sys.argv) < 2:
        exit('Too few command-line arguments')
    else:
        exit('Too many command-line arguments')

file_name = sys.argv[1]

dt = file_name.find('.')
if file_name[dt:] != '.py':
    exit('Not a Python file')

lines = 0

try:
    with open(file_name,'r') as file:
        for line in file:
            if line.strip().startswith('#'):
                continue
            if line.isspace():
                continue
            lines +=1
except FileNotFoundError:
    sys.exit('File does not exist')

print(lines)
