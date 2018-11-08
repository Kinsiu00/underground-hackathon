import requests
r = requests.get("https://www.feedspot.com/infiniterss.php?q=site:https%3A%2F%2Fwww.theonion.com%2Frss")

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find_all("div", attrs={"class":"ocni"})

records = []

for result in results:
    explantion = result.find("a").text

    records.append((explantion))

print(records[0])
