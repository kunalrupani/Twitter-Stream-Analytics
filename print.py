import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
twdict =json.load(response)

for i in range(10):
    print "tweet# " + str(i) + " " + twdict['results'][i]['text'] + '\n'

