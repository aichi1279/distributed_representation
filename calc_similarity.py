#!/usr/bin/python3

from gensim.models import word2vec
import sys

def main():

    args = sys.argv
    input_str = args[1]
    
    model = word2vec.Word2Vec.load("w2vec.model")

    # 単語のベクトル
    try:
        vec = model[input_str]
    except KeyError:
        print("key error")
        return
    
    # 類似の単語
    results = model.most_similar([vec],[],20)

    for word,sim in results:
        # 同じ単語は除去
        if sim < 0.98:
            print(word+" "+str(sim))
    
    
if __name__ == '__main__':
    
    main()
