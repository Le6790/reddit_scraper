import praw
import json  # Might move this to it's own file..
from praw.models import MoreComments
from os import path,mkdir

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
        
        hot_posts_list = []
        for submission in hot_submissions:
            if not submission.stickied:
                hot_posts_list.append(self.get_single_post(submission.id))

        return hot_posts_list

    def get_single_post(self, url) -> dict:
        """
            Arguments: 
                url:str
            Returns: 
                dictionary with specific post information

            Given a url to a reddit post, returns specific post information and top level comments(sorted by score)
        """
        if (".com" in url):
            submission = self.reddit_instance.submission(url=url)
        # url can be submission id or actual reddit url
        else:
            submission = self.reddit_instance.submission(url)

        post = {}
        post["author"] = submission.author.name
        post["post_name"] = submission.permalink.split("/")[-2] + "_" + str(submission.score)
        post["score"] = submission.score
        post["selftext"] = submission.selftext
        post["title"] = submission.title
        post["url"] = submission.permalink
        post["subreddit"] = submission.subreddit.display_name
        post["comments"] = self.get_comments_from_submission(submission)
        
        return post

    def get_comments_from_submission(self, submission: praw) -> list:
        """returns a list of (toplevel)comment dicts"""
        comment_list = []
        for comment in submission.comments:
            if type(comment) == MoreComments or type(comment) == None:
                continue
            if comment.body == None or comment.author == None:
                continue
            comment_dict = {}
            if isinstance(comment, MoreComments):
                continue
            if comment.stickied:
                continue

            comment_dict["comment"] = comment.body
            comment_dict["author"] = comment.author.name if comment.body != "[removed]" else ""
            comment_dict["score"] = comment.score
            comment_dict["id"]= comment.id
            comment_list.append(comment_dict)

        # sort comments by score(upvotes)
        comment_list = sorted(
            comment_list, key=lambda i: int(i['score']), reverse=True)

        return comment_list


