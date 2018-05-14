# -*- coding: UTF-8 -*-
import jieba.posseg as pseg
import jieba.analyse
import pynlpir

fn = open("C:\\Users\zyh-tony\Desktop\大创\input2.txt", "r", encoding='utf-8')
res = open("C:\\Users\zyh-tony\Desktop\大创\output.txt", "w+", encoding='utf-8')

jieba.load_userdict("C:\\Users\zyh-tony\Desktop\大创\dictionary.txt")  # 加载司法词典
# stopwords = {}.fromkeys([line.strip() for line in codecs.open(
# 'C:\\Users\zyh-tony\Desktop\大创\stoplist.txt', encoding='utf-8')])  # 加载停用词表


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def work1(sentence):  # 分词
    stopwords = stopwordslist('C:\\Users\zyh-tony\Desktop\大创\stoplist.txt')
    sentence_seged = jieba.cut(sentence.strip())
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:  # 与停用词表进行筛查比对
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


for line in fn:
    line_seg = work1(line)
    res.write(line_seg + '\n')  # 将分词之后的结果输出到目标文件中


res.close()
fn.close()


def work2():  # nlpir词性分析与关键词提取
    pynlpir.open()
    s = '因为明天是周三，所以我要有数据结构课，然而这课好难。'
    segments = pynlpir.segment(s, pos_names='all', pos_english=False)  # 全分析
    for segment in segments:
        print(segment[0], '\t', segment[1])
    key_words = pynlpir.get_key_words(s, weighted=True)  # 关键词提取
    for key_word in key_words:
        print(key_word[0], '\t', key_word[1])
    pynlpir.close()


# work2()
