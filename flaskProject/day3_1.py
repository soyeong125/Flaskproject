# 1. 플라스크 관련 모듈 임포트
from flask import Flask, render_template

# 2. 플라스크 app 객체 생성
app = Flask(__name__)

# 3. 라우터 등록 => 웹상 주소 생성
@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/sub1')
def sub1():
    return render_template('sub1.html')

@app.route('/sub2')
def sub2():
    return render_template('sub2.html')

# 4. app 실행
app.run(host='127.0.0.1', port=5000, debug=True)

# 5. 결과 확인은? - 웹브라우저
# http://127.0.0.1:5000/
# localhost:5000
