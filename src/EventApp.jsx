import { useEffect, useState } from "react";

export default function EventApp() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("/events.json")
      .then((res) => res.json())
      .then((data) => setEvents(data))
      .catch((err) => console.error("Fehler beim Laden der Events:", err));
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6"> Events in Tirol</h1>
      <div className="grid gap-4">
        {events.length === 0 ? (
          <p className="text-gray-500">Keine Events gefunden.</p>
        ) : (
          events.map((event, idx) => (
            <div key={idx} className="border rounded-xl p-4 shadow">
              <h2 className="text-xl font-semibold">{event.name}</h2>
              <p className="text-sm text-gray-600"> {event.date}</p>
              <p className="text-sm"> {event.location}</p>
              {event.cost && <p className="text-sm"> {event.cost}</p>}
              {event.link && (
                <a
                  href={event.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 underline text-sm mt-2 inline-block"
                >
                  Zur Veranstaltung →
                </a>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

