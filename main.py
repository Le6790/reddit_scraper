import argparse
import config
import PrawReddit
import Jsonify
import Text_To_Speech
import create_video

def main(args):

    reddit_read_only = PrawReddit.PrawReddit(config.CONFIG)
    save_folder= "./reddit_posts"
    
    post_dict = {}
    if args.url:
        post_dict = reddit_read_only.get_single_post(args.url)

        if args.save_folder:
            save_folder =  f'{args.save_folder}/{post_dict["subreddit"]}/{post_dict["post_name"]}/'
        else:
            save_folder = f'{save_folder}/{post_dict["subreddit"]}/{post_dict["post_name"]}/'

        Jsonify.write_to_json_file(post_dict,save_folder)
    


    input("Pausing to allow you to review the json. Press enter to continue.")

    updated_json = Jsonify.json_to_dict(save_folder + post_dict["post_name"].replace(" ", "_") + ".json")
    if post_dict != updated_json:
        print("Updated post dict json file!")
        post_dict = updated_json
    
    # Create TTS mp3s

    tts = Text_To_Speech.Text_To_Speech(post_dict,comment_limit=5,tts_method=args.tts_method)

    tts.create_mp3s()

    
    #Create videos

    if (input("Do you want to create a video from the given reddit submission? (y/n)") == "y"):
        video = create_video.Create_Video(post_dict,args.num_of_comments)
        title_clip = video.create_title_clip()
        #video.save_frame_of_clip(title_clip,"video_tests/title_clip.png")
        #video.save_video_clips(title_clip,"video_tests/title_clip.mp4")

        comment_clips = video.create_comment_clips()
        #video.save_frame_of_clip(comment_clips, "video_tests/comment_clips_frame.png")
        video.save_video_clips(comment_clips, f'{save_folder}{post_dict["post_name"]}.mp4', args.background_video)
    



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help="Reddit post URL", required=True)
    parser.add_argument('--save_folder', type=str, help="Folder to store files")
    parser.add_argument('--background_video', type=str, help="Background mp4 file to use in video", required=True)
    parser.add_argument('--num_of_comments', type=int, help="Number of comments to use (Defaults to 5)")
    parser.add_argument('--tts_method', type=str, help="Text to Speech Method (gtts(default) or polly)",default="gtts")
    args = parser.parse_args()
    main(args)
