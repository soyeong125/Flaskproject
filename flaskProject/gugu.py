# 전체 구구단 출력
def guguPrint1():
    for i in range(2, 10):
        print('-'*20)
        print('\t',i,'단')
        for j in range(1, 10):
            print(f'{i} X {j} = {i*j}')
        print()

# 특정 구구단 출력
def guguPrint2(n):
    print('-' * 20)
    print('\t', n, '단')
    for i in range(1, 10):
        print(f'{n} X {i} = {n*i}')

# guguPrint1()
# guguPrint2(9)