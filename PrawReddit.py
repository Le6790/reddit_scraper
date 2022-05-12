import praw


class PrawReddit:
    def __init__(self,config):
        self.reddit_instance = praw.Reddit(client_id=config["client_id"],         # your client id
                                   client_secret=config["client_secret"], # your client secret
                                   user_agent=config["user_agent"])       # your user agent
    

    def get_subreddit(self, subreddit):
        return self.reddit_instance.subreddit(subreddit)

    def get_hot_posts(self,subreddit_name,limit=None):

        subreddit = self.get_subreddit(subreddit_name)

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