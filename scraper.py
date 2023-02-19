import requests

http_urls = [
    'https://www.proxy-list.download/api/v1/get?type=http',
    'https://www.proxyscan.io/download?type=http',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http',
]

https_urls = [
    'https://www.proxy-list.download/api/v1/get?type=https',
    'https://www.proxyscan.io/download?type=https',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https',
]

socks4_urls = [
    'https://www.proxy-list.download/api/v1/get?type=socks4',
    'https://www.proxyscan.io/download?type=socks4',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4',
]

socks5_urls = [
    'https://www.proxy-list.download/api/v1/get?type=socks5',
    'https://www.proxyscan.io/download?type=socks5',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5',
]

all_urls = http_urls + https_urls + socks4_urls + socks5_urls

def scrape_proxies(proxy_type):
    if proxy_type == "http":
        urls = http_urls
        file = "http_proxies.txt"
    elif proxy_type == "https":
        urls = https_urls
        file = "https_proxies.txt"
    elif proxy_type == "socks4":
        urls = socks4_urls
        file = "socks4_proxies.txt"
    elif proxy_type == "socks5":
        urls = socks5_urls
        file = "socks5_proxies.txt"
    elif proxy_type == "all":
        urls = all_urls
        file = "all_proxies.txt"
    else:
        print("Invalid input")
        return

    print(f"Scraping {proxy_type} proxies...")
    with open(file, "w") as f:
        for url in urls:
            r = requests.get(url)
            for line in r.text.splitlines():
                f.write(line.strip() + "\n")
    print(f"Scraped {proxy_type} proxies saved to {file}")
    input("Press Enter to continue...")

if __name__ == "__main__":
    print("Options:")
    print("[1] Scrape HTTP Proxies")
    print("[2] Scrape HTTPS Proxies")
    print("[3] Scrape SOCKS4 Proxies")
    print("[4] Scrape SOCKS5 Proxies")
    print("[5] Scrape ALL Proxies")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        scrape_proxies("http")
    elif choice == "2":
        scrape_proxies("https")
    elif choice == "3":
        scrape_proxies("socks4")
    elif choice == "4":
        scrape_proxies("socks5")
    elif choice == "5":
        scrape_proxies("all")
    else:
        print("Invalid input")
