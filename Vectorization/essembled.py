from ID2 import *
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

import datetime
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)
delta = datetime.timedelta(days=1)

start_date_string = str(start_date)
end_date_string = str(end_date)

embeddings_list = []

while start_date <= end_date:
    date = str(start_date)
    print(date)
    id_list = obtain_ids(date)
    #print(id_list)
    top_posts_list = find_top_posts(id_list,date=date)
    #print(top_posts_list)
    string_day = combine_string_from_date(top_posts_list)
    embeddings = model.encode(string_day)
    embeddings_list.append(embeddings)
    start_date += delta

embeddings_df = pd.DataFrame(embeddings_list)
embeddings_df.to_csv('from_date_{}_to_date_{}.csv'.format(start_date_string,end_date_string))