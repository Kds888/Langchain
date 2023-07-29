# import os 
# import tweepy
# import logging
# import datetime

# logger = logging.getLogger('twitter')

# # auth = tweepy.OAuthHandler(
# #     os.environ.get('TWITTER_API_KEY'), os.environ.get('TWITTER_API_KEY_SECRET')
# # )

# # auth.set_access_token(
# #     os.environ.get('TWITTER_ACCESS_TOKEN'),os.environ.get('TWITTER_ACCESS_SECRET')
# # )

# # api = tweepy.API(auth) this autherntication is for v1.1 but we donot have access to that but only to v2, therefore we need to use tweepy.client 

# twitter_client= tweepy.Client(

#     bearer_token=os.environ['TWITTER_BEARER_TOKEN'],
#     consumer_key=os.environ['TWITTER_API_KEY'],
#     consumer_secret=os.environ['TWITTER_API_KEY_SECRET'],
#     access_token=os.environ['TWITTER_ACCESS_TOKEN'],
#     access_token_secret=os.environ['TWITTER_ACCESS_SECRET'] 
# )

# def scrape_user_tweets(username='elonmusk',num_tweets=5):
#     # This will be a dictionery and we will have 3 fields in it namely time_posted,text and url
#     user_id = twitter_client.get_user(username=username).date.id
#     tweets = twitter_client.get_users_tweets(id=user_id,max_results=num_tweets,exclude=['retweets','replies'])
#     tweet_list=[]
#     for tweet in tweets.data:
#         tweet_dict={}
#         tweet_dict['text']=tweet['text']
#         tweet_dict['url']=f"https://twitter.com/{username}/status{tweet.id}" 
#         tweet_list.append(tweet_dict)

#     return tweet_list 

# scrape_user_tweets()

# Whatever I do the twitter api won't work for some of the countries listed no matter what 
############################## SO I AM MAKING USE OF RAPID API #####################################################
# import requests
# def scrape_tweets(num_counts,username):
#     url = "https://twitter135.p.rapidapi.com/v2/UserByScreenName/"
#     querystring = {"username":f"{username}"}
#     headers = {
#         "X-RapidAPI-Key": "YOUR API KEY HERE",
#         "X-RapidAPI-Host": "twitter135.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers, params=querystring)
#     user_id=response.json()['data']['user']['result']['rest_id']
#     url = "https://twitter135.p.rapidapi.com/v2/UserTweets/"
#     querystring = {"id":f"{user_id}","count":f"{num_counts}"}
#     headers = {
#         "X-RapidAPI-Key": "YOUR API KEY HERE",
#         "X-RapidAPI-Host": "twitter135.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers, params=querystring)

#     print(response.json()), for the time bieng I am leaving this as I have to do a lot of research as to how to get the full text based of teh 
# num text given and Currently I am moving formward.

