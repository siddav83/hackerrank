x = int(input())
y = int(input())
z = int(input())
n = int(input())

answer = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if x+y+z != n]
print(answer)

answer = ([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
print(answer)
