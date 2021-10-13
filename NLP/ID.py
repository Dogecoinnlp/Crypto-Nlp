import praw
import numpy as np
import pandas as pd

from psaw import PushshiftAPI
from datetime import datetime

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

submissions = pd.read_csv('sub_list.csv')
submissions.head()

r = praw.Reddit(
    client_id="jjj5D707adNaIhRVNKPb6w",
    client_secret="qrp5rk7slJHYieRULSXCXhepw-cUpQ",
    password="myleancostmoredenurrent",
    user_agent="testscript by u/fakebot3",
    username="dogecoinnlp",
)

#Should print your username if you authenticated correctly
print(r.user.me())

#directs timestamped ids from PushshiftAPI to Praw submissions objects
#Submissions function doesn't work(can't obtain submissions)
#PushshiftAPI can get ids, but many datafields such as score and num_comments don't work
#so we need to combine the two
api = PushshiftAPI(r)

date_list = list(submissions.iloc[:,0])
date_len = len(date_list)

vector_list = []

for t in range(date_len):
  date = date_list[t]
  print(date)
  combined_list = []
  for i in range(100):
    id = submissions.iloc[t,1+i]
    post = r.submission(id)
    try:
        title = post.title

        combined_list.append(title)

        for comment in post.comments:

            body = comment.body

            if comment.score <= 40:
                break
            comment_date = datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d')
            if comment_date > date:
                continue

            combined_list.append(body)
    except:
        continue

  combined_string = '. '.join(combined_list)
  embeddings = model.encode(combined_string)
  vector_list.append(embeddings)


vector_df = pd.DataFrame(vector_list)

vector_df.to_csv('string.csv')