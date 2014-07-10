import os
 
from twitter.api import Twitter
from twitter.oauth import OAuth, read_token_file
from twitter.oauth_dance import oauth_dance
 
# Yes, these are public secrets, published in sixohsix-twitter github repo.
CONSUMER_KEY='2MQMk11nsY11CmJ0ABv314T6S'
CONSUMER_SECRET='FRViqoPUe7aqU4QpwFszW58dciKMqSwG37MFgYUFWPe3z5pi5R'
 
# Where OAuth credentials are saved, or where to save them.
oauth_filename = os.path.expanduser('~/.twitter_oauth')
 
# Create the OAuth credentials file if it doesn't already exist.
if not os.path.exists(oauth_filename):
    # Reusing credentials from Python Twitter Tools. Consider creating your own.
    oauth_dance("the Command-Line Tool",
                CONSUMER_KEY,
                CONSUMER_SECRET,
                oauth_filename)
 
# Read the local OAuth credentials file.
oauth_token, oauth_token_secret = read_token_file(oauth_filename)
 
# Create an instance of the twitter.api.Twitter class.
twitter = Twitter(
    auth=OAuth(
        oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET),
    secure=True,
    api_version='1.1',
    domain='api.twitter.com')
 
# Congratulations, you now have an object mapped to the Twitter API.
# Now do something.
 
# Example: print most recent user status update (doesn't include "Retweets").
mute = twitter.mutes.users.list()
print map(lambda a: a['screen_name'], mute['users'])