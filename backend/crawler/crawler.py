import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

def crawl_wikipedia(start_url, max_pages=5):
    visited = set()
    queue = [start_url]
    base_url = "https://de.wikipedia.org"

    links_to = {}

    headers = {
        'User-Agent': 'PythonCrawler/1.0'
    }

    print(f"Starte Crawler. Ziel: {max_pages} Seiten.\n" + "-"*40)

    while queue and len(visited) < max_pages:
        current_url = queue.pop(0)

        if current_url in visited:
            continue

        print(f"\nCrawle: {current_url}")

        try:
            response = requests.get(current_url, headers=headers)
            response.raise_for_status() # Prüft auf HTTP-Fehler (z.B. 404)
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Abrufen: {e}")
            continue

        # HTML mit BeautifulSoup parsen
        soup = BeautifulSoup(response.content, 'html.parser')
        visited.add(current_url)

        # --- DATEN EXTRAHIEREN ---

        # 1. Titel der Seite (steht im <h1> Tag mit der ID 'firstHeading')
        title_tag = soup.find('h1', id='firstHeading')
        title = title_tag.text if title_tag else "Kein Titel gefunden"
        print(f"Titel: {title}")

        # 2. Ersten echten Absatz extrahieren
        content_div = soup.find('div', class_='mw-parser-output')
        if content_div:
            # Finde alle <p> Tags direkt im Inhaltsbereich
            for p in content_div.find_all('p', recursive=False):
                if p.text.strip(): # Den ersten nicht-leeren Absatz nehmen
                    print(f"Vorschau: {p.text.strip()[:100]}...")
                    break

        # --- NEUE LINKS FINDEN ---

        links_to[current_url] = []

        for link in soup.find_all('a', href=True):
            href = link['href']

            if href.startswith("http"):
                links_to[current_url].append(href)


            if href.startswith('/wiki/') and ':' not in href:
                full_url = urljoin(base_url, href)

                if full_url not in visited and full_url not in queue:
                    queue.append(full_url)

        time.sleep(0.5)

    print("\n" + "-"*40 + f"\nCrawl beendet. {len(visited)} Seiten besucht.")
    print(links_to)