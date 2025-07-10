# scrape_events.py
import json
import os

# Beispielhafte Event-Daten (echte Scraper kommen später)
events = [
    {
        "name": "Musik im Park",
        "date": "2025-08-15",
        "location": "Telfs Zentrum",
        "cost": "frei",
        "link": "https://www.telfs.at/veranstaltungen"
    },
    {
        "name": "Bergfilmfestival",
        "date": "2025-09-01",
        "location": "Innsbruck - Leokino",
        "cost": "10 €",
        "link": "https://www.alpenverein.at/portal/bergsport/bergfilmfestival.php"
    }
]

# Stelle sicher, dass Ordner existiert
os.makedirs("public", exist_ok=True)

# Speichern der Events in JSON-Datei
with open("public/events.json", "w", encoding="utf-8") as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

print(f"{len(events)} Events gespeichert.")
