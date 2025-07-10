// 1. FRONTEND: React App mit Vite (statische Eventanzeige)

import { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";

export default function EventApp() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("/events.json")
      .then((res) => res.json())
      .then(setEvents);
  }, []);

  return (
    <div className="p-4 grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
      {events.map((event, i) => (
        <Card key={i}>
          <CardContent>
            <h2 className="text-xl font-bold">{event.name}</h2>
            <p className="text-sm">📍 {event.location}</p>
            <p className="text-sm">📅 {event.date}</p>
            <p className="text-sm">🎟️ {event.cost || "kostenlos"}</p>
            <a
              href={event.link}
              target="_blank"
              className="text-blue-600 underline text-sm"
            >
              Mehr Infos
            </a>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}

// 2. SCRAPER (Beispiel mit Python + BeautifulSoup für Telfs)
// Datei: scrape_events.py

/*
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
    json.dump(entries, f, indent=2)
*/

// 3. AUTOMATISIERUNG: GitHub Actions (z. B. alle 24h)
// Datei: .github/workflows/scrape.yml

/*
name: Scrape Events

on:
  schedule:
    - cron: '0 2 * * *'  # täglich um 2:00 Uhr UTC
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install beautifulsoup4 requests
      - name: Run scraper
        run: python scrape_events.py
      - name: Commit changes
        run: |
          git config --global user.name "github-actions"
          git config --global user.email "actions@github.com"
          git add public/events.json
          git commit -m "update events" || echo "No changes"
          git push
*/

