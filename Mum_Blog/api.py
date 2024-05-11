from json import load
from os.path import join, dirname
from random import randint

POSTS_PATH = join('Mum_Blog', 'data', 'posts.json')
QUOTES_PATH = join('Mum_Blog', 'data', 'quotes.json')

def read_json(path):
    with open(path, 'r') as file:
        return load(file)
    
def get_posts(limit:int=10, start:int=0):
    all_posts = read_json(POSTS_PATH)
    end = start + limit
    return all_posts[start:end]

def get_post(id:str):
    all_posts = read_json()
    for post in all_posts:
        if post['id'] == id:
            return post
    return None

def get_quotes():
    return read_json(QUOTES_PATH)