import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.mayrhofen.at/de/pages/events-zillertal"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

entries = []
for event in soup.select(".event-teaser"):
    name = event.select_one(".title").get_text(strip=True)
    date = event.select_one(".date").get_text(strip=True)
    location = event.select_one(".location").get_text(strip=True) if event.select_one(".location") else "Mayrhofen"
    link = "https://www.mayrhofen.at" + event.select_one("a")["href"]

    entries.append({
        "name": name,
        "date": date,
        "location": location,
        "cost": "",
        "link": link
    })

with open("public/events.json", "w") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
