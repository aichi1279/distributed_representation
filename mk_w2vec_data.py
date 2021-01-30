import cv2
import MeCab
import glob

mecab = MeCab.Tagger()

def main():
    Corpus = "/Users/comp6/Desktop/program/class_NL/Corpus/*/*.txt"
    files = glob.glob(Corpus)

    list = []
    files.sort()
    for file in files:
        Dir_num = int(file.split('/')[-2])#ディレクトリ番号100~200に指定
        #print(Dir_num)
        if Dir_num < 100:
            continue
        elif Dir_num > 200:
            break

        #print(file.split('/')[-1])
        sgml = open(file)
        lines = sgml.readlines()

        sub_list = []
        for line in lines:
            if "<title>" in line or "<class>" in line or "。" not in line:
                continue

            mecab_results = mecab.parse(line)
            results = mecab_results.split("\n")
            s=""
            for info in results:
                word = info.split("\t")[0]
                sub_list.append(word)



        list.append(sub_list)


    for key in list:
        key = str(key)
        key = key.replace('[','')
        key = key.replace(']' ,'')
        key = key.replace(',',' ')
        key = key.replace("'",'')
        key = key.replace('EOS' , '')
        key = key.replace('   ' , ' ')
        key = key.replace('  ' , ' ')
        key = key.replace('。 ' , '。 \n') #文毎に見やすくしたい
        print(key, end="")



if __name__ == "__main__":
        main()
