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
        for e in vec:
            print(e)
    except KeyError:
        print("error -> "+input_str, file=sys.stderr)
        # return -1
    
if __name__ == '__main__':
    
    main()
