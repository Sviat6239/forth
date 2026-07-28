code_line = []

file = 'xmpl001.forth'
f = open(file, "r")
for line in f:
    line = line.strip()
    if line:
        code_line.append(line)
        parts = line.split()

def compile_line(line):
    parts = line.split()
    token = parts[0]

    for token in parts:
        if token.isdigit():
            print("true")
            print(token)
        elif token == "-":
            print("minus")
        elif token == "+":
            print("plus")
        elif token == "*":
            print("multiply")
        elif token == "/":
            print("divide")
        elif token == ".":
            print("dot")
            
            

for line in code_line:
    compile_line(line)