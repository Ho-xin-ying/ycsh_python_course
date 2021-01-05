x = int(input())
y = int(input())
for i in range(x,y+1):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==2:
       print (i)