-- 코드를 입력하세요
SELECT ain.name, ain.DATETIME from ANIMAL_INS ain left join ANIMAL_OUTS aout
on ain.ANIMAL_ID = aout.ANIMAL_ID
where aout.ANIMAL_ID is null
order by ain.DATETIME
limit 3