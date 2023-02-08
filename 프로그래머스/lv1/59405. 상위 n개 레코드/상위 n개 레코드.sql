-- 코드를 입력하세요
SELECT name from ANIMAL_INS
where DATETIME = (select min(DATETIME) from ANIMAL_INS)