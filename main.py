import praw
import config
import PrawReddit
import Jsonify
import argparse


def main(args):

    reddit_read_only = PrawReddit.PrawReddit(config.CONFIG)
    save_folder= "./reddit_posts"
    
    post_dict = {}
    if args.url:
        post_dict = reddit_read_only.get_single_post(args.url)
        print(post_dict)

        if args.save_folder:
            save_folder =  f'{args.save_folder}/{post_dict["subreddit"]}/{post_dict["post_name"]}/'
        else:
            save_folder = f'{save_folder}/{post_dict["subreddit"]}/{post_dict["post_name"]}/'

        Jsonify.write_to_json_file(post_dict,save_folder)




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help="Reddit post URL", required=True)
    parser.add_argument('--save_folder', type=str, help="Folder to store files")

    args = parser.parse_args()
    main(args)
