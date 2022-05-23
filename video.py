import create_video
import Jsonify


#post_dict = Jsonify.json_to_dict("./reddit_posts/AskReddit/what_rules_were_put_in_place_because_of_you_39786/what_rules_were_put_in_place_because_of_you_39786.json")
post_dict = Jsonify.json_to_dict("reddit_posts/AskReddit/for_people_who_grew_up_with_little_money_what_29543/for_people_who_grew_up_with_little_money_what_29543.json")


video = create_video.Create_Video(post_dict)

title_clip = video.create_title_clip()

#video.save_frame_of_clip(title_clip,"video_tests/title_clip.png")
#video.save_video_clips(title_clip,"video_tests/title_clip.mp4")

comment_clips = video.create_comment_clips()
#video.save_frame_of_clip(comment_clips, "video_tests/comment_clips_frame.png")
video.save_video_clips(comment_clips, "video_tests/for_people_who_gre_up_with_little_money.mp4","background_videos/pexels-tima-miroshnichenko-6010489.mp4")