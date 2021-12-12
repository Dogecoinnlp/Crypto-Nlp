import praw
import numpy as np
import pandas as pd

from psaw import PushshiftAPI
from datetime import datetime
from datetime import datetime
from sentence_transformers import SentenceTransformer

#model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

r = praw.Reddit(
    client_id="jjj5D707adNaIhRVNKPb6w",
    client_secret="qrp5rk7slJHYieRULSXCXhepw-cUpQ",
    password="myleancostmoredenurrent",
    user_agent="testscript by u/fakebot3",
    username="dogecoinnlp",
)

print(r.user.me())

api = PushshiftAPI(r)

def obtain_ids(date = '2021-09-01'):
    start_epoch = int(datetime.fromisoformat(date).timestamp())
    end_epoch = start_epoch + 86400
    id_list = list(api.search_submissions(after=start_epoch, before=end_epoch, subreddit='Bitcoin'))
    #print(ids)
    return id_list

def obtain_comment_list(id,date = '2021-09-01'):
    start_epoch = int(datetime.fromisoformat(date).timestamp())
    end_epoch = start_epoch + 86400
    comment_list = [com for com in id.comments.list() if com.created_utc < end_epoch]
    return comment_list, len(comment_list)

def find_top_posts(id_list, date='2021-09-01',num_top_submission = 20):

    l = len(id_list)
    num_comments_list = np.zeros(l)
    comment_list = []

    for i in range(0, l):
        id_list[i].comments.replace_more(limit=None)
        comments, num_comment = obtain_comment_list(id_list[i], date)
        comment_list.append(comments)
        num_comments_list[i] = num_comment

    l = len(id_list)
    sorted_ids = pd.Series(data=num_comments_list, index=range(0, l)).sort_values(ascending=False)
    top_submissions = [id_list[i] for i in sorted_ids.index]

    return top_submissions[0:num_top_submission]

def combine_string_from_date(top_posts_list):
    string_day = []
    #print('one')
    for post in top_posts_list:
        try:
            post_title = post.title
            string_day.append(post_title)
            for comment in post.comments:
                string_day.append(comment.body)
        except:
            continue

    combined_string = '. '.join(string_day)
    return combined_string
