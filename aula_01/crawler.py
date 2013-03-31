#coding:utf-8
import os
import json
import requests
from bs4 import BeautifulSoup

START_URL = "http://bernardofontes.net"

def get_posts_links():
    """
    Returns an iterator with the a tags with the titles
    """
    html = requests.get(START_URL).content
    soup = BeautifulSoup(html)
    return soup.findAll('a', rel='bookmark')

def extract_data_from_link(post_link_tag):
    """
    Given a tag object, return it href value and post title
    """
    return {
        'link': post_link_tag.attrs['href'],
        'title': post_link_tag.getText(),
    }

def creates_output_file(data):
    """
    Creates a json file with data parameter
    """
    file_path = os.path.join(os.path.dirname(__file__), 'out.json')
    with open(file_path, 'w') as fp:
        json_data = json.dumps(data)
        fp.write(json_data)

if __name__ == '__main__':
    posts = get_posts_links()
    data = []

    for post in posts:
        post_data = extract_data_from_link(post)
        data.append(post_data)

    creates_output_file(data)
