import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.zillertalarena.com/winter/events/eventkalender/"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

entries = []
for event in soup.select(".event-list-entry"):
    name = event.select_one(".event-title").get_text(strip=True)
    date = event.select_one(".event-date").get_text(strip=True)
    location = event.select_one(".event-location").get_text(strip=True) if event.select_one(".event-location") else "Zillertal"
    link = URL

    entries.append({
        "name": name,
        "date": date,
        "location": location,
        "cost": "",
        "link": link
    })

with open("public/events.json", "w") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
