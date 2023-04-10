n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

top = []
bottom = []
if line % 2 == 0:
    for i in range(1,line+1):
        top.append(i)
    for i in range(line,0,-1):
        bottom.append(i)
else:
    for i in range(1,line+1):
        bottom.append(i)
    for i in range(line,0,-1):
        top.append(i)
index =line-(end-n)-1
print(f"{top[index]}/{bottom[index]}")
    
