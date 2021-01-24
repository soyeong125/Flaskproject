# 1. 플라스크 관련 모듈 임포트
from flask import Flask

# 2. 플라스크 app 객체 생성
app = Flask(__name__)
# print(app) # <Flask 'day2_2'>

# 3. 라우터 등록 => 웹상 주소 생성
# @app.route(주소)
# def 함수명(): 뷰함수 정의
#   return 문자열
@app.route('/')
def index():
    return '<h1>Hello World</h1><h2>Test....</h2>'

# 4. app 실행
app.run(host='127.0.0.1', port=5000, debug=True)

# 5. 결과 확인은? - 웹브라우저
# http://127.0.0.1:5000/
# localhost:5000
