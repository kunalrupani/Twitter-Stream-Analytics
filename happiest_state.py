import sys
import json
import unicodedata

# Global Data
sentDict = {}
tags = {}
sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])
statesent = {}

def hw():
    print '***************'

def lines(fp):
    print str(len(fp.readlines()))

def analyzeTweet(tweetText,statename):
	words = tweetText.split()
	sentiment = 0
	for word in words:
		if word.lower() in sentDict.keys():
			sentiment += float(sentDict[word.lower()])
	sentstr = "Tweet # " + tweetText + " Sentiment# " + str(sentiment) + "\n"
	
	if statename in statesent.keys():
			statesent[statename].append(sentiment)
	else:
		statesent[statename]=[sentiment]
	
def extractState(statestring):
	locationlist = statestring.split(', ')
	return str(locationlist[1])



def tweetstr():
    # Extract twitter post from feed data and analyze each tweet via analyzeTweet
    lines = tweet_file.readlines()
    for i in range(len(lines)):
    	tags = json.loads(lines[i])
    	if 'user' in tags.keys():
    		if 'lang' in tags['user'].keys():
    			if (tags['user']['lang'] == "en"): #and (tags['user']['geo_enabled'] == "true"))
    				if 'place' in tags.keys():
    					if isinstance(tags['place'], dict):
    						if (tags['place']['country_code'] == "US"):
    							state= extractState(tags['place']['full_name'])
    							#print state
    							if 'text' in tags.keys():
    								tweetText = tags['text'].encode('utf-8')
    								#print tweetText
    								analyzeTweet(tweetText,state)
    						
		
def main():
	hw()
	
	# Read sentiment file and add to dictionary
	lines = sent_file.readlines()
	for i in range(len(lines)):
		(key,val) = lines[i].split('\t')
		sentDict[key] = val
		

	tweetstr()

	usstatesent = {}
	for k in statesent:
		statesentiment=0
		i=0
		for i in range(len(statesent[k])):
			statesentiment += statesent[k][i]
		usstatesent[k] = str(statesentiment/len(statesent[k]))

	res = list(sorted(usstatesent, key=usstatesent.__getitem__, reverse=True))
	#print type(res), res
	print " ******* US States from most to least happy *******"
	for i in range(len(usstatesent)):
		if (len(res[i]) == 2):
			print "State " + res[i] + " has a sentiment of " + str(usstatesent[res[i]])
	print " ******* US States from most to least happy *******"

	# Close all files
	sent_file.close()
	tweet_file.close()

if __name__ == '__main__':
	main()
