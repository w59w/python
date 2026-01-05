import requests
from bs4 import BeautifulSoup

url = "https://www.sulpak.kg/f/smartfoniy"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="product__item")

result = []

for product in products:

    name_tag = product.find("h3", class_="product__title")
    name = name_tag.get_text(strip=True) if name_tag else "Нет названия"

    price_tag = product.find("div", class_="product__price")
    price = price_tag.get_text(strip=True) if price_tag else "Цена не указана"

    description = "Описание отсутствует"

    item = {
        "Название": name,
        "Цена": price,
        "Описание": description
    }

    result.append(item)

print("Найдено товаров:", len(result))
for r in result[:5]:
    print(r)
