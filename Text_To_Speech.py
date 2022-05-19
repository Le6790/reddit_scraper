import json
from gtts import gTTS
import os
import gtts
import pydub

class Text_To_Speech:
    def __init__(self, post_dict, lang="en",comment_limit=None):
        print("Creating text to speech object!")
        self.post_dict = post_dict
        self.lang = lang
        self.comment_limit = comment_limit

    def create_mp3s(self):

        # Create mp3 of the title
        self.create_mp3_title()

        self.create_mp3_selftext()

        self.create_mp3_comments()


    def create_mp3_title(self):
        print("Creating mp3 title")
        title = self.post_dict["title"]
        file_name = f'{self.post_dict["filepath"]}title.mp3'

        gtts_obj = gTTS(title, lang=self.lang)
        gtts_obj.save(file_name)
    
    def create_mp3_selftext(self):

        if self.post_dict["selftext"]:
            print("Creating mp3 selftext")
            selftext = self.post_dict["selftext"]
            file_name = f'{self.post_dict["filepath"]}selftext.mp3'

            gtts_obj = gTTS(selftext, lang=self.lang)
            gtts_obj.save(file_name)


    def create_mp3_comments(self):
        print("Creating mp3 comments")
        comments = self.post_dict["comments"]

        if self.comment_limit:
            comments = comments[:self.comment_limit]

        for comment in comments:
            
            file_name = f'{self.post_dict["filepath"]}comment_{comment["score"]}_{comment["id"]}.mp3'

            gtts_obj = gTTS(comment["comment"], lang=self.lang)
            gtts_obj.save(file_name)

    