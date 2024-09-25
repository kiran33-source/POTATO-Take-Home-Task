Write tests to validate your query functions using pytest:

from query_functions import count_tweets_per_day

def test_count_tweets_per_day():
    # Test that querying for a term returns results
    result = count_tweets_per_day('music')
    assert result['hits']['total']['value'] > 0
