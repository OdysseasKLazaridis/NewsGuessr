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
import numpy as np


def get_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    print(paragraphs)
    return ' '.join([para.get_text() for para in paragraphs])

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

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

keyword = "Trump"
page_number = 1
nouns = []
nouns_count = []
count = 0
urls_num = 0

for i in range(2):
    

    url = "https://www.nytimes.com/section/us?page="+str(page_number)
    class_type = "css-at9mc1 evys1bk0"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    request = requests.get(url,headers)
    soup = BeautifulSoup(request.text, 'html.parser')
    urls = soup.find_all('a', href=True)  # href=True ensures we only get <a> tags with href attributes

    # Filter links that contain '2024/10'
    filtered_urls = [url['href'] for url in urls if '2024/' in url['href']]
    urls_num = len(filtered_urls)
    final_urls = ["https://www.nytimes.com" + item for item in filtered_urls]
    print(final_urls)

    for url in final_urls:
        driver.get(url)
        html = driver.page_source

        # time.sleep(4)
        # # Create a request object with the URL and headers
        # request = urllib.request.Request(url, headers=headers)

        # # Open the URL with the request object
        # html = requests.get(url,headers=headers).text
        print(html)
        sentences = nltk.sent_tokenize(text_from_specific_class(html,class_type))


        for sentence in sentences:
            # Tokenize each sentence into words
            words = nltk.word_tokenize(sentence)

            # Flatten the list if you want a single list of all words
            all_words = [word for sentence in words for word in sentence]
            if keyword in all_words:
                blob = TextBlob(sentence)
                blob_nouns = blob.noun_phrases
                for noun_phrase in blob_nouns:
                    if noun_phrase in nouns:
                        nouns_count[nouns.index(noun_phrase)] += 1
                    else:
                        nouns.append(noun_phrase)
                        nouns_count.append(1)

# Save the arrays
np.savez('nouns_data.npz', nouns=nouns, nouns_count=nouns_count)

sorted_pairs = sorted(zip(nouns, nouns_count), reverse=True)

for string, number in sorted_pairs:
    print(f"{string}: {number}")

print(str(urls_num)+ " articles were scrapped")