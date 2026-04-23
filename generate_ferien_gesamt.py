import requests
from ics import Calendar
from datetime import datetime

urls = {
    "Hamburg": "https://ics.tools/Ferien/hamburg.ics", #hier ics URLS einfügen und den Rest nicht anfassen!ics urls kopieren von https://ics.tools/ //
    "Schleswig-Holstein": "https://ics.tools/Ferien/schleswig-holstein.ics",
    "Niedersachsen": "https://ics.tools/Ferien/niedersachsen.ics",
    "Mecklenburg-Vorpommern": "https://ics.tools/Ferien/mecklenburg-vorpommern.ics"
}

merged = Calendar()
seen = set()

for region, url in urls.items():
    r = requests.get(url)
    cal = Calendar(r.text)

    for event in cal.events:
        key = (event.name, event.begin.date(), event.end.date())

        # Duplikate vermeiden
        if key in seen:
            continue
        seen.add(key)

        # Bundesland hinzufügen
        event.name = f"{event.name} ({region})"

        merged.events.add(event)

# Datei speichern
with open("docs/ferien_gesamt.ics", "w", encoding="utf-8") as f:
    f.write(str(merged))

print("Fertig:", datetime.now())
