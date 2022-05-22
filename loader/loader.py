import logging

from flask import Blueprint, render_template, request


from loader.utils import get_new_post, load_json_data

from config import POST_PATH, UPLOAD_FOLDER

from my_logger import logger


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')


# Страница с формой для добавления нового поста
@loader_blueprint.route("/post_form/", methods=["POST", "GET"])
def page_post_form():

    return render_template('post_form.html')



@loader_blueprint.route("/post_uploaded/", methods=["POST", "GET"])
def page_post_uploaded():
    try:
        post_content = request.form['content']  # Получаем текст из формы
        picture = request.files.get('picture')  # Получаем изображение
        filename = picture.filename  # Получаем имя файла(изображения)
        picture_path = f"{UPLOAD_FOLDER}/{filename}"  # формируем путь для сохранения изображения
        picture.save(picture_path)  # Сохраняем изображение
        get_new_post(POST_PATH, picture_path, post_content, load_json_data(POST_PATH))  # Формируем новый пост
        logger.info('Загружен новый пост')
        return render_template('post_uploaded.html', post_content=post_content, picture_path=picture_path)
    except:
        logger.error('Ошибка загрузки данных поста')
        return render_template('error.html')

