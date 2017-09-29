import webapp2
import urllib

import urllib2
import json

class WeatherbyCity(webapp2.RequestHandler):

    def get(self, city):
        self.response.headers["Content-Type"] = "text/plain"
        #self.response.write('Weather by "%s"...\n\n%s\n' % (urllib.unquote_plus(city), YahooWeather.get(city=city)))
        data = YahooWeather.get(city=city)
        self.response.write('Weather by "%s"...\n\n%s\n' % (urllib.unquote_plus(city), \
                                                        json.dumps(data['channel']['item']['forecast'], \
                                                        indent=4, sort_keys=True)))

class WeatherInfo(webapp2.RequestHandler):
    def get(self):
        info = """
        Weather Info by City

             Utility to restory forecast/past week(s) weather info for a city.
             
             
             Usage:
             ======
                 http://<url-to-tool>/<city>%2C%20<two-letter-abbrev-state>
             
             
             Example Weather Info for Anaheim, CA
             ====================================
             curl http://<url-to-tool>/Anaheim%2C%20CA
             
        """
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("Weather Info...\n%s" % info)

class YahooWeather():

    @staticmethod
    def get(**kwargs):
        baseurl = "http://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"%s\")" \
                        % (kwargs['city'])
        yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
        result = urllib2.urlopen(yql_url).read()
        data = json.loads(result)
        return data['query']['results']

app = webapp2.WSGIApplication([
    ("/", WeatherInfo),
    ("/(.*)", WeatherbyCity),
], debug=True)