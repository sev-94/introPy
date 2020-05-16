import tweepy
import time

# API Key,
auth = tweepy.OAuthHandler('8Ik8nqnr4dyKj6rp8xFDJ65qS', 'OKh6cMR7V97irE0vmfsmEOABp7aKbaFRfKGTOXwEtaQMbQmtex')
auth.set_access_token('1261673452236398594-ItcFCatn5JLWpKyvePXVVZcao6dOpK',
                      'u6jbiOFIJcWf8nytFk8DaZ0nY5k2K7sRSw5F7Mzo6mHyX')

api = tweepy.API(auth)
user = api.me()

print(user.name)              # Name
print(user.screen_name)       # Twitter Handle
print(user.followers_count)   # Follower Count

# Print out tweets from home timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
   print(tweet.text)

# Twitter only lets you request from the server a certain amount of times in a period
# When that limit is reached, this try/except will wait until we can request again
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

# Print out followers list, one by one
# I dont have any followers so this section of code will not execute properly
#for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#    if follower.name == 'WayneRooney':
#        follower.follow()              # Follow Back this Follower
#        break
    #print(follower.name)              # Print Follower Name


# Search tweets with the word Python
# Search for the first two tweets with this word that you can find
search_string = 'python'
numbersOfTweets = 2

#For each tweet with the word 'Python,' like the tweet
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break