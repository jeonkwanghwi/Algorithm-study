-- 코드를 입력하세요
select INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF join ICECREAM_INFO using(flavor)
group by INGREDIENT_TYPE
order by TOTAL_ORDER

# select INGREDIENT_TYPE, COUNT(TOTAL_ORDER) AS TOTAL_ORDER
# FROM FIRST_HALF JOIN ICECREAM_INFO USING(FLAVOR)
# GROUP BY INGREDIENT_TYPE
# ORDER BY TOTAL_ORDER;