s = {4, 0, 7, 8}
t = 3, 5, 7, 9
s.add(t)
print(s)

print((dir(set)))

a = {3, 5, 6}
b = {4, 7, 8}
c = {6, 5}
print(a.intersection(b))
print(b.intersection(a))
print(a.intersection(c))
print(b.intersection(c))
print(c.intersection(a))

a = {3, 5, 6}
b = {4, 7, 8}
c = {6, 5}
print(a.union(b))
print(b.union(a))
print(a.union(c))
print(b.update(a))
print(c.difference(a))
