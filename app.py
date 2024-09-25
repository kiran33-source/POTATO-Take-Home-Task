This is the main application script, which integrates the data ingestion and querying functionality.

from query_functions import count_tweets_per_day, count_unique_users, avg_likes, top_user

def main():
    term = input("Enter a search term: ")

    # Example of calling query functions
    tweets_per_day = count_tweets_per_day(term)
    print(f"Tweets per day for '{term}': {tweets_per_day}")

    unique_users = count_unique_users(term)
    print(f"Unique users who tweeted '{term}': {unique_users}")

    average_likes = avg_likes(term)
    print(f"Average likes for tweets with '{term}': {average_likes}")

    top_tweeter = top_user(term)
    print(f"User with most tweets for '{term}': {top_tweeter}")

if __name__ == "__main__":
    main()
