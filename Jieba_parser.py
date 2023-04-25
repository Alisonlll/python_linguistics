# Time: 2021/11/20 
# Author: HJL
# File: Jieba_parser.py
# IDE: PyCharm
import jieba
import os
import jieba.analyse


def main():
    # jieba.load_userdict("Internet words dict.txt")  # import personal dictionary
    path = r"C:\Users\xxx\Desktop\w2"  # folder path
    sw_file = "No_stopwords.txt"  # personalize stopwords list
    jieba.add_word('加词1')
    jieba.add_word('加词2')

    sw_list = get_stopwords(sw_file)
    parser(path, sw_list)


def get_stopwords(file):
    stopwords = [line.strip() for line in open(file, "r", encoding="utf-8").readlines()]
    return stopwords


def parser(path, stopwords):
    # parsed_files = []
    files = os.listdir(path)  # get a list of file names in the folder
    for file in files:  # loop files in the file list
        position = path + '\\' + file  # absolute path
        print(position)
        with open(position, "r", encoding="utf-8") as file1:  # open the file in list[0]
            with open(position.replace('.txt', '_') + "parsed.txt", "w", encoding="utf-8") as parsed:  # new file
                for line in file1:  # loop lines in file1
                    line = line.strip()  # delete spaces
                    for p in jieba.lcut(line):  # loop every word after cut line[0]
                        if p not in stopwords:
                            parsed.write(p + "  ")  # write strings of line[0] and each add double spaces
                    parsed.write("\n")  # after finish line[0], write a \n
            print("saved")
    # return parsed_files


if __name__ == "__main__":  # execute in this file
    main()  # invoke the function


'''jieba.del_word('我的')  # separate "我的"
jieba.add_word('小心地滑')  # do not separate "小心地滑"
jieba.suggest_freq(('小心', '地滑'), True)  # 调整某个词语的词频，使得其在设置的词频高是能分出，词频低时不能分出'''
