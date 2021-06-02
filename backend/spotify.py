import json
import random
import urllib
from google.appengine.api import urlfetch

def get_bulk_data():
    try:
        with open('genres.json') as genres:
            data = json.load(genres)
        return data
    except Exception as e:
        print(e)
        return False
    

def get_random_artist(genre):
    try:
        data = get_bulk_data()
        random_index = random.randint(0, len(data[genre])-1)
        return data[genre][random_index]
    except Exception as e:
        print(e)
        return False  

def create_access_token():
    try:
        r = urlfetch.fetch(
            url='https://accounts.spotify.com/api/token', 
            headers={'Authorization': 'Basic OGY2OGNjMTBlOWQwNGNhMmIxNjg3MzA4Y2E2NDE1NGM6NTBhMTU5NjE3OWM2NDI5Y2E0ZmI4YzZkNWRjZTRlY2Q='},
            method='POST',
            payload = urllib.urlencode({'grant_type': 'client_credentials'})
        )

        res = json.loads(r.content)

        return res['access_token']
    except Exception as e:
        print(e)
        return False

def get_artist_id(access_token, artist):
    try:
        r = urlfetch.fetch(
            url='https://api.spotify.com/v1/search?type=artist&q={artist}'.format(artist=artist),
            headers={'Authorization': 'Bearer {access_token}'.format(access_token = access_token)},
            method='GET'
        )

        res = json.loads(r.content)
        
        return res['artists']['items'][0]['id']
    except Exception as e:
        print(e)
        return False

def get_top_tracks_by_artist_id(access_token, artist_id):
    try:
        r = urlfetch.fetch(
            url = 'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US'.format(artist_id = artist_id),
            headers={'Authorization': 'Bearer {access_token}'.format(access_token = access_token)},
            method='GET'
        )

        res = json.loads(r.content)
        
        return res['tracks']
    except Exception as e:
        print(e)
        return False