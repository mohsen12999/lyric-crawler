import requests
from bs4 import BeautifulSoup
import datetime

# Read main sitemap
sitemap_url = "https://lyrics.lol/sitemap.xml"
r = requests.get(sitemap_url)
soup = BeautifulSoup(r.content, 'lxml')

# Find all sub sitemap from main sitemap
sub_sitemap=[]
for row in soup.findAll('loc'):
    sub_sitemap.append(row.text)

# A function for open a sub sitemap, read all link, and append it to file 
def read_sub_sitemap(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    
    sitemap_links=[]
    for row in soup.findAll('loc'):
        sitemap_links.append(row.text)
    
    return sitemap_links


# Start iterate over all sub sitemap and retrieved all links
print(f"total sitemap links: {len(sub_sitemap)}")
output_file = f"sitemap_links_{str(datetime.date.today())}.txt"

for sub in sub_sitemap:
    print(sub)
    links = read_sub_sitemap(sub)
    print(len(links))
    with open(output_file ,'a') as my_file:
        my_file.write("\n".join(links))
