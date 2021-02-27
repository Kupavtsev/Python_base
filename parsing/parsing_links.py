import bs4 , requests

res = requests.get("http://allevents.in/lahore/")
soup = bs4.BeautifulSoup(res.text)
for link in soup.select('a[property="schema:url"]'):
    print link.get('href')