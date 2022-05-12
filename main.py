import praw
import config
import PrawReddit



def main():

    reddit_read_only = PrawReddit.PrawReddit(config.CONFIG)
    #reddit_read_only.get_hot_posts("formula1",10)

    post_dict = reddit_read_only.get_single_post("uo0v00")

    print(reddit_read_only.post_to_json(post_dict))
    reddit_read_only.write_post_to_json_file(post_dict,)


if __name__ == '__main__':
    main()
