-- 코드를 입력하세요
SELECT pt_name, PT_NO, GEND_CD, age, IFNULL(TLNO, "NONE") AS TLNO from patient
where age <= 12 and GEND_CD = 'W'
order by age desc, PT_NAME asc;