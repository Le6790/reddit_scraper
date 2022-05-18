# reddit_stories

This is a simple project to scrape posts and comments and save the data to a JSON file.

The purpose of this project is to quickly scrape text data for use in a text to speech project for reddit stories and then create TTS video stories.

Documentation:

https://praw.readthedocs.io/en/stable/



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
    "user_agent": "reddit_stories V# {your username}"
}
