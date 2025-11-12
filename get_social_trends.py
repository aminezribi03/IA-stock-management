import tweepy
import instaloader

def get_twitter_mentions(hashtag, api_key, api_secret, access_token, access_token_secret, nb=100):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=hashtag, count=nb, lang="fr")
    return len(tweets)

def get_instagram_mentions(hashtag):
    L = instaloader.Instaloader()
    posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()
    count = sum(1 for _ in posts)
    return count

def get_tiktok_mentions(hashtag):
    return 0  
