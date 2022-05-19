import moviepy.editor as mpye
from numpy import mintypecode
import Jsonify


vcodec = "libx264"

videoquality = "24"

compress = "slow"


post_dict = Jsonify.json_to_dict(
    "./reddit_posts/AskReddit/what_rules_were_put_in_place_because_of_you_39786/what_rules_were_put_in_place_because_of_you_39786.json")


class Create_Video:

    def __init__(self, post_dict):
        self.post_dict = post_dict

    def create_title_clip(self):

        title_text = self.post_dict["title"]
        title_mp3_file = self.get_files("title.mp3")

        final_title_clip = self.create_clip_with_background(title_text, title_mp3_file)

        return final_title_clip

    def create_clip_with_background(self, text, mp3_file):

        # Create the clip
        clip = mpye.TextClip(txt=text,
                                   fontsize=40,
                                   color="black",
                                   method="caption",
                                   size=(750, 0),
                                    stroke_color="white",
                                    stroke_width=3
                                   )
        clip = clip.set_position(("center"))
        clip_width, clip_height = clip.size

        # Create the clip background
        # colored background
        clip_color_background = mpye.ColorClip(size=(clip_width+100,
                                                   clip_height+50),
                                             color=(109, 109, 109))
        clip_color_background = clip_color_background.set_opacity(0.6)
    
        #compose the final clip + background
        final_clip = mpye.CompositeVideoClip([clip_color_background, clip])

        #set the final clip audio and the clip duration to the audio's duration
        audio_clip = mpye.AudioFileClip(mp3_file)

        final_clip = final_clip.set_duration(audio_clip.duration)

        final_clip.audio = audio_clip

        return final_clip

    def create_single_comment_clip(self, text, author, score, mp3_file,):
        # Create the clip

        ### Text Clip ###
        text_clip = mpye.TextClip(txt=text,
                                   fontsize=40,
                                   color="black",
                                   method="caption",
                                   size=(750, 0),
                                    stroke_color="white",
                                    stroke_width=3
                                   )
        text_clip = text_clip.set_position(("center"))
        text_clip_width, text_clip_height = text_clip.size

        ### END Text Clip ###

        ### Author Clip ###
        author_clip = mpye.TextClip(txt=f"u/{author}",
                                   fontsize=30,
                                   color="black",
                                   method="caption",
                                   size=(0,50),
                                    stroke_color="white",
                                    stroke_width=3
                                   )
        author_clip = author_clip.set_position(25,50)
        ### End Author Clip ###

        ### Score Clip ###
        score_clip = mpye.TextClip(txt=f"{score}",
                                   fontsize=30,
                                   color="black",
                                   method="caption",
                                   size=(0,50),
                                    stroke_color="white",
                                    stroke_width=3
                                   )
        score_clip = score_clip.set_position(25,100)

        # Create the clip background
        # colored background
        clip_color_background = mpye.ColorClip(size=(text_clip_width+100,
                                                   text_clip_height+50),
                                             color=(109, 109, 109))
        clip_color_background = clip_color_background.set_opacity(0.6)
    
        #compose the final clip + background
        final_clip = mpye.CompositeVideoClip([clip_color_background, author_clip, score_clip, text_clip])

        #set the final clip audio and the clip duration to the audio's duration
        audio_clip = mpye.AudioFileClip(mp3_file)

        final_clip = final_clip.set_duration(audio_clip.duration)

        final_clip.audio = audio_clip

        return final_clip

    def create_comment_clips(self):
        comments = self.post_dict["comments"]

        comment_clips = []
        for comment in comments[:3]: #TODO: loop over comments a different way
            actual_comment = comment["comment"]
            comment_mp3_filename = f"comment_{comment['score']}_{comment['id']}.mp3"
            comment_mp3_filepath = self.get_files(comment_mp3_filename)

            comment_clip = self.create_clip_with_background(actual_comment, comment_mp3_filepath)

            comment_clips.append(comment_clip)

        # #Check if clip's height is greater than a certain value, if so, exclude that clip
        # width = -1
        # height = -1
        # for clip in comment_clips:
        #     clip_width, clip_height = clip.size
        #     print(f"clip_width: {clip_width}")
        #     print(f"clip_height: {clip_height}")
        #     print("-----")
        #     if clip_height > height:
        #         height = clip_height
        #         width = clip_width
        # print(f"width: {width}")
        # print(f"height: {height}")
        # new_comment_clips = []
        # if width !=-1 and height != -1:
        #     for clip in comment_clips:
        #         clip.resize((width,height))

        #         new_comment_clips.append(clip)
            


        concatenated_comment_clips = mpye.concatenate_videoclips(comment_clips)
        return concatenated_comment_clips




    def save_frame_of_clip(self, clip, name):
        clip.save_frame(name)
        print(f"Saved clip - {name}.")

    def save_video_clips(self, clips:mpye.CompositeVideoClip, name):
        #add background
        background_clip = mpye.VideoFileClip("background_videos/boat_on_sea_2mins.mp4")
        background_clip = background_clip.set_duration(clips.duration)

        final_clip = mpye.CompositeVideoClip([background_clip,clips.set_position("center")])
        final_clip.write_videofile(name,fps=24)
        print(f"Saved clip as a video - {name}")

    def get_files(self, file):
        filepath = self.post_dict["filepath"]

        return filepath + file
