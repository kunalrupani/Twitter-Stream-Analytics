from __future__ import division
import sys
import json
import unicodedata

# Global Data

tags = {} # holds json formated tweet
freqDict = {}
tweet_file = open(sys.argv[1]) # tweet file

def hw():
    print '***************'

def lines(fp):
    print str(len(fp.readlines()))

def analyzeTweet(tweetText):
	words = tweetText.split()
	for word in words:
		if word in freqDict.keys():
			freqDict[word] += 1
		else:
			freqDict[word] = 1 

def calcFreq():
	for key in freqDict:
		print "Frequency of word: " + key + "is #" + ("%.5f" % float(freqDict[key]/len(freqDict)))
		
	
def tweetstr():
    # Extract twitter post from feed data and analyze each tweet via analyzeTweet
    lines = tweet_file.readlines()
    for i in range(len(lines)):
    	tags = json.loads(lines[i])
    	if 'user' in tags.keys():
    		if 'lang' in tags['user'].keys():
    			if (tags['user']['lang'] == "en"):
    				if 'text' in tags.keys():
    					tweetText = tags['text'].encode('utf-8')
    					analyzeTweet(tweetText)
		
def main():
    hw()
   	 
    tweetstr()
    calcFreq()
    
    # Close all files
    tweet_file.close()

if __name__ == '__main__':
    main()
