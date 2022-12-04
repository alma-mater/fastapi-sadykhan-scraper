import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    BASE_URL = "https://sadykhan.kz"
    URL = f"{BASE_URL}/malysh-i-mama/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    products = soup.find_all("div", class_="product-item")

    yo = []
    for p in products:
        image = p.find('img')
        src = f'{BASE_URL}{image["src"]}'
        title = p.find("span", class_="content-title")
        price = p.find('span', class_="price")
        res = {"image": src, "title": title.text, "price": price.text}
        yo.append(res)

    return yo
