import json


def load_json_data(POST_PATH):
    ''' загружает список постов из файла posts.json'''
    with open(POST_PATH, 'r') as file:
        posts = json.load(file)
        return posts


def get_new_post(POST_PATH, picture_path, post_content, posts):
    '''Добавляет новый пост в файл posts.json'''
    with open(POST_PATH, 'w') as file:
        posts.append({"pic": f"../{picture_path}", "content": post_content})
        json.dump(posts, file, ensure_ascii=False)
    return posts



