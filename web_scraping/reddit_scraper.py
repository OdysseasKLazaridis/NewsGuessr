import praw
from praw.models import MoreComments
import pandas as pd
import numpy as np
from tqdm import tqdm
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
 
BASE_PROJECT_DIR = Path(os.getenv("PROJECT_DIR"))

client_id = "OY460kUna6iiYLtTT-pNHg"
secret = "7h-1QRYJh8DAnf3MiWF0yjv_25gJxQ"
user_agent = "word_guessr"
import re

def split_into_sentences(text_list):
    # Initialize an empty list to store all sentences
    all_sentences = []
    
    # Iterate through each text in the list
    for text in text_list:
        # Split the current text into sentences and extend the result into all_sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        all_sentences.extend(sentences)
    
    return all_sentences

def get_all_comments(comment):
    sentences = split_into_sentences([comment.body])
    if comment.replies:
        
        for reply in comment.replies:
            sentences.extend(split_into_sentences(get_all_comments(reply)))
    return sentences

# Read-only instance
reddit_read_only = praw.Reddit(client_id = "OY460kUna6iiYLtTT-pNHg",		 # your client id
							client_secret = "7h-1QRYJh8DAnf3MiWF0yjv_25gJxQ",	 # your client secret
							user_agent = "word_guessr")	 # your user agent

subreddit_scraped = "solana"
subreddit = reddit_read_only.subreddit(subreddit_scraped)
posts = subreddit.top("day")
#get the urls of the top posts

base_url = "https://www.reddit.com"
urls = []
for post in posts:
	# URL of each post
    urls.append(base_url + post.permalink) # subreddit.url returns the url of the attached article if its a link post 
sentences = []
for url in tqdm(urls):
    submission = reddit_read_only.submission(url = url)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments:
        sentences = sentences + get_all_comments(comment) + split_into_sentences(submission.selftext)
# Save the arrays
file_name = BASE_PROJECT_DIR / 'data' / f'{subreddit_scraped}.npz'
np.savez(file_name,sentences=sentences)



