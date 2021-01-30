# distributed_representation



テキスト記事データ（Python入門２でダウンロードしたテキストデータ）のディレクトリ100～200まで記事データとして、word2vecを用いて単語の分散表現を得るモデルを作成した。
<br>

1. 学習データ（data.txt）の生成             <br>
python3 mk_w2vec_data.py > data.txt

2. モデル生成
python3 mk_w2vec_model_simple.py -i data.txt

<生成物(作成されるモデル)>　                <br>
(1)w2vec.model                         <br>
(2)w2vec.model.trainables.syn1neg.npy  <br>
(3)w2vec.model.wv.vectors.npy          <br>


3. 単語の分散表現の表示（300次元のベクトル．次元数は変更可能） <br>
python3 word2vec.py 電池

※「電池」は例でそれ以外も確認可能

 <br>
4. 類似単語の抽出（上位20を表示．変更可能） <br>
python3 calc_similarity.py 電池

※「電池」は例でそれ以外も確認可能
