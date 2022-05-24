import json
import time
from gtts import gTTS
import os
import gtts
import amazon_polly

class Text_To_Speech:
    def __init__(self, post_dict, lang="en",comment_limit=5, tts_method="gtts"):
        print("Creating text to speech object!")
        self.post_dict = post_dict
        self.lang = lang
        self.comment_limit = comment_limit
        self.tts_method = tts_method if tts_method in ["gtts", "polly"] else exit("tts_method is invalid. (gtts or polly only") #options are: gtts(default), polly

    def create_mp3s(self):

        # Create mp3 of the title
        self.create_mp3_title()
        # Create mp3 self texts
        self.create_mp3_selftext()
        # Create mp3 comments
        self.create_mp3_comments()


    def create_mp3_title(self):
        print("Creating mp3 title")
        title = self.post_dict["title"]
        file_name = f'{self.post_dict["filepath"]}title.mp3'

        if self.tts_method == "polly":
            self.polly_create_file(title,file_name)
        else:
            self.gtts_create_file(title,file_name)
    
    def create_mp3_selftext(self):

        if self.post_dict["selftext"]:
            print("Creating mp3 selftext")
            selftext = self.post_dict["selftext"]
            file_name = f'{self.post_dict["filepath"]}selftext.mp3'

            if self.tts_method == "polly":
                self.polly_create_file(selftext,file_name)
            else:
                self.gtts_create_file(selftext,file_name)



    def create_mp3_comments(self):
        print("Creating mp3 comments")
        comments = self.post_dict["comments"]

        if self.comment_limit:
            comments = comments[:self.comment_limit]

        for comment in comments:
            
            file_name = f'{self.post_dict["filepath"]}comment_{comment["score"]}_{comment["id"]}.mp3'
            if self.tts_method == "polly":
                self.polly_create_file(comment["comment"],file_name)
            else:
                self.gtts_create_file(comment["comment"],file_name)

    def gtts_create_file(self, text, file_name):
        gtts_obj = gTTS(text, lang=self.lang)
        gtts_obj.save(file_name)
        
        print(f"Finished creating gtts mp3 file: {file_name}")
    
    def polly_create_file(self, text, file_name):
        polly = amazon_polly.Amazon_Polly()
        polly.create_audio(text, file_name)
