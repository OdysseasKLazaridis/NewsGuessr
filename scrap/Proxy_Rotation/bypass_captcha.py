#https://anti-captcha.com/apidoc/task-types/AntiBotCookieTask

from anticaptchaofficial.antibotcookietask import *
proxy_host = "172.17.0.3"
proxy_port = "3128⁠"
proxy_login = "marmamia"
proxy_pass = "korkodilopaido12"

proxies = {
    'https': f"http://{proxy_login}:{proxy_pass}@{proxy_host}:{proxy_port}",
    'http': f"http://{proxy_login}:{proxy_pass}@{proxy_host}:{proxy_port}"
}

solver = antibotcookieTask()
solver.set_verbose(1)
solver.set_key("0bc163e04d2c2f33cfcdb191a67d32dd")
solver.set_website_url("https://www.nytimes.com/2024/10/31/business/elon-musk-trump.html")
solver.set_proxy_address(proxy_host)
solver.set_proxy_port(proxy_port)
solver.set_proxy_login(proxy_login)
solver.set_proxy_password(proxy_pass)


result = solver.solve_and_return_solution()
if result == 0:
    print("could not solve task")
    exit()

print(result)

cookies, localStorage, fingerprint = result["cookies"], result["localStorage"], result["fingerprint"]

if len(cookies) == 0:
    print("empty cookies, try again")
    exit()

cookie_string = '; '.join([f'{key}={value}' for key, value in cookies.items()])
user_agent = fingerprint['self.navigator.userAgent']
print(f"use these cookies for requests: {cookie_string}")
print(f"use this user-agent for requests: {user_agent}")

s = requests.Session()
proxies = {
  "http": f"http://{proxy_login}:{proxy_pass}@{proxy_host}:{proxy_port}",
  "https": f"http://{proxy_login}:{proxy_pass}@{proxy_host}:{proxy_port}"
}
s.proxies = proxies

content = s.get("https://www.allopneus.com/liste/pneu-auto?saison%5B%5D=4seasons&saison%5B%5D=ete&saison%5B%5D=hiver&page=1", headers={
    "Cookie": cookie_string,
    "User-Agent": user_agent
}).text
print(content)