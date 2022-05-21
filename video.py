import create_video
import Jsonify


#post_dict = Jsonify.json_to_dict("./reddit_posts/AskReddit/what_rules_were_put_in_place_because_of_you_39786/what_rules_were_put_in_place_because_of_you_39786.json")
post_dict = Jsonify.json_to_dict("reddit_posts/AskReddit/what_is_something_youre_willing_to_admit_only_to_22945/what_is_something_youre_willing_to_admit_only_to_22945.json")


video = create_video.Create_Video(post_dict)

title_clip = video.create_title_clip()

#video.save_frame_of_clip(title_clip,"video_tests/title_clip.png")
#video.save_video_clips(title_clip,"video_tests/title_clip.mp4")

comment_clips = video.create_comment_clips()
#video.save_frame_of_clip(comment_clips, "video_tests/comment_clips_frame.png")
video.save_video_clips(comment_clips, "video_tests/what_is_something_youre_.mp4")