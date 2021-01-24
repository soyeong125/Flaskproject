# 모듈의 종류 - 표준모듈, 외부모듈, 사용자정의모듈
# 모듈 임포트 방법 1
# import 모듈명
# 모듈명.함수(옵션)
# 모듈명.속성
# math 모듈은 수학과 관련된 함수와 속성 포함 => 표준모듈
# import math
# print(math.pi)
# print(math.sin(100))

# 모듈 임포트 방법 2 - 별칭
# import 모듈명 as 별칭
# 별칭.함수(옵션)
# 별칭.속성
# import math as m
# print(m.pi)
# print(m.sin(100))


# 모듈 임포트 방법 3 - from
# 모듈명을 사용하지 않고 특정 함수명이나 속성을
# 직접 호출하는 방법
# from 모듈명 import 함수명이나속성
# 함수(옵션)
# 속성
from math import pi, sin
print(pi)
print(sin(100))

# 사용자정의모듈 - 직접 모듈을 만들어서 사용한다.
# 1. 별도의 *.py 파이썬 파일 생성. 함수 정의
# 2. 별도의 파이썬 파일에서 1번에서 생성한 파일 임포트 하여 사용
# import 파이썬파일명
# import gugu

# 모듈안의 함수 호출
# gugu.guguPrint1()
# gugu.guguPrint2(5)

# 패키지안의 모듈 사용하기
# 1. 패키지 폴더 생성
#   Project 창에서 프로젝트 마우스 우측 클릭
#   Python Package
#   패키지 폴더안에서 자동으로 __init__.py
# 2. 패키지안에 모듈 파일 생성
#    모듈안에 함수 정의
# 3. 별도의 파이썬 파일에서 2번에서 생성한 파일 임포트 하여 사용
# import 패키지명.모듈
# import 패키지명.모듈 as 별칭
# from 패키지명.모듈 import 함수
# from 패키지명 import 모듈

# import AAA.calculator
# AAA.calculator.cal(34,7)

from AAA import calculator
calculator.cal(100, 7)

# 외부 모듈 => Flask, pymysql
# 설치1 - [File]-[Settings] 의 [Project ~]-[Interpreter] 대화상자 이용
#         하단의 [+] 클릭해서 설치할 패키지모듈명 검색 후 [Install Package] 클릭

# 설치2 - Terminal 모드를 이용하여 명령 입력후 실행
#         하단 [Terminal] 탭 클릭
# 설치되어 있는 목록 확인
# pip list
# conda list
# pymysql => MYSQL 연동하는 외부 모듈
# pip install 패키지모듈명
# conda install 패키지모듈명
# pip install pymysql
# conda install pymysql













