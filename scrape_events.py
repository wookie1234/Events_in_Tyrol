import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.telfs.at/Freizeit_Veranstaltungen/Veranstaltungsleben/Veranstaltungskalender"
BASE = "https://www.telfs.at"

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

entries = []
for item in soup.select(".termine-list div.termine-item"):
    name = item.select_one("h3").text.strip()
    date = item.select_one(".datum").text.strip()
    location = item.select_one(".ort").text.strip() if item.select_one(".ort") else "Telfs"
    link = BASE + item.select_one("a")["href"]

    entries.append({
        "name": name,
        "date": date,
        "location": location,
        "cost": "",
        "link": link
    })

with open("public/events.json", "w") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
print(soup.prettify()[:1000])  # Zeigt die ersten 1000 Zeichen des HTMLs
