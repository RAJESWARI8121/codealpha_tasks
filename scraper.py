import csv, requests
from bs4 import BeautifulSoup
url="https://quotes.toscrape.com/"
response=requests.get(url,timeout=20); response.raise_for_status()
soup=BeautifulSoup(response.text,"html.parser")
rows=[]
for box in soup.select(".quote"):
    q,a=box.select_one(".text"),box.select_one(".author")
    tags=[t.get_text(strip=True) for t in box.select(".tag")]
    if q and a: rows.append({"quote":q.get_text(strip=True),"author":a.get_text(strip=True),"tags":", ".join(tags)})
with open("quotes.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=["quote","author","tags"]);writer.writeheader();writer.writerows(rows)
print(f"Saved {len(rows)} quotes to quotes.csv")
