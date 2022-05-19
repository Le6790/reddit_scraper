import json
from gtts import gTTS
import os
import gtts
import pydub

class Text_To_Speech:
    def __init__(self, post_dict, lang="en"):
        self.post_dict = post_dict
        self.lang = lang


    def create_mp3s(self):

        # Create mp3 of the title
        self.create_mp3_title()

        self.create_mp3_selftext()

        self.create_mp3_comments()


    def create_mp3_title(self):
        
        title = self.post_dict["title"]
        file_name = f'{self.post_dict["filepath"]}title.mp3'

        gtts_obj = gTTS(title, lang=self.lang)
        gtts_obj.save(file_name)
    
    def create_mp3_selftext(self):

        selftext = self.post_dict["selftext"]
        file_name = f'{self.post_dict["filepath"]}selftext.mp3'

        gtts_obj = gTTS(selftext, lang=self.lang)
        gtts_obj.save(file_name)


    def create_mp3_comments(self):
        comments = self.post_dict["comments"]

        for comment in comments:
            file_name = f'{comment["score"]}_{comment["id"]}.mp3'

            gtts_obj = gTTS(comment.body, lang=self.lang)
            gtts_obj.save(file_name)

    