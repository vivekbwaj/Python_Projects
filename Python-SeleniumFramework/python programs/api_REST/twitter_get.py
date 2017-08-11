import oauth2
from pprint import pprint
import json

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
API_KEY="az1iGIE06Sdje5t8tQqgeJ8xL"
API_SECRET="hKKO9Lp1jicXicGmxa4NhisifzDDCub3qZcGPgGrEv2xV6ZsCM"
ACCESS_TOKEN="496956674-hU8wTZXnp5iPRWCJJl0jlfOQg2p9EZ9nkD0nPv5E"
ACCESS_TOKEN_SECRET="Ka4Mv66RAZDbEtZqRffJaOyqxfPkxZXhLSdXpCpP1hCfq"

consumer=oauth2.Consumer(key=API_KEY,secret=API_SECRET)
access_token=oauth2.Token(key=ACCESS_TOKEN,secret=ACCESS_TOKEN_SECRET)
client=oauth2.Client(consumer,access_token)

resp,res=client.request(url)
# This will return a tuple
# resp contains the response from twitter
# res contains the tweets data

tweets=json.loads(res)
for tweet in tweets:
    print(tweet['text'])
