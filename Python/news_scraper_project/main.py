import requests
from bs4 import BeautifulSoup
import csv

# BBC News URL
URL = "https://www.bbc.com/news"

# Send a request to the website
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract headlines using a more reliable approach
news_list = []
for article in soup.select("a[href^='/news']"):  # Select only /news links
    title = article.get_text(strip=True)
    link = "https://www.bbc.com" + article['href']

    if title and link:
        news_list.append((title, link))

# Check if any data was extracted
if not news_list:
    print("No news headlines found. The website structure may have changed.")
    exit()

# Save to a CSV file
with open("news_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "URL"])
    writer.writerows(news_list)

# Display the results
print("\nLatest News Headlines:")
for idx, (title, link) in enumerate(news_list[:10], start=1):
    print(f"{idx}. {title} - {link}")

print("\n✅ Headlines saved")
