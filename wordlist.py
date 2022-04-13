fname = input("Enter file name: ")  # filename.txt
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()  # 去空行
    i = line.split()  # 拆分成List
    # print(i)
    for w in i:
        # print(w)
        if w in lst:
            continue  # 跳过已有的词
        lst.append(w)  # 加入list
lst.sort()  # alphabetical 排序
print(lst)
