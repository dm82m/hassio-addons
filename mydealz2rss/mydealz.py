import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone
import json
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_deals(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    deals = []

    for article in soup.select("article.cept-thread-item"):
        title_elem = article.select_one("a.cept-tt.thread-link")
        if not title_elem:
            continue
        title = title_elem.get("title", "").strip()
        link = title_elem['href']
       
        desc_elem = article.select_one(".overflow--wrap-break.width--all-12.size--all-s.space--t-2.color--text-TranslucentSecondary.hide--toW3")
        description = desc_elem.get_text(strip=True) if desc_elem else ""

        price = "k.A."
        old_price = "k.A."
        percentage = "k.A."
        temperature = "k.A."
        merchant = "k.A."
        image_url = ""

        vue_data_elem = article.select_one("[data-vue3]")
        if vue_data_elem:
            vue_data_raw = vue_data_elem.get("data-vue3", "")
            try:
                vue_data = json.loads(vue_data_raw)
                thread = vue_data["props"]["thread"]
                
                price = thread.get("price", "k.A.")
                old_price = thread.get("nextBestPrice", "k.A.")
                temperature = round(thread.get("temperature", "k.A."))

                main_image = thread.get("mainImage")
                if main_image:
                    image_path = main_image.get("path", "")
                    image_name = main_image.get("name", "")
                    image_ext = main_image.get("ext", "")
                    image_url = f"https://static.mydealz.de/{image_path}/{image_name}.{image_ext}"

                merchant_data = thread.get("merchant")
                merchant = merchant_data.get("merchantName", "k.A.") if merchant_data else "k.A."

                user_data = thread.get("user")
                user = user_data.get("username", "k.A.") if user_data else "k.A."

            except json.JSONDecodeError:
                print("Fehler beim Parsen von data-vue3")

        if price != "k.A." and old_price != "k.A.":
            try:
                price_val = float(str(price).replace(",", "."))
                old_price_val = float(str(old_price).replace(",", "."))
                if price_val > 0 and old_price_val > 0:
                    percentage = int(round((old_price_val - price_val) / old_price_val * 100, 0))
            except ValueError:
                pass

        summary = f"<strong>Temperatur:</strong> {temperature}°<br>" \
            f"<strong>Preis:</strong> {price}€ | <s>{old_price}€</s> | -{percentage}%<br>" \
            f"<strong>Händler:</strong> {merchant} | <strong>Autor:</strong> {user}<br><br>" \
            f"<strong>Beschreibung:</strong> {description}<br>"
        if image_url:
            summary += f'<br><img src="{image_url}" width="300">'

        deals.append({
            "title": title,
            "link": link,
            "summary": summary,
            "image": image_url,
            "pubDate": datetime.now(timezone.utc)
        })

    return deals

def generate_rss(deals):
    fg = FeedGenerator()
    fg.title("mydealz2rss")
    fg.link(href="https://www.mydealz.de", rel="alternate")
    fg.description("Enthält alle Deals der mydealz.de Startseite.")
    fg.language("de")

    for deal in deals:
        fe = fg.add_entry()
        fe.title(deal["title"])
        fe.guid(deal["link"], True)
        fe.link(href=deal["link"])
        fe.description(deal["summary"])
        fe.pubDate(deal["pubDate"])

        if "image" in deal:
            fe.enclosure(deal["image"], 0, "image/jpeg")

    fg.rss_file("/homeassistant/www/mydealz.xml", pretty=True)

if __name__ == "__main__":
    while True:
        print("Fetching deals of mydealz main page ...")
        deals_main = fetch_deals("https://www.mydealz.de/")
        generate_rss(deals_main)
        print(f"Fetched {len(deals_main)} deals. RSS feed generated. Now sleeping for 10 minutes ...")
        time.sleep(600)
