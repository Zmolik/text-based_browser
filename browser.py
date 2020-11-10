import sys
import os
import re
import requests
from _collections import deque
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore
args = sys.argv  # arg[1] is name of directory to create
web_stack = deque()


def save_web(dir, content, url):
    file_name = url.split('.')[0].replace('https://', '')
    with open(f'{dir}\\{file_name}', 'w', encoding='utf-8') as file:
        file.write(content)


def load_file(dir, file_name):
    with open(f'{dir}\\{file_name}', 'r', encoding='utf-8') as file:
        print(file.read())


def get_soup(user_url):
    init(autoreset=True)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    response = requests.get(user_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    page = ''
    for tag in soup.find_all(['title', 'p', re.compile('^h'), 'a', 'ul', 'ol', 'li', 'span'], text=True):
        if tag.name == 'a':
            page += Fore.BLUE + tag.text + '\033[39m' + ' '
        else:
            page += tag.text + '\n'
    formatted_text = re.sub('\n+', '\n', page)
    formatted_text = re.sub('\s{2,}', '\n', formatted_text)
    return formatted_text


if os.path.exists(f'{args[1]}'):
    pass
else:
    os.makedirs(f'{args[1]}')

while (user_input := input('>')) != 'exit':
    if user_input == 'back':
        if len(web_stack) <= 1:
            print('Error: No previous web page in history')
            pass
        else:
            current = web_stack.pop()
            wanted = web_stack.pop()
            print(wanted)
            web_stack.append(wanted)
    elif '.' in user_input:
        if user_input.startswith('https://'):
            url = user_input
        else:
            url = 'https://' + user_input
        try:
            txt_page = get_soup(url)
        except Exception as err:
            print('Page not found', err)
            continue
        if txt_page:
            print(txt_page)
            save_web(args[1], txt_page, url)
            web_stack.append(txt_page)
        else:
            continue
    else:
        try:
            load_file(args[1], user_input)
        except FileNotFoundError:
            print('Error: File not found')
