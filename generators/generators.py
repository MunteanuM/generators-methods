def first_generator(n):
    '''generator as function'''
    for i in range(n):
        yield i


def second_generator(n):
    '''standard generator'''
    gen = (x for x in range(n))
    return gen


def third_generator(n):
    '''generator as object'''
    for i in range(n):
        yield i


# 1
print('\n#1\n')
for x in first_generator(5):
    print(x)

# 2
print('\n#2\n')
print(second_generator(5))

# 3
print('\n#3\n')
gen = third_generator(5)

for i in range(5):
    print(gen.__next__())
