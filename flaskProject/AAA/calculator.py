# AAA.calculator 모듈
# 사칙연산 함수 정의
def cal(n1, n2):
    print(f'{n1} + {n2} = {n1+n2}')
    print(f'{n1} - {n2} = {n1-n2}')
    print(f'{n1} * {n2} = {n1*n2}')
    # 소숫점 처리
    print(f'{n1} / {n2} = {(n1/n2):.2f}')

cal(100, 7)