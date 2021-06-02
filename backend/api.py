import webapp2
import urllib
import json
import spotify

class GenresOfMusic(webapp2.RequestHandler):
    def post(self):
        try:
            data = spotify.get_bulk_data()
            
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return self.response.out.write(json.dumps(data))
        except Exception as e:
            print(e)
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return self.response.out.write('{"success":false}')

class TopTracksByArtist(webapp2.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            access_token = spotify.create_access_token()
            artist = spotify.get_random_artist(data['genre'])
            artist_id = spotify.get_artist_id(access_token, urllib.quote_plus(artist))
            tracks = spotify.get_top_tracks_by_artist_id(access_token, artist_id)
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return self.response.out.write(json.dumps(tracks))
        except Exception as e:
            print(e)
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return self.response.out.write('{"success":false}')

app = webapp2.WSGIApplication([
    ('/api/genres-of-music', GenresOfMusic),
    ('/api/top-tracks-by-artist', TopTracksByArtist) 
], debug=True)