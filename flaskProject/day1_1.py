# 주석 (Comment) - Ctrl+/
"""
여러줄 주석처럼 사용하려면?
   홑따움표나 쌍따움표 3개씩 세트로 이용가능
"""
# 출력문 print(변수/데이타)
# 변수 = 값
# 자료형의 종류 = 숫자형(실수, 정수), 문자열, 논리형(True/False)
x = 100
y = 3.14
txt1 = 'Hello World'
# 여러줄 문자열
txt2 = ''' Python
        HTML+CSS 
        Flask
        MySQL 
        '''
z = True

# 출력
# print(...,...) : 쉼표를 이용한 한줄 출력
# print(...., end='공백이나 구분자')
# ctrl+d 복사붙이기
print(x)
print(x,y,z)
print('x = ', x, 'y = ', y)
print(txt1, end='**')
print(z)
# 이스케이스 문자 : \n, \t
print('*\n\t**\n\n\t\t***')

# 파이썬의 예약어
import keyword
print('파이썬 예약어는?')
print(keyword.kwlist)
print('예약어는 몇개인가?', len(keyword.kwlist))

# 입력문
# 변수 = input(질문메세지문자열)
# userName = input('고객님의 성함을 입력하여주세요...')
# print(userName, '님 오늘도 좋은 하루되세요 ^^')

# 캐스팅이란? 자료형 변환
# 파이썬의 대표적인 캐스팅관련 함수
# float() - 실수형 형변환
# int() - 정수형 형변환
# str() - 문자열 형변환
# type() - 데이터의 형 출력

a = 100
b = 12.456
c = 'Python'
d = False
print(a, type(a)) # 100 <class 'int'>
print(b, type(b)) # 12.456 <class 'float'>
print(c, type(c)) # Python <class 'str'>
print(d, type(d)) # False <class 'bool'>
e = float(a) # 100.0 <class 'float'>
f = int(b) # 12 <class 'int'>
g = str(d) # False <class 'str'>
print(e, type(e))
print(f, type(f))
print(g, type(g))

# 두수를 입력받은 후 사칙연산 결과를 출력하기
# num1 = int(input('첫번째 숫자를 입력해주세요...'))
# num2 = int(input('두번째 숫자를 입력해주세요...'))
# print(type(num1), type(num2) )  # <class 'int'> <class 'int'>
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)

# 연산자의 종류
# 산술 , 대입(+=, -=, *=, /=, //=, %=)
# 관계(비교) - >=, <=, <, >, ==, !=,
# 논리연산자 - not, and, or
n1 = 100
n2 = 200
t1 = '홍길동'
t2 = 'power'
print('n1 : ', n1) # n1 :  100
print('n2 : ', n2) # n2 :  200
print('-'*20) # 문자열 반복연산자 문자열*숫자
n1 += 10 # n1 = n1+100
n2 /= 10 # n2 = n2/10
print('n1 : ', n1) # n1 :  110
print('n2 : ', n2) # n2 :  20.0
print('-'*20)
print(t1 == '홍길동') # True
print(t2 == '홍길동') # False
print(t1 != '홍길동') # False
print(n1, n2) # 110 20.0
print(n1 < 0 ) # False
print('-'*20)
# 논리연산자 or 각항의 결과가 하나라도 참이면 True
# 논리연산자 and 각항의 모든결과가 모두 참이면 True
print((t1 == '홍길동') or (n1 < 0)) # True
print((t1 != '홍길동') or (n1 < 0)) # False
print((t1 == '홍길동') and (n1 < 0)) # False
print((t1 == '홍길동') and (n1 >= 0)) # True

# 문자열 인덱싱과 슬라이싱
# 문자열변수[n] : n은 인덱스숫자 0부터 시작.
# 인덱스가 음수인 경우에는 마지막 문자열이 -1
# 문자열변수[start:end] : start~end-1 까지 표시
# 문자열변수[start:]
# 문자열변수[:end]
sample = '가나다라마바사아자차카타파하'
print('-'*20)
print('sample = ', sample, len(sample))
print(sample[0]) # 가
print(sample[-2]) # 파
print(sample[5:10]) # 바사아자차
print(sample[5:]) # 바사아자차카타파하
print(sample[:10]) # 가나다라마바사아자차

# 문자열 포맷팅 f''
# print(f'{변수} 문자열....')
userName = '고길동'
userAge = 45
print(userName, userAge)
print(f'고객님의 이름은 {userName } 이고 나이는 {userAge} 입니다.  ')
# 고객님의 이름은 고길동 이고 나이는 45 입니다.

# QR 코드 4교시 출석 진행하시면 됩니다.
# 1:00~1:10분 사이
# 식사시간 이후에 다시 진행하겠습니다.








