import sys
import json
import unicodedata
import re

# Global Data
tags = {} # holds json formated tweet
freqDict = {}
tweet_file = open(sys.argv[1]) # tweet file

def hw():
	print '***************'

def lines(fp):
	print str(len(fp.readlines()))

def analyzeTweet(tweetText):
	ht = re.findall(r'#\w+', tweetText)
	if len(ht)>0:
		for i in range(len(ht)):
			if ht[i] in freqDict.keys():
				freqDict[ht[i]] += 1
			else:
				freqDict[ht[i]] = 1 



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

	#for key in freqDict:
		#print "Count of " + key + " is "+ str(freqDict[key])

	res = list(sorted(freqDict, key=freqDict.__getitem__, reverse=True))
	print " ******* Top 10 Hashtags *******"
	for i in range(10):
		print "HashTag# " + res[i] + " appeared " + str(freqDict[res[i]]) + " times"
	print " ******* Top 10 Hashtags *******"

	# Close all files
	tweet_file.close()

if __name__ == '__main__':
	main()
