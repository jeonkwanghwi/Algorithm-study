-- 코드를 입력하세요
SELECT b.book_id, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE from book b, author a
where b.category = "경제" and b.AUTHOR_ID = a.AUTHOR_ID
order by b.PUBLISHED_DATE asc;