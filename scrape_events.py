import requests
from bs4 import BeautifulSoup
import json

def scrape_telfs():
    url = "https://www.telfs.at/Freizeit_Veranstaltungen/Veranstaltungsleben/Veranstaltungskalender"
    events = []

    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for item in soup.select(".vmTitle"):
            name = item.get_text(strip=True)
            link = item.find("a")["href"] if item.find("a") else url
            date = item.find_next("div", class_="vmDate").get_text(strip=True) if item.find_next("div", class_="vmDate") else ""
            events.append({
                "name": name,
                "date": date,
                "location": "Telfs",
                "link": link,
                "cost": None
            })
    except Exception as e:
        print(f"[Telfs] Fehler: {e}")
    return events


def scrape_mayrhofen():
    url = "https://www.mayrhofen.at/events/"
    events = []

    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for item in soup.select("article.event"):
            name = item.select_one("h2").get_text(strip=True) if item.select_one("h2") else ""
            date = item.select_one(".date").get_text(strip=True) if item.select_one(".date") else ""
            link = "https://www.mayrhofen.at" + item.find("a")["href"] if item.find("a") else url
            events.append({
                "name": name,
                "date": date,
                "location": "Mayrhofen",
                "link": link,
                "cost": None
            })
    except Exception as e:
        print(f"[Mayrhofen] Fehler: {e}")
    return events


def scrape_innsbruck():
    url = "https://www.innsbruck.info/events.html"
    events = []

    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for item in soup.select("div.card-event"):
            name = item.select_one("h3").get_text(strip=True) if item.select_one("h3") else ""
            date = item.select_one(".event-date").get_text(strip=True) if item.select_one(".event-date") else ""
            link = "https://www.innsbruck.info" + item.find("a")["href"] if item.find("a") else url
            events.append({
                "name": name,
                "date": date,
                "location": "Innsbruck",
                "link": link,
                "cost": None
            })
    except Exception as e:
        print(f"[Innsbruck] Fehler: {e}")
    return events


def scrape_fiss():
    url = "https://www.serfaus-fiss-ladis.at/de/News-Events/Veranstaltungskalender"
    events = []

    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        for item in soup.select("div.teaser"):
            name = item.select_one("h2").get_text(strip=True) if item.select_one("h2") else ""
            date = item.select_one("span.date").get_text(strip=True) if item.select_one("span.date") else ""
            link = "https://www.serfaus-fiss-ladis.at" + item.find("a")["href"] if item.find("a") else url
            events.append({
                "name": name,
                "date": date,
                "location": "Fiss",
                "link": link,
                "cost": None
            })
    except Exception as e:
        print(f"[Fiss] Fehler: {e}")
    return events


def run_all_scrapers():
    all_events = []

    all_events.extend(scrape_telfs())
    all_events.extend(scrape_mayrhofen())
    all_events.extend(scrape_innsbruck())
    all_events.extend(scrape_fiss())

    print(f"Gesammelte Events: {len(all_events)}")

    with open("public/events.json", "w", encoding="utf-8") as f:
        json.dump(all_events, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    run_all_scrapers()
