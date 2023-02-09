-- 코드를 입력하세요
SELECT user_id, product_id FROM online_sale
group by user_id, product_id
having count(user_id) > 1
ORDER BY user_id ASC, product_id DESC