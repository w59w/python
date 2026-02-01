import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://intermedia.kg"
CATEGORY_URL = "https://intermedia.kg/catalog/noutbuki_i_aksessuary/noutbuki_i_ultrabuki/"
CATEGORY_NAME = "Ноутбуки и ультрабуки"

def parse_price(text: str) -> int | None:
    if not text:
        return None
    cleaned = text.replace("\xa0", " ")
    m = re.search(r"(\d[\d\s]*)\s*c", cleaned, flags=re.IGNORECASE)
    if not m:
        return None
    digits = re.sub(r"\s+", "", m.group(1))
    return int(digits) if digits.isdigit() else None

def get_html(url: str, session: requests.Session) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0 Safari/537.36"
    }
    r = session.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.text

def parse_catalog_page(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")

    product_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/catalog/noutbuki_i_aksessuary/noutbuki_i_ultrabuki/") and href.endswith(".html"):
            product_links.append(a)

    results = []
    seen_urls = set()

    for a in product_links:
        url = urljoin(BASE_URL, a["href"])
        if url in seen_urls:
            continue
        seen_urls.add(url)

        name = a.get_text(strip=True)
        if not name:
            continue

        parent = a
        for _ in range(5):
            if parent is None:
                break
            parent = parent.parent
            if parent and parent.get_text(strip=True):
                price = parse_price(parent.get_text(" ", strip=True))
                if price is not None:
                    results.append({
                        "category": CATEGORY_NAME,
                        "name": name,
                        "price": price,
                        "url": url
                    })
                    break
        else:
            results.append({
                "category": CATEGORY_NAME,
                "name": name,
                "price": 0,
                "url": url
            })

    return results


def parse_all_pages(max_pages: int = 5) -> list[dict]:

    items: list[dict] = []
    with requests.Session() as session:
        for page in range(1, max_pages + 1):
            url = CATEGORY_URL if page == 1 else f"{CATEGORY_URL}?PAGEN_1={page}"
            html = get_html(url, session)
            page_items = parse_catalog_page(html)

            if not page_items:
                break

            items.extend(page_items)
            print(f"Page {page}: +{len(page_items)} items (total {len(items)})")

    uniq = {}
    for it in items:
        uniq[it["url"]] = it
    return list(uniq.values())


if __name__ == "__main__":
    data = parse_all_pages(max_pages=3)
    print("\nПример первых 5 результатов:")
    for row in data[:5]:
        print(row)