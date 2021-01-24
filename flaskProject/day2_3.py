from flask import Flask
# render_template => html 파일 연동 모듈
from flask import render_template
# request => get/post 연동 모듈
from flask import request

# __name__ 파이썬에서 제공하는 특별한 변수
app = Flask(__name__)

# 시작 루트주소
@app.route('/')
def index():
    return render_template('index.html')

# 두번째 페이지 연동 주소 /second
@app.route('/second')
def second():
    return render_template('second.html')


# 세번째 페이지 연동 주소 /third
@app.route('/third')
def third():
    return render_template('third.html')


# getpost Test 페이지 연동주소 /formTest
@app.route('/formTest')
def getpost():
    return render_template('formTest.html')

# GET/POST 출력 처리 페이지 연동 주소 /result
# request.method : 메소드방식 출력
@app.route('/result', methods = ['GET', 'POST'])
def result():
    print(request.method)
    return 'request => ' + request.method


# getTest 페이지 연동주소 /getTest
@app.route('/getTest')
def getTest():
    return render_template('getTest.html')

# getTest 페이지 결과 /resultGet
# GET 방식의 전달받은 값 호출
# 변수는 텍스트필드 input:text 의 name값
# request.args['변수']
# request.args.get('변수')
# request.values.get('변수')
@app.route('/resultGet', methods=['GET'])
def resultGet():
    print('요청방식 =>', request.method)
    # 텍스트필드 값을 변수로 전달
    data1 = request.args['data1']
    data2 = request.args.get('data2')
    data3 = request.values.get('data3')
    print(data1, data2, data3)
    # 파이썬 변수값을 html 페이지에 전달하기
    # render_template('url', 변수1=변수2)
    # return 'result Get' + data1 + data2 + data3
    # html파일에서 전달받은 파이썬변수 사용은 {{변수명}}
    return render_template('result1.html', data1=data1, data2=data2, data3=data3)


# postTest 페이지 연동주소 /postTest
@app.route('/postTest')
def postTest():
    return render_template('postTest.html')

# resultPost 페이지 결과 /resultPost
# POST 방식의 전달받은 값 처리
# 변수는 텍스트필드 input:text 의 name값
# request.form['변수']
@app.route('/resultPost', methods=['POST'])
def resultPost():
    print('요청방식 =>', request.method)
    # 텍스트필드 값을 변수로 전달
    data1 = request.form['data1']
    data2 = request.form['data2']
    data3 = request.form['data3']
    print(data1, data2, data3)
    # 파이썬 변수값을 html 페이지에 전달하기
    # render_template('url', 변수1=변수2)
    # return 'result Get' + data1 + data2 + data3
    # html파일에서 전달받은 파이썬변수 사용은 {{변수명}}
    return render_template('result1.html', data1=data1, data2=data2, data3=data3)



# 앱실행.
# 이파일이 메인으로 실행하는가?
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


'''
# 웹서버의 라우터주소랑 html 연결
# render_template 모듈 이용 
1) html 문서 생성 
   templates 폴더 위치에 저장 
   ex) templates/index.html 
2) 파이썬 파일에서 모듈 임포트 
   from flask import render_template
    
3) @app.route(주소)
def 함수명():
    return render_template(html경로)

'''

'''
# static 폴더 
# - html 문서에 삽입되는 이미지, css, js 파일은 별도의 static 폴더에 저장 
# - 삽입시 경로는 static/파일이름.확장자
'''

# 2:00 ~ 2:10 사이 QR 5교시 체크