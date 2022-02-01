l = open('quijote.txt', 'r').read().split(' ')
print sorted({x:l.count(x) for x in set(l)}.items(),key=lambda t: t[1],reverse=True)[0:10]