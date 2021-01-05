n = int(input())

for a in range(2,n):
    if n % a == 0:
        print('不是質數')
        break    
    elif a == n-1:
        print('是質數')

if n == 2:
    print('是質數')