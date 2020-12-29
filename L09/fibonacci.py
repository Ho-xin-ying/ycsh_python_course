F = [0,1]


for i in range(2,500):
   
    Fn= F[i-1] + F[i-2]
    F.append(Fn)

n = int(input())
m = int(input())


ls = [ ]

for i in range(n,m+1):
    ls.append(F[i]) 

print(ls)