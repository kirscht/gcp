# Weather Info by City #

 Utility to display forecast/past week(s) weather info for a city.
                          
 ## Usage: ##

    https://weather-181405.appspot.com/<city>%2C%20<two-letter-abbrev-state>
             
             
   
## Example Weather Info for Anaheim, CA ##
             
      curl https://weather-181405.appspot.com/Anaheim%2C%20CA
      
# Approach #

* My preferred choice was "Google Cloud Functions," but the service is still in Beta and only supports node.js currently.  Node.js is not something that I've done a lot of programming in.
* Python running under Google App Engine was the next logical choice.  It's not as compact and efficient as "Functions," but is the next best tool.
* The Flask library would have been a great choice for route handling, but since I have never used Flask under Google Apps, so I chose to use the supported "webapp2" library.

* About 3-hours were spent on this task.  Most of that time was trying to work around the buggy version of URLLIB2 in the App Engine.  I did find workarounds and got it working.
* I spent a couple of hours trying to find a FREE data source that provides historical data, but the FREE services of the past are either gone or now charging.




 