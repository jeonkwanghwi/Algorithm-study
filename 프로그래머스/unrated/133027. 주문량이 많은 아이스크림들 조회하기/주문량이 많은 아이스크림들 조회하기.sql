-- 코드를 입력하세요
SELECT JULY.FLAVOR from FIRST_HALF fh, july
where fh.FLAVOR = july.FLAVOR
group by july.flavor
order by sum(july.TOTAL_ORDER) + sum(fh.TOTAL_ORDER) desc
limit 3;