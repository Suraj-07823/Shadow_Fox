# Web Scraping with BeautifulSoup

import requests
from bs4 import BeautifulSoup

# Step 1: Target website URL
url = "https://quotes.toscrape.com/"  # You can replace this with another blog/news site

# Step 2: Send HTTP request
response = requests.get(url)

# Step 3: Check if successful
if response.status_code == 200:
    print("Website loaded successfully!\n")

    # Step 4: Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 5: Extract data (quotes and authors)
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    print("📌 Quotes from the website:\n")
    for i in range(len(quotes)):
        print(f"{i+1}. {quotes[i].text} - {authors[i].text}")

else:
    print("Failed to retrieve the website. Status code:", response.status_code)
