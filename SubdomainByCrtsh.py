import requests
import re

TIME_OUT = 60
def get_SSL(domain):
    domains = []
    url = 'https://crt.sh/?q=%25.{}'.format(domain)
    response = requests.get(url,timeout=TIME_OUT)
    ssl = re.findall("<TD>(.*?).{}</TD>".format(domain),response.text)
    for i in ssl:
        i += '.' + domain
        domains.append(i)
    print(domains)

if __name__ == '__main__':
    get_SSL("github.com")
