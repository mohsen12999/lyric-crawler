import requests
from bs4 import BeautifulSoup

# print(soup.prettify())
def get_lyric_from_website(lyric_url):
    r = requests.get(lyric_url)
    soup = BeautifulSoup(r.content, 'lxml')

    lyric_div = soup.find('div',class_="lBody")

    lyric_info = lyric_url.split("/")[-1]
    dash_index = lyric_info.find("-")
    lyric_id = lyric_info[:dash_index]
    lyric_name = lyric_info[dash_index+1:]    

    return (lyric_id,lyric_name, str(lyric_div))


sample_lyric_url = "http://lyrics.lol/artist/835-michael-jackson/lyrics/4043200-beat-it"
print(get_lyric_from_website(sample_lyric_url))