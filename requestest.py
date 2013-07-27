import requests
from requests_oauthlib import OAuth1
import json 
import urllib2
import base64

API_BASE = 'https://api.twitter.com/1.1/'
auth_url = API_BASE + 'account/verify_credentials.json'
tweets_url = API_BASE + 'search/tweets.json'

auth = 'beckastar@gmail.com', 'arewenot13m'

r = requests.get('https://foauth.org/api.twitter.com/1.1/statuses/user_timeline.json', auth=auth)

tweets_params = {
	'q':'#hashtag',
	'count':100

}

# auth = OAuth1(
# # base_url='https://api.twitter.com/1/',
# # request_token_url = 'https://stream.twitter.com/1.1/statuses/sample.json',
# # access_token_url = "https://api.twitter.com/oauth/access_token",
# client_key = '8vT4akwvPR1sWQIbO6y8g',
# client_secret = '2YQxdvSVPerI51CoewMeIhyKsm8niwKZyuPIQAVg6s',
# #authorize_url = 'https://api.twitter.com/oauth/authorize'
# 	)


CONSUMER_KEY = b'8vT4akwvPR1sWQIbO6y8g'
CONSUMER_SECRET = b'2YQxdvSVPerI51CoewMeIhyKsm8niwKZyuPIQAVg6s'


base64_consumer_key_secret = base64.b64encode(
    urllib2.quote(CONSUMER_KEY) + b':' + urllib2.quote(CONSUMER_SECRET))


requests.get(auth_url, auth=auth)

request = urllib2.Request("https://api.twitter.com/oauth2/token")
request.add_header('Authorization', b'Basic ' + base64_consumer_key_secret)
request.add_header("Content-Type", b'application/x-www-form-urlencoded;charset=UTF-8')
request.add_data(b'grant_type=client_credentials')

resp = urllib2.urlopen(request)
data = json.load(resp)
if data['token_type'] != 'bearer':
    throw("Bad token_type: " + data['token_type'])
access_token = data['access_token']

print("access_token: " + access_token)
print('')


#
# Step 3: Authenticate API requests with the bearer token
#

request = urllib2.Request(
	"https://stream.twitter.com/1.1/statuses/sample.json"
    #    'https://api.twitter.com/1.1/statuses/user_timeline.json?count=3&screen_name=baratunde'
    )
request.add_header('Authorization', b'Bearer ' + access_token)

resp = urllib2.urlopen(request)
data = json.load(resp)

print("Result:")
print(json.dumps(data, indent=4, separators=(',', ': ')))

#requests.get('api.twitter.com/oauth/authenitcate/oauth_token=21369282-5h31qLNIH68WoJIvfoU01DK191ixS8W9g67y41QQ')

# tweets = requests.get(tweets_url, auth=auth, params=tweets_params)
# print tweets
# for status in tweets.json()['statuses']:
#     print status['text']