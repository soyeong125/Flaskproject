-- 4교시 출석체크 QR 1:00~1:10 분 사이 
-- sql 주석 
-- 명령문;
-- use 데이타베이스이름; -- 데이타베이스 사용설정 
-- show tables; -- 테이블 모두 보기 
-- select *|컬럼명 from 테이블명; -- 테이블 데이타보기  
-- select *|컬럼명 from 테이블명 where 컬럼명 = 값 
--        order by 컬럼명 asc/desc limit 갯수;    
use sample1;
show tables;
select * from worldcity;
select * from city;
select code, name from worldcity limit 5;
select code, name from worldcity where code="USA";
select * from worldcity order by no desc;

-- 테이블의 구조 확인 
-- desc 테이블명; 
desc worldcity;

select * from worldcity where no=5;

-- 레코드 추가 
-- insert into 테이블명 (컬럼명....) values (값....);
insert into worldcity (code, name, gnp, population)
	values ('FIN', 'Finland', 121914, 13789);
   
select * from worldcity order by no desc;    

-- 레코드 삭제 
-- delete from 테이블명 where 필드명=값;
-- 10번 레코드 삭제 
delete from worldcity where no=10;
select * from worldcity;  

-- 레코드 수정 
-- update 테이블명 set 필드명1=값1, ... where 필드명=값;
-- 레코드 수정 반영 해제 
-- [Edit]-[Preference] 
-- [SQL Editor] 에서 Safe Updates ~ 체크되어 있다면 해제 
update worldcity set gnp=1000, population=1000 where no=1;
select * from worldcity; 



