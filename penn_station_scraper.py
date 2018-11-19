# scrape information from the schedule of penn station

import requests
r = requests.get("http://traintime.lirr.org/departureResults.php?sta=NYK")

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find_all("div", attrs={"class":"trlist"})

# -------title of each columns-------
table_header = soup.find_all("th")
headers = []
for columns_titles in table_header:
    headers.append((columns_titles.text))


print("<:>", headers)
print("----------------------------------------------------")

# -------information about each train trip from Penn Station-------

info = soup.find_all("tr")[1:-7]
info_arr = []

for row in info:
    each_info = row.contents
    time = row.contents[1].text
    destination = row.contents[2].text
    departure = row.contents[3].text
    track = row.contents[4].text
    if track == '':
        track = "TBD"

    info_arr.append((time,destination,departure,track))

for travel in info_arr[0:4]:
    print("<:>", travel)


print("----------------------------------------------------")
print('\n')