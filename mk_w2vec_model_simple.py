#!/usr/bin/python3

from argparse import ArgumentParser
import numpy as np
import MeCab
from gensim.models import word2vec

mecab = MeCab.Tagger()

def main():

    data_file = args.input_file
    
    # 単語分割ファイルを読み込み
    corpus = get_corpus(data_file)
    
    # print(corpus)
    
    # word2vec のオプション一覧 -> https://qiita.com/dskst/items/a9571bdd74a30a5e8d55 (英語)
    #                           -> https://qiita.com/mergit/items/822dc49343c887019d44 (日本語)
    # -sg ({0, 1}, optional) – Training algorithm: 1 for skip-gram; otherwise CBOW.
    # -size <int>   Set size of word vectors; default is 100
    # -window <int>   Set max skip length between words; default is 5
    # -min-count <int>   This will discard words that appear less than <int> times; default is 5
    
    model = word2vec.Word2Vec(corpus, sg=1, size=300, min_count=5, window=10)
    model.save("w2vec.model")


# ファイルを読み込んで文に分割
def get_corpus(data_file):
    
    word_list = []

    fp = open(data_file)
    
    for line in fp:
        try:
            word_str = line.rstrip().split(" ")
            word_list.append(word_str)
        except:
            print(line)
        
    return word_list


if __name__ == '__main__':
    
    parser = ArgumentParser(description='Make Word2vec model')
    parser.add_argument('-i', '--input_file', help='sentence.txt', required=True)
    
    args = parser.parse_args()

    main()
