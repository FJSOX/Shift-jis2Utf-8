#!/usr/bin/python
# coding=utf-8
# by Fjsox 2020/11/13
# 本脚本用于将目录1（path1）下的txt文件从shift-jis转码成utf-8格式
import os

path1 = "D:\\mydir\\test\\t"  # 源文件所在位置
path2 = "D:\\mydir\\test\\tt"  # 目标文件生成位置

# 生成器，生成文件的绝对路径


def WalkDirYFile(path):
    for root, ds, fs in os.walk(path):
        for f in fs:
            if f.endswith('.txt'):  # 只返回以.txt结尾的地址
                yield os.path.join(root, f)  # 拼接完成的绝对路径


# 生成器，生成目录路径，未使用
def WalkDirYDir(path):
    for root, ds, fs in os.walk(path):
        for d in ds:
            yield os.path.join(root, d)  # 拼接完成的绝对路径


# 主函数
def main():
    for f in WalkDirYFile(path1):  # 遍历文件
        d = path2 + os.path.dirname(f).replace(path1, '')  # 拼接目标文件存放目录
        nf = path2 + f.replace(path1, '')  # 拼接目标文件地址
        if not os.path.exists(d):  # 校检文件夹存在性
            os.makedirs(d)  # 不存在就创建
        with open(f, 'r', encoding='shift-jis') as rf:  # 以shift-jis编码读取文件
            s = rf.read()
            with open(nf, 'wb') as wf:
                wf.write(s.encode('utf-8'))  # 以utf-8格式写入文件


main()
