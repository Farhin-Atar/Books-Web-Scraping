import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    name = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text.strip()
    price = price.replace("Â£", "£")
    rating = book.find("p", class_="star-rating")["class"][1]

    data.append({
        "Book Name": name,
        "Price": price,
        "Rating": rating
    })

df = pd.DataFrame(data)

print(df)

df.to_excel("books_data.xlsx", index=False)

print("Data successfully saved to Excel!")