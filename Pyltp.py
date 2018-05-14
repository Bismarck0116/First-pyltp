#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

Input = open("C:\\Users\zyh-tony\Desktop\大创\input2.txt", "r", encoding='utf-8')
Result = open("C:\\Users\zyh-tony\Desktop\大创\output.txt", "w+", encoding='utf-8')


def sentence_splitter(sentence):  # 分句，将文本分割为独立句子
    sents = SentenceSplitter.split(sentence)
    print('\n'.join(sents))


def stopwordslist(filepath):  # 加载停用词表
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def work():
    segmentor = Segmentor()  # 初始化实例（分词，词性，Ner）
    postagger = Postagger()
    recognizer = NamedEntityRecognizer()
    cws_model_path = "D:\\Academic\\LTP\\3.4.0\ltp_data_v3.4.0\cws.model"
    pos_model_path = "D:\\Academic\\LTP\\3.4.0\ltp_data_v3.4.0\pos.model"
    segmentor.load_with_lexicon(cws_model_path, "\\dictionary.txt")  # 加载模型和词典
    postagger.load_with_lexicon(pos_model_path, "\\dictionary.txt")
    recognizer.load('D:\\Academic\\LTP\\3.4.0\\ltp_data_v3.4.0\\ner.model')

    stopwords = stopwordslist('stoplist.txt')

    for line in Input.readlines():
        words = segmentor.segment(line)  # 分词
        words_list = list(words)
        word_list = []
        for word in words_list:
            if word not in stopwords :
                print(''.join(word) + ' ', end='')
                word_list.append(word)
        print()

        postags = postagger.postag(word_list)  # 词性分析
        postags_list = list(postags)
        for word, tag in zip(word_list, postags_list):
          print(word + ' /' + tag)
        print()

        netags = recognizer.recognize(word_list, postags)  # 命名实体识别
        for word, tag in zip(word_list, netags):
            if tag != 'O':
                print(word + '/' + tag)
        print()

    postagger.release()  # 释放模型
    segmentor.release()
    recognizer.release()


work()

Input.close()
Result.close()


'''
# 词性标注
def posttagger(words):
    postagger = Postagger()  # 初始化实例
    postagger.load('D:\\Academic\\LTP\\3.4.0\\ltp_data_v3.4.0\\pos.model')
    postags = postagger.postag(words)
    for word, tag in zip(words, postags):
        print(word + '/' + tag)
    postagger.release()
    return postags


# 依存语义分析(???)
def parse(words, postags):
    parser = Parser()  # 初始化实例
    parser.load('D:\\Academic\\LTP\\3.4.0\\ltp_data_v3.4.0\\parser.model')
    arcs = parser.parse(words, postags)  # 句法分析
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    parser.release()
    return arcs

# 测试分句
print('\n对给定句段的分句测试：')
sentence_splitter('明天是周三。所以我要上数据结构课，老师是王志海。然而这课好难。')
# 测试分词
print('\n分词测试：')
words = segmentor()
# 测试标注
print('\n词性标注测试：')
tags = posttagger(words)
# 测试命名实体识别
print('\n命名实体识别测试：')
netags = ner(words, tags)
'''




