from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

url = 'https://www.nytimes.com/2024/10/30/us/republican-congress-trump-johnson.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# Create a request object with the URL and headers
request = urllib.request.Request(url, headers=headers)

# Open the URL with the request object
html = urllib.request.urlopen(request).read()

# Extract and print visible text
print(text_from_html(html))