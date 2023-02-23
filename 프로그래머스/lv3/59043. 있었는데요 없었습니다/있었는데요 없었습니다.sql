-- 코드를 입력하세요
SELECT ain.animal_id, ain.name from ANIMAL_INS ain join ANIMAL_OUTS aout
on ain.ANIMAL_ID = aout.ANIMAL_ID
# ain.DATETIME = aout.DATETIME and  and ain.ANIMAL_TYPE = aout.ANIMAL_TYPE and ain.NAME = aout.NAME
where aout.DATETIME < ain.DATETIME
order by ain.DATETIME