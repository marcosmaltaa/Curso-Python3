def generator(n=0):
    yield 1
    print('continua')
    yield 2
    print('outra')
    yield 3
    print('acabou')
    return 'acabaste'

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))