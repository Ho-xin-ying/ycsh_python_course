n = int(input())

for c in range(2,n):
    if n % c == 0:
        print('不是質數')
        break    
    elif c == n-1:
        print('是質數')

if n == 2:
    print('是質數')