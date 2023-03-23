import requests

with open('proxy.txt', 'r') as f:
    proxy_list = [line.strip() for line in f]

working_proxies = []

for proxy in proxy_list:
    try:
        response = requests.get('https://www.google.com', proxies={'https': proxy}, timeout=1)
        if response.status_code == 200:
            working_proxies.append(proxy)
            with open('working_proxy.txt', 'a') as f:
                f.write(proxy + '\n')

    except Exception:
        pass
      
print('Workin proxy: ', working_proxies)
