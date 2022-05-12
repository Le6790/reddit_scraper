import praw
import config
import PrawReddit



def main():

    reddit_read_only = PrawReddit.PrawReddit(config.CONFIG)


    subreddit = reddit_read_only.get_subreddit("redditdev")

    print(subreddit.display_name)

    reddit_read_only.get_hot_posts("formula1",10)

if __name__ == '__main__':
    main()
