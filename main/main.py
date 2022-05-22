from flask import Blueprint, render_template, request


from main.utils import search_posts_by_substring

from config import POST_PATH

from my_logger import logger


main_blueprint = Blueprint('my_blueprint', __name__, template_folder='templates', static_folder='static')


# Главная страница сайта с формой поиска
@main_blueprint.route('/')
def index_page():
    try:
        logger.info('Загрузка главной страницы')
        return render_template('index.html')
    except:
        logger.critical('Приложение не работает!')
        return '<h1>Ошибка приложения!</h1>'


# Страница с найдеными по подстроке постами
@main_blueprint.route('/search/')
def search_page():
    try:
        s = request.args.get('s', '')  # Получаем из формы подстроку
        posts = search_posts_by_substring(s, POST_PATH)  # Список постов по подстроке
        logger.info('Загружен список постов по вхождению подстроки')
        return render_template('post_list.html', s=s, posts=posts)
    except:
        logger.error('Ошибка загрузки списка постов по вхождению подстроки')


