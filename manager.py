import twitter
import yaml

with open('settings.yaml', 'r') as yaml_file:
    config = yaml.load(yaml_file)

api = twitter.Api(consumer_key = config['consumer_key'],
consumer_secret= config['consumer_secret'],
access_token_key= config['access_token_key'],
access_token_secret= config['access_token_secret'])
user_info = api.VerifyCredentials()
friends = api.GetFriendIDs(user_info.screen_name)

print('modifying status for {0} relationships'.format(len(friends)))
for friend in friends:
    api.UpdateFriendship(user_id=friend, retweets=False)
print('finished')