def degrais(n):
     if n <= 1:
          return 1
     return degrais(n-1) + degrais(n-2)

n1 = 0
n2 = 1
for i in range(0, 45):
     temp = n2
     n2 = n2 + n1
     n1 = temp
print(n2)