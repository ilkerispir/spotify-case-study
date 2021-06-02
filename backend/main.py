import webapp2
import templates

class Main(webapp2.RequestHandler):
    def get(self):
        try:
            self.response.out.write(templates.render_template(self, 'index.html', {}))
        except Exception as e:
            print(e)
            self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return self.response.out.write('{"success":false}')

app = webapp2.WSGIApplication([
    ('/', Main)
], debug=True)