import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
text = ["This", "is", "a", "sample","sentence"]
res = [word for word in text if word.lower() not in stop_words]
print(res)