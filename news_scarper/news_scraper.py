

import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

# Step 2: Send request
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines (BBC uses <h2> for many headlines)
headlines = []
for h in soup.find_all("h2"):
    text = h.get_text(strip=True)
    if text and text not in headlines:  # avoid duplicates
        headlines.append(text)

# Step 5: Save to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for idx, headline in enumerate(headlines, start=1):
        f.write(f"{idx}. {headline}\n")

print(f"✅ {len(headlines)} headlines saved to headlines.txt")
