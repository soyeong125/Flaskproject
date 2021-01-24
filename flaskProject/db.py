# mysql 연동 모듈
import pymysql

# 데이터 베이스에 접속하는 함수
def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
                            password='1234', db='sample1', charset='utf8')
    # if conn:
    #     print('디비 접속 완료')
    #     print('conn')
    return conn

# 연결 테스트 함수호출
# get_connection()

# 전체 테이블 조회 및 저장 함수 정의
def get_country_list():
    # 연결자
    conn = get_connection()
    # 커서 생성
    cursor = conn.cursor()
    # sql 레코드 조회 - 마지막에 추가된 레코드가 가장 위에 표시
    sql = ''' select * from worldcity order by no desc; '''
    # sql 실행
    cursor.execute(sql)

    # 커서의 결과 데이타 저장 => 2차원 튜플 구조
    # fetchall() , fetchone(), fetchmany(n)
    # 전체 레코드
    result = cursor.fetchall()
    # 1개의 레코드
    # result = cursor.fetchone()
    # n개의 레코드
    # result = cursor.fetchmany(3)
    # print(type(result), len(result))
    # print(result)

    # 리스트 딕셔너리 :리스트안의 딕셔너리로 있는 자료구조
    temp_list = []
    for row in result:
        temp_dic = {}
        # 키이름을 테이블의 컬럼명으로 지정
        temp_dic['No'] = row[0]
        temp_dic['Code'] = row[1]
        temp_dic['Name'] = row[2]
        temp_dic['GNP'] = row[3]
        temp_dic['Population'] = row[4]
        temp_list.append(temp_dic)

    # 접속종료
    conn.close()
    # 리스트 딕셔너리 반환
    return  temp_list


# 전체 테이블 조회 함수 호출 및 데이타 구조  확인
# print(get_country_list())
# print(get_country_list()[0])

# 특정 레코드를 검색하는 저장 반환하는 함수 정의
# 검색 필드명은 기본키인 No
def country(country_no):
    # 연결자
    conn = get_connection()
    # 커서 생성
    cursor = conn.cursor()
    # sql 레코드 조회 - country_no으로 검색
    sql = ''' select * from worldcity where no= %s; '''
    # sql 실행
    cursor.execute(sql, country_no)
    # 결과 저장 => 튜플
    result = cursor.fetchone()

    # 튜플 => 딕셔너리 구조로 변경
    temp_dic = {}
    # 키이름을 테이블의 컬럼명으로 지정
    temp_dic['No'] = result[0]
    temp_dic['Code'] = result[1]
    temp_dic['Name'] = result[2]
    temp_dic['GNP'] = result[3]
    temp_dic['Population'] = result[4]

    # 접속종료
    conn.close()
    # 딕셔너리 반환
    return temp_dic

# 특정 레코드 조회 함수 호출
# print(country(12))


# 레코드 추가 함수
def country_add(code, name, gnp, population):
    # 연결자
    conn = get_connection()
    # 커서 생성
    cursor = conn.cursor()
    # sql 레코드 추가 명령
    sql = ''' insert into worldcity (code, name, gnp, population)
	                values (%s, %s, %s, %s); '''
    # sql 실행
    cursor.execute(sql, (code, name, gnp, population))
    # db 에 반영
    conn.commit()
    # 접속종료
    conn.close()

# 레코드 추가 테스트
# country_add('MCO', 'Monaco', 776, 34000)
# print(get_country_list())


# 레코드 삭제 함수 정의
def country_delete(no):
    # 연결자
    conn = get_connection()
    # 커서 생성
    cursor = conn.cursor()
    # sql 레코드 삭제제명령
    sql = ''' delete from worldcity where no=%s; '''
    # sql 실행
    cursor.execute(sql, no)
    # db 에 반영
    conn.commit()
    # 접속종료
    conn.close()

# 레코드 삭제 테스트
# country_delete(32)
# print(get_country_list())


# 레코드 수정 함수 정의
def country_update(gnp, population, no):
    # 연결자
    conn = get_connection()
    # 커서 생성
    cursor = conn.cursor()
    # sql 레코드 수정 명령 - 순서 주의
    sql = ''' update worldcity 
                set gnp=%s, population=%s where no=%s;'''
    # sql 실행
    cursor.execute(sql, (gnp, population, no))
    # db 에 반영
    conn.commit()
    # 접속종료
    conn.close()

# 레코드 수정 테스트
# 30번 레코드 수정
# country_update(100, 100, 30)
# print(country(30))