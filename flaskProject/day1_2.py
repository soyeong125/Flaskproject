# f' 포맷팅을 이용한 변수 출력
n1 = 100
n2 = 3
# 쉼표를 이용한 출력
print(n1, ' / ', n2, ' = ', n1/n2)
# f' 포맷팅을 이용한 소숫점 처리
# print(f'...{계산식또는변수:전체자릿수.소숫점이하자리수f} ...')
print(f'{n1}  /  {n2}  =  {(n1/n2):.2f}')
print(f'{n1}  /  {n2}  =  {(n1/n2):7.2f}')

# 문자열관련 함수
# 문자열변수.함수명(옵션)
# 문자열변수.count(문자) - 문자의 중복갯수
# 문자열변수.find(문자) - 문자의 위치
# 문자열변수.index(문자) - 문자의 위치
# 문자열변수.replace(문자A, 문자B) - 교체
# 문자열변수.strip() - 양쪽 공백 삭제
# 문자열변수.split() - 공백을 기준으로 낱개 글자로 리스트화
# 구분문자.join(문자열변수) - 구분문자가 문자마다 삽입

print('-'*20)
sample1 = 'Hello python'
sample2 = '    Welcome python    '
print(sample1.count('o')) # 2
print(sample1.find('o')) # 4
print(sample1.index('o')) # 4
print(sample1.replace('python', 'MySQL')) # Hello MySQL
print(f'$$$${sample2}$$$$') # $$$$    Welcome python    $$$$
print(f'$$$${sample2.strip()}$$$$') # $$$$Welcome python$$$$
result = sample2.split()
print(type(result)) # <class 'list'>
print(result) # ['Welcome', 'python']
print('/'.join(sample1)) # H/e/l/l/o/ /p/y/t/h/o/n

print('-'*20)
# 리스트명 = [데이타...]
list1 = [100, 45.678, False, 'Python', True]
print(f'{list1} => 길이 {len(list1)}, 데이타형 {type(list1)}')
print(list1[0], list1[-1], list1[2])
print(list1[0:3], list1[:2], list1[2:])
print(list1[::2], list1[1::2]) # 리스트명[start:end:step]
'''
[100, 45.678, False, 'Python', True] => 길이 5, 데이타형 <class 'list'>
100 True False
[100, 45.678, False] [100, 45.678] [False, 'Python', True]
[100, False, True] [45.678, 'Python']
'''
# CRUD Create/Read/Update/Delete
# 리스트명[인덱스] = 값
list1[0] = 500
print(list1) # [500, 45.678, False, 'Python', True]
# 값 추가 - append(), insert(), extend()
print('-'*20)
list2 = []
print(f' list2 = {list2}')
list2.append(11)
list2.append('플라스크')
print(f' list2 = {list2}')
list2.insert(0, '파이썬')
print(f' list2 = {list2}')
list2.extend([77, 88, 99])
print(f' list2 = {list2}')

# 삭제 - pop(),remove(), del(), clear()
print(f'삭제할 요소는? {list2.pop()}') # 삭제할 요소는? 99
print(f' list2 = {list2}') # list2 = ['파이썬', 11, '플라스크', 77, 88]
list2.remove(11)
print(f' list2 = {list2}') # list2 = ['파이썬', '플라스크', 77, 88]
del(list2[0])
print(f' list2 = {list2}') #  list2 = ['플라스크', 77, 88]
list2.clear()
print(f' list2 = {list2}') # list2 = []

# 정렬
list3 = ['가', 'python', '!!안녕', '플라스크', '123']
print(f' list3 = {list3}') # list3 = ['가', 'python', '!!안녕', '플라스크', '123']
list3.sort()
print(f' list3 = {list3}') # list3 = ['!!안녕', '123', 'python', '가', '플라스크']

print('-'*20)
# 2차원 리스트 : 리스트안의 길이가 서로 달라도 된다.
# 인덱싱 : 리스트변수[i][j]
list2D = [ 10, [True, False], [500, 600, 700, 800]]
print(f'list2D = { list2D }, 길이는? {len(list2D)}')
# list2D = [10, [True, False], [500, 600, 700, 800]], 길이는? 3
print(list2D[0])
print(list2D[1]) # [True, False]
print(list2D[2]) # [500, 600, 700, 800]
print(list2D[1][0], list2D[2][2]) # True 700

# 1차원 리스트 => 2차원 리스트
# 1차원 리스트 정의
kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]
score2D = [kor, math, eng]
print(f'score2D = {score2D}')
# score2D = [[55, 66, 34, 60], [78, 90, 45, 88], [56, 98, 78, 90]]
result = score2D[0][0] + score2D[0][1] + score2D[0][2] + score2D[0][3]
print(f'국어 과목의 총점은? {result} 평균은? {(result/4):.1f}')

# 집합자료형 - 리스트, 튜플, 집합, 딕셔너리
# 튜플(Tuple) - C, R, UD(추가만 가능. 값교체 및 부분 요소 삭제 X)
t1 = (100, 200, 'apple', 'banana', 'cat')
# 데이타가 1개인 튜플 생성시에는 마지막에는 쉼표(,)
# t2 = ('강아지') # t2 = 강아지, <class 'str'>
t2 = ('강아지',)
t3 = ()
print(f' t1 = {t1}, {type(t1)}')
# t1 = (100, 200, 'apple', 'banana', 'cat'), <class 'tuple'>
print(f' t2 = {t2}, {type(t2)}')
# t2 = ('강아지',), <class 'tuple'>
print(t1[0], t1[-1], t1[1:4]) # 100 cat (200, 'apple', 'banana')
# 튜플에서 요소 추가는 += (...)
print(f' t3 = {t3}, {type(t3)}') # t3 = (), <class 'tuple'>
t3 += ('쿠팡','NS쇼핑몰','공영쇼핑몰')
print(f' t3 = {t3}, {type(t3)}')
# t3 = ('쿠팡', 'NS쇼핑몰', '공영쇼핑몰'), <class 'tuple'>
t3 += ('인터파크',)
print(f' t3 = {t3}, {type(t3)}')
# t3 = ('쿠팡', 'NS쇼핑몰', '공영쇼핑몰', '인터파크'), <class 'tuple'>
# 값 교체 불가능
# TypeError: 'tuple' object does not support item assignment
# t3[0] = 'GS이샵'
# 전체 삭제는 가능
del t3
# print(f' t3 = {t3}, {type(t3)}')
# NameError: name 't3' is not defined

# 딕셔너리 - C R(슬라이싱X, 키인덱스) U D
# 딕셔너리변수 = {키:값....}
# 딕셔너리변수[키값] : 딕셔너리 인덱싱
print('-'*20)
dict1 = {'a':'apart', 'b':'boat', 'c':'cafe', 'd':'dress', 'a':'apple'}
print(f' dict1 = {dict1}, {len(dict1)}, {type(dict1)}')
# dict1 = {'a': 'apple', 'b': 'boat', 'c': 'cafe', 'd': 'dress'}, 4, <class 'dict'>
# 중복키가 있는 경우에는 마지막 키가 유효
print(dict1['a'], dict1['d']) # apple dress
# 값 수정
dict1['d'] = 'dog'
print(f' dict1 = {dict1}')
# dict1 = {'a': 'apple', 'b': 'boat', 'c': 'cafe', 'd': 'dog'}
# 새로운 아이템 추가
dict1['e'] = 'eye'
print(f' dict1 = {dict1}')
# dict1 = {'a': 'apple', 'b': 'boat', 'c': 'cafe', 'd': 'dog', 'e': 'eye'}
# 아이템 삭제
del dict1['b']
print(f' dict1 = {dict1}')
# dict1 = {'a': 'apple', 'c': 'cafe', 'd': 'dog', 'e': 'eye'}
# 딕셔너리 함수 : keys(), values(), items()
print(dict1.keys(), list(dict1.keys()))
print(dict1.values(), list(dict1.values()))
print(dict1.items(), list(dict1.items()))
'''
dict_keys(['a', 'c', 'd', 'e']) ['a', 'c', 'd', 'e']
dict_values(['apple', 'cafe', 'dog', 'eye']) ['apple', 'cafe', 'dog', 'eye']
dict_items([('a', 'apple'), ('c', 'cafe'), ('d', 'dog'), ('e', 'eye')]) [('a', 'apple'), ('c', 'cafe'), ('d', 'dog'), ('e', 'eye')]
'''
# 집합 - C
# 중복값을 허용하지 않는다.
# 집합변수 = set(리스트|튜플)
set1 = set([45, 67, 45, 100, 100, 100, 67])
print('-'*20)
print(f'set1 = {set1}, {len(set1)}, {type(set1)}')
# set1 = {67, 100, 45}, 3, <class 'set'>
# TypeError: 'set' object is not subscriptable
# print(set1[0])
# 집합 함수와 연산자
# 교집합 : & , intersection()
# 합집합 : | , union()
# 차집합 : - , difference()
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(f's1 = {s1}')
print(f's2 = {s2}')
print(f'교집합 = {s1 & s2}, {s1.intersection(s2)}')
print(f'합집합 = {s1 | s2}, {s1.union(s2)}')
print(f'차집합 = {s1 - s2}, {s1.difference(s2)}')
'''
교집합 = {4, 5, 6}, {4, 5, 6}
합집합 = {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}
차집합 = {1, 2, 3}, {1, 2, 3}
'''
# 아이템 추가 - add(), update()
set2 = set([10, 20, 30])
print(f'set2 = {set2}')
set2.add(100)
print(f'set2 = {set2}') # set2 = {100, 10, 20, 30}
set2.update([1, 2, 3])
print(f'set2 = {set2}') # set2 = {1, 2, 3, 100, 10, 20, 30}
# 아이템 삭제 - remove(), discard()
set2.remove(30)
set2.discard(100)
print(f'set2 = {set2}')
# set2 = {1, 2, 3, 10, 20}

print('-'*30)
# 조건문
# if, if ~ else, if ~ elif ~ else
'''
if 조건식:
    명령문

if 조건식:
    명령문1
else:
    명령문2    
    
    
if 조건식1:
    명령문1
elif 조건식2:
    명령문2    
else:
    명령문2   
        
'''

# x = 100
x = 50
if x>=100:
    print('x가 100보다 크거나 같다')
print('단순 if 테스트 종료 ')

print('+'*30)
if x>=100:
    print('x가 100보다 크거나 같다')
else:
    print('x는 100보다 작다')
print('if else 테스트 종료 ')

print('+'*30)
# 입력값에 따라서 메세지 출력
# 100이다. 100보다 크다, 100보다 작다
# ans = int(input('숫자 입력'))
# if ans == 100:
#     print('입력값은 100')
# elif ans>100:
#     print('입력값은 100보다 크다')
# else:
#     print('입력값은 100보다 작다. ')
# print('if elif else 테스트 종료 ')

# in, not in 연산자 => True/False
# 데이타값 in 리스트/튜플/문자열
# 데이타값 not in 리스트/튜플/문자열
userList = ['홍길동', '성춘향', '심청이']
print('심청이' in userList) # True
print('이몽룡' in userList) # False
print('이몽룡' not in userList) # True

# 조건문의 in/not in 연산자
'''
if 데이타값1 in/not in 리스트/튜플/문자열:
    명령문1
elif 데이타값2 in/not in 리스트/튜플/문자열:
    명령문2    
else:
    명령문3  
'''
bts = ['지민', 'RM', '슈가', '진', '정국', '뷔', '제이홉']
print('-'*30)
singer1 = '지민'
singer2 = '카이'
if singer2 in bts:
    print(f'{singer2} 는(은) BTS 멤버이다')
elif singer1 in bts:
    print(f'{singer1} 는(은) BTS 멤버이다')
# else:
#     pass
print('테스트 종료 ')

# 반복문 while
'''
초기치
while 조건식:
    명령문 
    증감치 
'''
print('-'*30)
# 1~10까지 출력하기
cnt = 1
while cnt <= 10:
    print(cnt)
    cnt += 1
print('테스트 종료 ')

# 10~1까지 출력하기
print('-'*30)
cnt = 10
while cnt > 0:
    print(cnt)
    cnt -= 1
print('테스트 종료 ')

# 1~100까지의 합 구하기
#  1+2+...+100 = ?
print('-'*30)
total = 0
cnt = 1
while cnt <= 100:
    total += cnt
    cnt += 1
print('테스트 종료 ')
print(f'1~100까지의 합은? {total}')

# 1~100사이에서 짝수만 출력하기
# 값%2 == 0 나머지가 0 짝수
print('-'*30)
cnt = 1
while cnt <= 100:
    if cnt%2 == 0:
        print(cnt, end=' ')
    cnt += 1
print('\n테스트 종료 ')


# continue : 하단 명령을 실행하지 않고 while 문은 지속
# 1~10 숫자사이에서 5를 제외하고 출력하기
print('-'*30)
cnt = 0
while cnt < 10:
    cnt += 1
    if cnt == 5:
        continue
    print(cnt, end=' ')
print('\n테스트 종료 ')

# break : 반복문을 탈출하는 용도로 사용
# 입력문을 이용해서 리스트에 추가한다.
# q를 입력하면 리스트 추가 종료
# True 인조건 => 공백이아닌문자열, 숫자(0제외), True, 값이 있는 리스트
result = []
# while True:
# while 1:
#     temp = input('값 입력하기(q는 입력종료) => ')
#     if temp=='q':
#         break
#     else:
#         result.append(temp)
# print('\n테스트 종료 ')
# print(result)

print('-'*30)
# list(range(start, end, step))
# start~end-1까지 연속적인 값 리스트 생성
print(range(1,20), type(range(1,20)))
print(list(range(1,20)), type(list(range(1,20))))
# range(1, 20) <class 'range'>


print('-'*30)
# for 인덱스변수 in range(start, end, step):
#       명령문
# 1 ~ 10 까지 출력
for i in range(1, 11):
    print(i)


# 1 ~ 50 까지 홀수만 출력
print('-'*30)
for i in range(1, 50, 2):
    print(i, end=' ')


# 20 ~ 1까지 감소 숫자 출력
print()
print('-'*30)
for i in range(20, 0, -1):
    print(i, end=' ')

# 1~100까지 누적합 구하기
print()
print('-'*30)
result = 0
for i in range(1, 101):
    result += i
print(f' 1~100까지의 합은? {result}')

# for문과 리스트/튜플/문자열
'''
for item변수 in 리스트/튜플/문자열:
    명령문 
'''
# 순차적으로 리스트/튜플/문자열 각각의 값 탐색
listA = ['사과', '바나나', '수박', '포도']
# print(listA[0])
# print(listA[1])
# print(listA[2])
# print(listA[3])
cnt = 1
for item in listA:
    print(cnt, item)
    cnt += 1
'''
1 사과
2 바나나
3 수박
4 포도
'''

print('-'*30)
sampleTxt = '아름다운우리나라'
cnt = 1
for item in sampleTxt:
    print('\t'*cnt,item)
    cnt += 1


# for문과 딕셔너리
'''
for key in 딕셔너리:
    딕셔너리[key]를 이용한 명령문 
'''
print('-'*20)
dict = { 100:'백', 200:'이백', 300:'삼백'}
# print(dict[300])
for key in dict:
    print(f'{key} => {dict[key]}')

# 중복 for문
print('-'*20)
for i in range(1,4):
    print(i)
    for j in range(1,4):
        print('\t\t', j)
    print('='*50)


# 구구단 출력하기
# 2 X 1 = 2
#  ...
# 9 X 9 = 81
for i in range(2, 10):
    print(f'\n\t\t {i} 단 ')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')

# 함수란? 명령어의 집합
'''
def 함수명(인자):
    명령문 ...
    return 결과변수나값  
'''

# 사용자함수1 - 인자X, returnX
# hello world 10번 출력하는 함수 정의
def helloWorld():
    print('-'*40)
    for i in range(10):
        print('Hello world')

# 함수 호출
helloWorld()
helloWorld()

# 사용자함수2 - 인자O, returnX
# 두수의 합과 차를 출력하는 함수 정의
def plusMinus(n1, n2):
    print('-' * 40)
    print(f'{n1} + {n2} = {n1+n2}')
    print(f'{n1} - {n2} = {n1-n2}')

# 함수 호출
plusMinus(10, 5)
plusMinus(50, -7)

# 사용자함수3 - 인자O, returnO
# n1~n2 까지의 총합을 구하는 함수 정의
def sumNM(n1, n2):
    result = 0
    for i in range(n1, n2+1):
        result += i
    return result

# 출력문안에서 함수 호출
print(f'1~100 까지의 합은? {sumNM(1, 100)}')
print(f'50~80 까지의 합은? {sumNM(50, 80)}')

# 사용자함수4 - 인자 O, return O
# return 값이 여러개인 경우 => 튜플
# 세수의 합과 곱의 결과를 반환한다.
def threeNumber(n1, n2, n3):
    return n1+n2+n3, n1*n2*n3

# 출력문안에서 함수 호출
print(threeNumber(10, 20, 45)) # (75, 9000)
result = threeNumber(10, 20, 45)
print(f'세수의 합은? {result[0]}')
print(f'세수의 곱은? {result[1]}')
'''
세수의 합은? 75
세수의 곱은? 9000
'''

# 사용자함수5 - 가변인자 O, return O/X
'''
def 함수명(*args):
    args튜플을이용한명령문 
'''
# n개의 숫자의 합을 반환한다.
def sumN(*args):
    result = 0
    for item in args:
        result += item
    return result, args

print(sumN(100, 200))
print(sumN(4, 5, 6, 7))

# 마지막 퇴실 QR 신호








