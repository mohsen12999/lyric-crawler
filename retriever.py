import os

text_files = [file_name for file_name in os.listdir(".") if file_name.startswith("sitemap") and file_name.endswith(".txt")]
text_files.sort()
last_text_file = text_files[-1]

def get_artist_data(link_url):
    link_parts = link_url.split("/")
    artist_part = link_parts[-1]
    dash_index = artist_part.find("-")
    artist_id = artist_part[:dash_index]
    artist_name = artist_part[dash_index+1:-1]

    return (artist_id, artist_name, link_url)

def get_lyric_data(link_url):
    link_parts = link_url.split("/")
    lyric_part = link_parts[-1]
    dash_index = lyric_part.find("-")
    lyric_id = lyric_part[:dash_index]
    lyric_name = lyric_part[dash_index+1:-1]

    artist_part = link_parts[-3]
    dash_index = artist_part.find("-")
    artist_id = artist_part[:dash_index]
    artist_name = artist_part[dash_index+1:]

    return (lyric_id, lyric_name, artist_id, artist_name, link_url)


artists = []
lyrics = []

with open(last_text_file, "r") as my_file:
    for file_line in my_file:
        if "/artist/" in file_line:
            if "/lyrics/" not in file_line:
                # artist
                artist_data = get_artist_data(file_line)
                artists.append(artist_data)
            else:
                # 
                lyric_data = get_lyric_data(file_line)
                lyrics.append(lyric_data)


# save artists
with open("artists.csv", "w") as my_file:
    my_file.write("id,name,link")
    for artist in artists:
        my_file.write(','.join(artist))

# save lyrics
with open("lyrics.csv", "w") as my_file:
    my_file.write("id,name,artist_id,artist_name,link")
    for artist in lyrics:
        my_file.write(','.join(artist))