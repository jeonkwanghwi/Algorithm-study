select b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book b natural join author a
where b.category = '경제'
order by b.PUBLISHED_DATE