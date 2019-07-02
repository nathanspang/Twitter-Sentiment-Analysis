import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
from nltk.tokenize import RegexpTokenizer


with open('Dell.txt', 'r', encoding = 'utf8') as file:
	data = file.read()

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(data)

stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if not w in stop_words]

frequency_dist = nltk.FreqDist(tokens)
top_10 = sorted(frequency_dist, key=frequency_dist.__getitem__, reverse=True)[0:10]
print(top_10)


#wordcloud 
wordcloud = WordCloud().generate_from_frequencies(frequency_dist)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()




def get_tweet_sentiment(tweet):
	 analysis = TextBlob(self.clean_tweet(tweet)) 
	 if analysis.sentiment.polarity > 0: 
	 	return 'positive'
	 elif analysis.sentiment.polarity == 0: 
	 	return 'neutral'
	 else: 
	 	return 'negative'
    