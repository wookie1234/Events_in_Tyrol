// src/EventApp.jsx
import React, { useEffect, useState } from "react";

const EventApp = () => {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/events.json")
      .then((res) => res.json())
      .then((data) => {
        setEvents(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Fehler beim Laden von events.json:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p className="p-4">Lade Events...</p>;

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Events in Tirol</h1>
      {events.length === 0 ? (
        <p>Keine Events gefunden.</p>
      ) : (
        <div className="grid gap-4">
          {events.map((event, i) => (
            <div
              key={i}
              className="border rounded-xl p-4 shadow-sm hover:shadow-md transition"
            >
              <h2 className="text-xl font-semibold">{event.name}</h2>
              <p className="text-sm">📅 {event.date}</p>
              <p className="text-sm">📍 {event.location}</p>
              {event.cost && <p className="text-sm">💶 {event.cost}</p>}
              {event.link && (
                <a
                  href={event.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 underline text-sm mt-2 inline-block"
                >
                  Mehr Infos
                </a>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default EventApp;
