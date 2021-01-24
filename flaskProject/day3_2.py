# 데이타베이스 연동

# 플라스크 관련 모듈 임포트
from flask import Flask, render_template, request
# db 연동 모듈 임포트
import db
# 페이지 이동 모듈 임포트
from flask import redirect, url_for


app = Flask(__name__)

# 시작 페이지
@app.route('/')
def index():
    # 테이블 전체 레코드 저장 => 리스트 딕셔너리
    country_list = db.get_country_list()
    # 문자열구조로 변경해서 반환
    # return str(country_list)
    return render_template('index4.html', country_list=country_list, totalCount = len(country_list))


# 레코드 상세 페이지 - 쿼리 스트링 방식으로 데이타 전달받아서
# 레코드 조회 함수에 전달하여 관련 레코드 저장
@app.route('/country/<no>')
def country(no):
    temp_dic = db.country(no)
    # return str(temp_dic)
    return render_template('country.html', temp_dic=temp_dic)

# 레코드 추가 페이지 - 폼문서로 연결
@app.route('/country_add')
def country_add():
    return render_template('country_add.html')

# 레코드 추가 폼에서 전달받은 데이타를
# db에 반영
@app.route('/country_add_pro', methods=['POST'])
def country_add_pro():
    # 입력데이타를 변수에 저장
    code = request.form['code']
    name = request.form['name']
    gnp = request.form['gnp']
    population = request.form['population']
    # DB에 반영
    db.country_add(code, name, gnp, population)
    # return '<h1>레코드 추가 완료</h1><p><a href="/">첫번째 페이지로</a></p>'
    # 시작 페이지로 주소로 이동    #
    return redirect('/')

# 레코드 삭제
@app.route('/country_delete_pro/<no>')
def country_delete_pro(no):
    # db에 반영
    db.country_delete(no)
    # 시작 페이지로 주소로 이동
    return redirect('/')

# 레코드 수정 페이지로 이동
@app.route('/country_update/<no>')
def country_update(no):
    # 레코드 번호에 해당하는 데이타 저장
    temp_dic = db.country(no)
    # 각각의 레코드 수정 페이지로 이동
    # return str(temp_dic)
    return render_template('country_update.html', temp_dic=temp_dic)


# 레코드 수정 폼에서 전달받은 데이타를
# db에 반영
@app.route('/country_update_pro', methods=['POST'])
def country_update_pro():
    # 입력데이타를 변수에 저장
    gnp = request.form['gnp']
    population = request.form['population']
    # 히든 필드에서 받은 데이타를 변수에 저장
    no = request.form['no']
    # DB에 반영
    db.country_update(gnp, population, no)
    # return '<h1>레코드 추가 완료</h1><p><a href="/">첫번째 페이지로</a></p>'
    # 시작 페이지로 주소로 이동    #
    # return redirect('/')
    # 레코드 상세 페이지로 이동
    # return redirect(url_for('뷰함수명', 변수1=변수2)))
    # country(no) 함수 호출
    return redirect(url_for('country', no=int(no)))



app.run(host='127.0.0.1', port=5000, debug=True)

