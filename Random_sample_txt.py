# File: Random_sample_txt.py
# Date: 2022/8/12
# Author: HJL
# IDE:  PyCharm
"""
Add serial numbers to TXT files, extract random samples from each file
Personalize sample size by %, extract 2 sample sets per run
Input three file paths (already exist)
"""
import os
import numpy as np
import time


def main():
    path1 = r"C:\Users\xxx\Desktop\test"  # original folder
    path2 = r"C:\Users\xxx\Desktop\test_num"  # numbered folder
    path3 = r"C:\Users\xxx\Desktop\sample"  # sampled folder

    start = time.time()
    files1 = os.listdir(path1)
    for file in files1:
        position = path1 + '\\' + file
        print(position)
        with open(position, "r", encoding="utf-8") as file1:
            with open(path2 + "\\" + file.replace(".txt", "_n.txt"), "w", encoding="utf-8") as output:
                add_serial_number(file1, output)
        print("succeed")

    files2 = os.listdir(path2)
    for file in files2:
        position = path2 + "\\" + file
        print(position)
        with open(position, "r", encoding="utf-8") as num_file:
            s1 = path3 + "\\" + file.replace(".txt", "_sample_a.txt")
            s2 = path3 + "\\" + file.replace(".txt", "_sample_b.txt")
            random_sample_txt(num_file, s1, s2)
        print("succeed")

    end = time.time()
    print(f"Running time: {end-start} secs")


# add serial number
def add_serial_number(file1, file2):
    lines = file1.readlines()
    n = len(lines)
    text_list = []
    for i in range(0, n):
        text_list.append(str(i+1)+"//"+lines[i])
    file2.writelines(text_list)  # writelines: write line by line (without quotation marks)
    return file2


# random sampling
def random_sample_txt(file1, file2, file3):
    lines = file1.readlines()
    lines_array = np.array(lines)

    size_a = int(0.1 * len(lines))
    size_b = int(0.3 * len(lines))
    print(f"Total: {len(lines)}")
    print(f"Sample_A size: {size_a} Sample_B size: {size_b}")

    sample_a = np.random.choice(lines_array, size=size_a, replace=False)  # 10% of total dataset
    sample_b = np.random.choice(lines_array, size=size_b, replace=False)  # replace=False, don't repeat in one set
    # print(type(sample_a))
    sample_a = sample_a.tolist()
    sample_b = sample_b.tolist()
    # print(type(sample_a))

    with open(file2, "w", encoding="utf8") as f2:
        f2.writelines(sample_a)
    with open(file3, "w", encoding="utf-8") as f3:
        f3.writelines(sample_b)


if __name__ == "__main__":
    main()
