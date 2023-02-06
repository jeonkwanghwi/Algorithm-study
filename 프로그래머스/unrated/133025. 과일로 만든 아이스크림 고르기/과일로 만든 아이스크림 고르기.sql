-- 코드를 입력하세요
# 총 주문량 > 3000
# 주성분 과일
# 총 주문량 큰 순서대로

select FIRST_HALF.flavor from FIRST_HALF, ICECREAM_INFO
where FIRST_HALF.flavor = ICECREAM_INFO.flavor and ICECREAM_INFO.INGREDIENT_TYPE = 'fruit_based' and FIRST_HALF.TOTAL_ORDER > 3000
order by FIRST_HALF.TOTAL_ORDER desc