import pickle
from flask import Flask, request, render_template
import librosa
import os
from datasketch import MinHash, MinHashLSH
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('soap.html')

@app.route('/upload', methods=['POST'])
def upload():
    # get uploaded file
    file = request.files['file']

    # save file to disk
    file.save(file.filename)    

    # calculate minhashes for each audio file in the folder
    folder = r"C:\Users\muham\Desktop\songs"
    mfccs = []

    # for filename in os.listdir(folder):
    #      if filename.endswith(".mp3"):
    #          y, sr = librosa.load(folder + "/" + filename)
    #          mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=30)
    #          mfccs.append(mfcc)
    minhashes = []
    # for mfcc in mfccs:
    #      minhash = MinHash(num_perm=10)
    #      for d in mfcc.flatten():
    #          minhash.update(str(d).encode('utf8'))
    #      minhashes.append(minhash)

    # with open('minhashes.pickle', 'wb') as f:
    #      pickle.dump(minhashes, f)    

    # calculate minhash for uploaded audio file
    new_audio, sr = librosa.load(file.filename)
    target_mfcc = librosa.feature.mfcc(y=new_audio, sr=sr, n_mfcc=30)
    target_minhash = MinHash(num_perm=10)
    for d in target_mfcc.flatten():
        target_minhash.update(str(d).encode('utf8'))


    #  # pickle the target_minhash for later use
    # with open('minhash.pickle', 'wb') as f:
    #     pickle.dump(target_minhash, f)   

    # perform LSH to find similar audio files
    lsh = MinHashLSH(threshold=0.25, num_perm=10)
   
    # unpickle the minhashes
    with open('minhashes.pickle', 'rb') as f:
        minhashes = pickle.load(f)

    for i, minhash in enumerate(minhashes):
        lsh.insert(i, minhash)

    result = lsh.query(target_minhash)

    # create dataframe with results
    files = os.listdir(folder)
    audio_df = pd.DataFrame({'Filename': files})
    similar_files = audio_df.loc[result]

   

    return render_template('result.html', similar_files=similar_files.to_html())

if __name__ == '__main__':
    app.run(debug=True)
