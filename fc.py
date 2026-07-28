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

    digitCount = 0
    digits = []

    for token in parts:
        if token.isdigit():
            print("true")
            digitCount += 1
            digits.append(token)
            print(token)
        elif token == "-":
            digitCount = 0
            print("minus")
        elif token == "+":
            digitCount = 0
            print("plus")
        elif token == "*":
            digitCount = 0
            print("multiply")
        elif token == "/":
            digitCount = 0
            print("divide")
        elif token == ".":
            print("dot")
        
        print(digitCount)

    print(digits)

for line in code_line:
    compile_line(line)