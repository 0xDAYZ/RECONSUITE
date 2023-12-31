import time
from subprocess import call


def cross_check_domain(url):
    if 'http://www.' in url:
        url = url.replace('http://www.', '')
    if 'https://www.' in url:
        url = url.replace('https://www.', '')
    if 'https://' in url:
        url = url.replace('https://', '')
    if 'http://' in url:
        url = url.replace('http://', '')
    if 'www.' in url:
        url = url.replace('www.', '')
    return url

def subdomain_crawl():
    """Crawls website for hidden Subdomains."""
    call("clear")
    print()
    url = input('Link > ')
    url = cross_check_domain(url)
    function = "crawl_for_subdomains"
    print()
    print(f"$ python ./tools/crawler.py -u {url} -f {function}")
    print()
    try:
        call(f"python ./tools/crawler.py -u {url} -f {function}", shell=True)
    except KeyboardInterrupt:
        time.sleep(1)


def subdirectory_crawl():
    """Crawls website for hidden Subdirectories."""
    call("clear")
    print()
    url = input('Link > ')
    url = cross_check_domain(url)

    if '/' in url[-1]:
        url = url[:-1]

    function = "crawl_for_subdirectories"
    print()
    print(f"$ python ./tools/crawler.py -u {url} -f {function}")
    print()
    try:
        call(f"python ./tools/crawler.py -u {url} -f {function}", shell=True)
    except KeyboardInterrupt:
        time.sleep(1)


def links_crawl():
    """Crawls website for href links."""
    call("clear")
    print()
    url = input('Link > ')
    url = cross_check_domain(url)
    function = "show_embed_links"
    print()
    print(f"$ python ./tools/crawler.py -u {url} -f {function}")
    print()
    try:
        call(f"python ./tools/crawler.py -u {url} -f {function}", shell=True)
    except KeyboardInterrupt:
        time.sleep(1)
