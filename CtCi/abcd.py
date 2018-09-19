# all pos int solutions for a, b, c, d < 1000
# a3 + b3 = c3 + d3
n = 1000
mapp = {}
for c in range(n+1):
    for d in range(n+1):
        result = pow(c, 3) + pow(d, 3)
        l = mapp.get(result);
        if l:
            l.append((c, d))
            mapp[result] = l
        else:
            mapp[result] = [(c, d)]

c = 0
for a in range(n+1):
    for b in range(n+1):
        result = pow(a, 3) + pow(b, 3)
        for pair in mapp.get(result):
            # print(a, b, pair[0], pair[1])
            c+=1
print(c) # 2015809 for n = 1000
        
