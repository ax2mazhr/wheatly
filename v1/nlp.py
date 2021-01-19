import nltk

stop_words = set(nltk.corpus.stopwords.words("english"))
example = "wake me up at 5 pm"
token = nltk.word_tokenize(example)
stop = [w for w in token if not w in stop_words]
print(stop)
