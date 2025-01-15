import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("my_database.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a artist table (if it doesn't already exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS artists (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

# Retrieve and print the ids of all artists
cursor.execute("SELECT id FROM artists")
artists_id_rows = cursor.fetchall()

database_id_set = {t[0] for t in artists_id_rows}

print(len(database_id_set),database_id_set)

artist_id_from_file = set()
artist_dict = {}
with open("artists.csv", "r") as my_file:
    for file_line in my_file:
        artist_id_str = file_line.split(",")[0]
        if(artist_id_str.isnumeric()):
            artist_id = int(artist_id_str)
            artist_id_from_file.add(artist_id)
            artist_dict[artist_id] = file_line.split(",")[1]

print(len(artist_id_from_file), len(artist_dict))

# Find Unique Elements from Both Lists
unique_elements = database_id_set ^ artist_id_from_file  
unique_elements_of_artist_id_from_file = unique_elements & artist_id_from_file

print(len(unique_elements_of_artist_id_from_file))


for id in unique_elements_of_artist_id_from_file:
    print((id,artist_dict[id]))
    cursor.execute("INSERT INTO artists (id, name) VALUES (?, ?)", (id, artist_dict[id]))

# Commit the changes
conn.commit()

# Close the connection
conn.close()