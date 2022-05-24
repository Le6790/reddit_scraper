# reddit_stories

This is a simple project to scrape posts and comments and save the data to a JSON file.

The purpose of this project is to quickly scrape text data for use in a text to speech project for reddit stories and then create TTS video stories that follow a similar design.

Reddit data -> TTS -> video creation

Tools/Libraries used:<br/>
[Praw Reddit API](https://praw.readthedocs.io/en/stable/) <br/>
[MoviePy](https://zulko.github.io/moviepy/) <br/>
[Google Text To Speech](https://gtts.readthedocs.io/en/latest/)<br/>
[Amazon Polly (optional)](https://aws.amazon.com/polly/)<br/>



## Getting Started:
---
## Installation
### 1. Clone Repo
```
git clone git@github.com:Le6790/reddit_stories.git
```

### 2. Create a python virtual environment and install dependencies
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create the config.py file with the following information
```
touch config.py
```
config.py (authenication information creation instructions from https://www.reddit.com/wiki/api)
```
CONFIG = {
    "client_id": "",
    "client_secret": "",
    "user_agent": "reddit_stories V# {your username}",
    "AWSAccessKeyId":"", # If using Amazon Polly
    "AWSSecretKey":"", #If using Amazon Polly
}
```
## Usage
---
```
python main.py --background_video <path to background video mp4 file> --url <url of reddit post>
```
All arguments:
```
--url  -Reddit post URL (required)
--background_video - backgorund mp4 file to use in video (required)
--save_folder - Folder to store all generated files (optional, defaults to reddit_posts/)
--num_of_comments - Number of comments from post to use in video (optional, defaults to 5)
--tts_method - Text to speech method - (optional, gtts(default) or Amazon Polly)
```