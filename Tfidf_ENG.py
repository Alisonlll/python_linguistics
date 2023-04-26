# File Name: Tfidf_ENG.py
# Date: 2022/4/4
# Author: HJL
# IDE: PyCharm
import re
import math
import nltk
import nltk.stem
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from collections import Counter
import os

path = r'C:\Users\xxx\Desktop\test'


s = nltk.stem.SnowballStemmer('english')   # 提取词干,语言：英语 OR 其他提取算法LancasterStemmer
# s = LancasterStemmer()
lem = WordNetLemmatizer()
comp = re.compile('[^A-Z^a-z^ ]+')  # [^A-Z^a-z^0-9^ ]


# stem counter
def stem_count(text):
    ltext = text.lower()  # lower case
    de_punctuation = comp.sub('', ltext)  # delete punctuation
    paragraph = nltk.word_tokenize(de_punctuation)  # tokenize,split words, return list
    # print(paragraph)

    de_stopwords = [w for w in paragraph if w not in stopwords.words('english')]    # delete stopwords, return list

    cleaned_text = []
    for j in range(len(de_stopwords)):
        cleaned_text.append(s.stem(de_stopwords[j]))  # loop paragraphs, stem, return list
        # cleaned_text.append(lem.lemmatize(de_stopwords[j]))  # lemmatizer
    count = Counter(cleaned_text)                 # count num of stems, return dic {'apple':3,'banana':5}
    return count  # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})


# TF-IDF calculation procedure
def doc_count(word, para_list):
    d_con = 0
    for paragraph in para_list:  # paragraph loop in all para.list 当前文本 in 总文本表
        if word in paragraph:  # if word exist in paragraph
            d_con += 1  # count += 1
    return d_con  # num of paragraph contain this word


def tf(word, count):  # term freq 词频 / 总词数
    return count[word] / sum(count.values())


def idf(word, para_list):  # 总文本数sum.doc / 1 + 包含该词的文本数doc_count
    return math.log(len(para_list)) / (1 + doc_count(word, para_list))


def tfidf(word, count, para_list):  # 当前词 词频表 总文本
    return tf(word, count) * idf(word, para_list)


texts = []
i = 0
files = os.listdir(path)  # get a list of file names in the folder
for file in files:  # loop files in the file list
    position = path + '\\' + file  # absolute path，"\\"，其中一个'\'为转义符
    # print(position)
    fhandle = open(position, "r", encoding="utf8").read()
    texts.append(fhandle)  # all files in one list
    # print(texts)


count_list = []
for line in texts:
    count_list.append(stem_count(line))
    # print(count_list)


for i in range(len(count_list)):  # loop 词干数 type
    tf_idf = {}
    print(f'For document {i+1}')
    for stem in count_list[i]:
        tf_idf[stem] = tfidf(stem, count_list[i], count_list)
    # print(tf_idf)

    sort = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)  # 字典转元组list 按照TF-IDF值从大到小排列
    for stem, tf_idf in sort[:20]:
        print(f"\tStem: {stem} : {round(tf_idf, 10)}")
        # print("\tStem: {} : {}".format(stem, round(tf_idf, 10)))
        # lem.lemmatize(stem) 需要lemmatize的情况使用

'''问题：
只能多个string放进来求值，多个文本互比, 每个文本成一个字符串，合并成list, 即texts = [text_1, text_2, text_3]，
运行可得出每个文本相对于整个库所有文本的关键词。
单文本不可求每段在整篇中的tfidf，只能得出每句话中的关键词，无意义。
参考：https://blog.csdn.net/weixin_43216017/article/details/86755145'''
