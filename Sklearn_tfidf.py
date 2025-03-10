# File Name: Sklearn_tfidf.py
# Date: 2022/4/6
# Author: HJL
# IDE: PyCharm
import codecs
import re
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

comp = re.compile('[^A-Z^a-z^0-9^ ]')

file = r'C:\Users\xxx\Desktop\Brown.txt'
text = codecs.open(file, "r", "utf-8")

data = []

for line in text:
    data.append(line)
# print(data)
print(len(data))

# 词袋化
vec = CountVectorizer()
X = vec.fit_transform(data)
print(vec.get_feature_names_out())
print(X)

# TF-IDF
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
print(tfidf)
