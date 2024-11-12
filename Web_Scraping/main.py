import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from textblob import TextBlob
import urllib.request
from collections import Counter
import nltk
from Proxy_Rotation.main import rotate_proxies_get
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from tqdm import tqdm


def get_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    return ' '.join([para.get_text() for para in paragraphs])

def unique_urls(urls):
    unique_urls = []
    seen = set()

    for url in urls:
        if url not in seen:
            unique_urls.append(url)
            seen.add(url)
    return unique_urls

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_specific_class(body, class_name):
    soup = BeautifulSoup(body, 'html.parser')
    elements = soup.find_all(class_=class_name)  # Find all elements with the specified class
    return " ".join(element.get_text(strip=True) for element in elements)

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def process_article(url, driver, class_type, keyword,lame_words):
    keyword = keyword.lower()
    lower_case_lame_words = [word.lower() for word in lame_words]
        # Check if lame_words is None
    if lame_words is None:
        print("Error: lame_words is None")
        return
    try:
        driver.get(url)
        html = driver.page_source
        sentences = nltk.sent_tokenize(text_from_specific_class(html,class_type))
        
        for sentence in sentences:
            # Tokenize each sentence into words
            words = nltk.word_tokenize(sentence)
            # Flatten the list if you want a single list of all words
            lower_case_words = [word.lower() for word in words]
            if keyword in lower_case_words:
                for word in lower_case_words:

                    if len(word)>2 and word not in lower_case_lame_words:

                        if word in all_words:
                            all_words_count[all_words.index(word)] += 1
                        else:
                            all_words.append(word)
                            all_words_count.append(1)
    except WebDriverException as e:
        # Catch errors like net::ERR_NAME_NOT_RESOLVED and others
        print(f"Error occurred while accessing {url}: {str(e)}")
    except Exception as e:
        # Handle other unexpected exceptions
        print(f"An unexpected error occurred: {str(e)}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


keyword = "Trump"

lame_words =  ["mr.","the", "and","for","not","was","they","who","from","will","would","The","had","been","what","also","him","more","which","his","has","with","donald","are","with","their","all","have","that","ms.","when","she","out"]
lame_words = [keyword] + lame_words
page_number = 10
nouns = []
nouns_count = []
count = 0
urls_num = 0
all_words = []
all_words_count = []


base_urls = ["https://www.nytimes.com/section/us","https://www.nytimes.com/section/world","https://www.nytimes.com/section/politics","https://www.nytimes.com/section/nyregion","https://www.nytimes.com/spotlight/california-news",
             "https://www.nytimes.com/section/climate","https://www.nytimes.com/section/business","https://www.nytimes.com/spotlight/donald-trump"]
class_type = "css-at9mc1 evys1bk0"

urls = []
# Request for article URLs
for base_url in base_urls:
    url = f"{base_url}?page={1}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')


    # Find URLs of individual articles
    urls = urls+([f"https://www.nytimes.com{a['href']}" for a in soup.find_all('a', href=True) if '2024/' in a['href']])
print(urls)
unique_urls = unique_urls(urls)
failed_urls = 0

for url in tqdm(unique_urls):
    try:
        process_article(url, driver, class_type, keyword,lame_words)
        # You can process the result here (e.g., store it in a list, process further, etc.)
        # Assuming you want to append the results to a list:
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
 

# Save the arrays
np.savez('all_words.npz', words=all_words, words_count=all_words_count)

sorted_pairs = sorted(zip(all_words, all_words_count), reverse=True)

for string, number in sorted_pairs:
    print(f"{string}: {number}")

print(str(len(urls))+ " articles were scrapped")