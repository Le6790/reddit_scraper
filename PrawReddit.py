import praw
import json  # Might move this to it's own file..
from praw.models import MoreComments


class PrawReddit:
    def __init__(self, config):
        """
            Input: 
                config file
                    CONFIG = {
                        "client_id": "",
                        "client_secret": "",
                        "user_agent": ""
                    }

            initiate a reddit PRAW instance
        """
        self.reddit_instance = praw.Reddit(client_id=config["client_id"],             # your client id
                                            client_secret=config["client_secret"],    # your client secret
                                            user_agent=config["user_agent"])          # your user agent

    def get_hot_posts(self, subreddit_name, limit=None) -> praw.models:
        """
            Arguments: 
                subreddit_name:str
                limit:int
            Returns:
                praw list of hot submissions

            Get the hot posts/submissions in a given subreddit
        """
        subreddit = self.reddit_instance.subreddit(subreddit_name)

        hot_submissions = subreddit.hot(limit=limit)

        for submission in hot_submissions:
            if not (submission.stickied):
                print(submission.title, submission.upvote_ratio)
                print(submission.id)
                print(submission.url)
                print('Comment Count', len(submission.comments))
                submission.comments.replace_more(limit=None)
                all_comments = []
                comment_queue = submission.comments[:]
                while comment_queue:
                    comment = comment_queue.pop(0)
                    comment_queue.extend(comment.replies)
                    all_comments.append(comment)
                print('All comment count: ', len(all_comments))
                print("-----")
        return hot_submissions

    def get_single_post(self, url) -> dict:
        """
            Arguments: 
                url:str
            Returns: 
                dictionary with specific post information

            Given a url to a reddit post, returns specific post information and top level comments(sorted by score)
        """

        # url can be submission id or actual reddit url
        submission = self.reddit_instance.submission(url)

        post = {}
        post["title"] = submission.title
        post["author"] = submission.author.name
        post["score"] = submission.score
        post["selftext"] = submission.selftext
        post["url"] = submission.url
        post["comments"] = self.get_comments_from_submission(submission)
        return post

    def get_comments_from_submission(self, submission: praw) -> list:
        """returns a list of (toplevel)comment dicts"""
        comment_list = []
        for comment in submission.comments:
            comment_dict = {}
            if isinstance(comment, MoreComments):
                continue
            if comment.stickied:
                continue
            comment_dict["comment"] = comment.body
            comment_dict["author"] = comment.author.name
            comment_dict["score"] = comment.score

            comment_list.append(comment_dict)

        # sort comments by score(upvotes)
        comment_list = sorted(
            comment_list, key=lambda i: int(i['score']), reverse=True)

        return comment_list

    def post_to_json(self, post: dict) -> json:
        """
            Input: 
                post: dict
            Return 
                json object

            Convert dictionary to json string
        """
        json_object = json.dumps(post, indent=4)
        return json_object

    def write_post_to_json_file(self, post: dict, directory_path: str = "") -> None:
        """
            Input: 
                post: dictionary
                directory_path: str
            Return 
                json object

            Convert dictionary to json and writes it to a file
        """
        filename = directory_path + post["title"].replace(" ", "_") + ".json"
        with open(filename, 'w') as outfile:
            json.dump(post, outfile)

        print(f"Dumped json into: {filename}")
