# web scraping from newspaper

import requests
r = requests.get("https://www.feedspot.com/infiniterss.php?q=site:https%3A%2F%2Fwww.theonion.com%2Frss")

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find_all("div", attrs={"class":"ocni"})

records = []

for result in results:
    titles = result.find("a").text

    records.append((titles))

print("<::> Top Headlines for Today <::>")
for headline in records[0:3]:
    print("<:> " + headline)