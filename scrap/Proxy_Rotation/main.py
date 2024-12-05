import requests 


sites_to_check = ["https://www.newsmax.com/newsfront/donald-trump-liz-cheney-social-media/2024/11/01/id/1186361/"]


def rotate_proxies_get(requests,url,headers):
    with open("Proxy_Rotation/valid_proxies.txt","r") as f:
        proxies = f.read().split("\n")

    for counter in range(10):
        try:
            print(f"Using proxy server : {proxies[counter]}")
            res = requests.get(url,headers=headers,proxies = {"https":proxies[counter],
                                                "https":proxies[counter]})
            return res
        except:
            print("Trying more proxies ")
    print("Failed. Find more proxies ")

