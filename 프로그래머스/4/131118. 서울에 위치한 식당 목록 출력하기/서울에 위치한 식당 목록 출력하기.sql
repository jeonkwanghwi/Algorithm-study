-- 코드를 입력하세요
# 서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회

# 리뷰 평균점수는 소수점 세 번째 자리에서 반올림 해주시고
# 결과는 평균점수를 기준으로 내림차순 정렬해주시고
# 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬

select ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, round(avg(rv.REVIEW_SCORE), 2) as SCORE
from REST_INFO ri join REST_REVIEW rv on ri.REST_ID=rv.REST_ID
group by ri.address
having address like '서울%'
order by SCORE desc, ri.FAVORITES desc