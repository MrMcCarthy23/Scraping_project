# Mark McCarthy
################################################################
# This program scrapes the Google Play Store to gather genre
# popularity and media type data to calculate the best option for
# investment.
################################################################
# To do: develop methodology to run this entire program as a 
# function.

import requests
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
# _______________________________________________________________________

# open google play site to top rated free books
with urlopen('https://play.google.com/store/books/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfZnJlZRAHGAE%3D:S'
             ':ANO1ljKG7Lo&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19mcmVlEAcYAQ%3D%3D:S:ANO1ljLtUdw') as main_books:

    # create beautiful soup obj
    soup_top_books = BeautifulSoup(main_books, 'lxml')
# _______________________________________________________________________



# go to each individual book page to retrieve its genres

# init a list to store the genres of each book
book_genres = []

# loop through the soup obj to find each book division
for data in soup_top_books.find_all('div', class_='ImZGtf mpg5gc'):

    # find the sub-div containing the link to the book page and convert to str
    book_link_raw = data.find('a', class_='poRVub')
    book_link_raw = str(book_link_raw)

    # slice str to beginning of path
    book_link_raw = book_link_raw[43:]

    # slice str at end of url
    index = book_link_raw.find('"')

    # concatenate protocol and resource name
    book_link = 'https://play.google.com' + book_link_raw[:index]

    # open constructed book page link
    with urlopen(book_link) as sub_page:

        # init new Beautiful soup obj
        soup_book = BeautifulSoup(sub_page, 'lxml')

    # !!!!hard coded counter to deal with indistinguishable divs
    # There are sections at the bottom of each book page with
    # information such as publisher, ISBN, genre, etc.
    # Need to find differentiating attr. to avoid hard coding here!!!!
    count = 0

    # loop through all the info spans at bottom of page
    for genre in soup_book.find_all('span', class_='htlgb'):

        # increment counter to appropriate div
        # there are a few books this section is off for
        # but the majority of them work fine (this is refered
        # to int the hard code comment above)
        count += 1

        # if count has reached the correct div, add the genre to the list
        if count == 8:
            book_genres.append(genre.text)
# _______________________________________________________________________



# loop through reference list and split the formatted strings
temp = []
for i in range(len(book_genres)):
    temp.append(book_genres[i].split('/'))

# loop through the temp list to separate the genres into individual str
result = []
for i in range(len(temp)):
    for j in range(len(temp[i])):
        result.append(temp[i][j])

# use dict to count the occurrences of each genre
count_dict = {}
for genre in result:
    if genre in count_dict:
        count_dict[genre] += 1
    else:
        count_dict[genre] = 1

print(count_dict)
################################################################

with urlopen('https://play.google.com/store/music/collection/cluster?clp=0g4dChsKFXRvcHNlbGxpbmdfcGFpZF90cmFjaxAHGAI%3D:S'
             ':ANO1ljLoK88&gsr=CiDSDh0KGwoVdG9wc2VsbGluZ19wYWlkX3RyYWNrEAcYAg%3D%3D:S:ANO1ljIhfqg') as main_songs:
    soup_top_songs = BeautifulSoup(main_songs,'lxml')

#################################################################
# The songs section only accounts for the top 50 songs
#################################################################

# go to each individual song page to retrieve its genres

# init a list to store the genres of each song
song_genres = []

# loop through the soup obj to find each song division
for data in soup_top_songs.find_all('div', class_='ImZGtf mpg5gc'):

    # find the sub-div containing the link to the song page and convert to str
    song_link_raw = data.find('a', class_='poRVub')
    song_link_raw = str(song_link_raw)

    # slice str to beginning of path
    song_link_raw = song_link_raw[43:]

    # slice str at end of url
    index = song_link_raw.find('"')

    # concatenate protocol and resource name
    song_link = 'https://play.google.com' + song_link_raw[:index]
    # open constructed song page link
    with urlopen(song_link) as sub_page_song:

        # init new Beautiful soup obj
        soup_song = BeautifulSoup(sub_page_song, 'lxml')

    # !!!!hard coded counter to deal with indistinguishable divs.
    # There are sections at the bottom of each song page with
    # information such as track, length, genre, etc.
    # Need to find differentiating attr. to avoid hard coding here!!!!
    count_song = 0

    # loop through all the info spans at bottom of page
    for genre in soup_song.find_all('span', class_='htlgb'):

        # increment counter to appropriate div
        count_song += 1

        # if count has reached the correct div, add the genre to the list
        if count_song == 1:
            song_genres.append(genre.text)
# _______________________________________________________________________


# loop through reference list and split the formatted strings
temp_song = []
for i in range(len(song_genres)):
    temp_song.append(song_genres[i].split('/'))

# loop through the temp list to separate the genres into individual str
result_song = []
for i in range(len(temp_song)):
    for j in range(len(temp_song[i])):
        result_song.append(temp_song[i][j])

# use dict to count the occurrences of each genre
count_dict_song = {}
for genre_song in result_song:
    if genre_song in count_dict_song:
        count_dict_song[genre_song] += 1
    else:
        count_dict_song[genre_song] = 1

print(count_dict_song)
################################################################

with urlopen(
        'https://play.google.com/store/apps/collection/cluster?clp'
        '=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:'
        'S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU') as main_apps:
    soup_top_apps = BeautifulSoup(main_apps, 'lxml')

#################################################################
# The apps section only accounts for the top 49 apps
#################################################################

# go to each individual app page to retrieve its genres

# init a list to store the genres of each app
app_genres = []

# loop through the soup obj to find each app division
for data in soup_top_apps.find_all('div', class_='ImZGtf mpg5gc'):

    # find the sub-div containing the link to the app page and convert to str
    app_link_raw = data.find('a', class_='poRVub')
    app_link_raw = str(app_link_raw)

    # slice str to beginning of path
    app_link_raw = app_link_raw[43:]

    # slice str at end of url
    index = app_link_raw.find('"')

    # concatenate protocol and resource name
    app_link = 'https://play.google.com' + app_link_raw[:index]

    # open constructed app page link
    with urlopen(app_link) as sub_page_app:

        # init new Beautiful soup obj
        soup_app = BeautifulSoup(sub_page_app, 'lxml')

    # counter for the two spans at the top of the page
    counter_app = 0
    # loop through all the genre links at top of page
    for genre in soup_app.find_all('a', class_='hrTbp R8zArc'):
        if counter_app == 1:
            app_genres.append(genre.text)
        counter_app += 1
# _______________________________________________________________________


# loop through reference list and split the formatted strings
temp_app = []
for i in range(len(app_genres)):
    temp_app.append(app_genres[i].split('/'))

# loop through the temp list to separate the genres into individual str
result_app = []
for i in range(len(temp_app)):
    for j in range(len(temp_app[i])):
        result_app.append(temp_app[i][j])

# use dict to count the occurrences of each genre
count_dict_app = {}
for genre_app in result_app:
    if genre_app in count_dict_app:
        count_dict_app[genre_app] += 1
    else:
        count_dict_app[genre_app] = 1

print(count_dict_app)
################################################################
