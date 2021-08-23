<!DOCTYPE html>
<html lang="ja">
 <head>
  <meta chartype="UTF-8">
 </head>
 <body>
  <h1 style="font-size: 70px;">distributed_representation</h1>
    <p>
     テキスト記事データのディレクトリ100～200まで記事データとして、word2vecを用いて単語の分散表現を得るモデルを作成した。<br>
     本プログラムの「1.学習データ（data.txt）の生成」でCorpusデータの読み込みを行っているが、このCorpusデータを本レポジトリにpushしていないため、「1.学習データ（data.txt）の生成」の実装はできない。
    </p>
     <p style="color: red;">※本レポジトリをダウンロードした際には、 「2.モデルの生成」から、実行可能である。</p>
    <h3>1.学習データ（data.txt）の生成</h3>
    <p>
     python3 mk_w2vec_data.py > data.txt
    </p>
    <h3>2.モデル生成</h3>
    <p>
     python3 mk_w2vec_model_simple.py -i data.txt
    </p>
  <h4>生成物(作成されるモデル)</h4>
   <ul>
    <li>w2vec.model</li>                     
    <li>w2vec.model.trainables.syn1neg.npy</li>
    <li>w2vec.model.wv.vectors.npy</li>
  </ul>
 <h3>3.単語の分散表現の表示（300次元のベクトル．次元数は変更可能） </h3>
   <p>python3 word2vec.py 電池<br>
   ※「電池」は例でそれ以外も確認可能</p>
 <h3>4.類似単語の抽出（上位20を表示．変更可能）</h3>
   <p>python3 calc_similarity.py 電池<br>
   ※「電池」は例でそれ以外も確認可能</p>
 </body>
</html>
 
