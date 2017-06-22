import sys
import json
import unicodedata

# Global Data
sentDict = {}
tags = {}
sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])
#fout = open('sentiment_output.txt', 'w')

def hw():
    print '***************'

def lines(fp):
    print str(len(fp.readlines()))

def analyzeTweet(tweetText):
	words = tweetText.split()
	sentiment = 0
	for word in words:
		if word.lower() in sentDict.keys():
			sentiment += float(sentDict[word.lower()])
	sentstr = "Tweet # " + tweetText + " Sentiment# " + str(sentiment) + "\n"
	#fout.write(sentstr)
	print sentstr
	
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
    
    # Read sentiment file and add to dictionary
    lines = sent_file.readlines()
    for i in range(len(lines)):
		(key,val) = lines[i].split('\t')
		sentDict[key] = val
		
    
    tweetstr()
    
    # Close all files
    #fout.close()
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()
