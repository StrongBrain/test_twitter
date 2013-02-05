# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import RequestContext
import datetime
from django.core.cache import cache
from sorteddict import *
#from django.core.context_processors import csrf

CURRENT_TWITTER_USER = 'Sugarman_Inside' 
"""
def fetch_cached_tweets(username):
    item = cache.get(username)
    if item is None:
        # Scenario 1: Cache miss - return empty result set and trigger a refresh
        update_tweets.delay(username, 60*15)
        return []
    tweets, expiry = item
    if expiry > datetime.datetime.now():
        # Scenario 2: Cached item is stale - return it but trigger a refresh
        update_tweets.delay(username, 60*15)
    return tweets

from celery import task


@task()
def update_tweets(username, ttl):
    tweets = fetch_tweets(username)
    now = datetime.datetime.now()
    cache.set(username, (tweets, now+ttl), 2592000)
"""
def main(request):
    
    context = {}
    return render_to_response('main.html',context,context_instance=RequestContext(request))

def my_tweets(request):
    
    context = {}
    return render_to_response('my_tweets.html',context,context_instance=RequestContext(request))

def find_tweets(request):
    context = {}
    try:
        print type(request.REQUEST['text'])
        context = {'find':findTweet(request.REQUEST['text'])}
        return render_to_response('find.html',context,context_instance=RequestContext(request))
        
    except:
      
        return render_to_response('find_tweets.html',context,context_instance=RequestContext(request))
    #'tweets':getTweets()},}
    #context.update(csrf(request))
   


"""
consumer_key = 'cgdzdgJXDbwt8F0joaLHuw'
consumer_secret = 'UbvoAnepF4b5bqjfdrfubskQvOBDo885gw1mAX8zvEc'
access_token_key ='160847405-7pvWPam1pHnedhgZjfON70uBe10S3C8NI1TsI2EN'
access_token_secret = 'Y8Chbe2ZwRKCPQO95RP41vv0KzcwlbKdExPygEQNd7Q'
api = twitter.api(consumer_key, consumer_secret,access_token_key,access_token_secret)
searching_tweets =api.search('#africa')
for tweet in searching_tweets:
    user = tweet.from_user
    print  user

"""
"""
def fetch_tweets():
    tweets = []
    dictionary = sorteddict()
    try:
        import twitter
        api = twitter.Api()
        latest = api.GetUserTimeline('Sugarman_Inside')
        for tweet in latest:
            status = tweet.text
            tweet_date = tweet.relative_created_at
            dictionary['status'] = status
            dictionary['date'] = tweet_date
            tweets.append(dictionary)
    except:
        tweets.append({'status':'Follow us @Sugarman_Inside','date':'about 10 minutes ago'})
    new_dict = sorteddict()
    new_dict['tweets']=tweets
    return new_dict
"""
def findTweet(keyword):
    tweets = []
    try:
        import twitter
        api = twitter.Api()
        searching_tweets = api.GetSearch(keyword)
        for tweet in searching_tweets:
            #print tweet
            text = tweet.text
            user = tweet.user
            #print 'Something else: ',tweet
            feed_date = tweet.created_at
            #print 'User attributes: ',dir(user)
            tweets.append({'user':user,'text':text,'date':feed_date})
    except:
        tweets.append({'user':'Sugarman_Inside'})
    #for tweet in tweets:
        #print 'Tweet: ', tweet['user']#dir(tweet.keys())
    return {'find':tweets }
