import jieba
import  jieba.analyse
jieba.analyse.set_stop_words(r"F:\github\TianWen\Search\stopwords.txt")


def cut(str):
    cut1 = jieba.analyse.extract_tags(str, topK=10)
    dic = ','.join(cut1).split(',')
    return dic