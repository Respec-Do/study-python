string = 'alice in the world'
a = string.count('alice')
print(a)

for i in string:
    a = string.count(i)
    print(f'{a}')