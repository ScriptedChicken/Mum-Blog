from json import load, dump
from requests import get
from os.path import join

def read_json(path):
    with open(path, "r") as file:
        return load(file)
    
def save_json(json_object, path):
    with open(path, "w") as  file:
        dump(json_object, file, indent=4)

def regenerate_authors(posts):
    response = get(fr"https://randomuser.me/api/?results={len(posts)}")
    if response.ok:
        random_users = response.json().get('results')
        for i, post in enumerate(posts):
            post['profile']['username'] = random_users[i]['login']['username']
            post['profile']['image'] = random_users[i]['picture']['thumbnail']
            posts[i] = post
    return posts


if __name__ == "__main__":
    path = join('Mum_Blog', 'data', 'posts.json')
    posts = read_json(path)
    posts = regenerate_authors(posts)
    save_json(posts, path)