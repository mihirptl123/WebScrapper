import requests
from bs4 import BeautifulSoup
import pandas as pd

url = input("Enter the website URL to scrape: ")
html_tag = input("Enter the HTML tag to search (e.g., span, a, div): ")
html_class = input("Enter the class name to filter by (leave blank if none): ")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

if html_class:
    elements = soup.find_all(html_tag, class_=html_class)
else:
    elements = soup.find_all(html_tag)

data = [element.get_text(strip=True) for element in elements if element.get_text(strip=True)]

# Saves the extracted data to the .csv file
df = pd.DataFrame({f"{html_tag} elements": data})
df.to_csv("scraped_output.csv", index=False)

print("✅ Scraping complete! Data saved to scraped_output.csv")
