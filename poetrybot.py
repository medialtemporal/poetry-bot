import tweepy
import random
import os

consumer_key = os.environ.get('API_KEY')
consumer_secret = os.environ.get('API_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('SECRET_ACCESS_TOKEN')

file_choices = [
    # Matthew Arnold
    'doverbeach.txt',
    # Octavio Paz
    'mutra.txt',
    # Seamus Heaney
    'postscript.txt',
    # Edna St. Vincent Millay
    'recuerdo.txt',
    'songofasecondapril.txt',
    # Allen Ginsberg
    'supermarket.txt',
    # Alfred, Lord Tennyson
    'ulysses.txt',
    # T.S. Eliot
    'wasteland.txt',
    'thedrysalvages.txt',
    'prufrock.txt',
    # E.E. Cummings
    'icarryyourheartwithme.txt',
    'whatifamuchofawhichofawind.txt',
    'youarelikethesnowonly.txt',
    'sincefeelingisfirst.txt',
    'somewhereihavenevertravelled.txt',
    'iflearneddarkness.txt',
    # William Wordsworth
    'iwanderedlonelyasacloud.txt',
    # Agha Shahid Ali
    'snowonthedesert.txt',
    # Vita Sackville-West
    'theland.txt',
    # Gerard de Nerval
    'eldesdichado.txt',
    # Margaret Atwood
    'nothing.txt',
    # Louise Glück
    'afternoonsandearlyevenings.txt',
    # Rabindranath Tagore
    '1996.txt',
    # Anahita Shukla
    'cityofcream.txt',
    # Lucille Clifton
    'blessingtheboats.txt'
]

poem_choice = "./poems/" + random.choice(file_choices)


def main(file):
    api = get_authorization()
    string = get_string(file)
    title = get_title(file)
    author = get_author(file)
    new_tweet = f'{string}\n\n— from "{title}", by {author}.'
    print(new_tweet)
    api.update_status(new_tweet)


def get_authorization():
    authorization = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authorization.set_access_token(access_token, access_token_secret)
    api = tweepy.API(authorization)
    return api


def get_string(file):
    string_choice = False
    reader = open(file, 'r', encoding='utf-8')
    line_count = -2
    for i in reader:
        line_count += 1
    reader.close()
    while not string_choice:
        line_choice = random.choice(range(line_count - 2))
        reader = open(file, 'r', encoding='utf-8')
        next(reader, None)
        next(reader, None)
        line = 3
        for i in reader:
            if line == line_choice:
                if len(i.strip()) > 20:
                    return i.strip()
            line += 1
        reader.close()


def get_title(file):
    title = ""
    reader = open(file, 'r', encoding='utf-8')
    for i in reader:
        title = i.strip()
        break
    reader.close()
    return title


def get_author(file):
    author = ""
    reader = open(file, 'r', encoding='utf-8')
    next(reader, None)
    for i in reader:
        author = i.strip()
        break
    reader.close()
    return author


main(poem_choice)

