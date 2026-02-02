import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
word = "pizzas"
lemmatiz = WordNetLemmatizer()
res = lemmatiz.lemmatize(word)
print(res)
