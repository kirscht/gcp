class WeatherbyCity(webapp2.RequestHandler):
    def get(self, city):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write('Weather by "%s"...' % (urllib.unquote_plus(city)))