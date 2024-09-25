This script contains various query functions, which will be called by the main application.

from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch()

def count_tweets_per_day(term):
    query_body = {
        "query": {"match": {"tweet_text": term}},
        "aggs": {
            "tweets_per_day": {
                "date_histogram": {"field": "created_at", "calendar_interval": "day"}
            }
        }
    }
    return es.search(index="twitter_data", body=query_body)

def count_unique_users(term):
    query_body = {
        "query": {"match": {"tweet_text": term}},
        "aggs": {"unique_users": {"cardinality": {"field": "user_id"}}}
    }
    return es.search(index="twitter_data", body=query_body)

def avg_likes(term):
    query_body = {
        "query": {"match": {"tweet_text": term}},
        "aggs": {"average_likes": {"avg": {"field": "likes"}}}
    }
    return es.search(index="twitter_data", body=query_body)

def top_user(term):
    query_body = {
        "query": {"match": {"tweet_text": term}},
        "aggs": {"top_user": {"terms": {"field": "user_id", "size": 1}}}
    }
    return es.search(index="twitter_data", body=query_body)

# Add other query functions here (e.g., place ID, times of day)
