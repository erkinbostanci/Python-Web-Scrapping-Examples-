# GOAL: Get title of every book with a 2 star rating

from email.mime import base
import requests
import bs4

two_stars_titles = []
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
for n in range(1,20):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0 :
            book_title = book.select('a')[1]['title']
            two_stars_titles.append(book_title)
print(two_stars_titles)
