from tweepy import API, OAuthHandler, Cursor
import csv

CONSUMER_KEY = "CHtKwf9hcRM1qjB8QwcTMPWJv"
CONSUMER_SECRET = "pvcVYOvnyt4OvFCPnoqUihxkGvdY6qskA72EmB86RDo83HFIg7"
ACCESS_TOKEN = "998691119453089793-APlcSNqDqocnxuRX9ZSFs1swFh0rfnC"
ACCESS_TOKEN_SECRET = "71RdfxBPPH2kK8TdFoE73jMxFDZzRzWOwnRaXwJg075zu"


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = API(auth)


def get_tweet_text(company_name, num_tweets):
    tweet_text = []
    queries = [f'{company_name} -filter:retweets', f'{company_name.lower()} -filter:retweets',
               f'#{company_name} -filter:retweets', f'#{company_name.lower()} -filter:retweets']

    for tweet in Cursor(api.search, q=queries, lang='en').items(num_tweets):
        if 'RT @' not in tweet.text:
            tweet_text.append(tweet.text)
    return tweet_text


def to_csv(company_name, text_list):
    with open(f'{company_name}.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(text_list)
    print('csv file created!')


if __name__ == '__main__':
    company = input('Enter company name: ')
    number = int(input('How many tweets would you like to analyze? '))
    tweet_text_list = get_tweet_text(company, number)
    to_csv(company, tweet_text_list)

