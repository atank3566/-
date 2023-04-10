Number = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n,b = input().split()
n = ''.join(reversed(n))
b = int(b)
result = []

for i in n:
    result.append(Number.index(i))
sum = 0
for j in range(len(n)-1,-1,-1):
    sum += (b**j)*result[j]

print(sum)