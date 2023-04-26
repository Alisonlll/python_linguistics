# File Name: Jieba_postag.py
# Date: 2022/4/4 0:49
# Author: HJL
# IDE: PyCharm
import jieba.posseg as pseg
import re
import codecs
# pseg.cut("text string")  return a dic

path = r"C:\Users\Alison\Desktop\test.txt"

text = codecs.open(path, "r", "utf-8")
with open(path + " tagged.txt", "w", encoding="utf-8") as tagged:
    for line in text:
        line = line.strip()
        comp = re.compile('[^A-Za-z0-9\u4e00-\u9fa5]')  # delete punctuations & emoji
        line = comp.sub('', line)
        # print(pseg.lcut(line))
        for word, flag in pseg.lcut(line):  # return list
            print(f'{word} {flag}')
            tagged.write(word + "  " + flag)  # format: apple  n
        tagged.write("\n")


# comp = re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5]')
# comp.sub('', text)
