# Weather Info by City #

 Utility to display forecast/past week(s) weather info for a city.
                          
 ## Usage: ##

    https://weather-181405.appspot.com/<city>%2C%20<two-letter-abbrev-state>
             
             
   
## Example Weather Info for Anaheim, CA ##
             
      curl https://weather-181405.appspot.com/Anaheim%2C%20CA
      
# Approach #

My preferred choice was "Google Cloud Functions," but the service is still in Beta and only supports node.js currently.  Node.js is not something that I've done a lot of programming in.
 