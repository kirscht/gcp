class WeatherInfo(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("Weather Info...")