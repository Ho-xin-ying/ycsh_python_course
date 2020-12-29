F = [0,1]

#print('F0:',F[0])
#print('F1:',F[1])
m = int(input())

for i in range(2,100):
   
    Fn= F[i-1] + F[i-2]
    F.append(Fn)
print(Fn)