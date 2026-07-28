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

    if token.isdigit() and token != " ":
        print("true")
        print(token)
        i = 1
        counter = 0
        while ((parts[i]).isdigit()):
            print("true")
            print(parts[i])
            i +=1
            counter += 1

            if parts[i] == "-" and parts[i+1] != " ":
                print("minus")
                if (parts[i+1]) == " ":
                    break
                else:
                    i+=1
                    continue

            if parts[i] == "*" and parts[i+1] != " ":
                print("multiply")
                if (parts[i+1]) == " ":
                    break
                else:
                    i+=1
                    continue
            
            if parts[i] == "+" and parts[i+1] != " ":
                print("plus")
                if (parts[i+1]) == " ":
                    break
                else:
                    i+=1
                    continue

            if parts[i] == "/" and parts[i+1] != " ":
                print("divide")
                if (parts[i+1]) == " ":
                    break
                else:
                    i+=1
                    continue

            if parts[i] == "." and parts[i+1] != " ":
                print("dot")
                if (parts[i+1]) == " ":
                    break
                else:
                    i+=1
                    continue

            if parts[i] == " ":
                break
            
            

for line in code_line:
    compile_line(line)