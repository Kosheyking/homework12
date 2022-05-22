import json


def load_json_data(POST_PATH):
    ''' Функция возвращает список постов из файла posts.json'''
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def search_posts_by_substring(substring, POST_PATH):
    ''' Функция возвращает список постов, в которые входит подстрока substring'''
    posts = load_json_data(POST_PATH)
    post_founded = []
    for post in posts:
        if substring.lower() in post['content'].lower():
            post_founded.append(post)
    return post_founded


