-- 코드를 입력하세요
SELECT aout.ANIMAL_ID, aout.NAME from ANIMAL_INS ain right join ANIMAL_OUTS aout
on ain.ANIMAL_ID = aout.ANIMAL_ID
where ain.ANIMAL_ID is null
order by aout.ANIMAL_ID