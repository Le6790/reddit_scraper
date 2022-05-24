import moviepy.editor as mpye
from numpy import mintypecode
import Jsonify
import os 
vcodec = "libx264"

videoquality = "24"

compress = "slow"

class Create_Video:

    def __init__(self, post_dict, comment_limit):
        self.post_dict = post_dict
        self.title_mp3 = self.get_files("title.mp3")
        self.comments_mp3 = self.get_files("comments.mp3")
        self.comment_limit = comment_limit
        self.duration = self.get_duration()

    def create_title_clip(self):

        title_text = self.post_dict["title"]
        title_mp3_file = self.title_mp3
        score = self.post_dict["score"]
        
        #set the final clip audio and the clip duration to the audio's duration
        audio_clip = mpye.AudioFileClip(title_mp3_file)

        # Create the clip
        clip = mpye.TextClip(txt=title_text,
                                   fontsize=40,
                                   color="black",
                                   method="caption",
                                   size=(750, 0),
                                    stroke_color="white",
                                    stroke_width=3
                                   )
        clip = clip.set_position(("center"))
        clip_width, clip_height = clip.size

        # ### Score Clip ###
        score_clip = self.create_title_score_clip(score,audio_clip.duration)
        score_clip = score_clip.set_position((10,10))
        ### END Score Clip ###



        # Create the clip background
        # colored background
        clip_color_background = mpye.ColorClip(size=(clip_width+150,
                                                   clip_height+50),
                                             color=(109, 109, 109))
        clip_color_background = clip_color_background.set_opacity(0.6)
    
        #compose the final clip + background
        final_clip = mpye.CompositeVideoClip([clip_color_background, score_clip, clip])

        final_clip = final_clip.set_duration(audio_clip.duration)

        final_clip.audio = audio_clip

        self.title_clip = final_clip
        return final_clip


    def create_single_comment_clip(self, text, author, score, mp3_file,):
        # Create the clip
        audio_clip = mpye.AudioFileClip(mp3_file)
        ### Text Clip ###
        text_clip = mpye.TextClip(txt=text,
                                   fontsize=30,
                                   color="white",
                                   method="caption",
                                   size=(750, 0),
                                    stroke_color="white",
                                    stroke_width=2
                                   )
        text_clip = text_clip.set_position(("center",100))
        text_clip_width, text_clip_height = text_clip.size

        ### END Text Clip ###

        ### Author Clip ###
        author_clip = mpye.TextClip(txt=f"Posted by u/{author}",
                                   fontsize=25,
                                   color="gray",
                                   method="caption",
                                   size=(800,0),
                                    stroke_color="rgb(217, 217, 217)",
                                    stroke_width=1,
                                    align="west"
                                   )
        author_clip = author_clip.set_position((25,20))
        ### End Author Clip ###

        # ### Score Clip ###
        score_clip = self.create_score_clip(score,audio_clip.duration)
        score_clip = score_clip.set_position((25,30))
        ### END Score Clip ###


        # Create the clip background
        # colored background
        clip_color_background = mpye.ColorClip(size=(text_clip_width+100,
                                                   text_clip_height+150),
                                                   color=(109, 109, 109))
        clip_color_background = clip_color_background.set_opacity(0.6)
    
        #compose the final clip + background
        final_clip = mpye.CompositeVideoClip([clip_color_background, author_clip, score_clip, text_clip])

        #set the final clip audio and the clip duration to the audio's duration
        

        final_clip = final_clip.set_duration(audio_clip.duration)

        final_clip.audio = audio_clip

        return final_clip

    def create_score_clip(self,score, duration):

        upvote_arrow = mpye.ImageClip("resources/upvote.png")
        upvote_arrow = upvote_arrow.resize(0.035)
        upvote_arrow = upvote_arrow.set_position(("left","center"))
        downvote_arrow =  mpye.ImageClip("resources/downvote.png")
        downvote_arrow = downvote_arrow.resize(0.035)
        downvote_arrow = downvote_arrow.set_position("right","center")
        
        
        
        score_clip = mpye.TextClip(txt=f"{score}",
                                   font="Helvetica",
                                   fontsize=26,
                                   color="white",
                                   method="caption",
                                   size=(0,50),
                                    stroke_color="white",
                                    stroke_width=1
                                   )
        score_clip = score_clip.set_position(("center"))

        score_clip_width, score_clip_height = score_clip.size

        background = mpye.ColorClip(size=(score_clip_width + 50,score_clip_height + 5),color=(255,0,0))
        background = background.set_opacity(0.0)

        final_score_clip = mpye.CompositeVideoClip([background,upvote_arrow,score_clip,downvote_arrow])
        final_score_clip = final_score_clip.set_duration(duration)

        return final_score_clip


    def create_title_score_clip(self, score, duration):
        upvote_arrow = mpye.ImageClip("resources/upvote.png")
        upvote_arrow = upvote_arrow.resize(0.035)
        upvote_arrow = upvote_arrow.set_position(("center","top"))
        downvote_arrow =  mpye.ImageClip("resources/downvote.png")
        downvote_arrow = downvote_arrow.resize(0.035)
        downvote_arrow = downvote_arrow.set_position("center","bottom")


        score_clip = mpye.TextClip(txt=f"{score}",
                                   font="Helvetica",
                                   fontsize=26,
                                   color="white",
                                   method="caption",
                                   size=(0,100),
                                    stroke_color="white",
                                    stroke_width=1
                                   )
        score_clip = score_clip.set_position(("center",0))

        score_clip_width, score_clip_height = score_clip.size

        background = mpye.ColorClip(size=(score_clip_width + 5,score_clip_height + 60),color=(255,0,0))
        background = background.set_opacity(0.0)

        final_score_clip = mpye.CompositeVideoClip([background,upvote_arrow,score_clip,downvote_arrow])
        final_score_clip = final_score_clip.set_duration(duration)


        return final_score_clip



    def create_comment_clips(self):
        comments = self.post_dict["comments"]

        comment_clips = []
        for comment in comments[:self.comment_limit]:
            actual_comment = comment["comment"]
            author = comment["author"]
            score = comment["score"]
            comment_mp3_filename = f"comment_{comment['score']}_{comment['id']}.mp3"
            comment_mp3_filepath = self.get_files(comment_mp3_filename)

            # comment_clip = self.create_clip_with_background(actual_comment, comment_mp3_filepath)
            comment_clip = self.create_single_comment_clip(actual_comment,author, score, comment_mp3_filepath)

            comment_clips.append(comment_clip)

        title_clip = self.title_clip

        comment_clips.insert(0,title_clip)
        concatenated_comment_clips = mpye.concatenate_videoclips(comment_clips)
        return concatenated_comment_clips




    def save_frame_of_clip(self, clip, name):
        clip.save_frame(name)
        print(f"Saved clip - {name}.")

    def save_video_clips(self, clips:mpye.CompositeVideoClip, name,background_clip):
        #add background
        background_clip = mpye.VideoFileClip(background_clip)
        background_clip = background_clip.without_audio()
        if (clips.duration > background_clip.duration):
            background_clip = background_clip.loop(duration=clips.duration)
        else:
            background_clip = background_clip.set_duration(clips.duration)
        background_clip = background_clip.resize((1080,1920))

        final_clip = mpye.CompositeVideoClip([background_clip,clips.set_position("center")])
        final_clip.write_videofile(name)
        print(f"Saved clip as a video - {name}")

    def get_files(self, file):
        filepath = self.post_dict["filepath"]

        comment_files = []
        if(file == "comments.mp3"):
            for (dirpath, dirnames,filenames) in os.walk(filepath):
                comment_files.extend([f"{filepath}{filename}" for filename in filenames if "comment" in filename])
            return comment_files

        return filepath + file

    def get_duration(self):
        
        full_duration = 0

        #title duration
        full_duration += mpye.AudioFileClip(self.title_mp3).duration

        #comments duration
        for comment in self.comments_mp3:
            full_duration += mpye.AudioFileClip(comment).duration

        return full_duration


