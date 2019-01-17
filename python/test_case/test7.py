a = [1, 2, 3, 4, 5]
print(a)
a.append(6)
print(a)

b = ['lala', 'blala']
c = a + b
print(c)

print(c[2])

c[2] = True
print(c[2])

print(c[2:])

# for i in c:
#     if i == 5:
#         print('Found')
#         break

# found = False
# for i in c:
#     if i == 5:
#         found = True
#         break

if 5 in c:
    print('Found')
else:
    print('Not found')


c.pop(3)
print(c)

del c[5]
print(c)

sl = {'k': 'value'}
print(sl)

sl['k'] = 'Hello'
print(sl)

sl['v'] = 'Join'
print(sl)

del sl['v']
print(sl)

l = {'a': 'Dom'}

sl.update(l)
print(sl)


q = {'a': 'ss'}

last = {**sl, **l, **q}
print(last)

if 'k' in last:
    print('found')
else:
    print('Not Found')

for value in last.values():
    if value == 'Hello':
        print('Found')


def test(a, b):
    return a+b+5

a1 = test(6, 4)
print(a1)


