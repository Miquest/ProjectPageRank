from collections import Counter
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time
import re
from .models import Keyword, PageKeyword, WebPage, Link


class Crawler:

    def __init__(self, start_url: str):
        self.start_url = start_url
        self.headers = {
            'User-Agent': 'PythonCrawler/1.0'
        }

    @staticmethod
    def clean_text(text: str):
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words

    def collect_page_metadata(self, soup: BeautifulSoup, url: str):
        title_tag = soup.find('title')
        title = title_tag.text if title_tag else "Kein Titel gefunden"
        print(f"Titel: {title}")

        expression_list = self.clean_text(soup.get_text())
        keyword_count = Counter(expression_list)

        print(url)

        if WebPage.objects.filter(url=url).exists():
            current_web_page = WebPage.objects.get(url=url)
        else:
            current_web_page = WebPage.objects.create(url=url,
                                                      title=title,
                                                      content=soup.get_text(
                                                          separator=" ", strip=True))

            current_web_page.save()

        for word, count in keyword_count.items():
            # Filter words like "is" or "I" etc.
            if len(word) < 3:
                continue

            keyword_object, _ = Keyword.objects.get_or_create(word=word)

            # Connection table between keywords and web pages
            PageKeyword.objects.update_or_create(
                page=current_web_page,
                keyword=keyword_object,
                frequency=count
            )

    def find_links(self, soup: BeautifulSoup, url: str) -> set:

        current_page = WebPage.objects.filter(url=url).first()
        anchors = soup.find_all("a", href=True)
        queue_items = set()

        for anchor in anchors:
            link = anchor["href"]

            # Skip links that do not start with http
            if not link.startswith("http"):
                continue

            target_page, _ = WebPage.objects.get_or_create(url=link)

            if current_page != target_page:
                Link.objects.get_or_create(
                    from_page=current_page,
                    to_page=target_page
                )

                queue_items.add(link)

        return queue_items

    def crawl(self, max_pages=5):

        visited = set()
        crawl_counter = 0
        queue = set()
        queue.add(self.start_url)

        while queue and crawl_counter < max_pages:
            current_url = queue.pop()

            if current_url in visited:
                continue

            print(f"\nCrawling: {current_url}")

            try:
                response = requests.get(current_url, headers=self.headers)
                response.raise_for_status()
            except RequestException:
                print("Error reaching this page. Continue...")
                continue

            # Parse content and add URL to visited set
            soup = BeautifulSoup(response.content, 'html.parser')
            visited.add(current_url)
            self.collect_page_metadata(soup, current_url)

            new_items = self.find_links(soup, current_url)
            queue = queue.union(new_items)

            time.sleep(0.3)

            crawl_counter += 1
