import sys
import json
import unicodedata

# Global Data
sentDict = {}
tags = {}
sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])
termsent = {}

def hw():
	print '***************'

def lines(fp):
	print str(len(fp.readlines()))

def analyzeTweet(tweetText):
	words = tweetText.split()
	sentiment = 0
	termlist = []
	for word in words:
		if word.lower() in sentDict.keys():
			sentiment += float(sentDict[word.lower()])
		else:
			termlist.append(word.lower())
			
	for term in termlist:
		if term in termsent.keys():
			termsent[term].append(sentiment)
		else:
			termsent[term]=[sentiment]
			
	#sentstr = "Tweet # " + tweetText + " Sentiment# " + str(sentiment) + "\n"
	
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
#Read sentiment file and add to dictionary
	lines = sent_file.readlines()
	for i in range(len(lines)):
		(key,val) = lines[i].split('\t')
		sentDict[key] = val
	tweetstr()
	for k in termsent:
		newwordsent=0
		i=0
		for i in range(len(termsent[k])):
			newwordsent += termsent[k][i]
		print k + "\t" + str(newwordsent/len(termsent[k]))

# Close all files
	sent_file.close()
	tweet_file.close()

if __name__ == '__main__':
    main()
