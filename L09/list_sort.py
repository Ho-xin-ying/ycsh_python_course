ls = []
for i in range(5):
    x = int(input())
    ls.append(x)
#print('before sort:',ls)
ls.sort()
ls.reverse()
print('after sort:',ls)