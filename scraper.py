# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_laptops():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data, status code: {response.status_code}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.content, "html.parser")
    # ⬇️ More reliable container selector
    products = soup.select("div.thumbnail")

    if not products:
        print("❌ No products found on the page.")
        return pd.DataFrame()

    titles, prices, descriptions = [], [], []

    for product in products:
        title_tag = product.select_one("a.title")
        price_tag = product.select_one("h4.price")
        description_tag = product.select_one("p.description")

        title = title_tag.text.strip() if title_tag else "N/A"
        price = price_tag.text.strip().replace("$", "") if price_tag else "0"
        description = description_tag.text.strip() if description_tag else "N/A"

        titles.append(title)
        prices.append(price)
        descriptions.append(description)

    df = pd.DataFrame({
        "Title": titles,
        "Price": prices,
        "Description": descriptions
    })

    df.to_csv("laptops_raw.csv", index=False)
    print("✅ Raw data saved to laptops_raw.csv")
    return df
