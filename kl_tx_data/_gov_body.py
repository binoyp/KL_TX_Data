import re 
import asyncio
import requests
from bs4 import BeautifulSoup

def get_loc_data(num: int):
    """[summary]

    :param num: [description]
    :type num: [type]
    """ 
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }

    params = (
        ('SearchLBID', f'{num}'), #1245
    )
    response = session.get('https://tax.lsgkerala.gov.in/epayment/index.php', headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    cookies = session.cookies.get_dict()
    mid_banner = soup.find(id='middle_banner2')
    if mid_banner:
        mdata = re.sub('\s+',' ',mid_banner.text.strip())
        return (True, mdata)
    else:
        return (False, '')

async def prc(n):
    success, data = get_loc_data(n)
    if success:
        print(n, data)

async def m2():
    #for i in range(100,300):
    await asyncio.gather(map(prc, list(range(100,150))))
