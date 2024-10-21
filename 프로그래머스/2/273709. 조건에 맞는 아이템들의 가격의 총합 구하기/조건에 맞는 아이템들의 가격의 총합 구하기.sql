-- 코드를 작성해주세요
select sum(price) as TOTAL_PRICE
from ITEM_INFO 
group by RARITY
having RARITY = 'LEGEND'