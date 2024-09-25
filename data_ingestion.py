This script will handle reading the TSV file and indexing it into Elasticsearch.
import pandas as pd
from elasticsearch import Elasticsearch, helpers

def ingest_data(file_path, index_name):
    # Initialize Elasticsearch client
    es = Elasticsearch()

    # Load TSV data into Pandas
    data = pd.read_csv(file_path, sep='\t', usecols=['tweet_id', 'user_id', 'tweet_text', 'place_id', 'created_at', 'likes'])
    data['created_at'] = pd.to_datetime(data['created_at'])

    # Prepare data for bulk indexing into Elasticsearch
    actions = [
        {
            "_index": index_name,
            "_source": {
                "tweet_id": row['tweet_id'],
                "user_id": row['user_id'],
                "tweet_text": row['tweet_text'],
                "place_id": row['place_id'],
                "created_at": row['created_at'],
                "likes": row['likes']
            }
        }
        for _, row in data.iterrows()
    ]

    # Bulk index the data
    helpers.bulk(es, actions)
    print(f"Data from {file_path} has been ingested into Elasticsearch index '{index_name}'")

if __name__ == "__main__":
    ingest_data('path_to_your_tsv_file.tsv', 'twitter_data')
