from flask import Flask, render_template, request

app = Flask(__name__)

# / 주소
@app.route('/')
def index():
    x = 100
    y = 200
    cityList = ['서울', '부산', '대전', '전주', '용인']
    wordDict = {'b':'boat', 's':'style', 'w':'west', 'e':'egg', 'h':'home'}
    # for 문이용해서 리스트와 딕셔너리 출력
    for item in cityList:
        print(item)
    print('-'*30)
    for key in wordDict:
        print(key, wordDict[key])

    return render_template('index2.html', x=x, y=y, cityList=cityList, wordDict=wordDict)


# if 테스트 /ifTest 주소
@app.route('/ifTest')
def ifTest():
    userAge = 30
    myNum = -90
    return render_template('if_result.html', userAge=userAge, myNum=myNum)


# 쿼리스트링 연동 페이지 주소
# /주소/<값1이나변수1>/<값2이나변수3>
# /user/<userName>/<userAge>
# 뷰함수 생성시 전달받은 변수는 인자파라미터로 전달
@app.route('/user/<userName>/<userAge>')
def user(userName, userAge):
    # return 'userName = ' + userName
    return render_template('qr_result.html', userName=userName, userAge=userAge)


app.run(host='127.0.0.1', port=5000, debug=True)

'''
# HTML 문서에서 파이썬 반복문 for 이용하기
{% for i in range(start, end, step) %}
  {{ 변수나 값 }}
{% endfor %}

{% for item in 리스트명 %}
  {{ item }}
{% endfor %}

{% for key in 딕셔너리명 %}
  {{ key, 딕셔너리명[key] }}
{% endfor %}


# HTML 문서에서 조건문  if   이용하기
{% if 조건식 %}
        {{ 값 }} 또는 태그, 문자열
 {% elif 조건식 %}
        {{ 값 }} 또는 태그, 문자열
  {% else %}
        {{ 값 }} 또는 태그, 문자열
  {% endif %}


# 쿼리 스트링 방식 => 하이퍼링크로 값 전달 
# 주소URL 형식
# @app.route('/url/<데이타변수1>/<데이타변수2>')
# 등록함수에서 데이타변수 출력
# return '문자열 : ' + 변수
# return f'문자열 : {변수}'
  
'''

