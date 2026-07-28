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
    stack = []

    for token in parts:
        if token.isdigit():
            stack.append(int(token))
            
        elif token == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
            
        elif token == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
            
        elif token == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
            
        elif token == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
            
        elif token == ".":
            if stack:
                print(stack.pop())
            else:
                print("Error: Stack Underflow!")

for line in code_line:
    compile_line(line)