import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

from scipy.spatial import distance

positive_comments = np.reshape(np.array(pd.read_excel('Positive_strings.xlsx')),-1)
negative_comments = np.reshape(np.array(pd.read_excel('Bert_validation.xlsx')),-1)


string_comapred = 'Bitcoin does not worth anything, you should not buy Bitcoin, Bitcoin market will crash'
benchmark = model.encode(string_comapred)

print('positive compare:')
for string in positive_comments:
    vector = model.encode(string)
    cos_dis = distance.cosine(benchmark, vector)
    print(string)
    print(cos_dis)

print('negative compare:')
for string in negative_comments:
    vector = model.encode(string)
    cos_dis = distance.cosine(benchmark, vector)
    print(string)
    print(cos_dis)