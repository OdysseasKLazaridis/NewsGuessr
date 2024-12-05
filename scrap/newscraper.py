#import what we need
from requests_html import HTMLSession
session = HTMLSession()

#use session to get the page
r = session.get('https://news.google.com/home?hl=en-US&gl=US&ceid=US:en')

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
r.html.render(sleep=1, scrolldown=5)

#find all the articles by using inspect element and create blank list
articles = r.html.find('article')
newslist = []
print(articles)
#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        print("1")
        print(newsitem)
        title = newsitem.text
        print("2")
        link = newsitem.absolute_links
        print("3")
        newsarticle = {
            'title': title,
            'link': link 
        }
        newslist.append(newsarticle)
    except:
       pass

#print the length of the list
print(len(newslist))