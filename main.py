import praw
import config
import PrawReddit
import Jsonify


def main():

    reddit_read_only = PrawReddit.PrawReddit(config.CONFIG)
    reddit_read_only.get_hot_posts("formula1",5)

    post_dict = reddit_read_only.get_single_post("uo0v00")

    print(Jsonify.dict_to_json(post_dict))
    Jsonify.write_to_json_filepost_dict,"reddit_posts")


    post_dict = reddit_read_only.get_single_post("https://www.reddit.com/r/movies/comments/uo6e8z/christopher_walken_to_play_emperor_shaddam_iv_in/")

    print(Jsonify.dict_to_json(post_dict))
    Jsonify.write_to_json_filepost_dict,"reddit_posts")

    formula1_posts = reddit_read_only.get_hot_posts("formula1",5)

    for post in formula1_posts:
        Jsonify.write_to_json_file(post,"formula1/")
if __name__ == '__main__':
    main()
