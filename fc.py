code_line = []

file = 'xmpl001.f'
f = open(file, "r")
for line in f:
    line = line.strip()
    if line:
        code_line.append(line)
        parts = line.split()

def compile_line(line):
    parts = line.split()
    token = parts[0]

    if token.isdigit():
        print("true")
        print(token)
        i = 1
        counter = 0
        while ((parts[i]).isdigit()):
            print("true")
            print(parts[i])
            i += 1
            counter += 1
            if parts[i] == "-":
                print("minus")
                continue
            
            

for line in code_line:
    compile_line(line)