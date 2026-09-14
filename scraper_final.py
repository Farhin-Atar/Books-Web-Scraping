import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

data = []

base_url = "https://books.toscrape.com/"

# Scrape 50 pages
for page in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    print("Scraping Page:", page)
    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # Book Name
        name = book.find("h3").find("a")["title"]

        # Price
        price = book.find("p", class_="price_color").text.strip()
        price = price.replace("Â£", "£")

        # Rating
        rating = book.find("p", class_="star-rating")["class"][1]

        # Availability
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        # Product URL
        product_link = book.find("h3").find("a")["href"]
        product_url = urljoin(base_url, "catalogue/" + product_link)

        # Open product detail page
        product_response = requests.get(product_url)

        product_soup = BeautifulSoup(
            product_response.text, "html.parser"
        )

        # Category
        breadcrumb = product_soup.find("ul", class_="breadcrumb")

        category = "Unknown"

        if breadcrumb:
            links = breadcrumb.find_all("a")

            if len(links) >= 3:
                category = links[2].text.strip()

        # Store data
        data.append({
            "Book Name": name,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Category": category,
            "Product URL": product_url
        })

    # Small delay between pages
    time.sleep(1)


# Convert to DataFrame
df = pd.DataFrame(data)

print("\nTotal Books Scraped:", len(df))

# Save data to Excel
with pd.ExcelWriter(
    "final_books_data.xlsx",
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        index=False,
        sheet_name="Books"
    )

    worksheet = writer.sheets["Books"]

    # Find Product URL column
    url_column = df.columns.get_loc("Product URL") + 1

    # Make Product URLs clickable
    for row in range(2, len(df) + 2):

        cell = worksheet.cell(
            row=row,
            column=url_column
        )

        cell.hyperlink = cell.value
        cell.style = "Hyperlink"


print("Final dataset successfully saved to Excel!")